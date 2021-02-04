#https://snorfalorpagus.net/blog/2014/03/04/symbology-of-vector-layers-in-qgis-python-plugins/

# define a lookup: value -> (color, label)
animals = {
    'cat': ('#f00', 'Small cat'),
    'dog': ('#0f0', 'Big dog'),
    'sheep': ('#fff', 'Fluffy sheep'),
    '': ('#000', 'Unknown'),
}

# create a category for each item in animals
categories = []
for animal_name, (color, label) in animals.items():
    symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor(color))
    category = QgsRendererCategoryV2(animal_name, symbol, label)
    categories.append(category)

# create the renderer and assign it to a layer
expression = 'animal' # field name
renderer = QgsCategorizedSymbolRendererV2(expression, categories)
layer.setRendererV2(renderer)