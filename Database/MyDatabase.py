from Connection import Connection
import sys


def imprime():
    print "OK; from subfolder database"


def executeQuery(databasename, sql, outfile):


    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # Choose your PostgreSQL version here
    #os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
    #D:\usbgis\apps\postgresql93\bin

    #os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'
    #os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

    #os.environ['PATH'] += r';C:\usbgis\apps\postgresql93\bin'

    dir_psth = con.getPathDatabase()

    import sys
    #sys.path
    sys.path.append(dir_psth)



    # http://www.postgresql.org/docs/current/static/libpq-envars.html
    os.environ['PGHOST'] = 'localhost'
    os.environ['PGPORT'] = '5432'
    os.environ['PGUSER'] = 'potgres'
    os.environ['PGPASSWORD'] = 'postgres'
    os.environ['PGDATABASE'] = 'prueba4'


    file = "C:/Data/Python/sql_temporal.txt"

    import Erites as w

    w.writefile(file, sql)


    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > 'outfile'"
    cmd = cmd.replace('outfile', outfile)
    subprocess.call(cmd, shell=True)







def getListofDatabases():






    def executeQueryHere(databasename, sql, outfile):
        import os, subprocess

        from Connection import Connection



        con2 = Connection()

        con = con2.getConnection()

        maquina = " -h " + con.host + " -p " + con.port

        # Choose your PostgreSQL version here
        # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
        # D:\usbgis\apps\postgresql93\bin

        # os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'
        # os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

        #os.environ['PATH'] += r';C:\usbgis\apps\postgresql93\bin'

        dir_psth = con.getPathDatabase()

        import sys
        # sys.path
        sys.path.append(dir_psth)

        # http://www.postgresql.org/docs/current/static/libpq-envars.html
        os.environ['PGHOST'] = 'localhost'
        os.environ['PGPORT'] = '5432'
        os.environ['PGUSER'] = 'potgres'
        os.environ['PGPASSWORD'] = 'postgres'
        os.environ['PGDATABASE'] = 'prueba4'

        file = 'C:/Data/Python/sql_temporal.txt'

        import Writes as w

        w.writefile(file, sql)

        cmd = "psql -U " + con.user + maquina + " " + databasename + " <  \"file\"  > \"out\" "
        cmd = cmd.replace('out', outfile)
        cmd = cmd.replace('file', file)

        print cmd


        subprocess.call(cmd, shell=True)


    def readDatabases(databasename, sql):

        import psycopg2

        # creating/connecting the test_db
        # conn = db.connect('test_db.sqlite')

        from Connection import Connection
        con3 = Connection()
        con2 = con3.getConnection()

        msg = ""

        # for the case it not exist the  iid

        existe = False

        try:

            # update type of buildings
            #sql = 'SELECT gid, name from fragility_values order by gid '
            sql = sql.replace('\n', ' ')

            print sql

            url = "dbname='postgres' user='pgis' host='127.0.0.1' port='5434' password='pgis'"

            url = con3.getStringToConnect(databasename)

            #url - con2.getStringToConnect("postgres")

            conn = psycopg2.connect(url)
            # creating a Cursor

            cur = conn.cursor()

            # testing library versions
            # atritt = readNamesAttributesData()


            cur.execute(sql)

            for record in cur:
                print "  inscide record "

                existe = True
                msg1 = record[0]

                print record[0]

                msg = msg1 + ";" + msg


            conn.commit()

            cur.close()
            conn.close()

        except :
            msg =""


            print 'My exception occurred, value:', sys.exc_info()[0]


        if existe:
            print "existe el item"
        else:
            msg = "0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"

        return msg


    import os, subprocess

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # sql = "\l"
    #sql = "SELECT datname from pg_database WHERE datname='prueba7'"
    sql = "SELECT datname from pg_database"


    databasename = "postgres"

    outfile = 'C:/Data/Python/lista.txt'

    print "Databases "
    return readDatabases(databasename, sql)


    # executeQueryHere( databasename, sql, outfile)




