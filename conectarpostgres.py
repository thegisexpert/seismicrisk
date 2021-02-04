#http://pyqgis.org/blog/2013/04/11/creating-a-postgresql-connection-from-a-qgis-layer-datasource/

'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from qgis.core import *
'''
import connectdb
import random

import sys
#sys.path.insert(0, "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database\\")
from Database.Connection import Connection
con2 = Connection()




import logging


from Database import Directory
logdir = Directory.getPathTempDir()
filelog = logdir + "seismicrisk.log"
logging.basicConfig(filename=filelog,level=logging.DEBUG)
logging.debug('This message should go to the log file')

'''
def run_script(iface):
    # get the active layer
    #layer = iface.activeLayer()

        inicio com   
        init postgres
        http://gis.stackexchange.com/questions/86983/how-to-properly-establish-a-postgresql-connection-using-qgscredentials
        
        fin com

    uri = QgsDataSourceURI()
    # assign this information before you query the QgsCredentials data store

    con = con2.getConnection()
    uri.setConnection(con.host, con.port(), con.database, con.user, con.password)
    connInfo = uri.connectionInfo()

    #(success, user, passwd) = QgsCredentials.instance().get(connInfo, "postgres", "postgres")

    success = True
    if success:
        uri.setPassword(con.password)
        uri.setUsername(con.user)
        uri.setDataSource("public", "popoliforpostgres", "geom")
        layer = QgsVectorLayer(uri.uri(), "LYR", "postgres")



    # get the underlying data provider
    provider = layer.dataProvider()
    if provider.name() == 'postgres':
        # get the URI containing the connection parameters
        uri = QgsDataSourceURI(provider.dataSourceUri())
        print uri.uri()
        # create a PostgreSQL connection using QSqlDatabase
        db = QSqlDatabase.addDatabase('QPSQL')
        # check to see if it is valid
        if db.isValid():
            print "QPSQL db is valid"
            # set the parameters needed for the connection
            

            con = con2.getConnection()

            db.setHostName(con.host)
            db.setDatabaseName(con.dattabase)
            db.setPort(con.port)
            db.setUserName(con.user)
            db.setPassword(con.passsword())

            if db.open():
                print "Opened %s" % uri.uri()
                # execute a simple query
                query = db.exec_("""select * from valutazione""")
                # loop through the result set and print the name
                while query.next():
                    print " while "
                    record = query.record()
                    print str(record.field('idstructure').value())
            else:
                err = db.lastError()
                print err.driverText()


            for idstructura in range(1,45):

                #otrosql = "update popoliforpostgres set vulnerab = (select  sum(paramvalue*(vkimportance-vkprotection))*(1/6)*(1/(select sum(paramvalue) from valutazione where idstructure= " + str(idstructura) + "))+ 0.5 from valutazione where idstructure= " + str(idstructura) +" ) where ogc_fid= " + str(idstructura) + ""

                sql = "update popoliforpostgres set vulnerab = "
                sql = sql + "(select   (sum(paramvalue*(vkimportance-vkprotection))/sum(paramvalue))/6 + 0.5 "
                sql = sql + "from valutazione where idstructure='" + str(idstructura)+"'"
                sql = sql + ") "
                sql = sql + "where gid='" + str(idstructura)+"'"

                print(sql + ";")




                try:
                  db.exec_(sql)



                except:
                  print "Error "


            sql = "update popoliforpostgres set damage = 0.53 + 1.15*vulnerab -4*vulnerab*vulnerab + 4.21*vulnerab*vulnerab*vulnerab"

            print sql
            db.exec_(sql)





        else:
            err = db.lastError()
            print err.driverText()

        print "Ok"




