# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Import_AutoFields.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImportAutoFieldsDialog(object):
    def setupUi(self, ImportAutoFieldsDialog):
        ImportAutoFieldsDialog.setObjectName(_fromUtf8("ImportAutoFieldsDialog"))
        ImportAutoFieldsDialog.resize(710, 426)
        self.verticalLayout = QtGui.QVBoxLayout(ImportAutoFieldsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ImportAutoFieldsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tblAutoFields = QtGui.QTableWidget(ImportAutoFieldsDialog)
        self.tblAutoFields.setLineWidth(1)
        self.tblAutoFields.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblAutoFields.setAlternatingRowColors(False)
        self.tblAutoFields.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tblAutoFields.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblAutoFields.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tblAutoFields.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.tblAutoFields.setShowGrid(True)
        self.tblAutoFields.setGridStyle(QtCore.Qt.SolidLine)
        self.tblAutoFields.setObjectName(_fromUtf8("tblAutoFields"))
        self.tblAutoFields.setColumnCount(6)
        self.tblAutoFields.setRowCount(4)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tblAutoFields.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tblAutoFields.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblAutoFields.setItem(3, 2, item)
        self.tblAutoFields.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tblAutoFields)
        self.buttonBox = QtGui.QDialogButtonBox(ImportAutoFieldsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ImportAutoFieldsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ImportAutoFieldsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ImportAutoFieldsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportAutoFieldsDialog)

    def retranslateUi(self, ImportAutoFieldsDialog):
        ImportAutoFieldsDialog.setWindowTitle(_translate("ImportAutoFieldsDialog", "Import AutoFields", None))
        self.label.setText(_translate("ImportAutoFieldsDialog", "Select, on the right hand side, layer and field for each AutoField loaded from file:", None))
        item = self.tblAutoFields.horizontalHeaderItem(0)
        item.setText(_translate("ImportAutoFieldsDialog", "Layer", None))
        item = self.tblAutoFields.horizontalHeaderItem(1)
        item.setText(_translate("ImportAutoFieldsDialog", "Field", None))
        item = self.tblAutoFields.horizontalHeaderItem(2)
        item.setText(_translate("ImportAutoFieldsDialog", "Value/Expression", None))
        item = self.tblAutoFields.horizontalHeaderItem(3)
        item.setText(_translate("ImportAutoFieldsDialog", "Assignation", None))
        item = self.tblAutoFields.horizontalHeaderItem(4)
        item.setText(_translate("ImportAutoFieldsDialog", "To layer", None))
        item = self.tblAutoFields.horizontalHeaderItem(5)
        item.setText(_translate("ImportAutoFieldsDialog", "To field", None))
        __sortingEnabled = self.tblAutoFields.isSortingEnabled()
        self.tblAutoFields.setSortingEnabled(False)
        item = self.tblAutoFields.item(0, 0)
        item.setText(_translate("ImportAutoFieldsDialog", "Layer1", None))
        item = self.tblAutoFields.item(0, 1)
        item.setText(_translate("ImportAutoFieldsDialog", "Field1", None))
        item = self.tblAutoFields.item(0, 2)
        item.setText(_translate("ImportAutoFieldsDialog", "area", None))
        item = self.tblAutoFields.item(1, 0)
        item.setText(_translate("ImportAutoFieldsDialog", "Layer4", None))
        item = self.tblAutoFields.item(1, 1)
        item.setText(_translate("ImportAutoFieldsDialog", "Field4", None))
        item = self.tblAutoFields.item(1, 2)
        item.setText(_translate("ImportAutoFieldsDialog", "area", None))
        item = self.tblAutoFields.item(2, 0)
        item.setText(_translate("ImportAutoFieldsDialog", "Layer2", None))
        item = self.tblAutoFields.item(2, 1)
        item.setText(_translate("ImportAutoFieldsDialog", "Field2", None))
        item = self.tblAutoFields.item(2, 2)
        item.setText(_translate("ImportAutoFieldsDialog", "length", None))
        item = self.tblAutoFields.item(3, 0)
        item.setText(_translate("ImportAutoFieldsDialog", "Layer3", None))
        item = self.tblAutoFields.item(3, 1)
        item.setText(_translate("ImportAutoFieldsDialog", "Field3", None))
        item = self.tblAutoFields.item(3, 2)
        item.setText(_translate("ImportAutoFieldsDialog", "x coordinate", None))
        self.tblAutoFields.setSortingEnabled(__sortingEnabled)

import resources_rc