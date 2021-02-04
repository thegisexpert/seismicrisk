import PyQt4.QtGui
from PyQt4.QtGui import *

import sys

#plugin_dir = "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\\"

import os


path = os.path.dirname(__file__)

path = path.replace("\\", "/")


path = path.replace("UI", "")

sys.path.insert(0,path)

print " lib_path is "
print path

'''
This should be in a separate package
class Directory
'''
import Directory

plugin_dir = Directory.getPluginDir()

sys.path.insert(0, plugin_dir)



import SeismicRiskDockWidget


def setShapefilePath(SeismicRiskDockWidget):
    fname = QFileDialog.getOpenFileName(SeismicRiskDockWidget, 'Open file',
                                        'd:\\Data\\Popoli', "*")



    completo =SeismicRiskDockWidget.checkShapefile(fname)

    if completo>0:
        SeismicRiskDockWidget.setNewConnectionShapefilePath.setText(fname)


def setWorkingDirectoryPath(SeismicRiskDockWidget):

    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.Directory)

    my_dir = QFileDialog.getExistingDirectory(
        SeismicRiskDockWidget,
        "Open a folder",
        "C:\\",
        QFileDialog.ShowDirsOnly
    )

    SeismicRiskDockWidget.setWorkingDirectorylineEdit.setText(my_dir + "\\")

    SeismicRiskDockWidget.setWorkingDirectorylineEdit.setText(my_dir + "\\")
    SeismicRiskDockWidget.predictveIndicatorsLineEdit.setText(my_dir + "\\fragilities.txt")
    SeismicRiskDockWidget.soilDetailsLineEdit.setText(my_dir + "\\soil.txt")


    SeismicRiskDockWidget.assignedFragilitiesLinesEdit.setText(my_dir + "\\fragilities_assignation.txt")

    SeismicRiskDockWidget.fragilityCurvesRouteLineEdit.setText(my_dir + "\\Curves\\")
    SeismicRiskDockWidget.CostValuespushFile.setText(my_dir + "\\losses.csv")


def updateLayerTable(SeismicRiskDockWidget):
    #fname = QFileDialog.getOpenFileName(SeismicRiskDockWidget, 'Open file',
    #                                    'd:\\Data\\Popoli', "*")

    from Logic.PredictiveModel import PredictiveModel

    database_exists = PredictiveModel.checkdatabase("test")



    fname = SeismicRiskDockWidget.setNewConnectionShapefilePath.text()

    if len(fname) > 0:
        databasename = fname.lower()
    else:
        return -1

    import ntpath
    name = ntpath.basename(fname)
    name = name.replace(".shp", "")

    import sys
    sys.path
    #sys.path.insert(0, 'C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database')

    database_dir = Directory.getPluginDir()

    sys.path.insert(0, database_dir + "Database")

    import MyDatabase

    existeshp = None

    try:

        namesoddb = MyDatabase.getListofDatabases()

        print " loaded list of databases line 99"

        #print  " dbname " + name
        #print  " all db " + namesoddb

        existeshp = name in namesoddb

        '''print existeshp'''

    except:
        existeshp = None



    SeismicRiskDockWidget.connectionComboBox.addItem(name)

    if not existeshp:
        SeismicRiskDockWidget.loadShapefile(fname, name)

        SeismicRiskDockWidget.loadComunityOfStudy( name)





        # self.bar = QgsMessageBar()
        # self.bar.pushMessage("Connection", "Created", level=Qgis.Info)
        widget = SeismicRiskDockWidget.iface.messageBar().createMessage("Darabase created", "New Connection")

        SeismicRiskDockWidget.iface.messageBar().pushWidget(widget, SeismicRiskDockWidget.iface.messageBar().INFO)

    else:

        widget = SeismicRiskDockWidget.iface.messageBar().createMessage("Database exists", "New Connection")
        # self.iface.messageBar().pushWidget(widget, Qgis.Warning)
        SeismicRiskDockWidget.iface.messageBar().pushWidget(widget, SeismicRiskDockWidget.iface.messageBar().WARNING)

        loadLayersFromDatabase(SeismicRiskDockWidget)

    SeismicRiskDockWidget.updateDatabasename(name)

    nomtabla = "communitytostudy"
    # SeismicRiskDockWidget.loadLayerIntoCanvas(name, nomtabla, "Losses")
    SeismicRiskDockWidget.loadLayerIntoCanvas(nomtabla, "Input")

    nomtabla = "valutazione"
    #SeismicRiskDockWidget.loadLayerIntoCanvas(name, nomtabla, "Losses")
    SeismicRiskDockWidget.loadLayerIntoCanvas( nomtabla, "Losses")



    path_form = Directory.getPluginDir()
    path_form = path_form  + 'UI\\building.ui'

    #path_form = 'C:\Users\AG\.qgis2\python\plugins\SeismicRisk\UI\\building.ui'

    nomtabla = "popolicommunitytostudy"

    SeismicRiskDockWidget.setForm(nomtabla, path_form)

    '''


    model = QtGui.QTableWidgetItem(fname)

    self.layersTableView.setRowCount(5)
    self.layersTableView.setColumnCount(1)


    print " Antes del set "


    try:
           self.layersTableView.setItem(1,1,model)

    except ValueError:
            print(str(ValueError))

    #5rice = QtGui.QTableWidgetItem(valor)

    self.layersTableView.resizeColumnsToContents()
    self.layersTableView.resizeRowsToContents()

    #self.le.setPixmap(QPixmap(fname))

    # self.loadHazards()
    Logica.populatehazard()

    databasename = "prueba7"
    self.loadShapefile(fname, databasename)

=
    Logica.populateparameters(90)

    print " I will load into canvas 1405 " + databasename
    self.loadLayerIntoCanvas(databasename, "popoliforpostgres")



    self.cargaLayerIntoCanvasByType(databasename, "type=1")

    self.cargaLayerIntoCanvasByType(databasename, "type=2")

    self.cargaLayerIntoCanvasByType(databasename, "type=3")

    self.cargaLayerIntoCanvasByType(databasename, "type=4")

    self.cargaLayerIntoCanvasByType(databasename, "type=5")






    Logica.addAttributesData()

    print " Populate comboBox "
    ids = Logica.readIds()

    idsstr = ids.split(";")

    try:

        for count in range(1,len(ids)):
            self.idComboBox.addItem(idsstr[count]
    except:
        print "Data loaded?"

    self.loadFragilities("prueba7")


        #self.calcularResiliencia()

      '''

    return 0

