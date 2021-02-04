#/***************************************************************************
# ZoomToPoint
# 
# Zoom to a specified point on the map
#                             -------------------
#        begin                : 2011-11-12
#        copyright            : (C) 2011 by GeoApt LLC
#        email                : gsherman@geoapt.com
# ***************************************************************************/
# 
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# Makefile for a PyQGIS plugin 

PLUGINNAME = zoomtopoint

PY_FILES = zoomtopoint.py zoomtopointdialog.py __init__.py

EXTRAS = icon.png 

UI_FILES = ui_zoomtopoint.py

RESOURCE_FILES = resources.py

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc4 -o $@  $<

%.py : %.ui
	pyuic4 -o $@ $<

# The deploy  target only works on unix like operating system where
# the Python plugin directory is located at:
# $HOME/.qgis/python/plugins
deploy: compile
	mkdir -p $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(EXTRAS) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)

# Create a zip package. Requires passing a valid commit or tag as follows:
#   make package VERSION=Version_0.3.2
package: compile
		rm -f zoomtopoint.zip

		git archive --prefix=zoomtopoint/ -o zoomtopoint.zip $(shell git rev-list --max-count=1 HEAD)

clean:
	rm $(UI_FILES) $(RESOURCE_FILES)
