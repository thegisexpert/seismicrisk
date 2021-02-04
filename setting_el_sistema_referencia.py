from PyQt4.QtCore import *
from PyQt4.QtGui import *


#layersNames = []
#for i in self.iface.mapCanvas().layers():
#   layersNames.append(str(i.name()))

for i in qgis.utils.iface.mapCanvas().layers():


    i.setCrs(QgsCoordinateReferenceSystem(3857, QgsCoordinateReferenceSystem.EpsgCrsId))
    i.triggerRepaint()
    #layersNames.append(str(i.name()))



display_name="prueba7popoliforpostgres"
layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

#QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # prmer elemento de la lista
'''
layer = layerExiste[0]
layer.selectAll()
#mCanvas = iface.mapCanvas()
qgis.utils.iface.mapCanvas().zoomToSelected()
layer.removeSelection()
'''
#https://gis.stackexchange.com/questions/53622/qgis-zoom-from-python-console

eMenu = qgis.utils.iface.viewMenu()
eMenu.actions() [12].trigger()


#qgis.utils.iface.mapCanvas().zoomToFullExtent()

#qgis.utils.iface.mapCanvas().zoomToSelected(layer)

#execfile("D:/usbgis/apps/qgis2/qgisconfig/Python/plugins/PruebaAutoFields/setting_el_sistema_referencia.py");