# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SeismicRisk
                                 A QGIS plugin
 A plugin for calculation of seismic risk at urban environment
                             -------------------
        begin                : 2018-03-26
        copyright            : (C) 2018 by UdA Chieti Pescara
        email                : gonzalez.aleksander@unich.it
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SeismicRisk class from file SeismicRisk.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .SeismicRisk import SeismicRisk
    return SeismicRisk(iface)
