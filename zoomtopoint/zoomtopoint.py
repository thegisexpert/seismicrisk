"""
/***************************************************************************
         ZoomToPoint  - A QGIS plugin to zoom the map canvas to a point
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from zoomtopointdialog import ZoomToPointDialog

class ZoomToPoint: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface

  def initGui(self):  
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(":/plugins/zoom_to_point/icon.png"), \
        "Zoom To Point", self.iface.mainWindow())
    self.action.setWhatsThis("Configuration for Zoom To Point plugin")
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Zoom to Point...", self.action)

  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Zoom to Point...",self.action)
    self.iface.removeToolBarIcon(self.action)

  # run method that performs all the real work
  def run(self): 
    # create and show the ZoomToPoint dialog 
    dlg = ZoomToPointDialog() 
    #dlg.setupUi(self)
    # fetch the last used values from settings and intialize the
    # dialog with them
    settings = QSettings("MicroResources", "ZoomToPoint")
    xValue = settings.value("coordinate/x", '')
    dlg.ui.xCoord.setText(str(xValue))
    yValue = settings.value("coordinate/y", '')
    dlg.ui.yCoord.setText(str(yValue))
    scale = settings.value("zoom/scale", 4)
    dlg.ui.spinBoxScale.setValue(int(scale))

    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1: 
      # Get the coordinates and scale factor from the dialog
      x = dlg.ui.xCoord.text() 
      y = dlg.ui.yCoord.text()
      scale = dlg.ui.spinBoxScale.value() 
      # Create a rectangle to cover the new extent
      #rect = QgsRectangle(float(x)-scale,float(y)-scale,float(x)+scale,float(y)+scale) 
      #QgsMessageLog.logMessage("X is {}".format(float(x)), 'Zoom to point', 1)
      rect = QgsRectangle(
              float(x) - scale,
              float(y) - scale, 
              float(x) + scale,
              float(y) + scale) 
      #QgsMessageLog.logMessage("zoom extent is {}".format(rect.toString()), 'Zoom to point', 1)

      #self.iface.messageBar().pushMessage("New Extent", rect.toString())
      # Get the map canvas
      mc=self.iface.mapCanvas() 
      # Set the extent to our new rectangle
      mc.setExtent(rect)
      # Refresh the map
      mc.refresh()
      # store the settings
      settings.setValue("coordinate/x", x)
      settings.setValue("coordinate/y", y)
      settings.setValue("zoom/scale", scale)

