#https://gis.stackexchange.com/questions/48613/applying-graduated-renderer-in-pyqgis
from PyQt4.QtGui import QColor

from qgis.core import QgsExpression, QgsStatisticalSummary, QgsSymbolV2,   QgsDataDefined
from qgis.core import QgsGraduatedSymbolRendererV2, QgsRuleBasedRendererV2, QgsMarkerSymbolV2, QgsRendererRangeV2, QgsGraduatedSymbolRendererV2

def validatedDefaultSymbol( geometryType ):
    symbol = QgsSymbolV2.defaultSymbol( geometryType )
    if symbol is None:
        if geometryType == QGis.Point:
            symbol = QgsMarkerSymbolV2()
        elif geometryType == QGis.Line:
            symbol =  QgsLineSymbolV2 ()
        elif geometryType == QGis.Polygon:
            symbol = QgsFillSymbolV2 ()
    return symbol

def makeSymbologyForRange( layer, min , max, title, color):
    symbol = validatedDefaultSymbol( layer.geometryType() )
    symbol.setColor( color )
    range = QgsRendererRangeV2( min, max, symbol, title )
    return range

def getSortedFloatsFromAttributeTable( layer, fieldName ):
    provider = layer.dataProvider()
    fieldIndex = provider.fieldNameIndex(fieldName)
    #provider.select( [fieldIndex] )
    values = []


    iter = layer.getFeatures()

    '''
    while iter.nextFeature( feature ):
        attrs = feat.attributes()
        values.append( feature.attributeMap()[fieldIndex].toFloat()[0] )

        values.append(attrs[fieldIndex].toFloat())
    '''

    for feat in layer.getFeatures():
        attrs = feat.attributes()
        #column = column + ";" + str(attrs[1])

        value = attrs[fieldIndex]

        try:
            suma = value + 1.5
        except:
            value =0


        values.append(value)

        #print attrs[1]

    values.sort()


    return values

def arbitaryColor( amount, max ):
    color = QColor()
    color.setHsv( 240 * amount / float( max - 1 ), 255, 255 )
    return color

def makeGraduatedRendererFromDivisionsList( layer, fieldName, divisions ):
    classes = len( divisions ) - 1
    rangeList = []
    for i in range( classes ):
        label = str( divisions[i] ) + " - " + str( divisions[i+1] )
        rangeList.append( makeSymbologyForRange( layer, divisions[i] , divisions[i+1], label, arbitaryColor( i, classes ) ) )
    renderer = QgsGraduatedSymbolRendererV2( fieldName, rangeList )
    renderer.setMode( QgsGraduatedSymbolRendererV2.Custom )
    return renderer

def applySymbologyEqualTotalValue( layer, classes, fieldName):
    values = getSortedFloatsFromAttributeTable( layer, fieldName )
    total = sum( values )
    step = total / float( classes )
    nextStep = step
    divisions = [ values[0] ]
    runningTotal = 0
    for value in values:
        runningTotal += value
        if runningTotal >= nextStep:
            divisions.append( value )
            nextStep += step
    if divisions[-1] != values[-1]:
        divisions.append(values[-1])
    renderer = makeGraduatedRendererFromDivisionsList( layer, fieldName, divisions )
    layer.setRendererV2( renderer )


def applyGraduatedSymbolRenderer(layer,  fieldName):
    renderer = QgsGraduatedSymbolRendererV2()
    renderer.setClassAttribute(fieldName)
    layer.setRendererV2(renderer)
    layer.rendererV2().updateClasses(layer, QgsGraduatedSymbolRendererV2.Jenks, 5)
    #layer.rendererV2().updateColorRamp(QgsGradientColorRamp(Qt.white, Qt.red))
'''

targetField = 'POP_OTHER'
classes = 3
layer = QgsVectorLayer( 'C:/data/ne_10m_populated_places.shp', 'Equal Total Value', 'ogr')
if layer.isValid():
    applySymbologyEqualTotalValue(layer, classes, targetField)
    QgsMapLayerRegistry.instance().addMapLayers( [layer] ) 
'''