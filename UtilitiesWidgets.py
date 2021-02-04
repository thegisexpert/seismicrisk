
def alignLayers():


    #https://gis.stackexchange.com/questions/26257/how-can-i-iterate-over-map-layers-in-qgis-python

    #qgis.utils.iface es self.iface
    layers = qgis.utils.iface.legendInterface().layers()

    for layer in layers:
       layerType = layer.type()
       if layerType == QgsMapLayer.VectorLayer:
          print " new vector "
          layer.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))


    layer = layers[0]


    #self.canvas.setExtent(layer.extent())

    #qgis.utils.iface.mapCanvas().setExtent(layer.extent())

    vl = QgsMapLayerRegistry.instance().mapLayer( layer.id() )
    print " name " + vl.name()
    canvas = qgis.utils.iface.mapCanvas()
    canvas.setExtent( vl.extent() )

    qgis.utils.iface.setActiveLayer(vl)

    qgis.utils.iface.zoomToActiveLayer()