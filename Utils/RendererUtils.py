#https://gis.stackexchange.com/questions/36915/can-i-dynamically-update-symbol-ranges

from PyQt4.QtGui import QColor              # import this namespace as I want to refer to QColor later
from PyQt4.QtCore import QVariant

def satramp(hue):
    layer = qgis.utils.iface.activeLayer()
    grads = len(layer.rendererV2().symbols())
    vinc = 0
    val = 180
    i = 0 - (255 / grads)                                       # used to increment the saturation value
    j = val - (grads * vinc)
    for sym in layer.rendererV2().symbols():        # loop through each symbol in the layer using 'new symbology'
        i += (255 / grads)
        j += vinc
        sym.setColor(QColor.fromHsv(hue,i,j))
    canvas = qgis.utils.iface.mapCanvas()
    canvas.refresh()

def rap():
    canvas = qgis.utils.iface.mapCanvas()
    layer = qgis.utils.iface.activeLayer()
    layer.reload()
    canvas.refresh()

# gets the layer for the passed index value based on the legend index
def getLayerByIndex(layerIndex):
    idx = 0
    for layer in qgis.utils.iface.legendInterface().layers():
        if idx == layerIndex:
            break
        idx += 1
    return layer

# gets the field index for the given field name
def getFieldIndex(fieldName,layer):
    mFieldMap = {}
    fields = layer.pendingFields()
    for ( key, field ) in fields.iteritems():
        if field.type() == QVariant.Int or field.type() == QVariant.Double:
            if field.name() == fieldName:
                return key

# sets a saturation ramp for a graduated layer only, based on the passed hue, value and index of the layer from the legend
def satramp(layerindex, hue, value):
    layer = getLayerByIndex(layerindex)
    grads = len(layer.rendererV2().symbols())                   # determine the number of graduations to use based on
    vinc = 0                                                    # value incrementer, currently not used, but can be adjusted to increment the value also
    val = value
    i = 0 - (255 / grads)                                       # used to increment the saturation value
    j = val - (grads * vinc)
    layer.reload()                                              # refresh the data source

    # determine range increments
    provider = layer.dataProvider()
    fieldName = layer.rendererV2().classAttribute()
    fieldIndex = getFieldIndex(fieldName,layer)
    min = provider.minimumValue(fieldIndex).toDouble()[ 0 ]     # get the min and max values to calculate the new gradations
    max = provider.maximumValue(fieldIndex).toDouble()[ 0 ]
    rangeCount = len(layer.rendererV2().ranges())
    rangeIncrement = (max - min) / rangeCount
    rangePoint = min

    # construt a new renderer using ranges based on the existing renderer
    rangeList = []
    for range in layer.rendererV2().ranges():
        newSymbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
        label = str(rangePoint) + " - " + str(rangePoint + rangeIncrement)
        newRange = QgsRendererRangeV2(rangePoint,rangePoint + rangeIncrement, newSymbol, label)
        rangeList.append(newRange)
        rangePoint += rangeIncrement

    newRenderer = QgsGraduatedSymbolRendererV2('',rangeList)
    newRenderer.setClassAttribute(layer.rendererV2().classAttribute())
    newRenderer.setMode(QgsGraduatedSymbolRendererV2.EqualInterval)
    layer.setRendererV2(newRenderer)

    for sym in layer.rendererV2().symbols():        # loop through each symbol in the layer using 'new symbology'
        i += (255 / grads)
        j += vinc
        sym.setColor(QColor.fromHsv(hue,i,j))

    qgis.utils.iface.legendInterface().refreshLayerSymbology(layer)
    canvas = qgis.utils.iface.mapCanvas()
    canvas.refresh()