def createLosses(workingDir,databasename):
    from Logic.LossModel import Loss
    Loss.createLosses(databasename)

    filenameexcel =  workingDir + "material.txt"

    Loss.populateMaterialAndCost(databasename, filenameexcel )

    #filenameout= filenameexcel
    #filenamemat = workingDir + "material.txt"
    filenamemat = workingDir + "losscsv.txt"

    Loss.exportLossForReadingfromUi(databasename, filenamemat)

    #Loss.createIndexDamage(databasename)

    #filenameout = workingDir + "material.txt"
    filenameout = workingDir + "losscsv.txt"
    Loss.exportLossesToText(filenameout, databasename)



def createTemplates(workingDir, databasename):

    from Logic.PredictiveModel import PredictiveModel
    PredictiveModel.populateValutazione(databasename)

    #SeismicRiskDockWidget.connectionComboBox.addItem(databasename)
    #filename = workingDir + "fragilities.csv"

    filename = workingDir + "fragilities.txt"

    PredictiveModel.exportValutazioneToExcelv2(filename)

    createLosses(workingDir,databasename)

    '''
    In this moment, the fragilities curves are not created
    '''
    
    from Logic.FragilityCurve import FragilityCurve

    FragilityCurve.createFragilityTable(databasename)

    FragilityCurve.insertFragilityCurves(databasename, 0)
    FragilityCurve.poputateFragilitiesCurvesToBuildings(databasename)


    try:
        fileassing = workingDir + "fragilities_assignation.xls"
        FragilityCurve.exportFragilitiesAssignationToExcel(fileassing, databasename)

    except:
        print ""


def loadLayersFromDatabase( SeismicRiskDockWidget):
    # 117

    namegroup = "Vulnerability"

    vulnerability_name = "popoliforpostgres"
    fragility_name = "view_fragility_curve_structure"


    try:

        LYR1 = SeismicRiskDockWidget.loadLayerIntoCanvas(vulnerability_name, namegroup)
        SeismicRiskDockWidget.colorVulnerabilityMap(LYR1)
    except:
        print ""


    try:

        LYR1 = SeismicRiskDockWidget.loadLayerIntoCanvas(fragility_name, namegroup)
        SeismicRiskDockWidget.colorFragilitiesMap(LYR1)
    except:
        print ""




    LYR = SeismicRiskDockWidget.loadLayerIntoCanvas("popoliloss", "Losses")


    SeismicRiskDockWidget.colorLYRWithTotalCost(LYR)

    '''
    SeismicRiskDockWidget.addHazardLayers(0)
    SeismicRiskDockWidget.addHazardLayers(1)
    SeismicRiskDockWidget.addHazardLayers(2)
    SeismicRiskDockWidget.addHazardLayers(3)
    '''

    SeismicRiskDockWidget.addGraduatedSymbolHazardLayer()

    SeismicRiskDockWidget.loadLayerIntoCanvas("epicenter", "epicenter")

    SeismicRiskDockWidget.populateFragilityCurvesComboBox()

    SeismicRiskDockWidget.readCostTable()
    '''
    
    :param SeismicRiskDockWidget: 
    :return: 
    
    try:



        namegroup = "Vulnerability"

        vulnerability_name = "popoliforpostgres"
        LYR1 =SeismicRiskDockWidget.loadLayerIntoCanvas(vulnerability_name, namegroup)


        SeismicRiskDockWidget.colorVulnerabilityMap(LYR1)

        LYR=SeismicRiskDockWidget.loadLayerIntoCanvas("popoliloss", "Losses")

        SeismicRiskDockWidget.colorLYRWithTotalCost(LYR)

      

        SeismicRiskDockWidget.addGraduatedSymbolHazardLayer()

        SeismicRiskDockWidget.populateFragilityCurvesComboBox()

        SeismicRiskDockWidget.readCostTable()
    except:
        print "Ok"
        
    '''








