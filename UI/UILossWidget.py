import PyQt4.QtGui
from PyQt4.QtGui import *

import sys
sys.path.insert(0, "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\\")

import SeismicRiskDockWidget


def readCostTableWidget(seismicRiskDockWidget, values, workingDir, filenametext):

    ''' Lectura de los atributos '''
    print " Leer atributos ...."
    #filename = "C:/Data/Python/material.txt"
    #filename = workingDir + "material.txt"
    if (filenametext != ""):
        infile = open(filenametext ,"r")
        lines = infile.readlines()

        print " lines for populating losses "
        print lines
        infile.close()

        seismicRiskDockWidget.costTableWidget.setRowCount(len(lines))
        seismicRiskDockWidget.costTableWidget.setColumnCount(6)


        for i in range(0, len(lines)):
            tokens = lines[i].strip().split("|")

            #print " tokens is " + str(tokens)

            #gid, name, area, material, cost



            try:
                valor0 = PyQt4.QtGui.QTableWidgetItem(tokens[0])
            except:
                valor0 = PyQt4.QtGui.QTableWidgetItem("0")


            try:
                valor1 = PyQt4.QtGui.QTableWidgetItem(tokens[1])
            except:
                valor1 = PyQt4.QtGui.QTableWidgetItem("0")

            try:
                valor2 = PyQt4.QtGui.QTableWidgetItem(tokens[2])
            except:
                valor2 = PyQt4.QtGui.QTableWidgetItem("0")

            try:
                valor3 = PyQt4.QtGui.QTableWidgetItem(tokens[3])
            except:
                valor3 = PyQt4.QtGui.QTableWidgetItem("0")

            try:
                valor4 = PyQt4.QtGui.QTableWidgetItem(tokens[4])
            except:
                valor4 = PyQt4.QtGui.QTableWidgetItem("0")

            try:
                valor5 = PyQt4.QtGui.QTableWidgetItem(tokens[5])
            except:
                valor5 = PyQt4.QtGui.QTableWidgetItem("0")

            '''

            try:
                valor6 = PyQt4.QtGui.QTableWidgetItem(tokens[6])
            except:
                valor6 = PyQt4.QtGui.QTableWidgetItem("0")
            '''


            item0 = PyQt4.QtGui.QTableWidgetItem(valor0)

            item1 = PyQt4.QtGui.QTableWidgetItem(valor1)
            item2 = PyQt4.QtGui.QTableWidgetItem(valor2)
            item3 = PyQt4.QtGui.QTableWidgetItem(valor3)
            item4 = PyQt4.QtGui.QTableWidgetItem(valor4)
            item5 = PyQt4.QtGui.QTableWidgetItem(valor5)
            #item6 = PyQt4.QtGui.QTableWidgetItem(valor6)

                # price = QtGui.QTableWidgetItem(valor)

            seismicRiskDockWidget.costTableWidget.setItem(i ,0 ,item0)
            seismicRiskDockWidget.costTableWidget.setItem(i, 1, item1)
            seismicRiskDockWidget.costTableWidget.setItem(i, 2, item2)
            seismicRiskDockWidget.costTableWidget.setItem(i, 3, item3)
            seismicRiskDockWidget.costTableWidget.setItem(i, 4, item4)
            seismicRiskDockWidget.costTableWidget.setItem(i, 5, item5)
            #seismicRiskDockWidget.costTableWidget.setItem(i, 5, item6)



            # self.tableViewMethodology.setItem(i,2,price)



    # self.tableWidget.data = data
    # http://stackoverflow.com/questions/22420496/reading-all-the-values-from-qtablewidget-in-pyqt

    seismicRiskDockWidget.costTableWidget.setHorizontalHeaderLabels((  'Gid','Name', 'Area', 'Unit Cost ', 'Total Cost ',  'damage'))

    seismicRiskDockWidget.costTableWidget.resizeColumnsToContents()
    seismicRiskDockWidget.costTableWidget.resizeRowsToContents()

    from Logic.LossModel import Loss

    cost= Loss.calculatetotalcost(seismicRiskDockWidget.getDatabasename())
    seismicRiskDockWidget.totalLosslineEdit.setText(str(cost))