'''


def initvalues():


    sqllist = ["update popoliforpostgres set  vulfactor='0', vulindex='0', damage='0'"]

    executeSQL(sqllist)



def populateparametersv2():

    conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')






    # creating a Cursorupdate

    table = "popolispatial"

    filename = "C:/Data/Python/archivoupdate.txt"

    cur = conn.cursor()



    for idstructura in range(1,50):

        for param in range(1,14):

            x= random.sample([0,1,2], 1)
            z= random.sample([0,1], 1)
            f = random.sample([0,1], 1)  ## dont know the ranges of values
            w1= random.sample([1,2], 1)
            w2= random.sample([1,2], 1)
            n = random.sample([0,1], 1)  ## dont know the ranges of values


            idstructura = str(idstructura)
            param= str(param)

            x= x[0]
            z=  z[0]
            f = f[0]
            w1=  w1[0]
            w2=  w2[0]
            n =  n[0]

            #vki = Z* W * F
            vki = w1*z*f

            #vkp = wz*m
            vkp = w2*z*n


            x= str(x)
            z=  str(z)
            f = str(f)
            w1=  str(w1)
            w2=  str(w2)
            n =  str(n)

            #vki = Z* W * F
            vki = str(vki)

            #vkp = wz*m
            vkp = str(vkp)



            try:

                sql = " insert into valutazione values (" + idstructura + "," + param + "," + x + ", " + z + ", " + f + "," + w1 + "," + w2 + ", " + n + "," + vki + "," + vkp +", 0)"

                print sql + ";"
                cur.execute(sql)




            except:
                jueego = 1
                #print " sentencia  otrosql erronea "


    sql = "update valutazione set  paramvalue='1.5' where (idparam=1 or idparam=2 or idparam=3 or idparam=13 )"
    print sql

    cur.execute(sql)


    sql = "update valutazione set  paramvalue='1' where (idparam=4 or idparam=5 or idparam=6 or idparam=7 )"
    print sql


    cur.execute(sql)


    sql = "update valutazione set  paramvalue='0.5' where idparam=9"
    print sql

    cur.execute(sql)

    sql = "update valutazione set  paramvalue='1' where idparam=10"
    print sql + ";"

    cur.execute(sql)

    sql = "update valutazione set  paramvalue='0.8' where (idparam=11 or idparam=8)"
    print sql + ";"

    cur.execute(sql)

    sql = "update valutazione set  paramvalue='0.5' where idparam=12"
    print sql + ";"

    cur.execute(sql)

    sql = "update valutazione set  paramvalue='1.5' where idparam=13"
    print sql + ";"

    cur.execute(sql)

    sql = "update valutazione set  paramvalue='0.3' where idparam=14"
    print sql + ";"

    cur.execute(sql)
    #cur.execute(otrosql)





    cur.execute("SELECT UpdateLayerStatistics(\'popolispatial\')")
    conn.commit()

    #rs.close()
    conn.close()




def calculatedamage(earthquakeintesity, databasename):

    try:
        logging.debug(" calculating damage in database: " + databasename)

        print  "   earthquake intensity " + earthquakeintesity


        import  psycopg2
        import numpy

        strcon = con2.getStringToConnect(databasename)
        logging.debug(" string de connection")


        print "strcon"
        print strcon
        logging.debug(strcon)

        conn=psycopg2.connect(strcon)

        cur = conn.cursor()
        try:
            cur.execute("SELECT gid, (" + earthquakeintesity+"* 6.25*vulfactor - 13.1)/2.3  from popoliforpostgres")
            #cur.execute("""SELECT gid, (7* vulfactor - 13.1)/2.3  from popoliforpostgres""")

        except:
            print "I can't SELECT from popoli for postgres"


        sqllist = []

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:

            try:

                print "Row 1 " + str(row[1])   + ", " + str(row[0])

                if str(row[1])=='None':
                   valor = 2.5*(1+ numpy.tanh(0))
                else:
                   valor = 2.5*(1 + numpy.tanh(float(str(row[1]))))
            except:
                valor = 2.5*(1+ numpy.tanh(0))

                import sys

                print "Calculating damage ", sys.exc_info()[0]

                print  sys.exc_info()[1]

            sql = "update damage set damage = '" + str(valor) + "' where gid= '" + str(row[0]) + "'"

            sql2 = "update popoliforpostgres set damage = '" + str(valor) + "' where gid= '" + str(row[0]) + "'"


            #otrosql = "update damage set damage = '" + str(valor) + "' where gid= '" + str(row[0]) + "'"

            sqllist.append(sql)

            sqllist.append(sql2)



        logging.debug("SQL list damage ")

        for x in sqllist:
            logging.debug(x)

        executeSQL(sqllist)
    except :
        import sys
        print "I am unable to connect to the database.", sys.exc_info()[0]
        raise





def populatedistancesfromEpicenter():

    sqllist =[]
    otrosql =  "update distance_from_epicenter set geom = (select ST_MakeLine((select geom from hazard where hazard.gid=distance_from_epicenter.gid), (select geom from epicenter where gid='0')))"


    sqllist.add(otrosql)





def addAttributesData():

    sqllist = []

    table = "popoliforpostgres";

    filename = "C:/Data/Python/metodologia.txt"


    if (filename != ""):
            infile = open(filename,"r")
            lines = infile.readlines()
            infile.close()

            for i in range(0, len(lines)):
                tokens = lines[i];

                sql = "ALTER TABLE " + table + " ADD COLUMN " + tokens + " real"
                sql = sql.replace("\n", "")
                sqllist.append(sql)

            connectdb.executeSQL(sqllist)


def executeSQL(sqllist):


    import os, subprocess

    from Database.Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # Choose your PostgreSQL version here

    # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
    # D:\usbgis\apps\postgresql93\bin

    os.environ['PATH'] += r';C:/usbgis/apps/postgresql93/bin'

    # http://www.postgresql.org/docs/current/static/libpq-envars.html
    os.environ['PGHOST'] = 'localhost'

    os.environ['PGPORT'] = '5432'
    os.environ['PGUSER'] = 'potgres'
    os.environ['PGPASSWORD'] = 'postgres'
    os.environ['PGDATABASE'] = 'roads'

    import Writes

    s = ""

    for x in sqllist:
        s = s + x + ";\n"

    logging.debug(" \n\n\n")
    logging.debug(" SSSSSSSSSSS")
    logging.debug(s)
    logging.debug(" \n\n\n")

    from Utils import Directory

    dir = Directory.getPathTempDir()

    file = dir + "sqltemporal2.txt"

    file_temp = dir + "errores.txt"

    Writes.writefile(file, s)


    logging.debug(" Coondection " + con.database)

    cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + file + " >  " + file_temp + ""
    print cmd

    subprocess.call(cmd, shell=True)


#run_script(iface)

