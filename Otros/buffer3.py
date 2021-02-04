#https://gis.stackexchange.com/questions/217218/how-to-create-rectangular-buffers-around-points-in-qgis-with-pyth# n
layer = iface.activeLayer()

feats = layer.getFeatures()

epsg = layer.crs().postgisSrid()

uri = "Polygon?crs=epsg:" + str(epsg) + "&field=id:integer&field=x:real&field=y:real&field=point_id:integer""&index=yes"

mem_layer = QgsVectorLayer(uri,
                           'rectangular_buffer',
                           'memory')

prov = mem_layer.dataProvider()

for i, feat in enumerate(feats):

    point = feat.geometry().asPoint()
    new_feat = QgsFeature()
    new_feat.setAttributes([i, point[0], point[1], feat.id()])
    bbox = feat.geometry().buffer(1000, -1).boundingBox()
    tmp_feat = bbox.asWktPolygon()
    xmin1,ymin1,xmax1,ymax1 = bbox.toRectF().getCoords()
    xmin2,ymin2,xmax2,ymax2 = feat.geometry().buffer(2000, -1).boundingBox().toRectF().getCoords()
    p1 = QgsPoint(xmin1, ymax2)
    p2 = QgsPoint(xmax1, ymin2)
    new_ext = QgsRectangle(p1,p2)
    new_tmp_feat = new_ext.asWktPolygon()
    print str("insert into bufferpopoli(gid, geom) values(" + str(i) + ", ST_AsText(ST_Multi(ST_GeomFromText('" +new_tmp_feat+"'))));")
    new_feat.setGeometry(QgsGeometry.fromWkt(new_tmp_feat))
    prov.addFeatures([new_feat])

QgsMapLayerRegistry.instance().addMapLayer(mem_layer)