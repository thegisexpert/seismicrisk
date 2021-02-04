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
 This script initializes the plugin, making it known to QGIS.
"""
def classFactory(iface): 
  # load ZoomToPoint class from file zoom_to_point.py 
  from zoomtopoint import ZoomToPoint 
  return ZoomToPoint(iface) 

