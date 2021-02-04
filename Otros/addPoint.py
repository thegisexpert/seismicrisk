#https://gis.stackexchange.com/questions/60307/how-can-i-create-a-line-with-three-points-with-python-in-qgis

line_start = QgsPoint(50,50)
line_end = QgsPoint(100,150)
line = QgsGeometry.fromPolyline([line_start,line_end])

# create a new memory layer
v_layer = QgsVectorLayer("LineString", "line", "memory")
pr = v_layer.dataProvider()
# create a new feature
seg = QgsFeature()
# add the geometry to the feature,
seg.setGeometry(QgsGeometry.fromPolyline([line_start, line_end]))
# ...it was here that you can add attributes, after having defined....
# add the geometry to the layer
pr.addFeatures( [ seg ] )
# update extent of the layer (not necessary)
v_layer.updateExtents()
# show the line
QgsMapLayerRegistry.instance().addMapLayers([v_layer])