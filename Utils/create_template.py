#https://gis.stackexchange.com/questions/56703/better-way-to-duplicate-a-layer-using-ogr-in-python/56722
'''
import shapefile

shape_path = "D:/Data/Dresden/shapefiles_dresden/gis.osm_buildings_v06.shp"


shape_path_new = "D:/Data/Dresden/new.shp"


r = shapefile.Reader(shape_path) # original shp file
w = shapefile.Writer()

w.fields = list(r.fields)
w._shapes.extend(r.shapes()) # copy over geometry without any changes
w.save(shape_path_new)
'''''


'''
uri = 'D:/Data/Fragility curves/FragilityCurves.xlsx'
layer = QgsVectorLayer(uri, 'test', 'ogr')

column = ""
for feat in layer.getFeatures():
    attrs = feat.attributes()
    column = column + ";" + str(attrs[1])
    print attrs[1]
'''


'''
path = "D:/repositorydef/SeismicRisk/Utils/create_template.py"
execfile(path)
'''
from PyQt4.QtCore import *
fname = "D:/Data/Dresden/shapefiles_dresden/gis.osm_buildings_v06.shp"

layer = QgsVectorLayer(fname, "testlayer", "ogr")
'''
for att in atributes:
    idx = layer.fieldNameIndex(att)
    print " \n Name " + str(idx) + ""

    if idx < 0:
        print  " Attribute " + att + " not found in the shapefile "
        completo = -1
'''

#https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/vector.html
'''
res = layer.dataProvider().addAttributes(
        [QgsField("mytext", QVariant.String),
        QgsField("myint", QVariant.Int)])

layer.updateFields()
print "ok"


fieldName= "mytext"

fieldIndex = layer.fieldNameIndex(fieldName)


field = layer.fields()[fieldIndex]

dictResults = {}
for feature in layer.getFeatures():
    context.setFeature(feature)
    result = '0'


    dictResults[feature.id()] = {fieldIndex: field.convertCompatible(result)}

layer.dataProvider().changeAttributeValues( dictResults )
'''


def changeFieldValues(fieldName, result):
    context = QgsExpressionContext()
    context.appendScope(QgsExpressionContextUtils.globalScope())
    context.appendScope(QgsExpressionContextUtils.projectScope())
    context.appendScope(QgsExpressionContextUtils.layerScope(layer))
    context.setFields(layer.fields())

    #fieldName = "myint"

    fieldIndex = layer.fieldNameIndex(fieldName)
    #if fieldIndex == -1:
    #    return
    field = layer.fields()[fieldIndex]

    dictResults = {}
    for feature in layer.getFeatures():
        context.setFeature(feature)
        #result = '0'

        dictResults[feature.id()] = {fieldIndex: field.convertCompatible(result)}

    layer.dataProvider().changeAttributeValues( dictResults )







atributes = [ "name",   "soil", "fault",  "fragility", "unitcost"]

completo = 1

for att in atributes:
    idx = layer.fieldNameIndex(att)
    print " \n Name " + str(idx) + ""

    if idx<0:
        print  " Attribute " + att + " not found in the shapefile "
        completo = -1

if completo<0:



    atributes = ["name", "soil", "fault", "fragility", "unitcost"]

    res = layer.dataProvider().addAttributes(
            [QgsField("name", QVariant.String),
            QgsField("soil", QVariant.Int),
            QgsField("fault", QVariant.Int),
             QgsField("fragility", QVariant.Int),
             QgsField("unitcost", QVariant.Int)])

    layer.updateFields()

    changeFieldValues(atributes[0], "")
    changeFieldValues(atributes[1], 0)
    changeFieldValues(atributes[2], 0)
    changeFieldValues(atributes[3], 0)
    changeFieldValues(atributes[4], 0)

    print "ok "

else:
    print " This file already have the requested attributes "