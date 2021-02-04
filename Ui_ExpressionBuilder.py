# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ExpressionBuilder.ui'
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

class Ui_ExpressionDialog(object):
    def setupUi(self, ExpressionDialog):
        ExpressionDialog.setObjectName(_fromUtf8("ExpressionDialog"))
        ExpressionDialog.resize(715, 425)
        ExpressionDialog.setMaximumSize(QtCore.QSize(16777215, 425))
        self.verticalLayout = QtGui.QVBoxLayout(ExpressionDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.expressionBuilderWidget = gui.QgsExpressionBuilderWidget(ExpressionDialog)
        self.expressionBuilderWidget.setObjectName(_fromUtf8("expressionBuilderWidget"))
        self.verticalLayout.addWidget(self.expressionBuilderWidget)
        self.buttonBox = QtGui.QDialogButtonBox(ExpressionDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ExpressionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExpressionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExpressionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExpressionDialog)

    def retranslateUi(self, ExpressionDialog):
        ExpressionDialog.setWindowTitle(_translate("ExpressionDialog", "Expression Builder for AutoFields", None))

from qgis import gui
