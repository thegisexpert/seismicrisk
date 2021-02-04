import random
from qgis.PyQt.QtCore import QVariant

#https://gis.stackexchange.com/questions/258910/creating-n-randomly-distributed-points-within-given-multipolygon-with-pyqgis
layer=iface.activeLayer()
crs = layer.crs().toWkt()

# Create the output layer
outLayer = QgsVectorLayer('Point?crs='+ crs, 'random_points' , 'memory')
prov = outLayer.dataProvider()
prov.addAttributes([QgsField('ID', QVariant.Int, '', 10, 0)])
outLayer.updateFields()


ext=layer.extent()
xmin = ext.xMinimum()
xmax = ext.xMaximum()
ymin = ext.yMinimum()
ymax = ext.yMaximum()

points =  50 # set as you want

first = True
for feat in layer.getFeatures():
    if first:
        outFeat = QgsFeature()
        outGeom = QgsGeometry(feat.geometry())
        first = False
    else:
        outGeom = outGeom.combine(feat.geometry())
outFeat.setGeometry(outGeom)

id = 0
p = 1
while p <= points:
    x_coord = random.uniform(xmin, xmax)
    y_coord = random.uniform(ymin, ymax)
    pt = QgsPoint(x_coord, y_coord)
    tmp_geom = QgsGeometry.fromPoint(pt)
    if tmp_geom.intersects(outFeat.geometry()):
        outGeom = QgsFeature()
        outGeom.setGeometry(tmp_geom)
        outGeom.setAttributes([id])
        prov.addFeatures([outGeom])
        id += 1
        p += 1

# Add the layer to the Layers panel
QgsMapLayerRegistry.instance().addMapLayer(outLayer)

