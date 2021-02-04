# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Assign_AutoField_to_Layer.ui'
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

class Ui_AssignAutoFieldToLayerDialog(object):
    def setupUi(self, AssignAutoFieldToLayerDialog):
        AssignAutoFieldToLayerDialog.setObjectName(_fromUtf8("AssignAutoFieldToLayerDialog"))
        AssignAutoFieldToLayerDialog.resize(400, 198)
        self.gridLayout = QtGui.QGridLayout(AssignAutoFieldToLayerDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(AssignAutoFieldToLayerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 1)
        self.cboLayer = QtGui.QComboBox(AssignAutoFieldToLayerDialog)
        self.cboLayer.setObjectName(_fromUtf8("cboLayer"))
        self.gridLayout.addWidget(self.cboLayer, 2, 0, 1, 1)
        self.label = QtGui.QLabel(AssignAutoFieldToLayerDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.label_2 = QtGui.QLabel(AssignAutoFieldToLayerDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.retranslateUi(AssignAutoFieldToLayerDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AssignAutoFieldToLayerDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AssignAutoFieldToLayerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AssignAutoFieldToLayerDialog)

    def retranslateUi(self, AssignAutoFieldToLayerDialog):
        AssignAutoFieldToLayerDialog.setWindowTitle(_translate("AssignAutoFieldToLayerDialog", "Assign AutoField to layer", None))
        self.label.setText(_translate("AssignAutoFieldToLayerDialog", "Choose a layer to assign the AutoField you have selected to it:", None))
        self.label_2.setText(_translate("AssignAutoFieldToLayerDialog", "Only editable vector layers having a field with the same name as the AutoField configuration are shown. After clicking OK, the original AutoField will be removed.", None))

