tablename = "popoliforpostgres"
geometrycol = "geom"
schema= "public"

from qgis.core import QgsVectorLayer, QgsDataSourceUri
uri = QgsDataSourceUri()
#uri.setConnection("localhost", "5432", "db", "user", "pass")
uri.setConnection("127.0.0.1", "5434", "popoli", "pgis", "pgis")
uri.setDataSource (schema, tablename, geometrycol)
#vlayer=QgsVectorLayer (uri .uri(False), tablename, "postgres")
QgsProject.instance().addMapLayer(vlayer)

'''
filename = "D:/repositorydef\SeismicRisk\python3/add_qgis3_layer.py"
filename = filename.replace("\\", "/")
exec(open(filename).read())
'''


LYR=QgsVectorLayer (uri .uri(False), tablename, "postgres")
index = LYR.dataProvider().fieldNameIndex('vulindex')
max = LYR.maximumValue(index)
min = LYR.minimumValue(index)

'''
attenzion .... these values are not condidered
'''
import numpy as np
values_0 = np.linspace(min, max, num=4)

# array([ 2.        ,  2.33333333,  2.66666667,  3.        ])

label1 = 'D1 ' + str(values_0[0]) + '-' + str(values_0[1])

label2 = 'D2 ' + str(values_0[1]) + '-' + str(values_0[2])

label3 = 'D3 ' + str(values_0[2]) + '-' + str(values_0[3])

values = (
    (label1, values_0[0], values_0[1], 'yellow'),
    (label2, values_0[1], values_0[2], 'blue'),
    (label3, values_0[2], values_0[3], 'green')

)



'''
values = (
    ('D1', 0, 1, 'yellow'),
    ('D2', 1.01, 2, 'blue'),
    ('D3', 2.01, 3, 'green'),
    ('D4', 3.01, 4, 'orange'),
    ('D5', 4.01, 5, 'gred')

)
'''

ranges = []
for label, lower, upper, color in values:
    symbol = QgsSymbol.defaultSymbol(LYR.geometryType())
    # symbol.setColor(QColor(color))
    rng = QgsRendererRanger(lower, upper, symbol, label)
    ranges.append(rng)

# create the renderer and assign it to a layer
expression = 'damage'  # field name
renderer = QgsGraduatedSymbolRenderer(expression, ranges)
# LYR.setRendererV2(renderer)

# https://gis.stackexchange.com/questions/207546/setting-marker-properties-using-scripts

# layer = qgis.utils.iface.activeLayer()


registry = QgsSymbolLayerV2Registry.instance()
symbol = QgsSymbol.defaultSymbol(LYR.geometryType())

#file="D:/repositorydef/SeismicRisk/python3/add_qgis3_layer.py"
#exec
