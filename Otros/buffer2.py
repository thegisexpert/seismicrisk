from qgis.utils import iface
from qgis.analysis import QgsGeometryAnalyzer
import processing

'''
mc = iface.mapCanvas()
layer = mc.currentLayer()

for i in range(5):
    layer.select(i)
    #my_path = "/home/zeito/pyqgis_data/output" + str(i) + ".shp"
    my_path = "D:/Data/Python/multi_buffer/output" + str(i) + ".shp"

    QgsGeometryAnalyzer().buffer(layer, my_path,5000,True,False,-1)

    layer.deselect(i)

#https://gis.stackexchange.com/questions/204553/create-individual-buffers-from-vector-points-in-qgis

'''
#Don't forget to Toggle Editing

lyr = qgis.utils.iface.activeLayer()
provider = lyr.dataProvider()
feat= QgsFeature()
alls = provider.attributeIndexes()
provider.select(alls)

while provider.nextFeature(feat):
    buff = feat.geometry().buffer(5,2)
    lyr.dataProvider().changeGeometryValues({feat.id(): buff})