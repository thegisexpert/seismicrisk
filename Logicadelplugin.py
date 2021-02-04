#http://gis.stackexchange.com/questions/31789/how-to-set-#the-color-of-a-feature-depending-on-attributes-with-#pyqgis

from PyQt4.QtCore import *
from PyQt4.QtGui import *


def colorearlayer:
    #layer = iface.activeLayer()
    
    # define ranges: label, lower value, upper value, color name
    # in the field named 'random' (attributes table) 
    values = (
        ('Low', 1, 8, 'yellow'),
        ('Medium', 9, 16, 'green'),
        ('High', 17, 24, 'orange'),
    )
    
    print "adding layer"
    
    layer = QgsVectorLayer("C:/Data/Popoli/popoli2.shp", "layer_popoli", "ogr");
    
    #layer.setEditForm('C:/Data/Python/formametodologia.ui')
    
    layer.setEditForm('C:/Data/Python/qtdialog.ui')
    
    layer.setEditForm('C:/Data/Python/formametodologia.ui')
    #self.warn("seteat el metodo de forma metodologia" 
    
    layer.setEditFormInit('formametodologia.my_form_open')
    
    if not layer:
      print "Layer failed to load!"
    
    QgsMapLayerRegistry.instance().addMapLayer(layer)
    # create a category for each item in values
    ranges = []
    for label, lower, upper, color in values:
        symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
        symbol.setColor(QColor(color))
        rng = QgsRendererRangeV2(lower, upper, symbol, label)
        ranges.append(rng)
    
    # create the renderer and assign it to a layer
    expression = 'random' # field name
    renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
    layer.setRendererV2(renderer)
    
    iface.mapCanvas().refresh() 