# -*- coding:utf-8 -*-
"""
/***************************************************************************
AutoFields
A QGIS plugin
Automatic attribute updates when creating or modifying vector features
                             -------------------
begin                : 2016-05-22 
copyright            : (C) 2016 by Germán Carrillo (GeoTux)
email                : gcarrillo@linuxmail.org 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from qgis.core import QgsApplication
from PyQt4.QtCore import ( Qt, QTranslator, QFileInfo, QCoreApplication, 
    QLocale, QSettings, QObject, SIGNAL )
from PyQt4.QtGui import QIcon, QAction, QDockWidget
import resources_rc
from SeismicRiskDockWidget import SeismicRiskDockWidget
from AutoFieldManager import AutoFieldManager
from MessageManager import MessageManager

from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QTimer
from PyQt4.QtGui import *
from PyQt4.QtGui import QAction, QIcon, QClipboard
from PyQt4 import uic
from qgis.core import *
from qgis.utils import plugins
from qgis.utils import plugins
from qgis.gui import QgsAttributeDialog
from functools import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from snappingdialog import snappingDialog
from identifygeometry import IdentifyGeometry
#from setdatasource import setDataSource
import os.path
from Database import Connection

try:

  from PyQt4.QtCore import QString
except ImportError:
  # we are using Python3 so QString is not defined
  QString = str


class SeismicRisk:

  def __init__( self, iface ):
    self.iface = iface
    self.messageMode = 'production' # 'production' or 'debug'
    self.language='en' 
    self.installTranslator()


    # Save reference to the QGIS interface
    self.iface = iface
    self.mapCanvas = iface.mapCanvas()
    self.utils = iface.mapCanvas().snappingUtils()
    # initialize plugin directory
    self.plugin_dir = os.path.dirname(__file__)
    #self.snapDlg = snappingDialog(iface)
    #self.DsDialog = setDataSource(iface)
    #self.tra = trace()
    #self.cb = QApplication.clipboard()


  def initGui( self ):

    self.messageManager = MessageManager(self.messageMode, self.iface)

    self.autoFieldManager = AutoFieldManager(self.messageManager, self.iface)
    self.autoFieldManager.readAutoFields()

    ''' if the widget is loaded .... then unlosad'''

    # Get list of all Dockwidgets
    existe = False
    for x in self.iface.mainWindow().findChildren(QDockWidget):
        name = x.objectName()

        if (name == "SeismicRiskDockWidget"):
            existe = True
            #self.iface.removeDockWidget(x)


    if (not existe):
        self.dockWidget = SeismicRiskDockWidget(self.iface.mainWindow(), self.iface, self.autoFieldManager,
                                             self.messageManager, self.language)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)

    self.actionDock = QAction(QIcon( ":/plugins/SeismicRisk/icon.png"), \
        "Seismic Risk plugin...", self.iface.mainWindow() )
    self.actionDock.triggered.connect( self.toggleDockWidget )



    # Add custom submenu to Vector menu
    self.iface.addPluginToVectorMenu( "&Seismic Risk ", self.actionDock )


    ''' section pick layers '''

    # icon_path = ':/plugins/pickLayer/icon.png'
    #icon_path = ':/plugins/PruebaAutoFields/icons/info.png'
    #icon_path = os.path.join(self.plugin_dir, "icons", "pickLayer.png")
    icon_path = os.path.join(self.plugin_dir, "icons", "points.png")

    # map tool action
    print " 66 iconpath " + icon_path
    self.mapToolAction = QAction(QIcon(icon_path), "Get seismic risk", self.iface.mainWindow())
    self.mapToolAction.setCheckable(True)


    self.mapTool = IdentifyGeometry(self.mapCanvas)
    self.mapTool.geomIdentified.connect(self.editFeature)

    self.mapTool.setAction(self.mapToolAction)
    self.mapToolAction.triggered.connect(self.setMapTool)
    #self.iface.addToolBarIcon(self.mapToolAction)
    self.iface.addPluginToMenu("&Pick to Layer in autofields", self.mapToolAction)

    '''  fin section pick layers'''
  
    # Remove Redo buttons from menus and toolbars, they can lead to crashes due 
    #   to a corrupted undo stack.
    redoActionList = [action for action in self.iface.advancedDigitizeToolBar().actions() if action.objectName() == u'mActionRedo']
    if redoActionList:
        self.iface.advancedDigitizeToolBar().removeAction( redoActionList[0] )
        self.iface.editMenu().removeAction( redoActionList[0] )    

    QSettings().setValue( "/shortcuts/Redo", "" ) # Override Redo shortcut

    # This block (2 options for disabling the Undo panel) didn't work
    #QSettings().setValue( '/UI/Customization/enabled', True )
    #QSettings( "QGIS", "QGISCUSTOMIZATION2" ).setValue( '/Customization/Panels/Undo', False )
    #undoDock = self.iface.mainWindow().findChild( QDockWidget, u'Undo' )
    #self.iface.removeDockWidget( undoDock )  
  
    # Create action that will start plugin configuration
    #self.action = QAction(QIcon( ":/plugins/AutoFields/icon.png"), "AutoFields plugin...", self.iface.mainWindow() )



    icon_path = os.path.join(self.plugin_dir, "icons", "lines.png")

    print " path " + icon_path

    self.action = QAction(QIcon(icon_path), "Seismic Risk plugin...", self.iface.mainWindow())

    #self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Show seismic Risk Calculator", self.mapToolAction)

    # connect the action to the run method
    self.action.triggered.connect( self.show )

    # Add a custom toolbar
    self.toolbar = self.iface.addToolBar("SeismicRisk")
    self.toolbar.setObjectName("SeismicRisk")
    self.toolbar.addAction(self.action)
    self.toolbar.addAction(self.mapToolAction)

    # Add custom submenu to Vector menu
    self.iface.addPluginToVectorMenu( "&AutoFields for calculating resilience", self.action )
    
    # Add a custom toolbar
    #self.toolbar = self.iface.addToolBar( "SeismicRisk" )
    #self.toolbar.setObjectName("SeismicRisk")
    self.messageManager = MessageManager( self.messageMode, self.iface )
    
    self.autoFieldManager = AutoFieldManager( self.messageManager, self.iface )
    self.autoFieldManager.readAutoFields()

    self.dockWidget = SeismicRiskDockWidget( self.iface.mainWindow(), self.iface, self.autoFieldManager, self.messageManager, self.language )
    self.iface.addDockWidget( Qt.RightDockWidgetArea, self.dockWidget )





    #QObject.connect(self.action, SIGNAL("triggered()"), self.mapToolInit)

    #http://planet.qgis.org/planet/user/12/tag/plugins/







  def run( self ):
    self.dockWidget.show()

  def  show(self):

    if self.dockWidget.isVisible():
        self.dockWidget.hide()
    else:
        self.dockWidget.show()

  def installTranslator( self ):
    userPluginPath = os.path.join( os.path.dirname( str( QgsApplication.qgisUserDbFilePath() ) ), "python/plugins/SeismicRisk" )
    systemPluginPath = os.path.join( str( QgsApplication.prefixPath() ), "python/plugins/SeismicRisk" )
    translationPath = ''

    locale = QSettings().value( "locale/userLocale", type=str )
    myLocale = str( locale[0:2] )
    if myLocale == 'es':
      self.language='es'

    if os.path.exists( userPluginPath ):
      translationPath = os.path.join( userPluginPath, 'i18n', "AutoFields_" + myLocale + ".qm" )
    else:
      translationPath = os.path.join( systemPluginPath, 'i18n', "AutoFields_" + myLocale + ".qm" )

    if QFileInfo( translationPath ).exists():
      self.translator = QTranslator()
      self.translator.load( translationPath )
      QCoreApplication.installTranslator( self.translator )

  '''
  errore qua
  
    def mapToolInit(self):
      print " here "
      canvas =  self.iface.mapCanvas()
      if self.action.isChecked() is False:
        canvas.unsetMapTool(self.mapTool)
        return
      self.action.setChecked(True)
      self.mapTool = IdentifyGeometry(canvas)
      QObject.connect(self.mapTool, SIGNAL("geomIdentified"), self.doSometing)
      canvas.setMapTool(self.mapTool)
      QObject.connect(canvas, SIGNAL("mapToolSet(QgsMapTool *)"), self.mapToolChanged)
      
  '''


  # metodos pick layers

  def editFeature(self, layer, feature):
    self.selectedLayer = layer
    self.selectedFeature = feature
    self.contextMenuRequest()
    pass


  def contextMenuRequest(self):
      contextMenu = QMenu()
      self.clipboardLayerAction = contextMenu.addAction("Layer: " + self.selectedLayer.name())
      '''
    if self.selectedLayer.type() == QgsMapLayer.VectorLayer:
      contextMenu.addSeparator()
      if self.selectedLayer.geometryType() == QGis.Point:
        pp = self.transformToCurrentSRS(self.selectedFeature.geometry().asPoint(), self.selectedLayer.crs())
        pg = self.transformToWGS84(self.selectedFeature.geometry().asPoint(), self.selectedLayer.crs())
        self.lonLat = str(round(pg.x(), 8)) + "," + str(round(pg.y(), 8))
        self.xy = str(round(pp.x(), 8)) + "," + str(round(pp.y(), 8))
        self.clipboardXAction = contextMenu.addAction("X: " + str(round(pp.x(), 2)))
        self.clipboardYAction = contextMenu.addAction("Y: " + str(round(pp.y(), 2)))
        self.clipboardXAction.triggered.connect(self.clipboardXYFunc)
        self.clipboardYAction.triggered.connect(self.clipboardXYFunc)
        self.clipboardLonAction = contextMenu.addAction("Lon: " + str(round(pg.x(), 6)))
        self.clipboardLatAction = contextMenu.addAction("Lat: " + str(round(pg.y(), 6)))
        self.clipboardLonAction.triggered.connect(self.clipboardLonLatFunc)
        self.clipboardLatAction.triggered.connect(self.clipboardLonLatFunc)
      elif self.selectedLayer.geometryType() == QGis.Line:
        self.leng = round(self.selectedFeature.geometry().length(), 2)
        bound = self.selectedFeature.geometry().boundingBox()
        self.clipboardNorthAction = contextMenu.addAction("North: " + str(round(bound.yMaximum(), 4)))
        self.clipboardSouthAction = contextMenu.addAction("South: " + str(round(bound.yMinimum(), 4)))
        self.clipboardEastAction = contextMenu.addAction("East: " + str(round(bound.xMinimum(), 4)))
        self.clipboardWestAction = contextMenu.addAction("West: " + str(round(bound.xMaximum(), 4)))
        self.clipboardLengAction = contextMenu.addAction("Length: " + str(self.leng))
        self.clipboardLengAction.triggered.connect(self.clipboardLengFunc)
      elif self.selectedLayer.geometryType() == QGis.Polygon:
        self.area = round(self.selectedFeature.geometry().area(), 2)
        self.leng = round(self.selectedFeature.geometry().length(), 2)
        bound = self.selectedFeature.geometry().boundingBox()
        self.clipboardNorthAction = contextMenu.addAction("North: " + str(round(bound.yMaximum(), 4)))
        self.clipboardSouthAction = contextMenu.addAction("South: " + str(round(bound.yMinimum(), 4)))
        self.clipboardEastAction = contextMenu.addAction("East: " + str(round(bound.xMinimum(), 4)))
        self.clipboardWestAction = contextMenu.addAction("West: " + str(round(bound.xMaximum(), 4)))
        self.clipboardLengAction = contextMenu.addAction("Perimeter: " + str(self.leng))
        self.clipboardLengAction.triggered.connect(self.clipboardLengFunc)
        self.clipboardAreaAction = contextMenu.addAction("Area: " + str(self.area))
        self.clipboardAreaAction.triggered.connect(self.clipboardAreaFunc)
    contextMenu.addSeparator()
    self.setCurrentAction = contextMenu.addAction(QIcon(os.path.join(self.plugin_dir, "icons", "mSetCurrentLayer.png")),
                                                  "Set current layer")
    self.hideAction = contextMenu.addAction(QIcon(os.path.join(self.plugin_dir, "icons", "off.png")), "Hide")
    self.openPropertiesAction = contextMenu.addAction(QIcon(os.path.join(self.plugin_dir, "icons", "settings.svg")),
                                                      "Open properties dialog")
    self.zoomToLayerAction = contextMenu.addAction(QIcon(os.path.join(self.plugin_dir, "icons", "zoomToLayer.png")),
                                                   "Zoom to layer extension")
    self.setCurrentAction.triggered.connect(self.setCurrentFunc)
    self.hideAction.triggered.connect(self.hideFunc)
    self.openPropertiesAction.triggered.connect(self.openPropertiesFunc)
    self.zoomToLayerAction.triggered.connect(self.zoomToLayerFunc)
    if self.selectedLayer.type() == QgsMapLayer.VectorLayer:
      print " 250 selected vector layer autofields "
      self.openAttributeTableAction = contextMenu.addAction(
        QIcon(os.path.join(self.plugin_dir, "icons", "mActionOpenTable.png")), "Open attribute table")
      self.openAttributeTableAction.triggered.connect(self.openAttributeTableFunc)
      self.setDataSourceAction = contextMenu.addAction(QIcon(os.path.join(self.plugin_dir, "icons", "dataSource.png")),
                                                       "Change Data source")
      self.setDataSourceAction.triggered.connect(self.setDataSourceFunc)
      contextMenu.addSeparator()
      self.zoomToFeatureAction = contextMenu.addAction(
        QIcon(os.path.join(self.plugin_dir, "icons", "zoomToFeature.png")), "Zoom to feature")
      self.zoomToFeatureAction.triggered.connect(self.zoomToFeatureFunc)
      if self.selectedLayer.isEditable():
        self.stopEditingAction = contextMenu.addAction(
          QIcon(os.path.join(self.plugin_dir, "icons", "mIconEditableEdits.png")), "Stop editing")
        self.stopEditingAction.triggered.connect(self.stopEditingFunc)
      else:
        self.startEditingAction = contextMenu.addAction(
          QIcon(os.path.join(self.plugin_dir, "icons", "mIconEditable.png")), "Start editing")
        self.startEditingAction.triggered.connect(self.startEditingFunc)
      self.utils.readConfigFromProject()
      # print self.iface, self.mapCanvas, self.utils, self.utils.SnapToMapMode()
      # if self.utils.SnapToMapMode() == QgsSnappingUtils.SnapAdvanced:
      # pass
      # self.snappingOptionsAction = contextMecreate_internu.addAction(QIcon(os.path.join(self.plugin_dir, "icons", "snapIcon.png")), "Snapping options")
      # self.snappingOptionsAction.triggered.connect(self.snappingOptionsFunc)
      if len(QgsApplication.clipboard().text().splitlines()) > 1:
        clipFeatLineTXT = QgsApplication.clipboard().text().splitlines()[1]
        clipFeatsTXT = clipFeatLineTXT.split('\t')
        self.clipAttrsFieldnames = QgsApplication.clipboard().text().splitlines()[0].split('\t')[1:]
        self.clipAttrsValues = clipFeatsTXT[1:]
        self.clipGeom = QgsGeometry.fromWkt(clipFeatsTXT[0])
        # if self.clipGeom.isGeosValid():
        if self.selectedLayer.isEditable() and self.clipGeom:
          self.pasteGeomAction = contextMenu.addAction(QIcon(os.path.join(self.plugin_dir, "icons", "pasteIcon.png")),
                                                       "Paste geometry on feature")
          self.pasteGeomAction.triggered.connect(self.pasteGeomFunc)
          self.pasteAttrsAction = contextMenu.addAction(QIcon(os.path.join(self.plugin_dir, "icons", "pasteIcon.png")),
                                                        "Paste attributes on feature")
          self.pasteAttrsAction.triggered.connect(self.pasteAttrsFunc)
      self.copyFeatureAction = contextMenu.addAction(QIcon(os.path.join(self.plugin_dir, "icons", "copyIcon.png")),
                                                     "Copy feature")
      self.copyFeatureAction.triggered.connect(self.copyFeatureFunc)
      '''
      self.attributeMenu = contextMenu.addMenu(QIcon(os.path.join(self.plugin_dir, "icons", "viewAttributes.png")),
                                               "Feature attributes view")
      self.populateAttributesMenu(self.attributeMenu)
      '''
      self.editFeatureAction = contextMenu.addAction(
        QIcon(os.path.join(self.plugin_dir, "icons", "mActionPropertyItem.png")), "Feature attributes edit")
      self.editFeatureAction.triggered.connect(self.editFeatureFunc)
      '''
      self.hazardAction = contextMenu.addAction(
        QIcon(os.path.join(self.plugin_dir, "icons", "viewAttributes.png")), "Hazard")

      self.hazardAction.triggered.connect(self.showHazard)

      self.vulnerabilityAction = contextMenu.addAction(
        QIcon(os.path.join(self.plugin_dir, "icons", "viewAttributes.png")), "Vulnerability")

      self.vulnerabilityAction.triggered.connect(self.showVulnerability)

      self.vulnerabilityAction = contextMenu.addAction(
          QIcon(os.path.join(self.plugin_dir, "icons", "viewAttributes.png")), "Loss")

      self.vulnerabilityAction.triggered.connect(self.showLoss)

      self.vulnerabilityAction = contextMenu.addAction(
          QIcon(os.path.join(self.plugin_dir, "icons", "viewAttributes.png")), " Edit Vulnerability")

      self.vulnerabilityAction.triggered.connect(self.editVulnerability)

      '''

      self.damageAction = contextMenu.addAction(
          QIcon(os.path.join(self.plugin_dir, "icons", "viewAttributes.png")), "Damage")

      self.damageAction.triggered.connect(self.showDamage)

      self.interdependeciesAction = contextMenu.addAction(
        QIcon(os.path.join(self.plugin_dir, "icons", "viewAttributes.png")), "Interdependencies")
      # self.attributeMenu.triggered.connect(self.calculateInterdependencies)

      self.interdependeciesAction.triggered.connect(self.calculateInterdependencies)

      self.editAction = contextMenu.addAction(
          QIcon(os.path.join(self.plugin_dir, "icons", "viewAttributes.png")), "Edit Values")
      # self.attributeMenu.triggered.connect(self.calculateInterdependencies)


      self.editAction.triggered.connect(self.abrirPopup)
      '''


      if self.selectedLayer.actions().listActions():
        actionOrder = 0
        contextMenu.addSeparator()
        for action in self.selectedLayer.actions().listActions():
          try:
            customIcon = action.icon()
          except:
            customIcon = QIcon(os.path.join(self.plugin_dir, "icons", "customAction.png"))
          newActionItem = contextMenu.addAction(customIcon, action.name())
          newActionItem.triggered.connect(partial(self.customAction, actionOrder))
          actionOrder += 1
      contextMenu.exec_(QCursor.pos())
      # fin metodos pick layers

      # https://github.com/NationalSecurityAgency/qgis-latlontools-plugin/blob/m# aster/latLonTools.py

  def abrirPopup(self):

      con = Connection()

      texto = QString(self.selectedFeature.attributes()[0])

      print " id selecr is " + texto

      from Writes import Writes

      wr = Writes()
      wr.writefile("C:/Data/Python/read.txt", texto);

      self.dockWidget.readDatabyId(texto)

      from QuickWKT.QuickWKTDialog import QuickWKTDialog
      self.QuickWKTDialog = QuickWKTDialog()
      self.QuickWKTDialog.show()

  def populateAttributesMenu(self, attributeMenu):
    field_names = [field.name() for field in self.selectedLayer.pendingFields()]
    for n in range(0, len(field_names)):
      fieldName = field_names[n]
      attributeValue = self.selectedFeature.attributes()[n]
      try:  # cut long strings
        self.attributeAction = attributeMenu.addAction("%s: %s" % (fieldName, attributeValue[:40]))
      except:
        self.attributeAction = attributeMenu.addAction("%s: %s" % (fieldName, attributeValue))
      self.attributeAction.triggered.connect(partial(self.copyToClipboard, attributeValue))


  def setMapTool(self):
    self.mapCanvas.setMapTool(self.mapTool)


  def zoomToFeatureFunc(self):
    featureBox = self.selectedFeature.geometry().boundingBox()
    p1 = self.transformToCurrentSRS(QgsPoint(featureBox.xMinimum(), featureBox.yMinimum()), self.selectedLayer.crs())
    p2 = self.transformToCurrentSRS(QgsPoint(featureBox.xMaximum(), featureBox.yMaximum()), self.selectedLayer.crs())
    print p1.x(), p1.y(), p2.x(), p2.y()
    self.mapCanvas.setExtent(QgsRectangle(p1.x(), p1.y(), p2.x(), p2.y()))
    self.mapCanvas.refresh()


  def zoomToLayerFunc(self):
    layerBox = self.selectedLayer.extent()
    p1 = self.transformToCurrentSRS(QgsPoint(layerBox.xMinimum(), layerBox.yMinimum()), self.selectedLayer.crs())
    p2 = self.transformToCurrentSRS(QgsPoint(layerBox.xMaximum(), layerBox.yMaximum()), self.selectedLayer.crs())
    print p1.x(), p1.y(), p2.x(), p2.y()
    self.mapCanvas.setExtent(QgsRectangle(p1.x(), p1.y(), p2.x(), p2.y()))
    self.mapCanvas.refresh()


  def setCurrentFunc(self):
    self.iface.setActiveLayer(self.selectedLayer)


  def setDataSourceFunc(self):
    self.DsDialog.changeDataSource(self.selectedLayer)


  def customAction(self, actionId):
    self.selectedLayer.actions().doActionFeature(actionId, self.selectedFeature)


  def hideFunc(self):
    self.iface.legendInterface().setLayerVisible(self.selectedLayer, False)


  def openPropertiesFunc(self):
    self.iface.showLayerProperties(self.selectedLayer)


  def openAttributeTableFunc(self):
    self.iface.showAttributeTable(self.selectedLayer)


  def copyToClipboard(self, copyValue):
    try:
      copytxt = unicode(copyValue)
    except:
      copytxt = str(copyValue)
    #self.cb.setText(copytxt)


  def clipboardXYFunc(self):
    self.cb.setText(self.xy)


  def clipboardLonLatFunc(self):
    self.cb.setText(self.lonLat)


  def clipboardLengFunc(self):
    self.cb.setText(str(self.leng))


  def clipboardAreaFunc(self):
    self.cb.setText(str(self.area))


  def stopEditingFunc(self):
    self.iface.setActiveLayer(self.selectedLayer)
    self.iface.actionToggleEditing().trigger()


  def startEditingFunc(self):
    self.iface.setActiveLayer(self.selectedLayer)
    self.iface.actionToggleEditing().trigger()


  def snappingOptionsFunc(self):
    self.snapDlg.getSnappingOptionsDialog(self.selectedLayer)


  def editFeatureFunc(self):
    self.iface.openFeatureForm(self.selectedLayer, self.selectedFeature, True)


  def copyFeatureFunc(self):
    bakActiveLayer = self.iface.activeLayer()
    self.iface.setActiveLayer(self.selectedLayer)
    self.selectedLayer.setSelectedFeatures([self.selectedFeature.id()])
    if 'attributePainter' in plugins:
      ap = plugins['attributePainter']
      ap.setSourceFeature(self.selectedLayer, self.selectedFeature)
      self.mapCanvas.setMapTool(self.mapTool)
      ap.apdockwidget.show()
    self.iface.actionCopyFeatures().trigger()
    self.iface.setActiveLayer(bakActiveLayer)


  def pasteGeomFunc(self):
    # self.selectedLayer.startEditing()
    # self.selectedFeature.setGeometry(self.clipGeom)
    self.selectedLayer.changeGeometry(self.selectedFeature.id(), self.clipGeom)
    self.selectedLayer.updateExtents()
    self.selectedLayer.setCacheImage(None)
    self.selectedLayer.triggerRepaint()


  def pasteAttrsFunc(self):
    for attrId in range(0, len(self.clipAttrsValues)):
      if self.selectedLayer.pendingFields().field(str(self.clipAttrsFieldnames[attrId])):
        self.selectedLayer.changeAttributeValue(self.selectedFeature.id(), attrId, self.clipAttrsValues[attrId])
  #https://github.com/NationalSecurityAgency/qgis-latlontools-plugin/blob/m# aster/latLonTools.py


  def transformToCurrentSRS(self, pPoint, srs):
      # transformation from provided srs to the current SRS
      crcMappaCorrente = self.iface.mapCanvas().mapRenderer().destinationCrs() # get current crs
      #print crcMappaCorrente.srsid()
      crsDest = crcMappaCorrente
      crsSrc = QgsCoordinateReferenceSystem(srs)
      xform = QgsCoordinateTransform(crsSrc, crsDest)
      return xform.transform(pPoint) # forward transformation: src -> dest

  def transformToWGS84(self, pPoint, srs):
      # transformation from the provided SRS to WGS84
      crsSrc = QgsCoordinateReferenceSystem(srs)
      crsDest = QgsCoordinateReferenceSystem(4326)  # WGS 84
      xform = QgsCoordinateTransform(crsSrc, crsDest)
      return xform.transform(pPoint) # forward transformation: src -> dest

  def calculateInterdependencies(self):
      print " calculate interdependencies 482 "
      self.calculateInterdependenciesbyid()
      self.dockWidget.PredictionModel.setCurrentIndex(6)
      #self.dockWidget.IdDamageComboBox_2.setCurrentIndex(2)

      ''' set combo box'''

      AllItems = [self.dockWidget.comboBoxFromLayer.itemText(i) for i in range(self.dockWidget.comboBoxFromLayer.count())]
      texto = QString(self.selectedFeature.attributes()[0])

      print " Items 492 " + str(texto)
      indice = 0
      num = 0

      for i in AllItems:

        print "comparing " + str(i) + " and " + texto

        try:



          if str(i).contains(texto):
            print " setted indice "
            indice = num

        except:
          print "comparing " + str(i) + " and " + texto
          print " exceot 513 "

        num = num + 1

      self.dockWidget.comboBoxFromLayer.setCurrentIndex(indice)
      ''' set combo box'''

  def showHazard(self):

     import PyQt4
     from PyQt4 import QtCore
     from PyQt4 import QtGui
     from PyQt4 import Qt



     self.dockWidget.PredictionModel.setCurrentIndex(1)
     self.dockWidget.hazardValueLineEdit.setText(QString(self.selectedFeature.attributes()[6]))
     #self.dockWidget.MomentumLineEdit.setText(QString(self.selectedFeature.attributes()[2]))
     self.dockWidget.RvalueLineEdit.setText(QString(self.selectedFeature.attributes()[4]))
     self.dockWidget.SoilLineEdit.setText(QString(self.selectedFeature.attributes()[5]))

     texto=QString(self.selectedFeature.attributes()[0])

     print " id selecr is " + texto

     AllItems = [self.dockWidget.IdHazardComboBox.itemText(i) for i in range(self.dockWidget.IdHazardComboBox.count())]

     print " Items 403 "
     indice = 0
     num = 0

     for i in AllItems:


        try:

         if str(i).startswith(texto):
           indice = num

        except:
          print " exceot 513 "

        num = num + 1


     self.dockWidget.IdHazardComboBox.setCurrentIndex(indice)

     id = self.selectedFeature.attributes()[0]
     self.dockWidget.addDistanceLayers(id)


  def showDamage(self):

     import PyQt4
     from PyQt4 import QtCore
     from PyQt4 import QtGui
     from PyQt4 import Qt




     self.dockWidget.PredictionModel.setCurrentIndex(4)

     try:
        self.dockWidget.lineEdit_3.setText(QString(self.selectedFeature.attributes()[2]))
     except:
         print ""

     texto=QString(self.selectedFeature.attributes()[0])

     print " id selecr is " + texto

     AllItems = [self.dockWidget.IdDamageComboBox_2.itemText(i) for i in range(self.dockWidget.IdDamageComboBox_2.count())]

     print " Items 403 "
     indice = 0
     num = 0

     for i in AllItems:


        try:

         if str(i).startswith(texto):
           indice = num

        except:
          print " exceot 513 "

        num = num + 1


     self.dockWidget.IdDamageComboBox_2.setCurrentIndex(indice)

  def showVulnerability(self):

     import PyQt4
     from PyQt4 import QtCore
     from PyQt4 import QtGui
     from PyQt4 import Qt




     self.dockWidget.PredictionModel.setCurrentIndex(2)
     #self.dockWidget.lineEdit_3.setText(QString(self.selectedFeature.attributes()[5]))
     texto=QString(self.selectedFeature.attributes()[0])

     print " id selecr is " + texto

     self.dockWidget.readDatabyId(texto)

     '''

     AllItems = [self.dockWidget.idVulnerabilityCurvesComboBox.itemText(i) for i in range(self.dockWidget.idVulnerabilityCurvesComboBox.count())]

     print " Items 403 "
     indice = 0
     num = 0

     for i in AllItems:


        try:

         if str(i).startswith(texto):
           indice = num

        except:
          print " exceot 513 "

        num = num + 1


     self.dockWidget.idVulnerabilityCurvesComboBox.setCurrentIndex(indice)
     '''

  def editVulnerability(self):

     import PyQt4
     from PyQt4 import QtCore
     from PyQt4 import QtGui
     from PyQt4 import Qt




     self.dockWidget.PredictionModel.setCurrentIndex(2)
     #self.dockWidget.lineEdit_3.setText(QString(self.selectedFeature.attributes()[5]))
     texto=QString(self.selectedFeature.attributes()[0])

     print " id selecr is " + texto

     self.dockWidget.readDatabyId(texto)

     '''
     uifile = os.path.join(os.path.dirname(__file__), 'youruifile.ui')

     uifile = "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\UI\\building.ui"

     uiinstance = uic.loadUi(uifile)
     uiinstance.exec_() 
     '''

     from zoomtopoint import ui_zoomtopoint

     '''

     QtGui.QDialog.__init__(self)
     # Set up the user interface from Designer.
     self.ui = Ui_ZoomToPoint()
     self.ui.setupUi(self)
     
     '''

     from QuickWKT.QuickWKTDialog import QuickWKTDialog

     self.QuickWKTDialog = QuickWKTDialog()
     self.QuickWKTDialog.id.setText(texto)
     self.QuickWKTDialog.show()

     '''

     from   zoomtopoint.ui_zoomtopoint import Ui_ZoomToPoint

     self.Ui_ZoomToPoint = Ui_ZoomToPoint()


     self.Ui_ZoomToPoint.run()
     '''

  def showLoss(self):

     import PyQt4
     from PyQt4 import QtCore
     from PyQt4 import QtGui
     from PyQt4 import Qt

     print " inside show loss "


     self.dockWidget.PredictionModel.setCurrentIndex(4)



  def calculateInterdependenciesbyid(self):

      print " calculate interdependencies 560 "
      from  PyQt4.QtCore import QSettings
      import Logica

      self.dockWidget.PredictionModel.setCurrentIndex(6)

      ''' set combo box'''

      AllItems = [self.dockWidget.comboBoxFromLayer.itemText(i) for i in range(self.dockWidget.comboBoxFromLayer.count())]
      texto = QString(self.selectedFeature.attributes()[0])

      id = texto

      print " Items 403 "
      indice = 0
      num = 0

      for i in AllItems:

        try:

          if str(i).startswith(texto):
            indice = num

        except:
          print " exceot 513 "

        num = num + 1

      self.dockWidget.comboBoxFromLayer.setCurrentIndex(indice)
      ''' set combo box'''

      s = QSettings()
      ## possible values are: prompt, useProject, useGlobal
      s.setValue("/Projections/defaultBehaviour", "useProject")

      idforshow = "1"

      id = str(self.selectedFeature.attributes()[0])

      print " 475 id es " + id

      Logica.calculateinterdependencyById(id)
      # init postgres
      # http://gis.stackexchange.com/questions/86983/how-to-properly-establish-a-postgresql-connection-using-qgscredentials


      uri = QgsDataSourceURI()
      # assign this information before you query the QgsCredentials data sQStringtore


      from Connection import Connection


      # maquina = " -h 127.0.0.1 -p 5434"

      con2 = Connection()

      con = con2.getConnection()

      uri.setConnection(con.host, con.port, con.database, con.user, con.password)
      connInfo = uri.connectionInfo()

      (success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

      if success:

        QgsCredentials.instance().put(connInfo, user, passwd)

        print " line 501 connect  "
        uri.setPassword(passwd)
        uri.setUsername(user)

        uri.setDataSource("public", "interdependencies", "geom")
        LYR = QgsVectorLayer(uri.uri(), "inter", "postgres")

        if (LYR.isValid()):
          print "Layer interdependencies valid"
        else:
          print  "Layer interdependencies not valid"

        display_name = "inter"
        layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

        try:
          QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # primer elemento de la lista
        except:
          print " except LYR "

        LYR.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))

        # QgsMapLayerRegistry.instance().addMapLayer(LYR)


        root = QgsProject.instance().layerTreeRoot()

        # mylayer = QgsVectorLayer("/Path/to/your/data.shp", "my layer", "ogr")

        QgsMapLayerRegistry.instance().addMapLayer(LYR, False)

        # root.addLayer(LYR)

        root.insertLayer(1, LYR)


        try:

          symbols = LYR.rendererV2().symbols()
          symbol = symbols[0]
          symbol.setColor(PyQt4.QtGui.QColor.fromRgb(255, 0, 0))

        except:

          print " reviewing the symbols of layers "


        self.iface.mapCanvas().refresh()


  def toggleDockWidget( self ):
    if self.dockWidget:
      if self.dockWidget.isVisible():
        self.dockWidget.hide()
      else:
        self.dockWidget.show()


  def unload( self ):
    # Remove the plugin menu and toolbar

    print " Running unload method "

    self.iface.removePluginVectorMenu( "&SeismicRisk", self.actionDock )
    self.iface.removePluginVectorMenu( "&SeismicRisk", self.mapToolAction )
    '''
    self.iface.removePluginVectorMenu( "&AutoFields", self.actionImport )
    '''
    self.iface.mainWindow().removeToolBar( self.toolbar )

    self.autoFieldManager.disconnectAll()

    self.dockWidget.disconnectAll()
    self.dockWidget.close()

    del self.toolbar

    # Get list of all Dockwidgets
    for x in self.iface.mainWindow().findChildren(QDockWidget):
        name = x.objectName()

        if (name=="SeismicRiskDockWidget"):
            self.iface.removeDockWidget(x)

    '''
    if self.dockWidget:
        if self.dockWidget.isVisible():
            self.dockWidget.hide()
        else:
            pass
            #self.dockWidget.show()
    self.iface.removeDockWidget( self.dockWidget )
    '''