#https://howtoinqgis.wordpress.com/2016/10/23/how-to-create-a-memory-layer-from-the-python-console/

# Specify the geometry type

from PyQt4.QtCore import QVariant
from qgis.core import (QgsFeature, QgsField, QgsFields,
                       QgsGeometry, QgsPoint, QgsVectorFileWriter)
from qgis.utils import QGis, iface

layer = QgsVectorLayer('Polygon?crs=epsg:4326', 'polygon', 'memory')

layer.startEditing()

fields = QgsFields()
fields.append(QgsField("first", QVariant.Int))
fields.append(QgsField("second", QVariant.String))
# Set the provider to accept the data source
prov = layer.dataProvider()

prov.addAttributes([QgsField("test", QVariant.Int)])
prov.addAttributes([QgsField("nombre", QVariant.String)])

layer.updateFields()

points = [QgsPoint(100, 100), QgsPoint(100, 200), QgsPoint(200, 200), QgsPoint(200, 100)]


# Add a new feature and assign the geometry
feat = QgsFeature()
feat.setGeometry(QgsGeometry.fromPolygon([points]))
feat.setAttributes([1, "text"])

prov.addFeatures([feat])

points2 = [QgsPoint(400, 400), QgsPoint(400, 600), QgsPoint(500, 500), QgsPoint(500, 400)]


feat2 = QgsFeature()
feat2.setGeometry(QgsGeometry.fromPolygon([points2]))
feat2.setAttributes([2, "text2"])

prov.addFeatures([feat2])

# Update extent of the layer
layer.updateExtents()

layer.commitChanges()
# Add the layer to the Layers panel
QgsMapLayerRegistry.instance().addMapLayers([layer])

#writer = QgsVectorFileWriter("D:/Data/shapes_gusardado.shp", "CP1250", fields, QGis.WKBPolygon, None, "ESRI Shapefile")

#if writer.hasError() != QgsVectorFileWriter.NoError:
#    print "Error when creating shapefile: ",  w.errorMessage()

error = QgsVectorFileWriter.writeAsVectorFormat(layer, "D:/Data/shapes_gusardado.shp",
                                                "CP1250", None,
                                                "ESRI Shapefile")

if error == QgsVectorFileWriter.NoError:
    print("success!")
