"""
/***************************************************************************
      ZoomToPointDialog  - A QGIS plugin to zoom the map canvas to a point
                         specified in the input dialog
                             -------------------
    begin                : 2007-10-14
    copyright            : (C) 2007 by Gary E.Sherman
    email                : sherman at mrcc.com
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
from ui_zoomtopoint import Ui_ZoomToPoint 
# create the dialog for zoom to point
class ZoomToPointDialog(QtGui.QDialog): 
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_ZoomToPoint() 
    self.ui.setupUi(self) 

