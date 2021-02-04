
import pyqt5ac

import PyQt5.uic.pyuic

#https://pypi.org/project/pyqt5ac/

'''
pyqt5ac.main(rccOptions='', uicOptions='--from-imports', force=False, config='',
             ioPaths=[[r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/DistroMap/ui_distromap.ui', r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/DistroMap/ui_distromap.py'],
                      [r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/DistroMap/resources.qrc', r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/DistroMap/resources_rc.py']])


pyqt5ac.main(rccOptions='', uicOptions='--from-imports', force=False, config='',
             ioPaths=[[r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/widget3/widget3_dockwidget_base.ui', r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/widget3/widget3_dockwidget.py'],
                      [r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/widget3/resources.qrc', r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/widget3/resources_rc.py']])
'''

'''
#from .widget3_dockwidget import widget3DockWidget
pyqt5ac.main(rccOptions='', uicOptions='--from-imports', force=False, config='',
             ioPaths=[[r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/widget3/widget3DockWidget.ui', r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/widget3/widget3_dockwidget.py'],
                      [r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/widget3/resources.qrc', r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/widget3/resources_rc.py']])
'''

#--- good dock mod----

pyqt5ac.main(rccOptions='', uicOptions='--from-imports', force=False, config='',
             ioPaths=[[r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/seismic_risk/seismicrisk_dockwidget_base.ui', r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/seismic_risk/seismicrisk_dockwidget.py'],
                      [r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/seismic_risk/resources.qrc', r'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/seismic_risk/resources.py']])

#C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/dockmod

#exec(open("D:/repositorydef/SeismicRisk/python3/ejecutar.py").read())
#python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py
#python -m PyQt5.uic.pyuic -x "C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/DistroMap/ui_distromap.ui" -o "C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/DistroMap/distromap.py"

#pyrcc5 "C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/DistroMap/resources_rc.qrc" -o "C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/DistroMap/resources_rc.py"

#cd C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/DistroMap/

#exec(open("D:/repositorydef/SeismicRisk/python3/compiler_pyqt5.py").read())

#pyqt5ac 'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/widget3/widget3DockWidget.ui' -o 'C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/widget3/widget3DockWidget.py'

#https://www.hatarilabs.com/ih-en/how-to-add-multiple-vector-layers-and-group-them-in-qgis-with-pyqgis-tutorial