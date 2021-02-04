#https://gis.stackexchange.com/questions/227876/finding-name-of-qgis-toolbar-in-python

from PyQt4.QtGui import QToolBar, QDockWidget, QMenuBar

# Get list of all ToolBars
for x in iface.mainWindow().findChildren(QToolBar):
    print x.objectName()