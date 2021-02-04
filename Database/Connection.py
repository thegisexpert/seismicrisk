import logging

import Directory
logdir = Directory.getPathTempDir()
filelog = logdir + "seismicrisk.log"
logging.basicConfig(filename=filelog,level=logging.DEBUG)
logging.debug('This message should go to the log file')


class Connection():

    host = ""
    port = ""
    user = ""
    password = ""
    database = ""

    import Directory

    pathsql = Directory.getPathSqlDir()
    pathconfig = pathsql.replace("Database/SQL/", "config/")
    print " pathsql " + pathconfig
    # sys.path.insert(0, "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database\\")
    fileconfig = pathconfig + "config.ini"

    def __init__(self):
        #super(Connection, self).__init__()
        self.host = ""
        self.port = ""
        self.user = ""
        self.password = ""
        self.database = ""



    def getConnection(self):

        import Writes

        #https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py




        try:

            import os

            #file = inspect.getfile(Connection.__class__)
            #path = os.path.dirname(file)

            #print path

            #path = "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database\Connection.py"

            # from ..Utils import Directory NON FUNXZIONA PERO DOVIESE
            import Directory



            #path = Directory.getPathSqlDir()

            path = Directory.getPathSqlDir()

            path = path + "currentdatabases.txt"

            print " in connecttion path is "

            print "\n PATH CON"
            print path

            logging.debug(path)



            namedatabase = Writes.readFile(path)[0]

        except:
            import sys
            print " not know the database 82", sys.exc_info()[0]
            raise Exception (" Not know the database" + namedatabase)
            namedatabase = "None"


        con = Connection()

        try:
            db = self.readDatabaseParameters()

            print "db is:"
            print db



            con.host = db["host"]
            con.port = db["port"]
            con.user = db["user"]
            con.password = db["password"]
            con.database = namedatabase
        except:
            import sys
            #print " not know the database 98 ", sys.exc_info()[0]
            print sys.exc_info()
            raise Exception (" Not know the database" + namedatabase)
            namedatabase = "None"



        return con


    def getConnection2(self):

        con = Connection()

        con.host = "127.0.0.1"
        con.port = "5434"
        con.user = "pgis"
        con.password = "postgres"
        con.database = "template1"

        return con



    def getStringToConnect(self, database):

        #return "dbname='prueba7' user='pgis' password='pgis'"

        con = "dbname='database' user='utente' host='maquina' port='puerto' password='password1'"

        db = self.readDatabaseParameters()


        con = con.replace("maquina", db["host"])
        con = con.replace("puerto", db["port"])
        con = con.replace("utente", db["user"])
        con = con.replace("password1", db["password"])
        con = con.replace("database", database)

        print con

        return con

    def getAAAStringToConnect2(self):

        #return "dbname='prueba7' user='pgis' password='pgis'"
        return "dbname='roads' user='pgis' host='127.0.0.1' port='5434' password='pgis'"

    def getPortasnumber(self):
        return 5434

    #http://www.postgresqltutorial.com/postgresql-python/connect/



    def readDatabaseParameters(self):
        # create a parser
        from ConfigParser import ConfigParser
        parser = ConfigParser()
        # read config file
        import Directory

        pathsql = Directory.getPathSqlDir()
        # sys.path.insert(0, "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database\\")

        pathsql = pathsql.replace("Database/SQL", "config" )
        filename = pathsql + "database.ini"

        section ='postgresql'

        #print "\n filename "

        #print filename
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        print db

        print db['host']

        return db

    def writeconfig(self):
        databasename = "popoli"
        filename = self.filename
        cfgfile = open(filename, 'w')

        '''

        import ConfigParser
        Config = ConfigParser.ConfigParser()

        
        '''

        from ConfigParser import ConfigParser
        parser = ConfigParser()
        # read config file


        #filename2 = 'D:\\repositorydef\SeismicRisk\Database\database2.ini'

        filename2 = self.filename
        parser.read(filename)

        # add the settings to the structu0re of the file, and lets write it out...


        filename = 'database3b.ini'
        #section = 'postgresql'

        section = 'postgresql'
        '''
        db_settings =self.config(filename, section)

        Config.add_section('postgresql')

        for param in db_settings:
            #db_settings[param[0]] = param[1]
            Config.set(section, param[0], param[1])
        '''

        #parser.set(section, 'name', databasename)

        '''

        filename = 'database3b.ini'
        section = 'postgresql'
        con.config(filename, section)

        Config.set('Person', 'Age', 50)
        '''
        parser.write(filename2)
        cfgfile.close()

    def __readDir(self):
        # create a parser
        from ConfigParser import ConfigParser
        parser = ConfigParser()
        # read config file
        #filename = "D:\\repositorydef\SeismicRisk\config\config.ini"
        fileconfig = self.fileconfig


        section = 'database'

        #print "\n filename "

        #print fileconfig
        parser.read(fileconfig)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        print db

        print db['path_database']

        return db

    def getPathDatabase(self):
        db = self.__readDir()

        path_database = db['path_database']

        return path_database




