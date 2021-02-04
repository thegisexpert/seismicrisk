#http://thebiobucket.blogspot.it/2015/10/qgis-processing-script-for-quick.html

7
from PyQt4.QtCore import *
from qgis.core import *
from qgis.utils import *

# ===============================================
##[User scripts]=group
##Gst_Nr=string
##Name_Layer=string 81127GST_V2
# ===============================================
# Gst_Nr is the field in which we are searching
# 81127GST_V2 is the default layer for searching
# ===============================================

canvas = iface.mapCanvas()

# First zoom to desired scale
#canvas.zoomScale(400)

Name_Layer = "buildingspopoliforpostgres"

allLayers = canvas.layers()
n = len(allLayers)
for i in range(0, n):
    if allLayers[i].name() == Name_Layer:
        break
tarL = allLayers[i]

# Get a featureIterator from an expression
#expr = QgsExpression("\"GNR\"='" + Gst_Nr + "'")
expr = QgsExpression("\"gid\"='146'")

it = tarL.getFeatures(QgsFeatureRequest(expr))

# Build a list of feature Ids from the result obtained above
ids = [j.id() for j in it]

# Select features with the ids
tarL.setSelectedFeatures(ids)

# Zoom to selected features
canvas.zoomToSelected(tarL)