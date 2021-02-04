
lyr = QgsVectorLayer(src, “Museums”, “ogr”)

Now we’ll use a python dictionary to define the font properties:
fontStyle = {}

fontStyle[‘color’] = ‘#000000’

fontStyle[‘font’] = ‘Webdings’

fontStyle[‘chr’] = ‘G’

fontStyle[‘size’] = ‘6’

Now we’ll create a font symbol layer:
symLyr1 = QgsFontMarkerSymbolLayerV2.create(fontStyle)

Then we’ll change out the default symbol layer of the vector layer with our font symbol information:
lyr.rendererV2().symbols()[0].changeSymbolLayer(0, symLyr1)

Finally, we add the layer to the map:
QgsMapLayerRegistry.instance().addMapLayer(lyr)