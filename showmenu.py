from PyQt4.QtCore import Qt
from qgis.gui import QgsMapTool
from qgis.utils import iface

class showMenu(QgsMapTool):

def __init__(self, iface):
    print "init"

    canvas = iface.mapCanvas()
    QgsMapTool.__init__(self,canvas)
    self.canvas = canvas

def canvasPressEvent(self,e):
    print "canvasPressEvent"
    if e.button() == Qt.RightButton:
        menu = QMenu()
        quitAction = menu.addAction("AnyAction")
        action = menu.exec_(self.canvas.mapToGlobal(QPoint(e.pos().x()+5, e.pos().y())))