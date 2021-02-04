

#docwidget definitivo
import sys

from Utils import Directory


pathsql = Directory.getPathSqlDir()
pathsql = pathsql.replace("SQL/", "")
print " pathsql " + pathsql
#sys.path.insert(0, "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database\\")
sys.path.insert(0, pathsql)

import resources_rc

from qgis.core import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui


from Ui_SeismicRisk_dock import Ui_SeismicRiskDockWidget
from ExpressionBuilderDialog import ExpressionBuilderDialog

from QuickWKT.QuickWKTDialog import QuickWKTDialog

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import Logica
from PointTool import PointTool

from symbol import except_clause
from __builtin__ import int
from osgeo.ogr import GetFieldTypeName

from Connection import Connection

import matplotlib
import numpy as np
'''import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
'''
import sys

import logging

import Directory
logdir = Directory.getPathTempDir()
filelog = logdir + "seismicrisk.log"
logging.basicConfig(filename=filelog,level=logging.DEBUG)


#import Logicadelplugin
from Logic.FragilityCurve import FragilityCurve

class SeismicRiskDockWidget( QDockWidget, Ui_SeismicRiskDockWidget ):
    """ Class in charge of all the UI logic """

    def __init__( self, parent, iface, autoFieldManager, messageManager, language='en' ):
        self.iface = iface
        self.msg = messageManager
        self.language = language
        QDockWidget.__init__( self, parent )
        # Set up the user interface from Designer.
        self.setupUi( self )



        self.autoFieldManager = autoFieldManager
        self.geometryDict = ['points','lines','polygons']
        self.fieldTypesDict = ['Integer','Real','String','Date']

        self.root = QgsProject.instance().layerTreeRoot()

        # UI stuff that wasn't set/initialized in Qt-Designer



        self.expressionDlg = None

        '''


        print " Populate comboBox "
        ids = Logica.readIds()

        idsstr = ids.split(";")
        for count in range(1,len(idsstr)):
             self.idComboBox.addItem(idsstr[count])

        print " Populate comboBox "



        print " Populate comboBox damage "
        #ids = Logica.readIds()

        idsstr = ids.split(";")
        for count in range(1, len(idsstr)):
            self.IdDamageComboBox_2.addItem(idsstr[count])

        print " Populate comboBox  damage "


        ids = Logica.readRoads()

        idsstr = ids.split(";")

        for count in range(0, len(idsstr)):
            self.comboBoxFromLayer.addItem(idsstr[count])

        print " Populate comboBox "
        ids = "Residential buildings; Roads; Hospitals; Fire stations"

        idsstr = ids.split(";")

        try:

            for count in range(0, len(ids)):
                self.typeLayerComboBox.addItem(idsstr[count])
        except:
            print "Data loaded?"

        print " Populate comboBox "
        ids = Logica.readIds()

        idsstr = ids.split(";")
        for count in range(1, len(idsstr)):
            self.IdHazardComboBox.addItem(idsstr[count])

        print " Populate comboBox "

        print " Populate comboBox "
        '''
        ids = "'';Level 1; Level 2; Level 3; Level 4"

        idsstr = ids.split(";")
        for count in range(1, len(idsstr)):
            self.levelDamagesComboBox.addItem(idsstr[count])

        print " Populate comboBox "



        '''
        ids = Logica.readTypeOfBuilding()

        idsstr = ids.split(";")
        
        '''

        '''for count in range(0, len(idsstr)):
            self.typeBuildingsVulnerabilityCurvesComboBox_2.addItem(idsstr[count])
        '''

        #hazard mlodels options



        '''self.hazardObjectsComboBox.addItem("")'''
        self.hazardObjectsComboBox.addItem("buildings")
        '''
        self.hazardObjectsComboBox.addItem("ramdoms")
        self.hazardObjectsComboBox.addItem("point")
        '''

        self.hazardModelComboBox.addItem("")
        self.hazardModelComboBox.addItem("model 1 (Soil)")
        self.hazardModelComboBox.addItem("model 2 (Not soil)")



        # About Tab

        self.resilienceButton.clicked.connect( self.calculateVulnerability )

        #self.resilienceButton.setVisible(False)


        #self.salvaButton.clicked.connect( self.saveData )

        #self.readButton.clicked.connect( self.readData)  ERASE

        #self.deleteButton.clicked.connect( self.deleteData)  EASE

        #self.deleteButton.clicked.connect(self.hideLayers)

        self.setNewConnectionButton.clicked.connect( self.setShapefilePath)

        self.setWorkingDirectorypushButton.clicked.connect(self.setWorkingDirectoryPath)

        #self.pushLayerButton.clicked.connect(self.updateLayerTable)

        self.createNewConnectionButton.clicked.connect(self.updateLayerTable)

        self.eraseLayerButton.clicked.connect(self.removeALLLayers)






        self.updateValutazione.clicked.connect(self.evaluateValutazione)

        #self.updateValutazione.setVisible(False)

        self.pushButton_Interdependencies.clicked.connect(self.calculateInterdependencies)

        #self.loadHazardButton.clicked.connect(self.calculateHazard)


        self.calculateHarzadPushButton_2.clicked.connect(self.addDamageLayers)

        #self.calculateHarzadPushButton.clicked.connect(self.viewHazardModel)


        #button save details of the hazard models
        #self.saveHazardModelButton.clicked.connect(self.viewHazardModel)

        self.LoadEpicenterpushButton.clicked.connect(self.loadEpicenter)

        self.alignLayerspushButton.clicked.connect(self.alignLayers)

        self.generateMapByCurveButton.clicked.connect(self.loadMapVulnerabilityCurves) #buutton generate map

        self.addFragilityCurveButton.clicked.connect(self.updateFragilityCurves)

        self.showAssignedFragilitiesButton.clicked.connect(self.showAssignedFragilities)

        self.assignFragilityPushButton.clicked.connect(self.assignFragilitiesToBuildings)

        self.deleteFragilityCurvesButton.clicked.connect(self.deleteFragilitiesCurves)

        self.updateCostAreaButton.clicked.connect(self.readCostTable)

        #self.updateCostAreaButton.setVisible(False)

        #self.populateTableMethodology()

        #self.leerAtributos(["uno", "dos", "tres"])

        self.leerResultadosMetodologia(["uno", "dos", "tres"])
        self.leerParametros(["uno", "dos", "tres"])

        self.disconnectButton.clicked.connect(self.disconnect)

        self.fragindexportButton.clicked.connect(self.exportFragilityIndicators)

        self.lossesImportButton.clicked.connect(self.importLoss)

        self.lossesExportButton.clicked.connect(self.exportLoss)

        #button of seismic prediction model

        self.fragindimportButton.clicked.connect(self.importFragilityIndicators)

        #button of fragilities curves

        self.importFragilitiesButton.clicked.connect(self.importFragilitiesAssignationToBuilding)

        self.exportFragilitiesButton.clicked.connect(self.exportFragilitiesAssignation)

        #self.updateCostAreaButton.clicked.connect(self.createLosses)

        from console import console
        console.show_console()



        self.saveHazardParametersPushButton.hide()

        self.tabinter.hide()

        '''
        
        The two buttons below are hidden because the tool make all calclucation 
        directly when the the user click over Load Epicenter
        '''

        self.calculateHazadPushButton.hide()

        self.loadHazardButton.hide()

        self.updateValutazione.hide()


        '''
        Adding of canvas listeners
        '''

        self.predictionmodelparameterslabel.hide()

        self.tableWidgetParameters.hide()
        self.widgetHazardValues.hide()

        self.widgetPredictionModelResults.hide()
        self.managerConnectionWidget.hide()
        self.importExportFragCurvesWidget.hide()
        self.managerConnectionWidget.hide()
        self.LossesConfigurationWidget.hide()

        self.fragilityCurvesResultsWidget.hide()



        print "por aqui "


        #self.iface.currentLayerChanged.connect(self.currentLayerChanged)  # aqui
        self.iface.mapCanvas().selectionChanged.connect(self.currentLayerChanged)  # aqui

        print "por aqui 2"
        

        from SendPointToolCoordinates import SendPointToolCoordinates
        layer, canvas = iface.activeLayer(), iface.mapCanvas()

        send_point_tool_coordinates = SendPointToolCoordinates(
            canvas,
            layer
        )
        canvas.setMapTool(send_point_tool_coordinates)

        print " updated canvas tool "

        #self.addVulnerabilibyCurveGraph()

        #self.addGraph()

        #self.vulnerability2tab.setDisabled(True)

        '''
        Hide vulnerability details while
        it's not finished
        '''

        #self.vulnerabilitydetailsttab.setVisible(False)

        self.PredictionModel.removeTab(3)


        self.PredictionModel.removeTab(6) # damage
        self.PredictionModel.removeTab(7) #general
        self.PredictionModel.removeTab(8) # interdependencies



        self.hazardModelWidget.setVisible(True)

        self.tabinter.setEnabled(False)

        self.layersTableView.setVisible(False)

        self.pushButton_4.setVisible(False)  #button for assigning fragilities
        self.assignedFragilitiesLinesEdit.setVisible(False) #not loading the fragilities from excel

        print " branch 2019 "



        try:



            onetoten = range(1, 5)
            for count in onetoten:
                print count


            for layer in self.iface.mapCanvas().layers():


                print " name " + str(layer.name()) +  ""



            for layer in self.iface.mapCanvas().layers():


                print " name " + str(layer.name()) + str(i) + ""
                if i==1:
                    print " name " + str(layer.name()) + str(i) + ""
                    self.iface.legendInterface().setLayerVisible(layer, False)

                if i==2:
                    print " name " + str(layer.name()) + str(i) + ""
                    self.iface.legendInterface().setLayerVisible(layer, False)

                i = i+1
        except:
            print("except hydding layers :", sys.exc_info())

        #import Writes as wr
        #wr.writefile("C:/Data/Python/read.txt", "ok from data python read txt")

        #self.QuickWKTDialog = QuickWKTDialog("safa")


        #self.QuickWKTDialog.show()


        self.PredictionModel.setTabEnabled(1, False)

        self.PredictionModel.setTabEnabled(2, False)

        self.PredictionModel.setTabEnabled(3, False)

        self.PredictionModel.setTabEnabled(4, False)

        self.PredictionModel.setTabEnabled(5, False)

        self.PredictionModel.setTabEnabled(6, False)

        '''
        hide the layers table view,
        because in tool is able to manage ne layer
        
        
        '''

        self.pushLayerButton.setVisible(False)

        self.eraseLayerButton.setVisible(False)

        self.updateLayerButton.setVisible(False)

        self.pushButton_4.setVisible(False)  # button for assigning fragilities
        self.assignedFragilitiesLinesEdit.setVisible(False)  # not loading the fragilities from excel


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

    def saveQueryAsShapefile(self):


        nomdatabase = self.getDatabasename()

        con.database = nomdatabase

        print " 617 I will load layer " + con.database

        uri = QgsDataSourceURI()

        # assign this information before you query the QgsCredentials data store
        uri.setConnection(con.host, con.port, nomdatabase, con.user, con.password)
        connInfo = uri.connectionInfo()

        # (success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

        success = True
        user = con.user
        passwd = con.password

        if success:
            QgsCredentials.instance().put(connInfo, user, passwd)

            uri.setPassword(passwd)
            uri.setUsername(user)
            # uri.setDataSource("public", "popoliforpostgres", "geom")

            nomdatabase = nomdatabase.lower()
            display_name = nomdatabase + "datos"

            uri.setDataSource("public", "datos", "geom")

            # display_name = "vulnerability" + earthquakeintensity

            # LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")

            print " uri es 647 " + uri.uri()

            LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")

            LYR.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))

            # Work with the layer (E.g. get feature count...)
            print "" + str(len(list(LYR.getFeatures())))
            print "suceess to load"


            error = QgsVectorFileWriter.writeAsVectorFormat(LYR, "C:/Data/Postgis/my_shapes.shp",
                                                                "4326", None,
                                                                "ESRI Shapefile")

            if error == QgsVectorFileWriter.NoError:
                print("success!")



            # display_name="LYR"
            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

            try:
                QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # primer elemento de la lista
            except:
                print " except remove layer "

            try:
                QgsMapLayerRegistry.instance().addMapLayer(LYR)

                # vl = QgsMapLayerRegistry.instance().mapLayersByName(display_name)[0]
                # self.iface.setActiveLayer(vl)

            except:
                print " except addinf layers name"
                import sys
                print("except lyr :", sys.exc_info())


            self.iface.mapCanvas().refresh()




    def viewHazardModel(self):
        print "in view hazard model"

        esta = self.hazardModelWidget.isVisible()

        if esta:
            self.hazardModelWidget.setVisible(False)
            texto = self.valuesHazardModelTextEdit.toPlainText()

            #self.loadEpicenter()
            momentum = self.MomentumLineEdit.text()

            if (momentum==""):
                momentum="1"
            else:

                try:
                    float(momentum)

                except ValueError:
                    print " momentum errato"
                    momentum = "1"

            Logica.updateHazardParameters(momentum, texto)

            self.addHazardLayers(0)
            self.addHazardLayers(1)
            self.addHazardLayers(2)
            self.addHazardLayers(3)
            self.addHazardLayers(-1)

        else:
            self.hazardModelWidget.setVisible(True)

        self.hazardModelTextEdit.setText("a + b*M + c*R + d*S")

        self.valuesHazardModelTextEdit.setText("a=0.098, b=0.11, c=0.98, d=0.67")

        print " 247 dopo  hazard model"

    def readData(self):

        num =self.idComboBox.currentText()

        num2 = num.split(",")

        id =0
        try:
          #id = int(num)
          id = int(num2[0])
        except:
          id =0

        print "id a seleccionar es " + str(id)

        databasename = self.getDatabasename()
        values2 = Logica.readData(databasename)

        values = values2.split(",")

        print " 245 " + values2

        self.leerResultadosMetodologia(values)

    def readDatabyId(self, id):


        print "id a seleccionar es " + str(id)

        databasename = self.getDatabasename()
        values2 = Logica.readData(id, databasename)




        values = values2.split(",")

        print " 245 " + values2

        self.leerResultadosMetodologia(values)


    def readData2(self):

        print " in read data "
        '''
        init postgres
        http://gis.stackexchange.com/questions/86983/how-to-properly-establish-a-postgresql-connection-using-qgscredentials
        '''

        uri = QgsDataSourceURI()
        # assign this information before you query the QgsCredentials data store


        from Connection import Connection

        #maquina = " -h 127.0.0.1 -p 5434"

        con2 = Connection()

        con = con2.getConnection()

        uri.setConnection(con.host, con.port, con.database, con.user, con.password)
        connInfo = uri.connectionInfo()

        #(success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

        success = True
        user = con.user
        passwd = con.password


        if success:

            QgsCredentials.instance().put(connInfo, user, passwd)
            uri.setPassword(passwd)
            uri.setUsername(user)
            uri.setDataSource("public", "popoliforpostgres", "geom")
            LYR = QgsVectorLayer(uri.uri(), "LYR", "postgres")

            # Work with the layer (E.g. get feature count...)
            print "" +str(len( list( LYR.getFeatures() ) ))


            print "suceess to load "

            display_name="LYR"
            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

            try:
                QgsMapLayerRegistry.instance().removeMapLayers( [layerExiste[0].id()] ) #primer elemento de la lista
            except:
                print " except LYR "

            QgsMapLayerRegistry.instance().addMapLayer(LYR)

            self.iface.mapCanvas().refresh()


            #self.iface.showAttributeTable(self.iface.activeLayer())



        # create a category for each item in values

        #colorear

        print " here \n \n \n \n \n \n \n \n \n \n "


        print "from Prueba  AutoFieldsDockQidget"

        print "adding layer addedsqlltitle"

        #layer = QgsVectorLayer("C:/Data/Popoli/popoli2.shp", "layer_popoli", "ogr");

        '''uri = QgsDataSourceURI()
        uri.setDatabase('C:/Data/Popoli/popolispatial.sqlite')
        schema = ''
        table = 'popolispatial'
        geom_column = 'geometry'
        uri.setDataSource(schema, table, geom_column)

        display_name = 'addedsqlltitle3'


        #erase the layer for not to add existing layes


        layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

        try:
            QgsMapLayerRegistry.instance().removeMapLayers( [layerExiste[0].id()] ) #primer elemento de la lista
        except:
            print " except "

        layer = QgsVectorLayer(uri.uri(), display_name, 'spatialite')

        if not layer:
          print "Layer failed to load!"

        #nit to adding sqlitle layer
        #QgsMapLayerRegistry.instance().addMapLayer(layer)

        self.iface.showAttributeTable(self.iface.activeLayer())



        self.iface.mapCanvas().refresh()
        '''

        values = (
            ('D1', 0, 1, 'yellow'),
            ('D2', 1.01, 2, 'green'),
             ('D3', 2.01, 3, 'green'),
        ('D4', 3.01, 4, 'orange'),
        ('D5', 4.01, 5, 'gred')

        )
        ranges = []
        for label, lower, upper, color in values:
            symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())
            symbol.setColor(QColor(color))
            rng = QgsRendererRangeV2(lower, upper, symbol, label)
            ranges.append(rng)

        # create the renderer and assign it to a layer
        expression = 'visibility' # field name
        renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
        LYR.setRendererV2(renderer)

        ##addung coloring also a postgres

        values2 = (
            ('D1', 0, 1, 'yellow'),
            ('D2', 1.01, 2, 'green'),
             ('D3', 2.01, 3, 'green'),
        ('D4', 3.01, 4, 'orange'),
        ('D5', 4.01, 5, 'gred')

        )
        ranges2 = []
        for label, lower, upper, color in values2:
            symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())
            symbol.setColor(QColor(color))
            rng = QgsRendererRangeV2(lower, upper, symbol, label)
            ranges2.append(rng)


        expression = 'damage' # field name
        renderer2 = QgsGraduatedSymbolRendererV2(expression, ranges2)
        LYR.setRendererV2(renderer2)


        selection=[]

        #num =self.idEdit.text()

        #num =self.idEdit.currentText()

        num =self.idComboBox.currentText()

        num2 = num.split(",")

        id =0
        try:
          #id = int(num)
          id = int(num2[0])
        except:
          id =0

        print "id a seleccionar es " + str(id)

        for feature in LYR.getFeatures():
            #geom = feature.geometry()
            selection.append(id)
            LYR.setSelectedFeatures(selection)

        #http://lists.osgeo.org/pipermail/qgis-developer/2015-January/036405.html
        '''
        id = self.idEdit.text()
        f = layer.getFeatures(QgsFeatureRequest(id)).next()
        r = QgsRubberBand(iface.mapCanvas())
        r.setColor(Qt.red)
        r.setToGeometry(f.geometry(), l)
        r.show()
        '''
        #self.iface.showAttributeTable(self.iface.activeLayer())

        #self.iface.showAttributeTable(LYR)


        self.iface.mapCanvas().refresh()



        #layer.setEditForm('C:/Data/Python/formametodologia.ui')

        #layer.setEditForm('C:/Data/Python/qtdialog.ui')

        #layer.setEditForm('C:/Data/Python/formametodologia.ui')
        #self.warn("seteat el metodo de forma metodologia"

        #self.iface.setActiveLayer(layer)

        print "Activatng layer from LOGICA plugin "

        #self.iface.zoomToActiveLayer()

        #layer.setEditFormInit('formametodologia.my_form_open')







        #self.leerResultadosMetodologia(values)

        #self.leerAtributos(values)


    def saveData2(self):

        s = self.attibutesEdit.toPlainText()


        #Logica.saveData(self.idEdit.text(), self.attibutesEdit.toPlainText() )

    def alignLayers(self):
        #import UtilitiesWidgets
        #UtilitiesWidgets.alignLayers()


        # https://gis.stackexchange.com/questions/26257/how-can-i-iterate-over-map-layers-in-qgis-python

        # qgis.utils.iface es self.iface
        layers = self.iface.legendInterface().layers()

        for layer in layers:
            layerType = layer.type()
            if layerType == QgsMapLayer.VectorLayer:
                print " new vector "
                layer.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))

        try:

            layer = layers[0]

            # self.canvas.setExtent(layer.extent())

            # qgis.utils.iface.mapCanvas().setExtent(layer.extent())

            vl = QgsMapLayerRegistry.instance().mapLayer(layer.id())
            print " name " + vl.name()
            canvas = self.iface.mapCanvas()
            canvas.setExtent(vl.extent())

            self.iface.setActiveLayer(vl)

            self.iface.zoomToActiveLayer()

        #borrar de aqui,  only for testing
        except:
            print "not found any layers"




    def leerAtributos(self, values):

         Ui_AutoFieldsDockWidget.leerAtributos(self, values)



    def saveData(self):


        allRows = self.tableViewMethodology.rowCount()
        data ="0"
        for row in xrange(0,allRows):
            #twi0 = self.ui.tableWidget.item(row,0)
            #twi1 = self.tableWidget.item(0,0)
            twi1 = self.tableViewMethodology.item(row,1)

            #twi2 = self.ui.tableWidget.cellWidget(row,2)
            #print twi0.text()+' '+twi1.currentText()+' '+twi2.currentText()
            print " text de la cell es (save data ) " + twi1.text()
            data = data + "," + twi1.text()


        #id = self.idEdit.text()

        text = self.idComboBox.currentText()  #idEdit

        id = text.split(",")
        Logica.saveData(id[0], data)
        '''
        num = int (id)

        es = num>0
        if es:
            Logica.saveData(id, data)
        else
            print " id en blanco" '''

    def deleteData(self):


        #Logica.deleteData(self.idEdit.text() )
        #Logica.addAttributesData()

        # descomentar las 2 siguientes

        #by now we are management 90 structures
        Logica.populateparameters(90)
        #Logica.populatehazard()

        #fin descomentar


        #Logica.updatevulnerability()
        #Logica.addBuildings()


        #self.cargaLayerIntoCanvasByType( "prueba7", "otrosql")

        self.saveQueryAsShapefile()


    def getDatabasename(self):


        '''
        
        
        :return: 
        
        namedatabase = self.connectionComboBox.currentText()

        if namedatabase=="":
            namedatabase="prueba7"


            raise Exception('the  name of the dabases is inkonown 961')
            
        '''


        from Utils import Directory
        # path_database = "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database"

        path_database = Directory.getPathScripts()

        sys.path.insert(0, path_database)

        import Writes

        path_current_database = Directory.getPathScripts() + "currentdatabases.txt"

        print " path_current_database "
        print path_current_database

        contens = Writes.readFile(path_current_database)

        namedatabase = contens[0]

        return namedatabase



    def updateDatabasename(self, namedatabase):


        if namedatabase=="":
            namedatabase="prueba7"


            raise Exception('the  name of the dabases is inkonown 961')


        from Utils import Directory
        #path_database = "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database"

        path_database  = Directory.getPathSqlDir()

        sys.path.insert(0, path_database)

        import Writes

        path_current_database = Directory.getPathSqlDir()  + "currentdatabases.txt"

        print " path_current_database "
        print path_current_database

        Writes.writefile(path_current_database, namedatabase)

        return  self.connectionComboBox.currentText()


    def exportFragilityIndicators(self):
        from Logic.PredictiveModel import PredictiveModel

        file_indicators = self.predictveIndicatorsLineEdit.text()
        file_indicators =file_indicators.replace("txt", "xls")


        database = self.getDatabasename()

        PredictiveModel.exportValutazioneToExcelv2( file_indicators)

        widget = self.iface.messageBar().createMessage("Fragilities indicators have been exported to workspace", 'Info')
        self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)



    def calculateVulnerability(self):


        #Logica.setData()

        #Logica.addVulnerabilityColumns()

        databasename =  self.getDatabasename()

        self.loadMetodologia(self.getDatabasename())
        #Logica.initvalues()  #init value populate valutazione

        self.importFragilityIndicators()

        from Logic.PredictiveModel import PredictiveModel
        #PredictiveModel.populateValutazione(databasename)




        PredictiveModel.updatevulnerabilityindex(databasename)
        PredictiveModel.updatevulnerabilityfactor(databasename)

        #filename = self.getDatabaseproject()
        filename = self.setWorkingDirectorylineEdit.text()

        print self.__class__.__name__
        print "1050"

        print "\n"
        print filename
        filename = filename + "/valutazione.csv"








        earthquakeintensity = ""



        try:

          earthquakeintensity  = self.predictiveModelLineEdit.text()
        except:
           earthquakeintensity ="0"

        if earthquakeintensity == "":
             earthquakeintensity = "0"

        '''allRows = self.tableViewMethodology.rowCount()
        data ="0"
        for row in xrange(0,allRows):
            #twi0 = self.ui.tableWidget.item(row,0)
            #twi1 = self.tableWidget.item(0,0)
            twi1 = self.tableViewMethodology.item(row,1)

            #twi2 = self.ui.tableWidget.cellWidget(row,2)
            #print twi0.text()+' '+twi1.currentText()+' '+twi2.currentText()
            print " text de la cell es (save data ) " + twi1.text()
            data = data + "," + twi1.text()
        '''
        print " ******************************************* earthquake intensity is " + earthquakeintensity + ""


        print " database of fdamage is " + self.getDatabasename()



        self.createDamage()
        PredictiveModel.updatedamage(earthquakeintensity, self.getDatabasename())



        self.addDamageLayers()

        #self.showFragilitiesInficators()


        #self.loadLayerIntoCanvas("prueba7", "popoliforpostgres")

        #layerExiste = QgsMapLayerRegistry.instance().mapLayersByName("prueba7popoliforpostgres")


        try:



            namegroup = "Vulnerability"

            vulnerability_name = "popoliforpostgres"
            self.loadLayerIntoCanvas( vulnerability_name, namegroup)

            #"prueba7popoliforpostgres"
            namedatabase = self.getDatabasename()
            #vulnerability_name = namedatabase + "popoliforpostgres"



            #layerExiste = QgsMapLayerRegistry.instance().mapLayersByName("prueba7popoliforpostgres")

            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(vulnerability_name)


            LYR = layerExiste[0]





            self.colorVulnerabilityMap( LYR)








            #LYR.loadNamedStyle("C:\Data\Python\Estilo\default\estilo2.qml")


            '''
            lYR.editFormConfig().setInitCodeSource(1)
            LYR.editFormConfig().setInitFilePath(python_file_path)
            LYR.setEditForm(ui_file_path
            LYR.setEditFormInit('formOpen')
            // fin comment inside coment
                 
            '''

            #LYR.editFormConfig().setInitCodeSource(1)
            #LYR.editFormConfig().setInitFilePath("D:\usbgis\apps\qgis2\qgisconfig\python\plugins\PruebaAutoFields\Ui_SeismicRisk_dock.ui")
            #LYR.setEditForm("D:/formas/Ui_SeismicRisk_dock.ui")
            #LYR.setEditForm("D:\usbgis\apps\qgis2\qgisconfig\python\plugins\PruebaAutoFields\Ui_SeismicRisk_dock.ui")
            #LYR.setEditFormInit('formOpen')


            targetField = 'vulfactor'
            classes = 5
            # layer = QgsVectorLayer('C:/data/ne_10m_populated_places.shp', 'Equal Total Value', 'ogr')
            if LYR.isValid():
                import QGISRenderer
                QGISRenderer.applySymbologyEqualTotalValue(LYR, classes, targetField)

                #QGISRenderer.applyGraduatedSymbolRenderer(LYR, targetField)   should work in v32

                QgsMapLayerRegistry.instance().addMapLayers([LYR])


            self.iface.mapCanvas().refresh()

            self.exportIntensityPredictiveModel()

        except:

            import sys

            print "Be carefull with layer popoliforpostgres", sys.exc_info()[0]

            print  sys.exc_info()[1]

            raise

    def colorVulnerabilityMap(self, LYR):



        index = LYR.dataProvider().fieldNameIndex('vulfactor')
        max = LYR.maximumValue(index)
        min = LYR.minimumValue(index)


        try:
            values_0 = np.linspace(min, max, num=4)

            label1 = 'V1 ' + str(values_0[0]) + '-' + str(values_0[1])

            label2 = 'V2 ' + str(values_0[1]) + '-' + str(values_0[2])

            label3 = 'V3 ' + str(values_0[2]) + '-' + str(values_0[3])

            values = (
                (label1, values_0[0], values_0[1], 'yellow'),
                (label2, values_0[1], values_0[2], 'blue'),
                (label3, values_0[2], values_0[3], 'green')

            )

            ranges = []
            for label, lower, upper, color in values:
                symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())
                # symbol.setColor(QColor(color))
                rng = QgsRendererRangeV2(lower, upper, symbol, label)
                ranges.append(rng)

            # create the renderer and assign it to a layer
            expression = 'vulfactor'  # field name
            # expression = 'damage'  # field name

            renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
            # LYR.setRendererV2(renderer)


            # prueba add symbol


            #
            fontStyle = {}

            fontStyle['color'] = '#000000'

            fontStyle['font'] = 'Webdings'

            fontStyle['chr'] = 'G'

            fontStyle['size'] = '6'

            symLyr1 = QgsFontMarkerSymbolLayerV2.create(fontStyle)

            renderer.symbols()[0].changeSymbolLayer(0, symLyr1)

            print " 747 setting font style by console"

            LYR.setRendererV2(renderer)
            LYR.triggerRepaint()


            # LYR.setRendererV2(renderer)


        except:

            print "Values not calculated"
            
        

    '''

    def exportFragilityIndicatorsv1(self):

        from Logic2.PredictiveModel import PredictiveModel

        databasename = self.getDatabasename()

        workingdir = self.setWorkingDirectorylineEdit.text()

        filenamein = workingdir + "fragilitiescsv.csv"
        filenameout = workingdir + "fragilities.xls"

        logging.debug("filenamein export")

        logging.debug(filenamein)


        logging.debug("filenameout export")

        logging.debug(filenameout)


        PredictiveModel.exportValutazioneToExcel(filenamein, databasename)
        from Utils import csvtoxls
        csvtoxls.exportToXLS(filenamein, filenameout)

        print " fragilities indicator exported to "
        print filenameout
        
    '''


    def importFragilityIndicators(self):

        from Logic.PredictiveModel import PredictiveModel

        databasename = self.getDatabasename()

        workingdir = self.setWorkingDirectorylineEdit.text()

        filenamein = workingdir + "fragilities.xls"




        PredictiveModel.deleteValutazione(databasename)
        #PredictiveModel.importValutazioneFromText(filenamein, databasename)

        print " 1326 databasename " +databasename

        ok = 1

        try:

            sqllist =PredictiveModel.importValutazioneFromExcelv2(filenamein, databasename)

        except:

            widget = self.iface.messageBar().createMessage("There is some incorrect dats with file frsafgili ind file",
                                                           'Info')
            self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)

            ok = -1

        if ok>0:
            widget = self.iface.messageBar().createMessage("Fragilities indicators have been imported from file", 'Info')
            self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)

    def exportLoss(self):

        #https://www.tutorialspoint.com/pyqt/pyqt_qfiledialog_widget.htm

        from Logic.LossModel import Loss

        databasename = self.getDatabasename()

        workingdir = self.setWorkingDirectorylineEdit.text()

        #filenamein = workingdir + "losscsv.csv"
        filenamein = workingdir + "losscsv.txt"
        filenameout = workingdir + "loss.csv"

        logging.debug("filenamein export")

        logging.debug(filenamein)

        logging.debug("filenameout export")

        logging.debug(filenameout)

        Loss.exportLossesToText(filenamein, databasename)

        from Utils import csvtoxls
        csvtoxls.exportToXLS(filenamein, filenameout)

        print " losses exported to "
        print filenameout

    def importLoss(self):

        from Logic.LossModel import Loss

        databasename = self.getDatabasename()

        workingdir = self.setWorkingDirectorylineEdit.text()

        filenamein = workingdir + "losscsv.txt"

        #Loss.deleteValutazione(databasename)


        Loss.deleteLoss(databasename)
        #Loss.importLossesFromText(filenamein, databasename)

        # just not forcing to load the losses from the file
        Loss.createLosses(databasename)
        #Loss.createIndexDamage(databasename)
        Loss.updateLoss(databasename)
        ''' pendiente read nuew values'''

        logging.debug("filenamein import")

        logging.debug(filenamein)

    def loadMapVulnerabilityCurves(self):

        from Logic.FragilityCurve import FragilityCurvesCalculation

        # Logica.setData()

        # Logica.addVulnerabilityColumns()

        databasename = self.getDatabasename()

        self.loadMetodologia(databasename)

        txtearthquakeintensity = ""

        earthquakeintensity =0




        # self.loadLayerIntoCanvas("prueba7", "popoliforpostgres")

        # layerExiste = QgsMapLayerRegistry.instance().mapLayersByName("prueba7popoliforpostgres")


        try:

            earthquakeintensity = self.earthquakeIntensityVulverabilityCurvesText.text()

            try:
                earthquakeintensity = float(earthquakeintensity)
            except:
                earthquakeintensity = 0


            if earthquakeintensity <= 0:
                #self.msg.show("Not loaded the hazard model, or the fragility curves", 'warning')

                widget = self.iface.messageBar().createMessage("The earthqkake intensity is not specified", 'Info')
                self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)





            txtnivel =self.levelDamagesComboBox.currentText()
            level=0

            if ("1" in txtnivel):
                level =1

            if ("2" in txtnivel):
                level = 2


            if ("3" in txtnivel):
                level =3


            if ("4" in txtnivel):
                level =4



            import random
            idfragility = random.randint(0, 1)

            idfragility = idfragility + 1

            print " 1009 " + str(idfragility)

            #Logica.showVulnerabilityValues( earthquakeintensity, vulnerabilidad, "prueba7", idfragility, 1, 0)

            working_dir = self.setWorkingDirectorylineEdit.text()

            from Logic import Common



            FragilityCurvesCalculation.createViewFragilityCurveStructures(level)

            #number_of_structures = Common.calculatenumberofstructures(databasename)

            number_of_structures = Common.calculatenumberofstructuresinfragilityview(databasename)

            if number_of_structures <= 0:
                #self.msg.show("Not loaded the hazard model, or the fragility curves", 'warning')

                widget = self.iface.messageBar().createMessage("The hazard model or the fragility curves are not loaded", 'Info')
                self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)

            if number_of_structures>0 and earthquakeintensity>0:

                self.removeLayerFromCanvas("popoliview_fragility_curve_structure")

                msg = "The program will analyze " + str(number_of_structures) + " structures. This will take a while "

                widget = self.iface.messageBar().createMessage(msg, 'Info')
                self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)

                '''

                for idstructure in range(0, number_of_structures):
                    # showVulnerabilityValues(pga, vulnerabilidad, databasename, idfragility, idlevel, gid, working_dir):7

                    try:
                        pga = FragilityCurvesCalculation.getHazardValue(databasename, idstructure)
                    except:

                        pga =0
                        import sys
                        print(" value of hazard not calculated ", sys.exc_info())

                    print "calculate  vulnerability of " + str(idstructure)

                    FragilityCurvesCalculation.updateVulnerabilityValues( pga,  databasename, idfragility, level, idstructure, working_dir)


                '''
                FragilityCurvesCalculation.updateVulnerabilityValuesLot(databasename)
                '''
                sql =  "select * "
                sql += "from fragility_values, fragility_curve_structure "
                sql += "where  fragility_values.gid=fragility_curve_structure.type_structure"
                
                '''



                self.loadLayerIntoCanvas( "view_fragility_curve_structure", "Vulnerability")

                self.loadLayerIntoCanvas( "view_fragility_curve_level", "Vulnerability")

                #https: // georepublic.info / en / blog / 2013 / joining - tables -with-sql - using - pyqgis /

                namelayer =  "view_fragility_curve_structure"


                layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(namelayer)


                try:
                    LYR = layerExiste[0]

                    '''
    
                    fid = 1  # the second feature (zero based indexing!)
                    iterator = layer.getFeatures(QgsFeatureRequest().setFilterFid(fid))
    
                    idx = LYR.fieldNameIndex('value')
    
                    for feature in iterator:
                        print "values "
                        print(feature.attributes()[0])
                        
                    '''




                    # Logicadelplugin.Colorearlayer()
                    # layer = iface.activeLayer()

                    # define ranges: label, lower value, upper value, color name
                    # in the field named 'random' (attributes table)
                    # layer = iface.activeLayer()

                    # define ranges: label, lower value, upper value, color name
                    # in the field named 'random' (attributes table)

                    #how to apply equal interval in qgis

                    #https://gis.stackexchange.com/questions/48613/how-to-apply-a-graduated-renderer-in-pyqgis

                    self.colorFragilitiesMap( LYR)

                    '''
                    lYR.editFormConfig().setInitCodeSource(1)
                    LYR.editFormConfig().setInitFilePath(python_file_path)
                    LYR.setEditForm(ui_file_path
                    LYR.setEditFormInit('formOpen')
                    // fin comment inside coment
        
                    '''

                    #if LYE.geometryType() == QGis.Point:

                    #LYR.loadNamedStyle('C:/Data/Python/Estilo/fragility.qml')
                    #LYR.triggerRepaint()

                    import Utils.RendererUtils as ru

                    ru.satramp(0, 255, 9 )


                    self.alignLayers()


                    self.iface.mapCanvas().refresh()

                    # LYR.editFormConfig().setInitCodeSource(1)
                    # LYR.editFormConfig().setInitFilePath("D:\usbgis\apps\qgis2\qgisconfig\python\plugins\PruebaAutoFields\Ui_SeismicRisk_dock.ui")
                    # LYR.setEditForm("D:/formas/Ui_SeismicRisk_dock.ui")
                    # LYR.setEditForm("D:\usbgis\apps\qgis2\qgisconfig\python\plugins\PruebaAutoFields\Ui_SeismicRisk_dock.ui")
                    # LYR.setEditFormInit('formOpen')

                    widget = self.iface.messageBar().createMessage("The fragilities curves have been calculated", 'Info')
                    self.iface.messageBar().pushWidget(widget, self.iface.messageBar().INFO)



                except:
                    '''
                    import sys

                    widget = self.iface.messageBar().createMessage("Please check the parameters of the fragilities", 'Info')
                    self.iface.messageBar().pushWidget(widget, self.iface.messageBar().ERROR)
                    '''

                    print "ok"

                    import sys
                    print("except valuazione_fragility :", sys.exc_info())


            self.iface.mapCanvas().refresh()


            '''
            try to write thre fragility curves in xls
            '''

            #Logica.readFragilityCurveData(idfragility, "prueba7")

            #uri = "/some/path/file.csv?delimiter=%s&xField=%s&yField=%s" % (";", "x", "y")
            #uri = "'D:/Data/Python/OtherFiles/somefile4.csv?delimiter=%s" % (",")

            pathd= self.getPathScripts()

            uri = "'" + pathd + "'OtherFiles/somefile4.csv?delimiter=%s'" % (",")

            #name = 'D:/Data/Python/OtherFiles/somefile4.csv'
            LYR = QgsVectorLayer(uri, "fragility_curves_used", 'delimitedtext')


            try:
                QgsMapLayerRegistry.instance().addMapLayer(LYR)

                # vl = QgsMapLayerRegistry.instance().mapLayersByName(display_name)[0]
                # self.iface.setActiveLayer(vl)

            except:
                print " except excel layer with fragility curves "
                import sys
                print("except lyr :", sys.exc_info())



            '''
            end try to write thre fragility curves in xls
            '''



        except :

            import sys
            print("Problem with layer popoliforpostgres vulnerabilityByFragility", sys.exc_info())
            raise

    def colorFragilitiesMap(self, LYR):
        import numpy as np

        # from Logic.FragilityCurve import FragilityCurvesCalculation

        # minmax = FragilityCurvesCalculation.readMinMaxFragilitiesValue(databasename)

        index = LYR.dataProvider().fieldNameIndex('value')

        max = LYR.maximumValue(index)
        min = LYR.minimumValue(index)

        values_0 = np.linspace(min, max, num=4)

        # array([ 2.        ,  2.33333333,  2.66666667,  3.        ])

        label1 = 'V1 ' + str(values_0[0]) + "- " + str(values_0[1])

        label2 = 'V2 ' + str(values_0[1]) + "- " + str(values_0[2])

        label3 = 'V3 ' + str(values_0[2]) + "- " + str(values_0[3])

        values = (
            (label1, values_0[0], values_0[1], 'yellow'),
            (label2, values_0[1], values_0[2], 'blue'),
            (label3, values_0[2], values_0[3], 'green')

        )

        '''

        values = (
            ('V1', 0, 0.45, 'yellow'),
            ('V2', 0.46, 0.56, 'blue'),
            ('V3', 0.57, 1, 'green')

        )
        '''

        ranges = []
        for label, lower, upper, color in values:
            symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())
            # symbol.setColor(QColor(color))
            rng = QgsRendererRangeV2(lower, upper, symbol, label)
            ranges.append(rng)

        # create the renderer and assign it to a layer
        # expression = 'vulfactor' # field name
        expression = 'value'  # field name

        renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
        # LYR.setRendererV2(renderer)


        # prueba add symbol


        #
        fontStyle = {}

        fontStyle['color'] = '#000000'

        fontStyle['font'] = 'Webdings'

        fontStyle['chr'] = 'G'

        fontStyle['size'] = '6'

        symLyr1 = QgsFontMarkerSymbolLayerV2.create(fontStyle)

        renderer.symbols()[0].changeSymbolLayer(0, symLyr1)

        print " 747 setting font style by console"

        LYR.setRendererV2(renderer)

    def setForm(self, nomlayer, pathform):

        try:


            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(nomlayer)

            #https: // gis.stackexchange.com / questions / 220392 / building - custom - form -for -qgis - in -python - plugin?rq=1
            layer = layerExiste[0]



            '''
            layer.editFormConfig().setInitCodeSource(1)
            python_file_path = 'C:\Users\AG\.qgis2\python\plugins\SeismicRisk\UI\\building.py'
            layer.editFormConfig().setInitFilePath(python_file_path)
            layer.setEditForm(pathform)
            #layer.setEditFormInit('formOpen')
            '''

            #layer.setEditForm(pathform)

            layer.setEditFormInit('formOpen')
        except:
            print " Not found the layer for setting form"


    def readValues(self):
        print "ok"





    def loadLayerIntoCanvas(self, nomtabla, namegroup):





        #layer = QgsVectorLayer("C:/Data/Popoli/popoli2.shp", "layer_popoli", "ogr");

        con2 = Connection()

        con = con2.getConnection()

        #con.database = nomdatabase




        uri = QgsDataSourceURI()
        nomdatabase =con.database

        print "\n"
        print " database is " + nomdatabase
        # assign this information before you query the QgsCredentials data store
        uri.setConnection(con.host, con.port, nomdatabase, con.user, con.password)


        connInfo = uri.connectionInfo()


        #(success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

        success = True
        user = con.user
        passwd = con.password

        if success:
            QgsCredentials.instance().put(connInfo, user, passwd)

            uri.setPassword(passwd)
            uri.setUsername(user)
            #uri.setDataSource("public", "popoliforpostgres", "geom")

            nomdatabase = nomdatabase.lower()
            #display_name = nomdatabase + nomtabla
            display_name =  nomtabla

            namegeom = "geom"

            uri.setDataSource("public", nomtabla,  namegeom)

            #display_name = "vulnerability" + earthquakeintensity

            #LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")

            print " uri es 647 " + uri.uri()

            LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")

            LYR.setCrs( QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId) )

            # Work with the layer (E.g. get feature count...)
            print "" +str(len( list( LYR.getFeatures() ) ))
            print "suceess to load "

            #display_name="LYR"
            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

            try:
                QgsMapLayerRegistry.instance().removeMapLayers( [layerExiste[0].id()] ) #primer elemento de la lista
            except:
                print " except remove layer "


            try:
                QgsMapLayerRegistry.instance().addMapLayer(LYR, False)

                #lyr = QgsMapLayerRegistry.instance().mapLayersByName("hazard")[0]
                root = QgsProject.instance().layerTreeRoot()
                # myGroup1 = root.addGroup("My Group 1")
                # If you want to add it to a particular position in the ToC, use:



                myGroup1 = root.findGroup(namegroup)

                if myGroup1 is None:

                    myGroup1 = root.insertGroup(0, namegroup)

                root = myGroup1.insertLayer(0, LYR)

                #vl = QgsMapLayerRegistry.instance().mapLayersByName(display_name)[0]
                #self.iface.setActiveLayer(vl)

            except:
                print " except addinf layers name"
                import sys
                print("except lyr :", sys.exc_info())

            '''
            import MyWnd
            w = MyWnd.MyWnd(self.iface.mapCanvas())
            w.show()
            '''


            self.iface.mapCanvas().refresh()



            ''' remove and add again for udepate in the qgis view '''


            # self.iface.showAttributeTable(self.iface.activeLayer())



            #add layer sqlitle3
            #QgsMapLayerRegistry.instance().addMapLayer(layer)
            # create a category for each item in values
            '''
            ranges = []
            for label, lower, upper, color in values:
                symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())
                #symbol.setColor(QColor(color))
                rng = QgsRendererRangeV2(lower, upper, symbol, label)
                ranges.append(rng)

            # create the renderer and assign it to a layer
            expression = 'damage' # field name
            renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
            LYR.setRendererV2(renderer)
            
            

            // comment inside coment 
            lYR.editFormConfig().setInitCodeSource(1)
            LYR.editFormConfig().setInitFilePath(python_file_path)
            LYR.setEditForm(ui_file_path
            LYR.setEditFormInit('formOpen')
            // fin comment inside coment

            LYR.editFormConfig().setInitCodeSource(1)
            #LYR.editFormConfig().setInitFilePath("D:\usbgis\apps\qgis2\qgisconfig\python\plugins\PruebaAutoFields\Ui_SeismicRisk_dock.ui")
            LYR.setEditForm("D:/formas/Ui_SeismicRisk_dock.ui")
            #LYR.setEditForm("D:\usbgis\apps\qgis2\qgisconfig\python\plugins\PruebaAutoFields\Ui_SeismicRisk_dock.ui")
            #LYR.setEditFormInit('formOpen')



            self.iface.mapCanvas().refresh()
            '''

            return LYR




    def removeLayerFromCanvas(self, name):

        layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(name)

        try:
            QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # primer elemento de la lista
        except:
            print " except remove layer "

    def cargaLayerIntoCanvasByType(self, nomdatabase, type):

        # Logicadelplugin.Colorearlayer()
        # layer = iface.activeLayer()

        # define ranges: label, lower value, upper value, color name
        # in the field named 'random' (attributes table)
        # layer = iface.activeLayer()

        # define ranges: label, lower value, upper value, color name
        # in the field named 'random' (attributes table)
        values = (
            ('D1', 0, 1, 'yellow'),
            ('D2', 1.01, 2, 'blue'),
            ('D3', 2.01, 3, 'green'),
            ('D4', 3.01, 4, 'orange'),
            ('D5', 4.01, 5, 'gred')

        )
        print "from Prueba  AutoFieldsDockQidget"

        print "adding layer addedsqlltitle"

        # layer = QgsVectorLayer("C:/Data/Popoli/popoli2.shp", "layer_popoli", "ogr");

        con.database = nomdatabase

        print " 617 I will load layer " + con.database

        uri = QgsDataSourceURI()
        # assign this information before you query the QgsCredentials data store
        uri.setConnection(con.host, con.port, nomdatabase, con.user, con.password)
        connInfo = uri.connectionInfo()
        # (success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

        success = True
        user = con.user
        passwd = con.password

        if success:
            QgsCredentials.instance().put(connInfo, user, passwd)

            uri.setPassword(passwd)
            uri.setUsername(user)
            # uri.setDataSource("public", "popoliforpostgres", "geom")

            nomdatabase = nomdatabase.lower()
            display_name = nomdatabase + type


            display_name = display_name.replace("1", "schools")
            display_name = display_name.replace("2", "chiesa")
            display_name = display_name.replace("3", "hospital")
            display_name = display_name.replace("4", "res_building")
            display_name = display_name.replace("5", "industry")



            uri.setDataSource("public", "popoliforpostgres", "geom", type)

            #otrosql =  "type=" + type

            #uri.setDataSource("public", "popoliforpostgres", "geom", otrosql)

            # display_name = "vulnerability" + earthquakeintensity

            # LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")

            print " uri es 647 " + uri.uri()

            LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")
            LYR.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))

            # Work with the layer (E.g. get feature count...)
            print "" + str(len(list(LYR.getFeatures())))
            print "suceess to load "

            # display_name="LYR"
            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

            try:
                QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # primer elemento de la lista
            except:
                print " except remove layer "

            try:
                QgsMapLayerRegistry.instance().addMapLayer(LYR)

                # vl = QgsMapLayerRegistry.instance().mapLayersByName(display_name)[0]
                # self.iface.setActiveLayer(vl)

            except:
                print " except addinf layers name"
                import sys
                print("except lyr :", sys.exc_info())

            '''
            import MyWnd
            w = MyWnd.MyWnd(self.iface.mapCanvas())
            w.show()
            '''

            self.iface.mapCanvas().refresh()

            ''' remove and add again for udepate in the qgis view '''

            #self.iface.showAttributeTable(self.iface.activeLayer())

            self.iface.mapCanvas().refresh()

            # add layer sqlitle3
            # QgsMapLayerRegistry.instance().addMapLayer(layer)
            # create a category for each item in values
            '''
            ranges = []
            for label, lower, upper, color in values:
                symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())
                #symbol.setColor(QColor(color))
                rng = QgsRendererRangeV2(lower, upper, symbol, label)
                ranges.append(rng)

            # create the renderer and assign it to a layer
            expression = 'damage' # field name
            renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
            LYR.setRendererV2(renderer)

            // comment inside coment 
            lYR.editFormConfig().setInitCodeSource(1)
            LYR.editFormConfig().setInitFilePath(python_file_path)
            LYR.setEditForm(ui_file_path
            LYR.setEditFormInit('formOpen')
            // fin comment inside coment

            LYR.editFormConfig().setInitCodeSource(1)
            #LYR.editFormConfig().setInitFilePath("D:\usbgis\apps\qgis2\qgisconfig\python\plugins\PruebaAutoFields\Ui_SeismicRisk_dock.ui")
            LYR.setEditForm("D:/formas/Ui_SeismicRisk_dock.ui")
            #LYR.setEditForm("D:\usbgis\apps\qgis2\qgisconfig\python\plugins\PruebaAutoFields\Ui_SeismicRisk_dock.ui")
            #LYR.setEditFormInit('formOpen')



            self.iface.mapCanvas().refresh()
            '''

    def populateLayersTable( self, foo=None, foo2=None, foo3=None ):
        """ List vector layers that support changes in attributes and are writable.
            Arguments are 3 and optional because this function listens to several
            SIGNALs.
        """




        # Initialize Layers Table
        self.tblLayers.clearContents()
        self.tblLayers.setRowCount( 0 )

        vLayers = []
        for layer in QgsMapLayerRegistry.instance().mapLayers().values():
            if layer.type() == QgsMapLayer.VectorLayer:
                if layer.dataProvider().capabilities() & QgsVectorDataProvider.ChangeAttributeValues:
                    if not layer.isReadOnly():
                        if layer.geometryType() < 3: # Avoid UnknownGeometry and NoGeometry
                            vLayers.append( layer )

        self.tblLayers.setRowCount( len( vLayers ) )
        self.tblLayers.setColumnCount( 3 )

        self.tblLayers.setSortingEnabled( False )
        for row, lyr in enumerate( vLayers ):
            item = QTableWidgetItem( QIcon( ":/plugins/AutoFields/icons/" + \
                self.geometryDict[lyr.geometryType()] + ".png"),
                str( lyr.geometryType() ) )
            self.tblLayers.setItem( row, 0, item )

            item = QTableWidgetItem( lyr.name() )
            item.setData( Qt.UserRole, lyr.id() )
            self.tblLayers.setItem( row, 1, item )

            tmpTreeLayer = self.root.findLayer( lyr.id() )
            if tmpTreeLayer:
                group = tmpTreeLayer.parent().name()
                self.tblLayers.setItem(row, 2,
                    QTableWidgetItem( group if group else QApplication.translate("AutoFieldsDockWidgetPy",
                        "< root >" ) ) )

        self.tblLayers.setSortingEnabled( True )


    def updateFieldAndExpressionControls( self ):
        """ After a selection is changed, reflect possible values in field controls """
        self.msg.show( "New selection " + str(len( self.tblLayers.selectedItems() ) / 3), 'info', True )

        if not self.tblLayers.selectedItems():
            self.frameFields.setEnabled( False )
            self.frameExpression.setEnabled( False )
            return
        else:
            self.frameFields.setEnabled( True )
            self.frameExpression.setEnabled( True )

        # List common fields in cboField and get geometries selted
        geometryTypeSet = self.updateFieldList()


        # Update expression controls
        if 0 in geometryTypeSet and len( geometryTypeSet ) == 1: # Points
            self.optXCoord.setEnabled( True )
            self.optYCoord.setEnabled( True )
            self.optLength.setEnabled( False )
            self.optPerimeter.setEnabled( False )
            self.optArea.setEnabled( False )
        elif 1 in geometryTypeSet and len( geometryTypeSet ) == 1: # Lines
            self.optXCoord.setEnabled( False )
            self.optYCoord.setEnabled( False )
            self.optLength.setEnabled( True )
            self.optPerimeter.setEnabled( False )
            self.optArea.setEnabled( False )
        elif 2 in geometryTypeSet and len( geometryTypeSet ) == 1: # Polygons
            self.optXCoord.setEnabled( False )
            self.optYCoord.setEnabled( False )
            self.optLength.setEnabled( False )
            self.optPerimeter.setEnabled( True )
            self.optArea.setEnabled( True )
        else:
            self.optXCoord.setEnabled( False )
            self.optYCoord.setEnabled( False )
            self.optLength.setEnabled( False )
            self.optPerimeter.setEnabled( False )
            self.optArea.setEnabled( False )

        if not self.btnGroup.checkedButton().isEnabled():
            self.optCustomExpression.setChecked( True ) # Default selection
            self.updateExpressionControls( self.optCustomExpression )

        self.expressionDlg = None # Initialize the dialog


    def updateFieldList( self ):
        """ Update field list and return geometries selected """
        commonFields = []
        geometryTypeSet = set()
        bFirstFlag = True
        for item in self.tblLayers.selectedItems():
            if item.column() == 1: # It's the layer name item
                self.msg.show( "ID " + item.data( Qt.UserRole ), 'info', True ) # Get layer id
                layer = QgsMapLayerRegistry.instance().mapLayer( item.data( Qt.UserRole ) )
                geometryTypeSet.add( layer.geometryType() )
                tmpFields = [field.name() for field in layer.dataProvider().fields()] # Get field names stored in the provider
                if bFirstFlag: # Initialize commonFields
                    commonFields = tmpFields
                    bFirstFlag = False
                else: # Intersect fields
                    if commonFields: # Avoid intersecting if no common fields
                        commonFields = list( set( commonFields ) & set( tmpFields ) )

        commonFields.sort()
        self.msg.show( "FIELDS: "+ str(commonFields), 'info', True)

        self.cboField.clear()
        if not commonFields:
            self.optExistingField.setEnabled( False )
            self.optNewField.setChecked( True )
        else:
            self.optExistingField.setEnabled( True )
            self.cboField.addItems( commonFields )

        return geometryTypeSet


    def newFieldToggled( self ):
        """ Alternate between controls of new field and existing field """
        newIsChecked = self.optNewField.isChecked()

        self.cboField.setEnabled( not newIsChecked )

        self.lblFieldName.setEnabled( newIsChecked )
        self.lblFieldType.setEnabled( newIsChecked )
        self.txtFieldName.setEnabled( newIsChecked )
        self.cboFieldType.setEnabled( newIsChecked )

        if newIsChecked:
            self.fieldTypeChanged( self.cboFieldType.currentIndex() )
        else:
            self.lblFieldLength.setEnabled( newIsChecked )
            self.lblFieldPrecision.setEnabled( newIsChecked )
            self.txtFieldLength.setEnabled( newIsChecked )
            self.txtFieldPrecision.setEnabled( newIsChecked )

        self.expressionDlg = None # Initialize the dialog


    def fieldTypeChanged( self, idx ):
        """ Update field length and field precision controls' state and values """
        text = self.fieldTypesDict[idx]
        if text == 'Integer':
            self.txtFieldLength.setRange( 1, 10 )
            self.txtFieldLength.setEnabled( True )
            self.txtFieldPrecision.setEnabled( False )
            self.lblFieldLength.setEnabled( True )
            self.lblFieldPrecision.setEnabled( False )
        elif text == 'Real':
            self.txtFieldLength.setRange( 1, 20 )
            self.txtFieldPrecision.setRange( 0, 15 )
            self.txtFieldLength.setEnabled( True )
            self.txtFieldPrecision.setEnabled( True )
            self.lblFieldLength.setEnabled( True )
            self.lblFieldPrecision.setEnabled( True )
        elif text == 'String':
            self.txtFieldLength.setRange( 1, 255 )
            self.txtFieldLength.setEnabled( True )
            self.txtFieldPrecision.setEnabled( False )
            self.lblFieldLength.setEnabled( True )
            self.lblFieldPrecision.setEnabled( False )
        else: # Date
            self.txtFieldLength.setEnabled( False )
            self.txtFieldPrecision.setEnabled( False )
            self.lblFieldLength.setEnabled( False )
            self.lblFieldPrecision.setEnabled( False )


    def fieldChanged( self, idx ):
        """ Just to initialize the expression dialog if selected field changes """
        self.expressionDlg = None # Initialize the dialog


    def saveAutoField( self ):
        """ Do some validation and then call AutoFieldManager """

        # Check layers
        if not self.tblLayers.selectedItems():
            self.msg.show( QApplication.translate( "AutoFieldsDockWidgetPy",
                "[Warning] Please first select a layer." ), 'warning' )
            return

        # Check expression
        expression = u''
        if self.optXCoord.isChecked():
            expression = u'$x'
        elif self.optYCoord.isChecked():
            expression = u'$y'
        elif self.optLength.isChecked():
            expression = u'$length'
        elif self.optPerimeter.isChecked():
            expression = u'$perimeter'
        elif self.optArea.isChecked():
            expression = u'$area'
        elif self.optDate.isChecked():
            expression = u'now()'
        elif self.optCustomExpression.isChecked():
            if self.expressionDlg:
                expression = self.expressionDlg.expression
            if not self.expressionDlg or not expression:
                self.msg.show( QApplication.translate( "AutoFieldsDockWidgetPy",
                    "[Warning] Please first set a valid custom expression." ),
                    'warning' )
                return
        else: # optSpatialValue
            pass

        # Check fields
        fieldName = ''
        if self.optNewField.isChecked():
            if self.txtFieldName.text():

                fieldName = self.txtFieldName.text().strip()
                newField = QgsField( fieldName,
                    self.cboFieldType.itemData( self.cboFieldType.currentIndex(), Qt.UserRole) )

                length = self.txtFieldLength.value()
                precision = self.txtFieldPrecision.value()
                # Ensure length and precision are valid values when dealing with Real numbers
                if self.fieldTypesDict[self.cboFieldType.currentIndex()] == 'Real':
                    if precision > length:
                        precision = length
                newField.setLength( length )
                newField.setPrecision( precision )

                for item in self.tblLayers.selectedItems():
                    if item.column() == 1: # It's the layer name item
                        layer = QgsMapLayerRegistry.instance().mapLayer( item.data( Qt.UserRole ) )
                        if layer.fieldNameIndex( fieldName ) != -1:
                            self.msg.show(
                                QApplication.translate( "AutoFieldsDockWidgetPy",
                                    "[Error] The field " ) + fieldName + \
                                QApplication.translate( "AutoFieldsDockWidgetPy",
                                    " already exists in layer " ) + layer.name() + ". " + \
                                QApplication.translate( "AutoFieldsDockWidgetPy",
                                    " If you want to create an AutoField on it, you need to choose it from 'Existing Field' list." ),
                                'warning' )
                        else:
                            res = layer.dataProvider().addAttributes( [ newField ] )
                            if res:
                                layer.updateFields()

                                # Check if fieldName is preserved by the provider after field creation.
                                if layer.fieldNameIndex( fieldName ) == -1:
                                    self.msg.show(
                                        QApplication.translate( "AutoFieldsDockWidgetPy",
                                            "[Error] The field " ) + fieldName + \
                                        QApplication.translate( "AutoFieldsDockWidgetPy",
                                            " was probably created with another name by the layer (" ) + \
                                        layer.name() + \
                                        QApplication.translate( "AutoFieldsDockWidgetPy",
                                            ") provider. " ) + \
                                        QApplication.translate( "AutoFieldsDockWidgetPy",
                                            " If you want to create an AutoField on it, you need to choose it from 'Existing Field' list." ),
                                        'warning' )
                                else:

                                    self.doSaveAutoField( layer, fieldName, expression )

                            else:
                                self.msg.show( QApplication.translate( "AutoFieldsDockWidgetPy",
                                    "[Error] Couldn't create " ) + newField.name() + \
                                    QApplication.translate( "AutoFieldsDockWidgetPy",
                                        " field in " ) + layer.name() + \
                                    QApplication.translate( "AutoFieldsDockWidgetPy", " layer." ),
                                    'warning' )

                # Some fields might have been created, update the field list once
                self.updateFieldList()

            else:
                self.msg.show( QApplication.translate( "AutoFieldsDockWidgetPy",
                    "[Warning] Please first set a name for the new field." ), 'warning' )
                return
        else:
            fieldName = self.cboField.currentText()

            for item in self.tblLayers.selectedItems():
                if item.column() == 1: # It's the layer name item
                    layer = QgsMapLayerRegistry.instance().mapLayer( item.data( Qt.UserRole ) )
                    self.doSaveAutoField( layer, fieldName, expression )


    def doSaveAutoField( self, layer, fieldName, expression ):
        """ Repetitive logic to save or overwrite an AutoField """
        # Check if the field is an AutoField and ask if we should overwrite it
        res = True
        bCalculateOnExisting = self.chkCalculateOnExisting.isChecked()
        if self.autoFieldManager.isFieldAnAutoField( layer, fieldName ):
            reply = QMessageBox.question( self.iface.mainWindow(),
                QApplication.translate( "AutoFieldsDockWidgetPy", "Confirmation" ),
                QApplication.translate( "AutoFieldsDockWidgetPy", "The field '" ) + \
                fieldName + QApplication.translate( "AutoFieldsDockWidgetPy",
                    "' from layer '" ) + layer.name() + \
                QApplication.translate( "AutoFieldsDockWidgetPy",
                    "' is already an AutoField.\nDo you want to overwrite it?" ),
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No )

            if reply == QMessageBox.Yes:
                res = self.autoFieldManager.overwriteAutoField( layer, fieldName, expression, calculateOnExisting=bCalculateOnExisting )

        else:
            res = self.autoFieldManager.createAutoField( layer, fieldName, expression, calculateOnExisting=bCalculateOnExisting )

        if not res:
            # res will only be False if create/overwriteAutoField return False
            self.msg.show( "[Error] The AutoField for layer '" + layer.name() + \
                "' and field '" + fieldName + "' couldn't be created.", 'warning', True )


    def setCustomExpression( self ):
        """ Initialize and show the expression builder dialog """
        layer = None
        if len( self.tblLayers.selectedItems() ) / 3 == 1: # Single layer selected?
            for item in self.tblLayers.selectedItems():
                if item.column() == 1: # It's the layer name item
                    layer = QgsMapLayerRegistry.instance().mapLayer( item.data( Qt.UserRole ) )

        if not self.expressionDlg:
            self.expressionDlg = ExpressionBuilderDialog( self.iface.mainWindow() )
            context = QgsExpressionContext()
            context.appendScope( QgsExpressionContextUtils.globalScope() )
            context.appendScope( QgsExpressionContextUtils.projectScope() )

            # Initialize dialog with layer-based names and variables if single layer selected
            if len( self.tblLayers.selectedItems() ) / 3 == 1:
                context.appendScope( QgsExpressionContextUtils.layerScope( layer ) )
                self.expressionDlg.expressionBuilderWidget.setLayer( layer )
                self.expressionDlg.expressionBuilderWidget.loadFieldNames()

                # This block was borrowed from QGIS/python/plugins/processing/algs/qgis/FieldsCalculator.py
                da = QgsDistanceArea()
                da.setSourceCrs( layer.crs().srsid() )
                da.setEllipsoidalMode( self.iface.mapCanvas().mapSettings().hasCrsTransformEnabled() )
                da.setEllipsoid( QgsProject.instance().readEntry( 'Measure', '/Ellipsoid', GEO_NONE )[0] )
                self.expressionDlg.expressionBuilderWidget.setGeomCalculator( da )

                # If this layer-field is an AutoField, get its expression
                if self.optExistingField.isChecked():
                    fieldName = self.cboField.currentText()
                    expression = self.autoFieldManager.getFieldExpression( layer, fieldName )
                    self.expressionDlg.expressionBuilderWidget.setExpressionText( expression )
                    self.expressionDlg.expression = expression # To remember it when closing/opening

            self.expressionDlg.expressionBuilderWidget.setExpressionContext( context )

        self.expressionDlg.show()





    def leerParametros(self, values):

        ''' Lectura de los atributos '''
        #print " Leer atributos ...."

        #filename = "C:/Data/Python/archivoparametros.txt"

        filename =  self.getPathScripts() + "archivoparametros.txt"

        filename = filename.replace("Utils","Database/SQL")
        if (filename != ""):
            infile = open(filename,"r")
            lines = infile.readlines()
            infile.close()

            self.tableWidgetParameters.setRowCount(len(lines))
            self.tableWidgetParameters.setColumnCount(3)


            for i in range(0, len(lines)):
                tokens = lines[i].strip().split(",")
                make = QtGui.QTableWidgetItem(tokens[0])

                valor = -1
                try:
                   valor = tokens[i]
                   #valor = "0"
                   print " Values es " + valor
                except:
                   print " problem with value"



                make = QtGui.QTableWidgetItem(valor)
                model = QtGui.QTableWidgetItem(valor)

                #price = QtGui.QTableWidgetItem(valor)

                self.tableWidgetParameters.setItem(i,0,make)
                #self.tableWidgetParameters.setItem(i,1,model)
                #self.tableViewMethodology.setItem(i,2,price)


            self.tableWidgetParameters.resizeColumnsToContents()
        #self.tableWidget.data = data
        #http://stackoverflow.com/questions/22420496/reading-all-the-values-from-qtablewidget-in-pyqt

        self.tableWidgetParameters.resizeColumnsToContents()
        self.tableWidgetParameters.resizeRowsToContents()

    def readCostTable(self):


        print " reading cost  table "

        from Logic.LossModel import Loss

        self.importLoss()





        # loss = Loss()

        databasename = self.getDatabasename()



        filenameLosses = self.CostValuespushFile.text()

        filenameLosses = self.setWorkingDirectorylineEdit.text() + "/losses.txt"
        filenamematerial = self.setWorkingDirectorylineEdit.text() + "/material.txt"

        if self.fragilitiesRadioButton.isChecked():
            print " \n updating losses from fragilities curves "
            Loss.updateIndexDamageFromFragilitiesCurves(databasename)

        else:
            print " \n updating losses from predictive modelo "

            Loss.updateIndexDamageFromSeismicPredictionModel(databasename)

        Loss.exportLossesToText(filenamematerial, databasename)



        #Loss.importLossesFromText(filenameLosses, databasename)

        '''


        Loss.createLosses(databasename)
        Loss.createIndexDamage(databasename)
        Loss.populateMaterialAndCost(databasename)
        '''




        from UI import UILossWidget

        #uiLossWidget = UILossWidget()

        filenameLosses = self.CostValuespushFile.text()

        #filenameMaterial = filenameLosses.replace("loss.csv", "material.txt")
        workingDir = self.setWorkingDirectorylineEdit.text()

        exportLossForReadingfromUi = workingDir + "lossesforui.txt"
        Loss.exportLossForReadingfromUi(databasename, exportLossForReadingfromUi)
        UILossWidget.readCostTableWidget(self, "", workingDir, exportLossForReadingfromUi)

        LYR = self.loadLayerIntoCanvas( "popoliloss", "Losses")

        self.colorLYRWithTotalCost(LYR)

        widget = self.iface.messageBar().createMessage("The losses have been calculated", 'Info')
        self.iface.messageBar().pushWidget(widget, self.iface.messageBar().INFO)


    def colorLYRWithTotalCost(self, LYR):

        try:

            index = LYR.dataProvider().fieldNameIndex('totalcost')
            max = LYR.maximumValue(index)
            min = LYR.minimumValue(index)

            if max ==None:
                max =0

            if min ==None:
                min =0





            '''
            attenzion .... these values are not condidered
            '''

            values_0 = np.linspace(min, max, num=6)

            # array([ 2.        ,  2.33333333,  2.66666667,  3.        ])

            label1 = 'C1 ' + str(values_0[0]) + '-' + str(values_0[1])

            label2 = 'C2 ' + str(values_0[1]) + '-' + str(values_0[2])

            label3 = 'C3 ' + str(values_0[2]) + '-' + str(values_0[3])

            label4 = 'C4' + str(values_0[3]) + '-' + str(values_0[4])
            label5 = 'C5 ' + str(values_0[4]) + '-' + str(values_0[5])
            values = (
                (label1, values_0[0], values_0[1], 'green'),
                (label2, values_0[1], values_0[2], 'blue'),
                (label3, values_0[2], values_0[3], 'yellow'),
                (label4, values_0[3], values_0[4], 'orange'),
                (label5, values_0[4], values_0[5], 'red')

            )


            ranges = []
            for label, lower, upper, color in values:
                symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())
                symbol.setColor(QColor(color))
                rng = QgsRendererRangeV2(lower, upper, symbol, label)
                ranges.append(rng)

            # create the renderer and assign it to a layer
            expression = 'totalcost'  # field name
            renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
            LYR.setRendererV2(renderer)
            LYR.triggerRepaint()

        except:
            print "Probably the total cost have not been setled"




        #LYR.loadNamedStyle('C:/Data/Python/Estilo/buildingscost.qml')




    def leerResultadosMetodologia(self, values):

        ''' Lectura de los atributos '''
        print " Leer atributos ...."
        #filename = "C:/Data/Python/archivometodologia.txt"

        try:

            filename = self.getPathScripts() + "/archivometodologia.txt"

            if (filename != ""):
                infile = open(filename,"r")
                lines = infile.readlines()
                infile.close()

                self.tableViewMethodology.setRowCount(len(lines))
                self.tableViewMethodology.setColumnCount(3)


                for i in range(0, len(lines)):
                    tokens = lines[i].strip().split(",")
                    make = QtGui.QTableWidgetItem(tokens[0])

                    valor = -1
                    try:
                       valor = values[i]
                       print " Values es " + valor
                    except:
                       print " problem with value"



                    model = QtGui.QTableWidgetItem(valor)

                    #price = QtGui.QTableWidgetItem(valor)

                    self.tableViewMethodology.setItem(i,0,make)
                    self.tableViewMethodology.setItem(i,1,model)
                    #self.tableViewMethodology.setItem(i,2,price)


                self.tableViewMethodology.resizeColumnsToContents()
            #self.tableWidget.data = data
            #http://stackoverflow.com/questions/22420496/reading-all-the-values-from-qtablewidget-in-pyqt

            self.tableViewMethodology.resizeColumnsToContents()
            self.tableViewMethodology.resizeRowsToContents()

        except:
            print ""


    def setShapefilePath(self):

        from UI import UILayerWidget

        UILayerWidget.setShapefilePath(self)


    def setWorkingDirectoryPath(self):

        from UI import UILayerWidget

        UILayerWidget.setWorkingDirectoryPath(self)


    def updateLayerTable(self):

        from Logic.PredictiveModel import PredictiveModel

        database_exists = PredictiveModel.checkdatabase("test")

        if (database_exists < 0):
            widget = self.iface.messageBar().createMessage(
                "Please ckeck the database system is running ")
            self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)

            return -1

        else:

            from UI import UILayerWidget

            UILayerWidget.updateLayerTable(self)

            databasename = self.getDatabasename()

            if not(databasename==""):

                #FragilityCurve.createFragilityTable(databasename)  #this was coomented, why?

                self.PredictionModel.setTabEnabled (1, True)

                self.PredictionModel.setTabEnabled (2, True)

                self.PredictionModel.setTabEnabled (3, True)

                self.PredictionModel.setTabEnabled (4, True)





    def removeALLLayers(self):

        for layer in QgsMapLayerRegistry.instance().mapLayers().values():
            print layer.name()

            display_name = layer.name()
            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

            try:
                QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # primer elemento de la lista
            except:
                print " except removing all Layers "

        Logica.removeALLLayers()



    def updateFragilityCurves(self):




        def valores(uri, index):

            # uri = 'D:/Data/Fragility curves/FragilityCurves.xlsx'
            layer = QgsVectorLayer(uri, 'test', 'ogr')

            column = ""
            for feat in layer.getFeatures():
                attrs = feat.attributes()
                column = column + ";" + str(attrs[1])
                print attrs[1]

            column = ""
            for feat in layer.getFeatures():
                attrs = feat.attributes()
                column = column + ";" + str(attrs[index])
                # print attrs[1]

            # print " column 1 " + column

            columns = column.split(";")

            print " limit state "

            median =columns[2]

            st=columns[3]

            print " median " + columns[2]

            print " st " + columns[3]

            return  [median,st]

        def showError():
            pass


        databasename = self.getDatabasename()

        print " 1393 databasenane " + str(databasename)

        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'D:\\Data\\Fragility curves', "*")

        print "leer es " + fname

        #uri = 'D:/Data/Fragility curves/FragilityCurves.xlsx'

        uri = fname

        #uri = fname

        params =valores(uri, 2)

        # here UPDATE THRE FRAGILITY

        stringfragility= self.selectCurvescomboBox.currentText()

        columns = stringfragility.split(",")

        idfragility = columns[0]
        idfragility = idfragility.strip()

        print " 2301  (SismicRiskdDockWidget) Id fragility is " + str(idfragility)


        idlevel="2"



        try:


            idfragilitystr = FragilityCurve.getNewIdFragility(self.getDatabasename())

            print " Logica idfragility is " + idfragilitystr

            idfragility =0
            try:

                idfragility = int(idfragilitystr)
            except:
                idfragility =0



            if idfragility>10:
                print " Logica idfragility less than 10 "

                self.widget = self.iface.messageBar().createMessage("Fragility curves", "More thahn 10")

                from qgis.gui import QgsMessageBar

                self.iface.messageBar().pushWidget(self.widget, QgsMessageBar.WARNING)

            else :



                FragilityCurve.insertFragilityCurves(databasename, idfragility)

                print " Logica idfragility greater than 10 "
                idlevel = 1
                params = valores(uri, idlevel)

                param1=params[0]
                param2 = params[1]

                FragilityCurve.updateFragilityCurves(databasename, idfragility, idlevel, param1, param2)



                idlevel = 2
                params = valores(uri, idlevel)

                param1=params[0]
                param2 = params[1]

                FragilityCurve.updateFragilityCurves(databasename, idfragility, idlevel, param1, param2)


                idlevel = 3
                params = valores(uri, idlevel)

                param1=params[0]
                param2 = params[1]

                FragilityCurve.updateFragilityCurves(databasename, idfragility, idlevel, param1, param2)


                idlevel = 4

                try:
                    params = valores(uri, idlevel)

                    param1=params[0]
                    param2 = params[1]

                    if (param1!="") and (param2!=""):

                        FragilityCurve.updateFragilityCurves(databasename, idfragility, idlevel, param1, param2)
                except:
                    print ""

                try:
                    params = valores(uri, idlevel)

                    param1 = params[0]
                    param2 = params[1]

                    if (param1 != "") and (param2 != ""):
                        FragilityCurve.updateFragilityCurves(databasename, idfragility, idlevel, param1, param2)
                except:
                    print ""

                ids = FragilityCurve.readFragilityCurves(databasename)

                self.selectCurvescomboBox.clear()

                idsstr = ids.split(";")

                print " id str " + str(idsstr) + ""

                for count in range(0, len(idsstr)):
                    self.selectCurvescomboBox.addItem(idsstr[count])

                self.minimMaximIMLcomboBox.clear()

                ranges = self.rangesIMLintensities(uri)

                if (ranges==""):
                    self.minimMaximIMLcomboBox.addItem("1 5")
                else:
                    self.minimMaximIMLcomboBox.addItem(ranges)

                widget = self.iface.messageBar().createMessage("The fragilities have been added", 'Info')
                self.iface.messageBar().pushWidget(widget, self.iface.messageBar().INFO)




        except:
            print(" read bad parameterds", sys.exc_info())





    def rangesIMLintensities(self, uri):

            # uri = 'D:/Data/Fragility curves/FragilityCurves.xlsx'
            layer = QgsVectorLayer(uri, 'test', 'ogr')

            column = ""
            for feat in layer.getFeatures():
                attrs = feat.attributes()
                column = column + ";" + str(attrs[1])

                range = attrs[0] #word range

                min = attrs[1]
                max = attrs[2]

            return str(min) + "-" + str(max)


    def loadEpicenter(self):
        print "I will load the epicenter ..."

        x = "13.8336151359"

        y = "42.1746958775"

        coordinadasstr = self.epicenterLineEdit.text()
        coordinadas = coordinadasstr.split(";")

        momentum = self.MomentumLineEdit.text()

        parametros = self.valuesHazardModelTextEdit.toPlainText()

        if (momentum == ""):
            momentum = "1"

        else:

            try:
                float(momentum)

            except ValueError:
                print " momentum errato"
                momentum = "1"
                self.MomentumLineEdit.setText("1")

        try:
            x = coordinadas[0]
            y = coordinadas[1]

        except:
            x = ""
            y = ""


        print " x " + x
        print " y " + y

        modeloHazard = 0

        objetos = 0


        print "self.hazardObjectsComboBox.currentText()" + str(self.hazardObjectsComboBox.currentText())
        print "self.hazardModelsComboBox.currentText()" + str(self.hazardModelComboBox.currentText())

        if (self.hazardModelComboBox.currentText()=="model 1 (Soil)"):
            self.hazardModelTextEdit.setText("hazard=a+ b*momentum + c*rdistance + d*soilfactor;")
            modeloHazard=1
        else:
            self.hazardModelTextEdit.setText("hazard=1.2474 + 0.3735*momentum - 0.4383*log(rdistance/1000)+10;")
            modeloHazard = 0

        if (self.hazardObjectsComboBox.currentText() == "buildings"):
            objetos = 1

        if (len(x)>0 and len(y)>0):

            from Logic.HazardModel import Hazard


            Hazard.createEpicenter(momentum, x, y, parametros,objetos, modeloHazard)

            import requests, urllib

            # https://stackoverflow.com/questions/8928730/processing-http-get-input-parameter-on-server-side-in-python
            # r = requests.get('http://127.0.0.1:8000/?param=hazard')

            #execfile("D:/repositorydef/SeismicRisk/servers/request.py")


            LYR = self.loadLayerIntoCanvas( "epicenter", "Hazard")

            if LYR.geometryType() == QGis.Point:
                LYR.loadNamedStyle('C:\Data\Python\Estilo\epicenter.qml')


            #self.calculateHazard()  #este metodo deberia ser usado slamente por el metodo create epicenter
            #self.loadHazards()

            '''
            In this moment instead of adding hazard Layers
            for levels, I will add the graduated symbols
            
            self.addHazardLayers(0)
            self.addHazardLayers(1)
            self.addHazardLayers(2)
            self.addHazardLayers(3)
            self.addHazardLayers(-1)
            '''



            self.addGraduatedSymbolHazardLayer()
            self.alignLayers()

            self.exportHazardParameters()

            #self.addDistanceLayers(1)

    def assignFragilitiesToBuildings(self):

        '''

        databasename = self.getDatabasename()

        from Logic2.FragilityCurve import FragilityCurve

        FragilityCurve.assignFragilitiesCurvesToBuildings(databasename)
        '''
        self.importFragilitiesAssignationToBuilding()

        widget = self.iface.messageBar().createMessage("The fragilities have been asaigned", 'Info')
        self.iface.messageBar().pushWidget(widget, self.iface.messageBar().INFO)

    def deleteFragilitiesCurves(self):

        from Logic.FragilityCurve import FragilityCurve

        databasename = self.getDatabasename()


        stringfragility = self.selectCurvescomboBox.currentText()

        columns = stringfragility.split(",")

        idfragility = columns[0]
        idfragility = idfragility.strip()

        FragilityCurve.deleteFragilitiesCurves(databasename, idfragility)

        self.selectCurvescomboBox.clear()

        ids = FragilityCurve.readFragilityCurves(databasename)

        idsstr = ids.split(";")

        for count in range(0, len(idsstr)):
            self.selectCurvescomboBox.addItem(idsstr[count])

    def showAssignedFragilities(self):
        print " 2387 show fragilities button "

        databasename = self.getDatabasename()

        dir = self.getPathScripts()

        workingdir = self.setWorkingDirectorylineEdit.text()

        dir =  workingdir

        #filename = dir +"fragility/fragility_curve_level_values.csv"

        #filename2 = dir +"fragility/fragility_curve_structures.csv"

        filename = dir +"fragility_curve_level_values.csv"

        filename2 = dir +"fragility_curve_structures.csv"

        #uri = "file:///C:/Data/Python/fragility/fragility_curve_level_values.csv?type=csv&geomType=none&subsetIndex=no&watchFile=no"

        Logica.exportFragilityValuesToExcel(filename, filename2, databasename)





        uri = "file:///" + filename + "?type=csv&geomType=none&subsetIndex=no&watchFile=no"

        #uri = filename + "?delimiter=%s" % (",")

        vlayer = QgsVectorLayer(uri, "fragilities_curves", "delimitedtext")

        if not vlayer.isValid():
            print "Layer failed to load!"

        display_name = "fragilities_curves"
        layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

        try:
            QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # primer elemento de la lista
        except:
            print " except fragilities_curves "

        QgsMapLayerRegistry.instance().addMapLayer(vlayer)

        uri = "file:///" + filename2 + "?type=csv&geomType=none&subsetIndex=no&watchFile=no"

        #uri = filename + "?delimiter=%s" % (",")

        vlayer = QgsVectorLayer(uri, "fragilities_curves_structures", "delimitedtext")

        if not vlayer.isValid():
            print "Layer failed to load!"

        display_name = "fragilities_curves_structures"
        layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

        try:
            QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # primer elemento de la lista
        except:
            print "fragilities_curves_structures"

        QgsMapLayerRegistry.instance().addMapLayer(vlayer)

        widget = self.iface.messageBar().createMessage("Fragilities have been loaded in the layer panel", 'Info')
        self.iface.messageBar().pushWidget(widget, self.iface.messageBar().INFO)

    def showFragilitiesInficators(self):  #no sirve
        print " 2387 show fragilities button "

        databasename = self.getDatabasename()


        wd = self.setWorkingDirectorylineEdit.text()
        self.exportFragilityIndicators()


        filename = wd + "fragilitiescsv.csv"



        uri = "file:///" + filename + "?type=csv&geomType=none&subsetIndex=no&watchFile=no"

        uri = uri + "?delimiter=%s" % (",")

        vlayer = QgsVectorLayer(uri, "fragilities_indicators", "delimitedtext")

        if not vlayer.isValid():
            print "Layer failed to load!"

        display_name = "fragilities_indicators"
        layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

        try:
            QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # primer elemento de la lista
        except:
            print " except fragilities_curves "

        QgsMapLayerRegistry.instance().addMapLayer(vlayer)





    def checkShapefile(self,  fname):

        layer = QgsVectorLayer(fname, "testlayer", "ogr")

        idx = layer.fieldNameIndex('name')

        print " \n id " + str (idx) + ""

        atributes = [ "name",   "soil", "fault",  "fragility", "unitcost"]

        completo = 1

        for att in atributes:
            idx = layer.fieldNameIndex(att)
            print " \n Name " + str(idx) + ""

            if idx<0:
                print  " Attribute " + att + " not found in the shapefile "
                completo = -1

        if completo<0:



            widget = self.iface.messageBar().createMessage("The shapefile structure is not adequate.[name,   soil, fault, fragility, unitcost]")
            self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)

        return completo

    def loadShapefile(self, fname, databasename):

        from Logic.PredictiveModel import PredictiveModel

        database_exists =  PredictiveModel.checkdatabase("test")

        if (database_exists<0):
            widget = self.iface.messageBar().createMessage(
                "Please ckeck the database system is running ")
            self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)

            return -1
        else:

            self.updateDatabasename(databasename)  # write the datamadase name in the file

            print " loading tha shapefile "

            import inspect

            #sqldir = inspect.getfile(SeismicRiskDockWidget.__class__)

            import os
            #path = os.path.dirname(SeismicRiskDockWidget.__file__)

            #from Database.SQL import sql

            #path = sql.getWorkingDir()

            from Utils import Directory

            sqldir = Directory.getPathSqlDir()
            #sqldir = path.replace("Utils", "Database/SQL")
            sqldir = sqldir + "/"

            print sqldir

            logging.debug(" where i am ")


            logging.debug(sqldir)


            import os, subprocess



            from Connection import Connection



            con2 = Connection()
            con = con2.getConnection()

            user = con.user

            # Choose your PostgreSQL version here
            os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
            os.environ['PATH'] += "r';" + con.getPathDatabase()
            #D:\usbgis\apps\postgresql93\bin

            #os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'
            #os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

            #maquina = " -h 127.0.0.1 -p 5434"

            maquina = " -h " + con.host + " -p " + con.port

            #os.environ['PATH'] += r';C:\usbgis\apps\postgresql93\bin'

            dir_path = con.getPathDatabase()

            import sys
            # sys.path
            sys.path.append(dir_path)

            #os.environ['PATH'] += r';D:\Program Files\PostgreSQL\11\bin'





            # http://www.postgresql.org/docs/current/static/libpq-envars.html

            '''
            os.environ['PGHOST'] = 'localhost'
            os.environ['PGPORT'] = '5432'
            os.environ['PGUSER'] = 'potgres'
            os.environ['PGPASSWORD'] = 'postgres'
            os.environ['PGDATABASE'] = 'prueba4'
            '''


            '''
            base_dir = r"c:\Data\Popoli\Popoli"
            full_dir = os.walk(base_dir)
            shapefile_list = []
            for source, dirs, files in full_dir:
                for file_ in files:
                    if file_[-3:] == 'shp':
                        shapefile_path = os.path.join(base_dir, file_)
                        shapefile_list.append(shapefile_path)
                        '''

            shapefile_list = []
            shapefile_list.append(fname)

            print " 1393 databasenane " + str(databasename[0])

            # pgsql2shp -f qds_cnt -h localhost -u postgres -P password gisdb
            # pgsql2shp -f 'C:/Data/postgis/posrgis.shp' -h  127.0.0.1 -p 5434 -u pgis -P  pgis

            ''' essempio using append
            shp2pgsql -t 2D D:/Data/Popoli/popolifeb2017.shp popoliforpostgres  -s SRID=4320 -U postgres > C:/Data/Python/insert.txt
            shp2pgsql -a -t 2D C:/Data/Postgis/my_shapes.shp  popoliforpostgres  -s SRID=4320  -U postgres > C:/Data/Python/insert2.txt
    
            '''




            for shape_path in shapefile_list:
                #cmds = "shp2pgsql -S -s SRID=4326 -t 2D \"" + shape_path + "\" popoliforpostgres   -U postgres "

                cmds = "shp2pgsql -s SRID=4326 -t 2D \"" + shape_path + "\" popoliforpostgres   -U postgres "

                #cmds = cmds + '> "C:/Data/Python/insert.txt"'


                from Utils import Directory

                path = Directory.getPathSqlDir()

                #path = sql.getWorkingDir()

                sqldir = path.replace("Utils", "Database/temp")
                #sqldir = sqldir + "/"
                dirs = sqldir
                cmds = cmds + '> "' + dirs + 'insert.txt"'

                #cmds = cmds.replace("C:/Data/Python", sqldir)
                print cmds
                subprocess.call(cmds, shell=True)

            cmd = "dropdb  -U " +user + maquina + " " + databasename
            print cmd
            logging.debug(cmd)

            subprocess.call(cmd, shell=True)

            cmd = "createdb   -U " +user + maquina + " " + databasename + " --encoding='UTF8'"

            print cmd
            logging.debug(cmd)

            subprocess.call(cmd, shell=True)


            #cmd = "psql -d " + databasename +" -U " +con.user + maquina + " < C:/Data/Python/extension_postgis.txt"
            cmd = "psql -d " + databasename + " -U " + user + maquina + " < \"" + sqldir+ "extension_postgis.txt\""
            print cmd

            logging.debug(cmd)

            subprocess.call(cmd, shell=True)




            #cmd = "psql -d " + databasename +" -U " +con.user + maquina + " < C:/Data/Python/function_get_random_number.txt"
            cmd = "psql -d " + databasename + " -U " + user + maquina + " <  \"" + sqldir +"function_get_random_number.txt\""
            print cmd

            logging.debug(cmd)

            subprocess.call(cmd, shell=True)



            cmd = "psql -d " + databasename + " -U " + user + maquina + " <  \"" + sqldir + "function_calculate_pga.txt\""
            print cmd

            logging.debug(cmd)

            subprocess.call(cmd, shell=True)

            #cmd = "psql -d " + databasename + " -U " + con.user + maquina + " < C:/Data/Python/random_points_in_qgis.txt"
            cmd = "psql -d " + databasename + " -U " + user + maquina + " < \"" + sqldir + "random_points_in_qgis.txt\""
            #cmd = cmd.replace("C:/Data/Python/", sqldir)
            print cmd

            logging.debug(cmd)

            #subprocess.call(cmd, shell=True)

            #cmd = "psql -U " +con.user + maquina + " " + databasename + " < C:/Data/Python/insert.txt"
            cmd = "psql -U " + user + maquina + " " + databasename + " < \"" + sqldir + "insert.txt\""
            #cmd = cmd.replace("C:/Data/Python/", sqldir)
            print cmd

            logging.debug(cmd)

            subprocess.call(cmd, shell=True)


            #cmd = "psql -U " +con.user + maquina + " " + databasename+" < C:/Data/Python/create_valutazione.txt"
            cmd = "psql -U " + user + maquina + " " + databasename + " < \"" + sqldir + "create_valutazione.txt\""
            #cmd = cmd.replace("C:/Data/Python/", sqldir)
            print cmd

            logging.debug(cmd)

            subprocess.call(cmd, shell=True)

            from UI import UILayerWidget

            workingdir = self.setWorkingDirectorylineEdit.text()

            lossfile = workingdir + "losscsv.txt"

            self.CostValuespushFile.setText(lossfile)


            if (workingdir!="") and databasename!="":



                self.updateDatabasename(databasename)  #write the datamadase name in the file

                '''
                update the name of the current database
                '''
                UILayerWidget.createTemplates(workingdir, databasename)
                print "Created the templates"

            else:
                print "Not created the templates"
                logging.debug("Not posible create templates")



            from Logic.FragilityCurve import FragilityCurve

            databasename = self.getDatabasename()

            ids = FragilityCurve.readFragilityCurves(databasename)

            idsstr = ids.split(";")

            for count in range(0, len(idsstr)):
                self.selectCurvescomboBox.addItem(idsstr[count])

            return 1


    def loadMetodologia(self,  databasename):

        import os, subprocess



        maquina = " -h 127.0.0.1 -p 5434"

        con2 = Connection()

        con = con2.getConnection()

        # Choose your PostgreSQL version here
        # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
        # D:\usbgis\apps\postgresql93\bin

        os.environ['PATH'] += r';C:\usbgis\apps\postgresql93\bin'

        # http://www.postgresql.org/docs/current/static/libpq-envars.html
        os.environ['PGHOST'] = 'localhost'

        os.environ['PGPORT'] = '5432'
        os.environ['PGUSER'] = 'potgres'
        os.environ['PGPASSWORD'] = 'postgres'
        os.environ['PGDATABASE'] = 'prueba4'

        '''
        base_dir = r"c:\Data\Popoli\Popoli"
        full_dir = os.walk(base_dir)
        shapefile_list = []
        for source, dirs, files in full_dir:
            for file_ in files:
                if file_[-3:] == 'shp':
                    shapefile_path = os.path.join(base_dir, file_)
                    shapefile_list.append(shapefile_path)
                        '''


        from Database.SQL import sql


        path = sql.getWorkingDir()

        print " working dir is "
        print path
        logging.debug("path")
        logging.debug(path)

        path = path.replace("\\", "/")


        cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + path + "/metodologia_script.txt"
        print cmd

        subprocess.call(cmd, shell=True)

        #cmd = "psql -d " + databasename + " -U " + con.user + maquina + " < " + path + "/create_valutazione.txt"
        #print cmd

        subprocess.call(cmd, shell=True)




    def loadComunityOfStudy(self,  databasename):

        import os, subprocess





        con2 = Connection()

        con = con2.getConnection()

        maquina = " -h " + con.host+" -p " + con.port

        # Choose your PostgreSQL version here
        # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
        # D:\usbgis\apps\postgresql93\bin

        os.environ['PATH'] += r';C:\usbgis\apps\postgresql93\bin'

        # http://www.postgresql.org/docs/current/static/libpq-envars.html
        os.environ['PGHOST'] = 'localhost'

        os.environ['PGPORT'] = '5432'
        os.environ['PGUSER'] = 'potgres'
        os.environ['PGPASSWORD'] = 'postgres'
        os.environ['PGDATABASE'] = 'prueba4'

        '''
        base_dir = r"c:\Data\Popoli\Popoli"
        full_dir = os.walk(base_dir)
        shapefile_list = []
        for source, dirs, files in full_dir:
            for file_ in files:
                if file_[-3:] == 'shp':
                    shapefile_path = os.path.join(base_dir, file_)
                    shapefile_list.append(shapefile_path)
                        '''


        from Database.SQL import sql


        path = sql.getWorkingDir()

        print " working dir is "
        print path
        logging.debug("path")
        logging.debug(path)

        path = path.replace("\\", "/")


        cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + path + "/community_input_script.txt"
        print cmd


        subprocess.call(cmd, shell=True)

        #cmd = "psql -d " + databasename + " -U " + con.user + maquina + " < " + path + "/create_valutazione.txt"
        #print cmd

        subprocess.call(cmd, shell=True)

    def loadFragilities(self,  databasename):


        import os, subprocess

        from Connection import Connection

        maquina = " -h 127.0.0.1 -p 5434"

        con2 = Connection()

        con = con2.getConnection()

        # Choose your PostgreSQL version here
        # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
        # D:\usbgis\apps\postgresql93\bin

        os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

        # http://www.postgresql.org/docs/current/static/libpq-envars.html
        os.environ['PGHOST'] = 'localhost'

        os.environ['PGPORT'] = '5432'
        os.environ['PGUSER'] = 'potgres'
        os.environ['PGPASSWORD'] = 'postgres'
        os.environ['PGDATABASE'] = 'prueba4'


        sqld = self.getPathScripts()

        cmd = "psql -d " + databasename + " -U " + con.user + maquina + " < " + sqld + "/create_fragility.txt"
        print cmd

        subprocess.call(cmd, shell=True)

    def loadHazardsNotUtilizable(self):

        import os, subprocess

        from Connection import Connection

        maquina = " -h 127.0.0.1 -p 5434"

        con2 = Connection()

        con = con2.getConnection()

        # Choose your PostgreSQL version here
        # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
        # D:\usbgis\apps\postgresql93\bin

        os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

        # http://www.postgresql.org/docs/current/static/libpq-envars.html
        os.environ['PGHOST'] = 'localhost'
        os.environ['PGPORT'] = '5432'
        os.environ['PGUSER'] = 'potgres'
        os.environ['PGPASSWORD'] = 'postgres'
        os.environ['PGDATABASE'] = 'prueba4'

        sqld = self.getPathScripts()

        cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + sqld + " > " + sqld +"/errores.txt"
        print cmd

        subprocess.call(cmd, shell=True)



    def createDamage(self):
        import os, subprocess

        from Connection import Connection

        maquina = " -h 127.0.0.1 -p 5434"

        con2 = Connection()

        con = con2.getConnection()

        # Choose your PostgreSQL version here
        # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
        # D:\usbgis\apps\postgresql93\bin

        path_database = con2.getPathDatabase()

        os.environ['PATH'] += "r" + path_database

        #os.environ['PATH'] += r';C:\usbgis\apps\postgresql93\bin'

        # http://www.postgresql.org/docs/current/static/libpq-envars.html
        os.environ['PGHOST'] = 'localhost'
        os.environ['PGPORT'] = '5432'
        os.environ['PGUSER'] = 'potgres'
        os.environ['PGPASSWORD'] = 'postgres'
        os.environ['PGDATABASE'] = 'prueba4'

        from Database.SQL import sql

        path = sql.getWorkingDir()

        print " working dir is "
        print path
        logging.debug("path")
        logging.debug(path)

        path = path.replace("\\", "/")



        databasename = con.database

        sqld =  self.getPathScripts()

        cmd = "psql -d " + databasename + " -U " + con.user + maquina + " < " + path + "/create_damage.txt > " + sqld +"/errores.txt"
        print cmd


        subprocess.call(cmd, shell=True)


    def evaluateValutazione(self):

        filename = "select the filename"
        database =self.getDatabasename()

        Logica.updateValutazioneLot(filename, database)


    def evaluateValutazione2(self):

        """
        from QuickWKT.QuickWKTDialog import QuickWKTDialog
        self.QuickWKTDialog = QuickWKTDialog()
        self.QuickWKTDialog.show()
        """


        num =self.idComboBox.currentText()

        num2 = num.split(",")

        id =0

        try:
           #id = int(num)
          id = int(num2[0])
        except:
          id =0

        print "id a seleccionar es " + str(id)
        filename = QFileDialog.getOpenFileName(self, 'Open file',
           'c:\\',"*")

        print " Valutazione will be update from: " + filename

        nombretabla = "popoliforpostgres"

        if (filename!="" and id>0):
          Logica.updateValutazioneFromExcel(id, filename, nombretabla)

          #ochio It should be one puntual calculus '

          Logica.updatevulnerabilityindex()
          Logica.updatevulnerabilityfactor()


          try:
              earthquakeintensity = self.tableWidgetParameters.item(0,1).text()
          except:
              earthquakeintensity ="0"

          if earthquakeintensity == "":
              earthquakeintensity = "0"


          Logica.updatedamage(earthquakeintensity)

          databasename = self.getDatabasename()
          msg =Logica.readData(databasename)

          values = msg.split(",")
          print msg
          print "values are " + str(values)

          self.leerResultadosMetodologia(values)
          



    def getfiles(self):
          dlg = QFileDialog()
          dlg.setFileMode(QFileDialog.AnyFile)
          dlg.setFilter("Text files (*.txt)")
          filenames = QStringList()

          if dlg.exec_():
             filenames = dlg.selectedFiles()
             f = open(filenames[0], 'r')

             with f:
                data = f.read()
                self.contents.setText(data)


    def populateTableMethodology(self):
            self.tableViewMethodology = QtGui.QTableWidget(1,3)
            #self.tableViewMethodology.setGeometry(QtCore.QRect(40, 210, 211, 131))
            #self.tableViewMethodology.setObjectName(_fromUtf8("tableViewMethodology"))

            ''' data methodologia
            '''

            print " Populate table methodology "

            from Utils import Directory

            pathd = Directory.getPathSqlDir()

            filename = "C:/Data/Python/archivolectura.txt"

            filename = pathd + "archivolectura.txt"

            if (filename != ""):
                infile = open(filename,"r")
                lines = infile.readlines()
                infile.close()
                #self.tableViewMethodology.setRowCount(len(lines))

                self.tableViewMethodology.setRowCount(5)

                self.tableViewMethodology.setColumnCount(3)

                for i in range(0, len(lines)):
                    tokens = lines[i].strip().split(",")
                    make = QtGui.QTableWidgetItem(tokens[0])
                    model = QtGui.QTableWidgetItem(tokens[1])
                    price = QtGui.QTableWidgetItem(tokens[2])
                    self.tableViewMethodology.setItem(i,0,make)
                    self.tableViewMethodology.setItem(i,1,model)
                    self.tableViewMethodology.setItem(i,2,price)
                self.tableViewMethodology.resizeColumnsToContents()
            #self.tableViewMethodology.data = data

            self.tableViewMethodology.resizeColumnsToContents()
            self.tableViewMethodology.resizeRowsToContents()

            ''' fin data methodologia '''


    def calculateInterdependencies(self):

        #self.setComboBox()

        from  PyQt4.QtCore import QSettings

        s = QSettings()
        ## possible values are: prompt, useProject, useGlobal
        s.setValue("/Projections/defaultBehaviour", "useProject")


        idforshow = "1"

        print " idforshow es " + idforshow

        try:

            layer2 = QgsMapLayerRegistry.instance().mapLayersByName("popoliforpostgres")[0]

        except:
            self.addRoadsLayers()
            layer2 = QgsMapLayerRegistry.instance().mapLayersByName("popoliforpostgres")[0]

        print "name " + layer2.name()

        try:
            print "name " + layer2.name()
            selected_feature = layer2.selectedFeatures()[0]
            idforshow = str(selected_feature[0])

        except:
            idforshow = "1"



        print " 2nd idforshow es " + idforshow

        #layer =self.comboBoxFromLayer.currentText()

        #AllItems = [self.comboBoxFromLayer.itemText(i) for i in range(self.comboBoxFromLayer.count())]

        geom = ""

        for i in range(self.comboBoxFromLayer.count()):
            opcion = self.comboBoxFromLayer.itemText(i)
            opciones = opcion.split(",")
            id = opciones[0]

            print " id es : " + id

            if id.strip()==idforshow.strip():
                geom = opciones[2]

            print " opcion:  " + self.comboBoxFromLayer.itemText(i)

        #geom = layer.split(",")



        param = geom

        print " geom es: " + geom


        '''
        layer = QgsMapLayerRegistry.instance().mapLayersByName("popoliforpostgres")[0]

        layer.selectAll()
        # layer = QgsMapLayerRegistry.instance().mapLayersByName("inter")[0]


        selected_features = layer.selectedFeatures()
        for i in selected_features:
            attrs = i.attributes()

            # attrs is a list. It contains all the attribute values of this feature

            param = i.geometry()
            print attrs
            
        '''


        Logica.calculateinterdependency(param)
        #init postgres
        #http://gis.stackexchange.com/questions/86983/how-to-properly-establish-a-postgresql-connection-using-qgscredentials
        

        uri = QgsDataSourceURI()
        # assign this information before you query the QgsCredentials data store


        from Connection import Connection

        #maquina = " -h 127.0.0.1 -p 5434"

        con2 = Connection()

        con = con2.getConnection()

        uri.setConnection(con.host, con.port, con.database, con.user, con.password)
        connInfo = uri.connectionInfo()

        #(success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

        success = True
        user = con.user
        passwd = con.password

        if success:
            QgsCredentials.instance().put(connInfo, user, passwd)

            uri.setPassword(passwd)
            uri.setUsername(user)

            uri.setDataSource("public", "interdependencies", "geom")
            LYR = QgsVectorLayer(uri.uri(), "inter", "postgres")

            if (LYR.isValid()):
                print "Layer interdependencies valid"
            else:
                 print  "Layer interdependencies not valid"

            LYR.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))

            display_name="inter"
            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

            try:
                QgsMapLayerRegistry.instance().removeMapLayers( [layerExiste[0].id()] ) #primer elemento de la lista
            except:
                print " except LYR "

            LYR.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))

            QgsMapLayerRegistry.instance().addMapLayer(LYR)

            self.iface.setActiveLayer(LYR)


            try:
                symbols = LYR.rendererV2().symbols()
                symbol = symbols[0]
                symbol.setColor(QtGui.QColor.fromRgb(255, 0, 0))

            except:
                print(" review symbols of layers", sys.exc_info())


            self.iface.mapCanvas().refresh()

    def getinterdependenciesbyid(self, id):

        # self.setComboBox()

        from  PyQt4.QtCore import QSettings

        s = QSettings()
        ## possible values are: prompt, useProject, useGlobal
        s.setValue("/Projections/defaultBehaviour", "useProject")

        idforshow = "1"

        Logica.calculateinterdependencyById(id)
        # init postgres
        # http://gis.stackexchange.com/questions/86983/how-to-properly-establish-a-postgresql-connection-using-qgscredentials


        uri = QgsDataSourceURI()
        # assign this information before you query the QgsCredentials data store


        from Connection import Connection

        # maquina = " -h 127.0.0.1 -p 5434"

        con2 = Connection()

        con = con2.getConnection()

        uri.setConnection(con.host, con.port, con.database, con.user, con.password)
        connInfo = uri.connectionInfo()

        #(success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

        success = True

        if success:

            QgsCredentials.instance().put(connInfo, con2.user, con2.password)

            print " line 1661 connect  "
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

            #LYR.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))

            #QgsMapLayerRegistry.instance().addMapLayer(LYR)


            root = QgsProject.instance().layerTreeRoot()

            #mylayer = QgsVectorLayer("/Path/to/your/data.shp", "my layer", "ogr")

            QgsMapLayerRegistry.instance().addMapLayer(LYR, False)

            #root.addLayer(LYR)

            root.insertLayer(1, LYR)



            symbols = LYR.rendererV2().symbols()
            symbol = symbols[0]
            symbol.setColor(QtGui.QColor.fromRgb(255, 0, 0))

            self.iface.mapCanvas().refresh()


    def setComboBox(self):

        layer = None

        try:
            layer = QgsMapLayerRegistry.instance().mapLayersByName("popoliforpostgres")[0]
        except:
            self.addRoadsLayers()
            layer = QgsMapLayerRegistry.instance().mapLayersByName("popoliforpostgres")[0]

        if (layer.isValid()):


            selected_features = layer.selectedFeatures()

            text = ""
            for i in selected_features:
                attrs = i.attributes()

                print attrs


                text = attrs[1]
                print attrs

            text = "Line 1"
            print " text es " + str(text)


            index = self.comboBoxToLayer.findText(text, QtCore.Qt.MatchFixedString)

            if index >= 0:
                self.comboBoxToLayer.setCurrentIndex(index)



    def addRoadsLayers(self):

        #Logica.setData()

        con = con2.getConnection2()


        #layer = QgsVectorLayer("C:/Data/Popoli/popoli2.shp", "layer_popoli", "ogr");



        uri = QgsDataSourceURI()
        # assign this information before you query the QgsCredentials data store
        uri.setConnection(con.host, con.port, con.database, con.user, con.password)
        connInfo = uri.connectionInfo()


        (success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

        if success:
            uri.setPassword(passwd)
            uri.setUsername(user)
            uri.setDataSource("public", "popoliforpostgres", "geom")


            display_name = "popoliforpostgres"

            LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")

            # Work with the layer (E.g. get feature count...)
            print "" +str(len( list( LYR.getFeatures() ) ))
            print "suceess to load "

            try:

                # display_name="LYR"
                layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

                QgsMapLayerRegistry.instance().removeMapLayers( [layerExiste[0].id()] ) #primer elemento de la lista
            except:
                print " except LYR "


            QgsMapLayerRegistry.instance().addMapLayer(LYR)



            try:
                #vl = QgsMapLayerRegistry.instance().mapLayersByName(display_name)[0]
                #self.iface.setActiveLayer(vl)

                self.iface.mapCanvas().selectionChanged.connect(self.actuaLiza88())


            except:
                print "Error"


            '''
            import MyWnd
            w = MyWnd.MyWnd(self.iface.mapCanvas())
            w.show()
            '''


            self.iface.mapCanvas().refresh()



            ''' remove and add again for udepate in the qgis view '''


            #self.iface.showAttributeTable(self.iface.activeLayer())


            #self.iface.mapCanvas().refresh()


#https://gis.stackexchange.com/questions/113215/l3ayer-with-custom-ui-not-working-properly/113230#113230


    def addHazardLayers(self, tipo):

        #Logica.setData()

        con2 = Connection()

        con = con2.getConnection()


        #layer = QgsVectorLayer("C:/Data/Popoli/popoli2.shp", "layer_popoli", "ogr");


        uri = QgsDataSourceURI()
        # assign this information before you query the QgsCredentials data store
        uri.setConnection(con.host, con.port, con.database, con.user, con.password)
        connInfo = uri.connectionInfo()


        #(success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

        success = True

        sql = "hazard<0.3"
        if tipo >= 1:
            sql = "hazard<0.9"

        if tipo >= 2:
            sql = "hazard>0.9 and hazard<1.2"

        if tipo >= 3:
            sql = "hazard>1.2"

        if tipo <0:
            sql=""

        #sql = sql.replace("hazard", "rdistance")
        # prueba de visualuzacion rdistance

        if success:
            uri.setPassword(con.password)
            uri.setUsername(con.user)
            uri.setDataSource("public", "hazard", "geom", sql)


            display_name = "hazard" + str(tipo)

            LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")

            # Work with the layer (E.g. get feature count...)
            print "" +str(len( list( LYR.getFeatures() ) ))
            print "suceess to load "

            try:

                # display_name="LYR"
                layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

                QgsMapLayerRegistry.instance().removeMapLayers( [layerExiste[0].id()] ) #prmer elemento de la lista
            except:
                print " except LYR "


            QgsMapLayerRegistry.instance().addMapLayer(LYR)

            '''
            symbol layer
            
            https://gis.stackexchange.com/questions/216223/multi-symbol-for-pointlayer-in-pyqgis/216313
            '''

            symbol = QgsMarkerSymbolV2.createSimple(
                {'name': 'circle', 'color': 'grey'})

            # Delete first default symbollayer:
            symbol.deleteSymbolLayer(0)

            # Create and insert multiple symbollayers (Example):
            colors = []


            radio =1

            if tipo>=1:
                radio=1
                colors = ['red']

            if tipo >= 2:
                radio = 2
                colors = ['green']

            if tipo >= 3:
                radio = 3
                colors = ['blue']


            for i, color in enumerate(colors):
                new_symbollayer = QgsSimpleMarkerSymbolLayerV2()
                new_symbollayer.setSize(radio-i )
                new_symbollayer.setFillColor(QColor(color))
                # See QgsSimpleMarkerSymbolLayer for more parameters...

                # Add symbollayer to the symbol:
                symbol.appendSymbolLayer(new_symbollayer)
            # layer.rendererV2().setSymbol(symbol)

            try:
                LYR.rendererV2().setSymbol(symbol)
            except:
                print "AutoiFieldDockWidget 2689"
            #


            # setting up triangules

            # https://gis.stackexchange.com/questions/207546/setting-marker-properties-using-scripts

            # layer = qgis.utils.iface.activeLayer()


            #https://gis.stackexchange.com/questions/136526/how-to-add-label-to-qgsvectorlayer-by-python

            LYR.setCustomProperty("labeling", "hazard")
            LYR.setCustomProperty("labeling/enabled", "true")
            LYR.setCustomProperty("labeling/fontFamily", "Arial")
            LYR.setCustomProperty("labeling/fontSize", "10")
            LYR.setCustomProperty("labeling/fieldName", "ename")
            LYR.setCustomProperty("labeling/placement", "2")

            '''
            registry = QgsSymbolLayerV2Registry.instance()
            symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())

            # Create new SimpleMarker style
            triangle = registry.symbolLayerMetadata("SimpleMarker").createSymbolLayer(
                {'name': 'triangle',
                 u'color_dd_expression': u'CASE WHEN "STATUS" = \'ON\' THEN  color_rgba(0,255,0,255)\r\nWHEN "STATUS" = \'OFF\' THEN  color_rgba(255,0,0,100)\r\nEND',
                 'color_border': '0,0,0',
                 'offset': '0,0',
                 u'size_dd_expression': u'CASE WHEN "BCCH" < 200 THEN 25\r\nWHEN "BCCH" > 200 THEN 12 \r\nEND',
                 u'angle_dd_expression': u'"AZIMUTH" +180'})

            # Delete previous symbol style
            symbol.deleteSymbolLayer(0)
            symbol.appendSymbolLayer(triangle)

            # Update renderer of current layer
            renderer = QgsSingleSymbolRendererV2(symbol)
            LYR.setRendererV2(renderer)
            LYR.triggerRepaint()
            
            '''

            '''
            import MyWnd
            w = MyWnd.MyWnd(self.iface.mapCanvas())
            w.show()
            '''


            self.iface.mapCanvas().refresh()



            ''' remove and add again for udepate in the qgis view '''


            #self.iface.showAttributeTable(self.iface.activeLayer())


            #self.iface.mapCanvas().refresh()

    def addDistanceLayers(self, idhazard):

        # Logica.setData()

        con2 = Connection()

        con = con2.getConnection()

        # layer = QgsVectorLayer("C:/Data/Popoli/popoli2.shp", "layer_popoli", "ogr");


        uri = QgsDataSourceURI()
        # assign this information before you query the QgsCredentials data store
        uri.setConnection(con.host, con.port, con.database, con.user, con.password)
        connInfo = uri.connectionInfo()

        # (success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)

        success = True

        if success:
            uri.setPassword(con.password)
            uri.setUsername(con.user)
            sql = "gid=" + str (idhazard)
            uri.setDataSource("public", "distance_from_epicenter", "geom", sql)

            display_name = "hazard_distance"

            LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")

            LYR.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))

            # Work with the layer (E.g. get feature count...)
            print "" + str(len(list(LYR.getFeatures())))
            print "suceess to load "

            try:

                # display_name="LYR"
                layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

                QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # prmer elemento de la lista
            except:
                print " except LYR "

            QgsMapLayerRegistry.instance().addMapLayer(LYR)

            '''
            import MyWnd
            w = MyWnd.MyWnd(self.iface.mapCanvas())
            w.show()
            '''

            self.iface.mapCanvas().refresh()

            ''' remove and add again for udepate in the qgis view '''


            # self.iface.showAttributeTable(self.iface.activeLayer())


            # self.iface.mapCanvas().refresh()

    def addDamageLayers(self):



        #self.createDamage()               when I arrive here the damage is already created
        #Logica.setData()

        con2 = Connection()

        con = con2.getConnection()

        print " database con 2 es " + con.database


        #layer = QgsVectorLayer("C:/Data/Popoli/popoli2.shp", "layer_popoli", "ogr");


        uri = QgsDataSourceURI()
        # assign this information before you query the QgsCredentials data store
        uri.setConnection(con.host, con.port, con.database, con.user, con.password)
        connInfo = uri.connectionInfo()


        #(success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)





        success = True



        if success:

            print " ADD DAmage layer .... dopo di entrase al success "
            uri.setPassword(con.password)
            uri.setUsername(con.user)
            uri.setDataSource("public", "damage", "geom")


            display_name = "damage"

            LYR = QgsVectorLayer(uri.uri(), display_name, "postgres")

            # Work with the layer (E.g. get feature count...)
            print "" +str(len( list( LYR.getFeatures() ) ))
            print "suceess to load "

            try:

                # display_name="LYR"
                layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

                QgsMapLayerRegistry.instance().removeMapLayers( [layerExiste[0].id()] ) #primer elemento de la lista
            except:
                print " except LYR "

            try:
                namegroup = "Losses"
                QgsMapLayerRegistry.instance().addMapLayer(LYR, False)

                # lyr = QgsMapLayerRegistry.instance().mapLayersByName("hazard")[0]
                root = QgsProject.instance().layerTreeRoot()
                # myGroup1 = root.addGroup("My Group 1")
                # If you want to add it to a particular position in the ToC, use:



                myGroup1 = root.findGroup(namegroup)

                if myGroup1 is None:
                    myGroup1 = root.insertGroup(0, namegroup)

                root = myGroup1.insertLayer(0, LYR)

                # vl = QgsMapLayerRegistry.instance().mapLayersByName(display_name)[0]
                # self.iface.setActiveLayer(vl)

            except:
                print " except addinf layers name"
                import sys
                print("except lyr :", sys.exc_info())

            index = LYR.dataProvider().fieldNameIndex('damage')
            max = LYR.maximumValue(index)
            min = LYR.minimumValue(index)

            '''
            attenzion .... these values are not condidered
            '''

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
                symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())
                # symbol.setColor(QColor(color))
                rng = QgsRendererRangeV2(lower, upper, symbol, label)
                ranges.append(rng)

            # create the renderer and assign it to a layer
            expression = 'damage'  # field name
            renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
            #LYR.setRendererV2(renderer)

            # https://gis.stackexchange.com/questions/207546/setting-marker-properties-using-scripts

            # layer = qgis.utils.iface.activeLayer()


            registry = QgsSymbolLayerV2Registry.instance()
            symbol = QgsSymbolV2.defaultSymbol(LYR.geometryType())

            valor =str(values_0[1])
            # Create new SimpleMarker style
            triangle = registry.symbolLayerMetadata("SimpleMarker").createSymbolLayer(
                {'name': 'triangle',
                 u'color_dd_expression': u'CASE WHEN "STATUS" = \'ON\' THEN  color_rgba(0,255,0,255)\r\nWHEN "STATUS" = \'OFF\' THEN  color_rgba(255,0,0,100)\r\nEND',
                 'color_border': '0,0,0',
                 'offset': '0,0',
                 u'size_dd_expression': u'CASE WHEN "damage" > ' +valor + 'THEN 5\r\nWHEN "damage" < ' +valor + ' THEN 1 \r\nEND',
                 u'angle_dd_expression': u'"AZIMUTH" +180'})

            # Delete previous symbol style
            try:
                symbol.deleteSymbolLayer(0)
                symbol.appendSymbolLayer(triangle)
            except:
                print "AutoFieldDocWidget 2902 "



            # Update renderer of current layer
            renderer = QgsSingleSymbolRendererV2(symbol)
            LYR.setRendererV2(renderer)
            LYR.triggerRepaint()

            #if LYR.geometryType() == QGis.Point:
            #    LYR.loadNamedStyle('C:\Data\Python\Estilo\Estilo.qml')






            '''
            import MyWnd
            w = MyWnd.MyWnd(self.iface.mapCanvas())
            w.show()
            '''

            # Sets canvas CRS

            LYR.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))



            self.iface.mapCanvas().refresh()



            ''' remove and add again for udepate in the qgis view '''


            #self.iface.showAttributeTable(self.iface.activeLayer())


            #self.iface.mapCanvas().refresh()
    def actuaLiza88(self):
        try:
            layer = self.iface.activeLayer()

            print " 1863 activelayer " + layer.name

            ids = layer.selectedFeaturesIds()

            for id in ids:
                print " 1868 selected id " + str(id)

            #layer =QgsMapLayerRegistry.instance().mapLayersByName("popoliforpostgres")[0]
            selected_feature = layer.selectedFeatures()[0]





            refCat = str(selected_feature[0])
            print " refcat es " + refCat

        except:
             import sys
             print("Error inesperado 56 :", sys.exc_info())


    def currentLayerChanged(self, layer):

        print " layer changed "

        #self.browserAction.setEnabled(enable)

        try:


            '''
            from PyQt4.QtGui import QAbstractItemView
            self.iface.layerTreeView().setSelectionMode(QAbstractItemView.MultiSelection)

            # Select your layers, this time they are not mutually exclusive

            layer = QgsMapLayerRegistry.instance().mapLayersByName("popoliforpostgres")[0]

            self.iface.layerTreeView().setCurrentLayer(layer)


            layer2 = QgsMapLayerRegistry.instance().mapLayersByName("LYR0")[0]

            self.iface.layerTreeView().setCurrentLayer(layer2)


            self.iface.layerTreeView().setSelectionMode(QAbstractItemView.ExtendedSelection)
            '''




            print layer.name()

            id = -1


            for feature in layer.selectedFeaturesIds():
                id = feature
                print " here in currentLayerChanged " + str(feature)

            print " id es " + str(id)



            if id<0:

                layer = QgsMapLayerRegistry.instance().mapLayersByName("LYR0")[0]

                for feature in layer.selectedFeaturesIds():
                    id = feature
                    print " here in currentLayerChanged " + str(feature)

            if id>0:
                print " inside the if 1929 id es " + str(id)
                self.getinterdependenciesbyid(id)
                #self.addRoadsLayers()

                self.idComboBox.setCurrentIndex(id)



        except:
            import sys
            print("Error inespe 57 :", sys.exc_info())


    def addVulnerabilibyCurveGraph(self):

        print " add vulnerability graph "

        '''

        

        # Plot object
        #plot1 = MyMplCanvas# )

        fig = Figure()
        #FigureCanvas.__init__(self, self.fig)


        fig.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])

        #fig.add_subplot(111).plot((1, 2, 3), (4, 3, 4))

        plt.savefig('D:/Data/zzz_proof_books_read.png')

        # With this definition it would resize as expected
        # l = QtGui.QVBoxLayout(self.main_widget)
        # l.addWidget(plot1)

        # Unfortunatly it is not resizing if I use QStackedWidget
        #self.stackedWidget = QtGui.QStackedWidget(self.main_widget)
        #self.stackedWidget.setSizePolicy(QtGui.QSizePolicy.Expanding,
        #                              QtGui.QSizePolicy.Expanding)

        print " 1998 as figure canvas "
        self.stackedWidget.addWidget(FigureCanvas(fig))
        
        '''

    '''
    def addGraph(self):

        # add matplotlib figure to dialog
        print " in add graph  2010 "
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111).plot([0, 1, 2, 3, 4])



        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib.mlab as mlab
        import math

        mu = 0
        variance = 1
        sigma = math.sqrt(variance)
        #x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)

        x = np.linspace(mu - 2 * sigma, mu * sigma, 100)



        #plt.plot(x, mlab.normpdf(x, mu, sigma))

        self.figure = plt.figure()

        y = mlab.normpdf(x, mu, sigma)

        print " value of x is " + str(x)

        print " value of y is " + str(y)

        print " value of 5 " + str(x[5]) + " value " + str(y[5])

        z =   mlab.normpdf(x, mu, sigma)



        self.axes = self.figure.add_subplot(111).plot(x, mlab.normpdf(x, mu, sigma))

        line2d = self.axes

        xvalues = line2d[0].get_xdata()
        yvalues = line2d[0].get_ydata()

        print " z " + str(xvalues[5]) + " y " + str(yvalues[5])

        #x= [-1, 3]

        #print " vsalor de la funcion de probabilidad normal es " + str(mlab.normpdf(x, mu, sigma))



        #self.figure.add_subplot(plt.plot(x, mlab.normpdf(x, mu, sigma)))

        #https://stackoverflow.com/questions/30877546/resizing-of-qstackedwidget

  

        from scipy.stats import lognorm
        import matplotlib.pyplot as plt
        import numpy as np
        self.figure, ax = plt.subplots(1, 1)
        s = 0.954
        mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')

        x = np.linspace(lognorm.ppf(0.01, s),
                        lognorm.ppf(0.99, s), 100)
        ax.plot(x, lognorm.pdf(x, s),
                'r-', lw=5, alpha=0.6, label='lognorm pdf')
        rv = lognorm(s)
        ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

        vals = lognorm.ppf([0.001, 0.5, 0.999], s)
        np.allclose([0.001, 0.5, 0.999], lognorm.cdf(vals, s))

        r = lognorm.rvs(s, size=1000)

        ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
        ax.legend(loc='best', frameon=False)
        #plt.show()

   
        import numpy as np

        import matplotlib.pyplot as plt

        x = [13.9415, 13.9412, 13.9413, 13.9419, 13.9414, 13.9418, 13.9416, 13.9417, 13.942, 13.9421]

        x = [0.12, 1.23, 2.34, 3.45, 4.56, 5.67, 6.78, 7.81, 8.98, 9.87]

        # print x

        # x = [float("13.942"),float("139.421"),float("139.418"),float("139.413"),float("13.942"),float("139.419"),float("139.41"),float("139.419"),float("139.421"),float("139.418"),float("139.419")]

        # x = [129, 130, 131, 132, 133, 134, 135, 136, 137, 138]

        # print "3993 "  + str(x)

        # here put the values of pga for each building

        #pdfvalue = (np.exp(-(np.log(x1) - mu) ** 2 / (2 * sigma ** 2)) / (x1 * sigma * np.sqrt(2 * np.pi)))
        #pdf0.append(pdfvalue)
        # print pdfvalue

        # pdf = x

        #print " pdf0 " + str(pdf0)
        #plt.plot(x, pdf0, linewidth=2, color='r')

        mu = 6
        sigma = 0.4  # mean and standard deviation

        pdf = []

        for x1 in x:
            pdfvalue = (np.exp(-(np.log(x1) - mu) ** 2 / (2 * sigma ** 2)) / (x1 * sigma * np.sqrt(2 * np.pi)))
            pdf.append(pdfvalue)
            # print pdfvalue

        # pdf = x
        print " pdf1 " + str(pdf)
        plt.plot(x, pdf, linewidth=2, color='g')

        mu, sigma = 4., 3.  # mean and standard deviation

        pdf2 = []

        for x1 in x:
            pdfvalue = (np.exp(-(np.log(x1) - mu) ** 2 / (2 * sigma ** 2)) / (x1 * sigma * np.sqrt(2 * np.pi)))
            pdf2.append(pdfvalue)
            # print pdfvalue

        # pdf = x

        print " pdf2 " + str(pdf2)
        plt.plot(x, pdf2, linewidth=2, color='y')

        mu, sigma = 8., 4.  # mean and standard deviation

        pdf3 = []

        for x1 in x:
            pdfvalue = (np.exp(-(np.log(x1) - mu) ** 2 / (2 * sigma ** 2)) / (x1 * sigma * np.sqrt(2 * np.pi)))
            pdf3.append(pdfvalue)
            # print pdfvalue

        # pdf = x

        print " pdf3 " + str(pdf3)
        plt.plot(x, pdf3, linewidth=2, color='b')

        axes = plt.gca()
        # axes.set_xlim([-0.5 + x, x - 0.5])

        # axes.set_ylim([0.1, 0.5])


        # plt.axis('tight')


        #plt.show()

        #plt.savefig("D:/Data/Frsgilities.png")

        #self.figure = plt.figure()

        #import matplotlib.image as mpimg
        #self.figure = mpimg.imread("D:/Data/Frsgilities.png")


  


        self.canvas = FigureCanvas(plt.figure())
        # self.mpltoolbar = NavigationToolbar(self.canvas, self.widgetPlot)
        # lstActions = self.mpltoolbar.actions()
        # self.mpltoolbar.removeAction(lstActions[7])

        # add the graphics of vulneratility

        self.layoutPlot.addWidget(self.canvas)                          #graoh not visible self.layoutPlot.setVisible(false)


        # fin comment graphics of vulneratility

        # self.layoutPlot.addWidget(self.mpltoolbar
        '''

    def calculateHazard(self):
        print " I am in calculate hazards "
        #self.loadHazards()  #ojo con este metodi
        Logica.populatehazard()  # assign values to hazard calculations
        self.addHazardLayers(0)
        self.addHazardLayers(1)
        self.addHazardLayers(2)
        self.addHazardLayers(3)
        self.addHazardLayers(-1)

        self.addDistanceLayers(1)

    '''
    def addGraduatedSymbolLayer(self):
        from qgis.core import *

        myVectorPath = "D:/Data/Popoli/PopoliHazard/popoliHazard.shp"
        myVectorLayer = QgsVectorLayer(myVectorPath, "myName", 'ogr')
        myTargetField = 'hazard' #'target_field'

        idx = myVectorLayer.fieldNameIndex(myTargetField)

        minimo = myVectorLayer.minimumValue(idx)
        maximo =  myVectorLayer.maximumValue(idx)
        centro = (minimo + maximo)/2

        print "min " + str(myVectorLayer.minimumValue(idx))
        print "max " + str(myVectorLayer.maximumValue(idx))

        myRangeList = []
        myOpacity = 1
        # Make our first symbol and range...
        myMin = minimo
        myMax = centro
        myLabel = 'Group 1'
        myColour = QtGui.QColor('#ffee00')
        mySymbol1 = QgsSymbolV2.defaultSymbol(myVectorLayer.geometryType())
        mySymbol1.setColor(myColour)
        mySymbol1.setAlpha(myOpacity)
        myRange1 = QgsRendererRangeV2(myMin, myMax, mySymbol1, myLabel)
        myRangeList.append(myRange1)
        # now make another symbol and range...
        myMin = centro
        myMax = maximo
        myLabel = 'Group 2'
        myColour = QtGui.QColor('#00eeff')
        mySymbol2 = QgsSymbolV2.defaultSymbol(
             myVectorLayer.geometryType())
        mySymbol2.setColor(myColour)
        mySymbol2.setAlpha(myOpacity)
        myRange2 = QgsRendererRangeV2(myMin, myMax, mySymbol2, myLabel)
        myRangeList.append(myRange2)
        myRenderer = QgsGraduatedSymbolRendererV2('', myRangeList)
        myRenderer.setMode(QgsGraduatedSymbolRendererV2.EqualInterval)
        myRenderer.setClassAttribute(myTargetField)

        myVectorLayer.setRendererV2(myRenderer)
        QgsMapLayerRegistry.instance().addMapLayer(myVectorLayer)

        import numpy as np
        a = np.array([1, 2, 3, 4, 5])

        a= np.arange(3, 7)

        p = np.percentile(a, 25)  # return 50th percentile, e.g median.
        print "25 " + str(p)

        p = np.percentile(a, 50)  # return 50th percentile, e.g median.
        print "50 " + str(p)


        p = np.percentile(a, 75)  # return 50th percentile, e.g median.
        print "75 " + str(p)

        p = np.percentile(a, 100)  # return 50th percentile, e.g median.
        print "199 " + str(p)
    '''

    def addGraduatedSymbolHazardLayer(self):

        con2 = Connection()

        con = con2.getConnection()

        print " database con 2 es " + con.database

        # layer = QgsVectorLayer("C:/Data/Popoli/popoli2.shp", "layer_popoli", "ogr");


        uri = QgsDataSourceURI()
        # assign this information before you query the QgsCredentials data store
        uri.setConnection(con.host, con.port, con.database, con.user, con.password)
        connInfo = uri.connectionInfo()

        # (success, user, passwd) = QgsCredentials.instance().get(connInfo, con.user, con.password)





        success = True

        if success:
            print " ADD DAmage layer .... dopo di entrase al success "
            uri.setPassword(con.password)
            uri.setUsername(con.user)
            uri.setDataSource("public", "hazard", "geom")



            display_name = "hazard"

            # display_name="LYR"
            layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

            try:
                QgsMapLayerRegistry.instance().removeMapLayers([layerExiste[0].id()])  # primer elemento de la lista
            except:
                print " except remove layer "

            myVectorLayer = QgsVectorLayer(uri.uri(), display_name, "postgres")
            self.addGraduatedLayerv2(myVectorLayer)

        '''

        from qgis.core import *

        myVectorPath = "D:/Data/Popoli/PopoliHazard/popoliHazard.shp"
        #myVectorLayer = QgsVectorLayer(myVectorPath, "myName", 'ogr')
        myTargetField = 'hazard'  # 'target_field'

        idx = myVectorLayer.fieldNameIndex(myTargetField)

        minimo = myVectorLayer.minimumValue(idx)
        maximo = myVectorLayer.maximumValue(idx)
        centro = (minimo + maximo) / 2

        print "min " + str(myVectorLayer.minimumValue(idx))
        print "max " + str(myVectorLayer.maximumValue(idx))

        myRangeList = []
        myOpacity = 1
        # Make our first symbol and range...
        myMin = minimo
        myMax = centro
        myLabel = 'Group 1 (' + str(minimo) + ' ' + str(centro) + ')'
        myColour = QtGui.QColor('#ffee00')
        mySymbol1 = QgsSymbolV2.defaultSymbol(myVectorLayer.geometryType())
        mySymbol1.setColor(myColour)
        mySymbol1.setAlpha(myOpacity)
        myRange1 = QgsRendererRangeV2(myMin, myMax, mySymbol1, myLabel)
        myRangeList.append(myRange1)
        # now make another symbol and range...
        myMin = centro
        myMax = maximo
        myLabel = 'Group 2 (' + str(centro) + ' ' + str(maximo) + ')'
        myColour = QtGui.QColor('#00eeff')
        mySymbol2 = QgsSymbolV2.defaultSymbol(
            myVectorLayer.geometryType())
        mySymbol2.setColor(myColour)
        mySymbol2.setAlpha(myOpacity)
        myRange2 = QgsRendererRangeV2(myMin, myMax, mySymbol2, myLabel)
        myRangeList.append(myRange2)
        myRenderer = QgsGraduatedSymbolRendererV2('', myRangeList)
        myRenderer.setMode(QgsGraduatedSymbolRendererV2.EqualInterval)
        myRenderer.setClassAttribute(myTargetField)

        myVectorLayer.setRendererV2(myRenderer)
        QgsMapLayerRegistry.instance().addMapLayer(myVectorLayer)

        import numpy as np
        a = np.array([1, 2, 3, 4, 5])

        a = np.arange(3, 7)

        p = np.percentile(a, 25)  # return 50th percentile, e.g median.
        print "25 " + str(p)

        p = np.percentile(a, 50)  # return 50th percentile, e.g median.
        print "50 " + str(p)

        p = np.percentile(a, 75)  # return 50th percentile, e.g median.
        print "75 " + str(p)

        p = np.percentile(a, 100)  # return 50th percentile, e.g median.
        print "199 " + str(p)
        '''




    def addGraduatedLayerv2(self, layer):

        # define ranges: label, lower value, upper value, color name

        max_hazard = layer.maximumValue(6)
        min_hazard = layer.minimumValue(6)

        print " min hazard " + str(min_hazard) + " max hazard " + str(max_hazard)

        if max_hazard is None or max_hazard=="NoneType" :
            max_hazard =0



        if min_hazard is None or min_hazard=="NoneType":
            min_hazard = 0

        cuarto = 0

        try:
            cuarto = (max_hazard - min_hazard)/4
        except:
            cuarto = 0


        try:
            mitad = cuarto*2

            tres_cuartos = cuarto*3

            '''
            l1 l2
            m1 m2
            h1 h2
            v1 v2
            '''

            l1 = min_hazard
            l2 = min_hazard+cuarto

            m1 = l2
            m2 = min_hazard + mitad

            h1 = m2
            h2 =  min_hazard+tres_cuartos

            v1 =h2
            v2 = max_hazard

            ranges_of_values = (
                ('Low (' + str(l1) + ', ' + str(l2) + ')', l1, l2, 'green'),
                ('Medium(' + str(m1) + ', ' + str(m2) + ')', m1, m2, 'yellow'),
                ('High (' + str(h1) + ', ' + str(h2) + ')', h1, h2, 'orange'),
                ('Very High (' + str(v1) + ', ' + str(v2) + ')', v1, v2, 'red'),
            )

        except:
            print("")

            ranges_of_values = (
            ('Low ', 0, 0, 'green'),
                ('Medium', 0, 0, 'yellow'),
                ('High ', 0, 0, 'orange'),
                ('Very High ', 0, 0, 'red'),
            )

        # create a category for each item in hazard scale
        ranges = []
        for label, lower, upper, color in ranges_of_values:
            symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())

            if symbol is not None:
                symbol.setColor(QColor(color))
                rng = QgsRendererRangeV2(lower, upper, symbol, label)
                ranges.append(rng)

        # create the renderer and assign it to a layer
        expression = 'hazard'  # field name
        renderer = QgsGraduatedSymbolRendererV2(expression, ranges)
        layer.setRendererV2(renderer)

        QgsMapLayerRegistry.instance().addMapLayer(layer, False)

        # lyr = QgsMapLayerRegistry.instance().mapLayersByName("hazard")[0]
        root = QgsProject.instance().layerTreeRoot()
        # myGroup1 = root.addGroup("My Group 1")
        # If you want to add it to a particular position in the ToC, use:

        namegroup = "Hazard"



        myGroup1 = root.findGroup(namegroup)

        if myGroup1 is None:
            myGroup1 = root.insertGroup(0, namegroup)

        root = myGroup1.insertLayer(0, layer)




    def disconnect(self):

        self.PredictionModel.setTabEnabled(1, False)

        self.PredictionModel.setTabEnabled(2, False)

        self.PredictionModel.setTabEnabled(3, False)

        self.PredictionModel.setTabEnabled(4, False)

        self.PredictionModel.setTabEnabled(5, False)

        self.PredictionModel.setTabEnabled(6, False)



        self.connectionComboBox.clear()


    def importFragilitiesAssignationToBuilding(self):

        from Logic.FragilityCurve import FragilityCurve

        workingdir = self.setWorkingDirectorylineEdit.text()

        #filename = workingdir + "fragilities_assignation.txt"

        fragilitesAssignationFile = self.assignedFragilitiesLinesEdit.text()

        print " fragilitesAssignationFile" + fragilitesAssignationFile
        databasename = self.getDatabasename()

        FragilityCurve.deleteFragilitiesAssignation(databasename)

        #FragilityCurve.importFragilitiesAssignationFromText(fragilitesAssignationFile, databasename)
        #not importing the fragilities from filed, but fro  the input layer

        FragilityCurve.importFragilitiesAssignationFromInput()


    def exportFragilitiesAssignation(self):

        from Logic.FragilityCurve import FragilityCurve

        workingdir = self.setWorkingDirectorylineEdit.text()

        filename = workingdir + "fragilities_assignation.txt"
        databasename = self.getDatabasename()

        FragilityCurve.exportFragilitiesAssignationToExcel(filename, databasename)

    def exportHazardParameters(self):
        from Database import Writes

        workingdir = self.setWorkingDirectorylineEdit.text()

        filename = workingdir + "hazard_parameters.txt"
        epicenter = self.epicenterLineEdit.text()
        momentum = self.MomentumLineEdit.text()

        from time import gmtime, strftime

        start_time = strftime("%d %b %Y %H:%M:%S", gmtime())

        try:
            contentsbefore = Writes.readFileAsString(filename)
        except:
            contentsbefore = ""


        contentsnew = "\n " + start_time + " epicenter " + str(epicenter) +  " intensity " + str(momentum)
        contents = contentsbefore + contentsnew

        Writes.writefile(filename, contents)

    def exportIntensityPredictiveModel(self):
        from Database import Writes

        workingdir = self.setWorkingDirectorylineEdit.text()

        filename = workingdir + "intensity_predictive_model.txt"
        momentum = self.MPredictiveModelLineEdit.text()

        from time import gmtime, strftime

        start_time = strftime("%d %b %Y %H:%M:%S", gmtime())

        try:
            contentsbefore = Writes.readFileAsString(filename)
        except:
            contentsbefore = ""

        contentsnew = "\n " + start_time + " intensity " + str(momentum)
        contents = contentsbefore + contentsnew

        Writes.writefile(filename, contents)

    def getPathScripts(self):
        #return "C:/Data/Python/"
        #return ""

        from Utils import Directory

        return Directory.getPathScripts()

    def populateFragilityCurvesComboBox(self):

        print " Populsating the fragility curves combo box "

        databasename = self.getDatabasename()

        ids = FragilityCurve.readFragilityCurves(databasename)

        self.selectCurvescomboBox.clear()

        idsstr = ids.split(";")

        print " id str " + str(idsstr) + ""

        for count in range(0, len(idsstr)):
            self.selectCurvescomboBox.addItem(idsstr[count])

        self.minimMaximIMLcomboBox.clear()

        #ranges = self.rangesIMLintensities(uri)

        ranges = ""

        '''
        Attenzione, the rangfes are readen from the file
        '''
        if (ranges == ""):
            self.minimMaximIMLcomboBox.addItem("1 5")
        else:
            self.minimMaximIMLcomboBox.addItem(ranges)


        '''
    
        from Database.SQL import sql

        path = sql.getWorkingDir()

        print " working dir is "
        print path
        logging.debug("path")
        logging.debug(path)

        path = path.replace("\\", "/")
        
        '''



