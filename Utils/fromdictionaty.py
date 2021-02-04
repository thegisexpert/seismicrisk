#https://gis.stackexchange.com/questions/155412/pyqgis-use-of-predefined-color-ramps/157678#157678

from PyQt4.QtGui import QColor
import qgis.utils

layer = qgis.utils.iface.activeLayer()


myStyle = QgsStyleV2().defaultStyle()

defaultColorRampNames = myStyle.colorRampNames()
print defaultColorRampNames
print defaultColorRampNames[22]

ramp = myStyle.colorRamp(defaultColorRampNames[22])  #Spectral name

rp = ramp.properties()
print rp
print "my style" , myStyle.symbolCount()

dictionary = {
    1: (QColor(215,25,28,255), '1'),
    2: (QColor(43,131,186,255), '2'),
    3: (QColor(253,174,97,255), '3'),
    4: (QColor(255,255,191,255), 'Unknown'),
}

categories = []

for item, (color, label) in dictionary.items():
    symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor(color))
    category = QgsRendererCategoryV2(item, symbol, label)
    categories.append(category)

renderer = QgsCategorizedSymbolRendererV2("value", categories)

renderer.setSourceColorRamp(ramp)

layer.setRendererV2(renderer)
layer.triggerRepaint()