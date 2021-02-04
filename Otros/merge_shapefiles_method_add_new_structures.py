#https://gis.stackexchange.com/questions/89706/how-to-merge-shapefiles-with-attributes-from-a-python-script-in-qgis
'''

import processing
processing.alglist("merge")


display_name="prueba7popoliforpostgres"

layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

layer1 = layerExiste[0]

display_name="popoli2"

layerExiste = QgsMapLayerRegistry.instance().mapLayersByName(display_name)

layer2 = layerExiste[0]


#processing.runalg("qgis:mergevectorlayers", layer1, layer2,"C:/Data/Python/outputfilename.shp")

output="C:/Data/Python/outputfilename.shp"

layer_merge = QgsVectorLayer('LineString', 'line', "memory")
#layer_merge.setCrs(crs_4326)
pr_merge = layer_merge.dataProvider()

processing.tools.general.runalg("qgis:mergevectorlayers", layer1 ,layer2, layer_merge)

'''
'''dopo
'''
import processing


''' create sql as table, and after export.
processing.runalg("qgis:mergevectorlayers",
                  "D:\Data\Queries\pruebapopoli.shp;D:\Data\Queries\pruebapopoli2.shp",
                  "D:\Data\Queries\pruebapopoli3.shp")

processing.runalg("qgis:mergevectorlayers",
                  "/docs/geodata/AMAZONAS.shp;/docs/geodata/PUTUMAYO.shp",
                  "/docs/merged.shp")


D:\Data\Queries\pruebapopoli.shp



pgsql2shp -f "/path/to/jpnei" -h myserver -u apguser -P apgpassword mygisdb


pgsql2shp -f "D:\Data\Queries\popoliqueries.shp" -h 127.1.1.0 -u pgis -P pgis prueba7 hazard


D:\Data\Queries\popoliqueries.shp




generar el query, crear la tabla
exportar popoliforpostgres y la table a shapefile
hacer el mergefiles,
load the shapefile merge

'''


def createNewStructures( fname, databasename):
    import os, subprocess



    maquina = " -h 127.0.0.1 -p 5434"



    # Choose your PostgreSQL version here
    # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
    # D:\usbgis\apps\postgresql93\bin

    # os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'
    # os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

    os.environ['PATH'] += r';C:\usbgis\apps\postgresql93\bin'

    # http://www.postgresql.org/docs/current/static/libpq-envars.html
    os.environ['PGHOST'] = 'localhost'
    os.environ['PGPORT'] = '5432'
    os.environ['PGUSER'] = 'potgres'
    os.environ['PGPASSWORD'] = 'postgres'
    os.environ['PGDATABASE'] = 'prueba4'

    '''
    base_dir = r"c:\Data\Popoli\Popoli"
    full_dir = os.walk(base_dir)
    shapefile_list = []
    for source, dirs, files in full_dir:
        for file_ in files:
            if file_[-3:] == 'shp':
                shapefile_path = os.path.join(base_dir, file_)
                shapefile_list.append(shapefile_path)
                '''

    shapefile_list = []
    shapefile_list.append(fname)


    # pgsql2shp -f qds_cnt -h localhost -u postgres -P password gisdb
    # pgsql2shp -f 'C:/Data/postgis/posrgis.shp' -h  127.0.0.1 -p 5434 -u pgis -P  pgis

    ''' essempio using append
    shp2pgsql -t 2D D:/Data/Popoli/popolifeb2017.shp popoliforpostgres  -s SRID=4320 -U postgres > C:/Data/Python/insert.txt
    shp2pgsql -a -t 2D C:/Data/Postgis/my_shapes.shp  popoliforpostgres  -s SRID=4320  -U postgres > C:/Data/Python/insert2.txt

    '''

    cmd = "psql  -h 127.1.1.0 -p 5434 -U pgis   prueba7 < \"C:\Data\Python\create_new_structures.txt\" > \"C:\Data\Python\errores.txt\""
    print cmd
    subprocess.call(cmd, shell=True)

    cmd = "pgsql2shp -f \"D:\Data\Queries\popoliforpostgres.shp\" -h 127.1.1.0 -p 5434 -u pgis  prueba7 popoliforpostgres"
    print cmd
    subprocess.call(cmd, shell=True)

    cmd = "pgsql2shp -f \"D:\Data\Queries\popoliqueries.shp\" -h 127.1.1.0 -p 5434 -u pgis  prueba7 addstructures"
    print cmd

    subprocess.call(cmd, shell=True)

    import processing
    processing.runalg("qgis:mergevectorlayers",
                      "D:\Data\Queries\popoliforpostgres.shp;D:\Data\Queries\popoliqueries.shp",
                      "D:\Data\Queries\merged.shp")

    from qgis.core import *
    from qgis.utils import *

    layer = qgis.utils.iface.addVectorLayer("D:\Data\Queries\merged.shp", "my layer", "ogr")
    if not layer:
        print "Layer failed to load!"


createNewStructures('', '')


