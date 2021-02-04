#https://webgeodatavore.github.io/pyqgis-samples/gui-group/QgsMapTool.html
# coding: utf-8
from PyQt4.QtCore import Qt
from qgis.gui import *
from qgis.utils import iface

try:
    from qgis.gui import QgsMapToolIdentify
except:
    from qgis.gui import QgsMapTool as QgsMapToolIdentify

from PyQt4 import QtGui


class SendPointToolCoordinates(QgsMapToolIdentify):
    """ Enable to return coordinates from clic in a layer.
    """
    def __init__(self, canvas, layer):
        """ Constructor.
        """
        QgsMapToolIdentify.__init__(self, canvas)
        self.canvas = canvas
        self.layer = layer
        self.setCursor(Qt.CrossCursor)


    '''    def canvasPressEvent(self, e):
        p = self.toMapCoordinates(e.pos())
        layers = self.canvas.layers()
        w = self.canvas.mapUnitsPerPixel() * 3
        rect = QgsRectangle(p.x()-w, p.y()-w, p.x()+w, p.y()+w)
        for layer in layers:
            if layer.type() == QgsMapLayer.RasterLayer:
                continue
            lRect = self.canvas.mapSettings().mapToLayerCoordinates(layer, rect)
            layer.select(lRect, False)
    '''

    def canvasReleaseEvent(self, event):

        '''if event.button() == Qt.RightButton:
            menu = QMenu()
            quitAction = menu.addAction("AnyAction")
            action = menu.exec_(self.canvas.mapToGlobal(QPoint(e.pos().x() + 5, e.pos().y())))
        '''

        '''
        popupMenu = QtGui.QMenu(self.canvas())

        popupMenu.addAction(QtGui.QAction("test", popupMenu))

        popupMenu.popup(self.canvas().mapToGlobal(event.pos())
        '''


        point = self.toLayerCoordinates(self.layer, event.pos())

        print(point.x(), point.y())

        p = self.toMapCoordinates(event.pos())
        layers = self.canvas.layers()
        w = self.canvas.mapUnitsPerPixel() * 3
        rect = QgsRectangle(p.x() - w, p.y() - w, p.x() + w, p.y() + w)
        for layer in layers:
            #if layer.type() == QgsMapLayer.RasterLayer:
            #    continue
            lRect = self.canvas.mapSettings().mapToLayerCoordinates(layer, rect)
            layer.select(lRect, False)

        '''
        results = self.identify(event.x(), event.y(), self.selectionMode, layer)

        if len(results) > 0:
           self.geomIdentified.emit(results[0].mLayer, QgsFeature(results[0].mFeature))
        

        try:

            # display_name="LYR"
            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName("popoliforpostgres")

            rlayer = layerExiste[0]  # primer elemento de la lista


            ident = rlayer.dataProvider().identify(QgsPoint(15.30, 40.98), \
                                               QgsRaster.IdentifyFormatValue)
            if ident.isValid():
                print ident.results()
        except:
            print " except LYR "
        '''

        '''if event.button() == Qt.RightButton:
            menu = QMenu()
            quitAction = menu.addAction("AnyAction")
            action = menu.exec_(self.canvas.mapToGlobal(QPoint(event.pos().x() + 5, event.pos().y())))
            '''

