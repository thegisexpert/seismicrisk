# -*- coding: utf-8 -*-
"""
***************************************************************************
Name			 	 : QuickWKT
Description          : QuickWKT
Date                 : 11/Oct/2010
copyright            : (C) 2010 by ItOpen
email                : info@itopen.it
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
from PyQt4 import QtCore, QtGui
from PyQt4 import uic
import os


EXAMPLES = {
        '' : '',
        'POINT (WKT)' : 'POINT (30 10)',
        'LINESTRING (WKT)' : 'LINESTRING (30 10, 10 30, 40 40)',
        'POLYGON (WKT)' : 'POLYGON ((30 10, 10 20, 20 40, 40 40, 30 10))',
        'POINT (EWKT)' : 'SRID=4326;POINT (30 10)',
        'LINESTRING (EWKT)' : 'SRID=4326;LINESTRING (30 10, 10 30, 40 40)',
        'POLYGON (EWKT)' : 'SRID=4326;POLYGON ((30 10, 10 20, 20 40, 40 40, 30 10))',
        'POINT (WKB)' : r'0101000020E61000000000000000003E400000000000002440',
        'LINESTRING (WKB)' : r'0102000020E6100000030000000000000000003E40000000000000244000000000000024400000000000003E4000000000000044400000000000004440',
        'POLYGON (WKB)' : r'0103000020E610000001000000050000000000000000003E4000000000000024400000000000002440000000000000344000000000000034400000000000004440000000000000444000000000000044400000000000003E400000000000002440'
    }

class QuickWKTDialog(QtGui.QDialog ):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        #ui_path = os.path.join(os.path.dirname(__file__), 'Ui_QuickWKT.ui')

        ui_path = "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\zoomtopoint\ui_zoomtopoint.ui"

        from ..UI import Directory

        dir_sql = Directory.getPluginDir()

        ui_path = "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\UI\\building.ui"

        ui_path = dir_sql + "building.ui"

        print "\n uni_path"
        print ui_path

        dlg = uic.loadUi(ui_path, self)

        #self.exampleComboBox.addItems(EXAMPLES.keys())

        #attrs = vars(dlg.tab_4)


        # {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
        # now dump this in some way or another
        print 'Atributtes:'
        #print ', '.join("%s: %s" % item for item in attrs.items())

        #dlg.lineEdit.setText("safa")

        from Writes import Writes

        stringleido = ""
        try:

            wr = Writes()
            stringleido= wr.readFile("C:/Data/Python/read.txt")
        except:
            stringleido = ""

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.guardar)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)


        #dlg.lineEdit.setText(stringleido)

    @QtCore.pyqtSlot(str)
    def on_exampleComboBox_currentIndexChanged(self, index):
        """
        Set and loads examples
        """
        #example = EXAMPLES[str(index)]
        #self.wkt.setPlainText(example)
        print "ok"

    def guardar(self):
        print "ok"
        values = str(self.id.text()) + str(self.name.text()) + " , " + str(self.description.text()) + ", " + str(self.cost.text())
        print values
        self.accept()


    '''
    def zoom(self):
        from .. import  SeismicRiskDockWidget
        SeismicRiskDockWidget.
    '''


