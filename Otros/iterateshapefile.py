layer = iface.activeLayer()

features = layer.getFeatures()
for f in features:
  geom = f.geometry()
  print "Area:", geom.area()
  print "Perimeter:", geom.length()
  print "Polygon:", geom.asPolygon()