import sys
sys.path
sys.path.append('D:/repositorydef/SeismicRisk')

class ModuloShapefile():

    def loadShapefile(self, fname, databasename):

        database_exists = 1

        if (database_exists < 0):
            widget = self.iface.messageBar().createMessage(
                "Please ckeck the database system is running ")
            self.iface.messageBar().pushWidget(widget, self.iface.messageBar().WARNING)

            return -1
        else:

            #self.updateDatabasename(databasename)  # write the datamadase name in the file

            #print " loading tha shapefile "

            import inspect

            # sqldir = inspect.getfile(SeismicRiskDockWidget.__class__)

            import os
            # path = os.path.dirname(SeismicRiskDockWidget.__file__)

            # from Database.SQL import sql

            # path = sql.getWorkingDir()

            #from Utils import Directory

            #sqldir = Directory.getPathSqlDir()
            # sqldir = path.replace("Utils", "Database/SQL")
            sqldir = "D:/repositorydef/SeismicRisk/Database/SQL"
            sqldir = sqldir + "/"


            import os, subprocess



            host = "127.0.0.1"
            port = "5434"
            user = "pgis"
            password = "postgres"
            database = "popoli"

            # Choose your PostgreSQL version here
            os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
            #os.environ['PATH'] += "r';" + con.getPathDatabase()  ATTENZION
            # D:\usbgis\apps\postgresql93\bin

            # os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'
            # os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

            # maquina = " -h 127.0.0.1 -p 5434"

            maquina = " -h " + host + " -p " + port

            # os.environ['PATH'] += r';C:\usbgis\apps\postgresql93\bin'

            #dir_path = con.getPathDatabase()

            dir_path = ""

            import sys
            # sys.path
            sys.path.append(dir_path)

            # os.environ['PATH'] += r';D:\Program Files\PostgreSQL\11\bin'





            # http://www.postgresql.org/docs/current/static/libpq-envars.html

            '''
            os.environ['PGHOST'] = 'localhost'
            os.environ['PGPORT'] = '5432'
            os.environ['PGUSER'] = 'potgres'
            os.environ['PGPASSWORD'] = 'postgres'
            os.environ['PGDATABASE'] = 'prueba4'
            '''

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

            for shape_path in shapefile_list:
                # cmds = "shp2pgsql -S -s SRID=4326 -t 2D \"" + shape_path + "\" popoliforpostgres   -U postgres "

                cmds = "shp2pgsql -s SRID=4326 -t 2D \"" + shape_path + "\" popoliforpostgres   -U postgres "

                # cmds = cmds + '> "C:/Data/Python/insert.txt"'


                from Utils import Directory

                path = Directory.getPathSqlDir()

                # path = sql.getWorkingDir()

                sqldir = path.replace("Utils", "Database/temp")
                # sqldir = sqldir + "/"
                dirs = sqldir
                cmds = cmds + '> "' + dirs + 'insert.txt"'

                # cmds = cmds.replace("C:/Data/Python", sqldir)
                #print cmds
                subprocess.call(cmds, shell=True)

            cmd = "dropdb  -U " + user + maquina + " " + databasename

            subprocess.call(cmd, shell=True)

            cmd = "createdb   -U " + user + maquina + " " + databasename + " --encoding='UTF8'"


            subprocess.call(cmd, shell=True)

            # cmd = "psql -d " + databasename +" -U " +con.user + maquina + " < C:/Data/Python/extension_postgis.txt"
            cmd = "psql -d " + databasename + " -U " + user + maquina + " < \"" + sqldir + "extension_postgis.txt\""

            subprocess.call(cmd, shell=True)

            # cmd = "psql -d " + databasename +" -U " +con.user + maquina + " < C:/Data/Python/function_get_random_number.txt"
            cmd = "psql -d " + databasename + " -U " + user + maquina + " <  \"" + sqldir + "function_get_random_number.txt\""

            subprocess.call(cmd, shell=True)

            cmd = "psql -d " + databasename + " -U " + user + maquina + " <  \"" + sqldir + "function_calculate_pga.txt\""
            #print cmd

            #logging.debug(cmd)

            subprocess.call(cmd, shell=True)

            # cmd = "psql -d " + databasename + " -U " + con.user + maquina + " < C:/Data/Python/random_points_in_qgis.txt"
            cmd = "psql -d " + databasename + " -U " + user + maquina + " < \"" + sqldir + "random_points_in_qgis.txt\""
            # cmd = cmd.replace("C:/Data/Python/", sqldir)

            # subprocess.call(cmd, shell=True)

            # cmd = "psql -U " +con.user + maquina + " " + databasename + " < C:/Data/Python/insert.txt"
            cmd = "psql -U " + user + maquina + " " + databasename + " < \"" + sqldir + "insert.txt\""
            # cmd = cmd.replace("C:/Data/Python/", sqldir)

            subprocess.call(cmd, shell=True)

            # cmd = "psql -U " +con.user + maquina + " " + databasename+" < C:/Data/Python/create_valutazione.txt"
            cmd = "psql -U " + user + maquina + " " + databasename + " < \"" + sqldir + "create_valutazione.txt\""
            # cmd = cmd.replace("C:/Data/Python/", sqldir)

            subprocess.call(cmd, shell=True)



fname=""
databasename="python3"
fname="D:/Data/Popoli/febrero2019/popoli.shp"

md = ModuloShapefile()
md.loadShapefile( fname, databasename)

#exec(open("D:/repositorydef/SeismicRisk/python3/ModuloShapefile.py").read())

