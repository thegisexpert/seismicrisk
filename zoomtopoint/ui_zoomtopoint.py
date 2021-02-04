# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_zoomtopoint.ui'
#
# Created: Fri Dec 16 17:43:15 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ZoomToPoint(object):
    def setupUi(self, ZoomToPoint):
        ZoomToPoint.setObjectName(_fromUtf8("ZoomToPoint"))
        ZoomToPoint.resize(453, 163)
        ZoomToPoint.setWindowTitle(QtGui.QApplication.translate("ZoomToPoint", "Zoom to Point", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(ZoomToPoint)
        self.buttonBox.setGeometry(QtCore.QRect(268, 98, 176, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(ZoomToPoint)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 35, 435, 33))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.hboxlayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setText(QtGui.QApplication.translate("ZoomToPoint", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.xCoord = QtGui.QLineEdit(self.layoutWidget)
        self.xCoord.setObjectName(_fromUtf8("xCoord"))
        self.hboxlayout.addWidget(self.xCoord)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setText(QtGui.QApplication.translate("ZoomToPoint", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.hboxlayout.addWidget(self.label_2)
        self.yCoord = QtGui.QLineEdit(self.layoutWidget)
        self.yCoord.setObjectName(_fromUtf8("yCoord"))
        self.hboxlayout.addWidget(self.yCoord)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setText(QtGui.QApplication.translate("ZoomToPoint", "Scale view by", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinBoxScale = QtGui.QSpinBox(self.layoutWidget)
        self.spinBoxScale.setObjectName(_fromUtf8("spinBoxScale"))
        self.gridlayout.addWidget(self.spinBoxScale, 0, 1, 1, 1)
        self.hboxlayout.addLayout(self.gridlayout)
        self.label_4 = QtGui.QLabel(ZoomToPoint)
        self.label_4.setGeometry(QtCore.QRect(9, 9, 253, 20))
        self.label_4.setText(QtGui.QApplication.translate("ZoomToPoint", "Zoom to Point", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(ZoomToPoint)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 221, 64))
        self.label_5.setText(QtGui.QApplication.translate("ZoomToPoint", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">For geographic data, X is longitude and </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">Y is latitude. For projected data, enter</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"> the X and Y in appropriate units for the </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">projection, such as meters or feet.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(ZoomToPoint)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ZoomToPoint.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ZoomToPoint.reject)
        QtCore.QMetaObject.connectSlotsByName(ZoomToPoint)
        ZoomToPoint.setTabOrder(self.xCoord, self.yCoord)
        ZoomToPoint.setTabOrder(self.yCoord, self.spinBoxScale)
        ZoomToPoint.setTabOrder(self.spinBoxScale, self.buttonBox)

    def retranslateUi(self, ZoomToPoint):
        pass

