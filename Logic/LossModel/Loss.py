import sys
sys.path.append('../../')

import logging

import Directory
logdir = Directory.getPathTempDir()
filelog = logdir + "seismicrisk.log"

logging.basicConfig(filename=filelog,level=logging.DEBUG)

#logging.basicConfig(filename='C:/logplugin/example.log',level=logging.DEBUG)

import inspect
print inspect.stack()[0][1]
path = inspect.getfile(inspect.currentframe())

path=path.replace("Logic2\LossModel\Loss.py", "Utils\\")
print " path " + path
sys.path.append(path)
print sys.path


#sys.path.append("C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database")

import Writes as w
from Connection import Connection
import os, subprocess
import psycopg2

from Utils import Directory


def imprime():
    print "OK; from subfolder"

    from Database import MyDatabase
    MyDatabase.imprime()


def createLosses(databasename):




    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    sql = "drop table if exists popoliloss;\n"

    #sql += "create table popoliloss as select gid, name, geom, unitcost, ST_area(geom::geography) as area from communitytostudy;\n"
    sql += "create table popoliloss as select gid, name, geom, unitcost, ST_area(geom) as area from communitytostudy;\n"

    sql += "alter table popoliloss add totalcost float;"

    sql += "alter table popoliloss add material text;"
    sql += "alter table popoliloss add costaux text;"
    sql += "alter table popoliloss add damage float;"






    print " sql losses " + sql

    dir_temp = Directory.getPathTempDir()

    # file = "C:/Data/Python/sql.txt"

    file = dir_temp + "sql.txt"
    w.writefile(file, sql)

    file_err = dir_temp + "errores.txt"

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > " + file_err

    print "Loss 72 \n"

    print cmd
    subprocess.call(cmd, shell=True)




def createMaterial(databasename):
    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "alter table popoliloss add material text;"

    sql = "alter table popoliloss add material text;"



    print " sql losses " + sql

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"

    file = dir_temp + "sql.txt"

    w.writefile(file, sql)

    file_err = dir_temp + "errores.txt"

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > " + file_err
    subprocess.call(cmd, shell=True)







def updateIndexDamageFromFragilitiesCurves(databasename):
    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()





    sql = "update popoliloss set damage = value from view_fragility_curve_structure where view_fragility_curve_structure.gid =popoliloss.gid"

    print " sql losses " + sql

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"

    file = dir_temp + "sql.txt"

    w.writefile(file, sql)

    file_err = dir_temp + "errores.txt"

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > " + file_err

    print "\n"
    print cmd

    subprocess.call(cmd, shell=True)

    sql = "update popoliloss set totalcost = area*unitcost*damage;"


    print " sql losses " + sql

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"

    file = dir_temp + "sql.txt"

    w.writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > " + file_err

    print "\n"
    print cmd

    subprocess.call(cmd, shell=True)





def updateIndexDamageFromSeismicPredictionModel(databasename):
    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()




    sql = "update popoliloss set damage = (select damage from popoliforpostgres where popoliforpostgres.gid =popoliloss.gid)"

    print " sql losses " + sql

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"

    file = dir_temp + "sql.txt"

    w.writefile(file, sql)

    file_err = dir_temp + "errores.txt"

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > " + file_err
    subprocess.call(cmd, shell=True)

    sql = "update popoliloss set totalcost = area*unitcost*damage"


    print " sql losses " + sql

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"

    file = dir_temp + "sql.txt"

    w.writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > " + file_err
    subprocess.call(cmd, shell=True)




def populateMaterialAndCost(databasename, filenameexcel):

    import random



    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"

    file = dir_temp + "sql.txt"

    #file = filenameexcel

    sql = ""

    numberofstructures = calculatenumberofstructures(databasename)

    for i in range(0, numberofstructures):

        cost = random.randrange(0, 100, 1)

        sql += "update popoliloss set material = 'material " + str(i)+ "',  unitcost= " + str (cost)+ " where gid= '" + str(i)+ "' ;\n"


    w.writefile(file, sql)


    sql += "update popoliloss set  totalcost= unitcost*area*damage ;\n"

    w.writefile(file, sql)

    file_err = dir_temp + "errores.txt"

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > " + file_err
    subprocess.call(cmd, shell=True)



def exportLossForReadingfromUi(databasename, filenameut):
    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()
    sql = "select gid, name, area,  unitcost, totalcost, damage from popoliloss order by gid;"

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"

    file = dir_temp + "sql.txt"

    #file = dir_temp + "sql.txt"

    w.writefile(file, sql)

    cmd = "psql -t -U " + con.user + maquina + " " + databasename + " < " + file + " > " + filenameut
    subprocess.call(cmd, shell=True)


def exportLossesToText(filenameout,  databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    #sql = "Copy (select gid, name, area, material, unitcost, totalcost, damage from popoliloss order by gid) To  '" + filenameout+ "' With CSV DELIMITER ','  HEADER;"
    sql = "Copy (Select gid, name,  ROUND(unitcost,2)  From popoliloss order by gid) To  '" + filenameout+ "' With CSV DELIMITER ',' ;"

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"

    file = dir_temp + "sql.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)





def importLossesFromText(filename, databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    #sql = "Copy   popoliloss from '" + filename+ "' delimiter |"
    sql = "Copy   popoliloss(gid, name, unitcost) from '" + filename + "' delimiter ','"

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql_temporal.txt"

    file = dir_temp + "sql_temporal.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)

    print " Loss imported from '" + filename+ "'"




def updateLoss(databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    sql = "update popoliloss set costaux='0' where costaux=''; \n"

    dir_temp = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql_temporal.txt"

    file = dir_temp + "sql_temporal.txt"
    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)

    '''

    sql += "update popoliloss set unitcost=  cast(costaux as double precision); \n"


    #file = "C:/Data/Python/sql_temporal.txt"
    file = dir_temp + "sql_temporal.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)
    '''

    sql2 = "update popoliloss set geom= popoliforpostgres.geom, area =  ST_area(popoliforpostgres.geom::geography) "
    sql2  += "from popoliforpostgres "
    sql2 +=  "where popoliforpostgres.gid=popoliloss.gid;\n"

    print sql2

    sql += sql2

    #file = "C:/Data/Python/sql_temporal.txt"
    file = dir_temp + "sql_temporal.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)

    sql = "update popoliloss set totalcost= unitcost*area*damage\n"
    #file = "C:/Data/Python/sql_temporal.txt"
    file = dir_temp + "sql_temporal.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)




def deleteLoss(databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "delete from popoliloss "
    #file = "C:/Data/Python/sql_temporal.txt"

    dir_temp = Directory.getPathTempDir()
    file = dir_temp + "sql_temporal.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)

def deleteValutazioneTHISCANNOTBEHERE(databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "delete from popoli "
    #file = "C:/Data/Python/sql_temporal.txt"
    file = dir_temp + "sql_temporal.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)


'''private'''



def calculatenumberofstructures( databasename):

    try:
        logging.debug(" calculating number of structures in database: " + databasename)


        import  psycopg2
        import numpy

        con2 = Connection()


        strcon = con2.getStringToConnect(databasename)
        logging.debug(" string de connection")


        print "strcon"
        print strcon
        logging.debug(strcon)

        conn=psycopg2.connect(strcon)

        cur = conn.cursor()
        try:
            cur.execute("SELECT count(gid) from popoliforpostgres")
            #cur.execute("""SELECT gid, (7* vulfactor - 13.1)/2.3  from popoliforpostgres""")

        except:
            print "I can't SELECT from popoli for postgres", sys.exc_info()[0]


        sqllist = []

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:

            try:

                print "Row 1 " + str(row[0])

                if str(row[0])=='None':
                   valor = 0
                else:
                   valor = row[0]
            except:
                valor = -1


    except :
        import sys
        print "I am unable to connect to the database.", sys.exc_info()[0]
        raise

    return valor





def calculatetotalcost( databasename):

    try:
        logging.debug(" calculating number of structures in database: " + databasename)


        import  psycopg2
        import numpy

        con2 = Connection()


        strcon = con2.getStringToConnect(databasename)
        logging.debug(" string de connection")


        print "strcon"
        print strcon
        logging.debug(strcon)

        conn=psycopg2.connect(strcon)

        cur = conn.cursor()
        try:
            cur.execute("SELECT sum(totalcost) from popoliloss")
            #cur.execute("""SELECT gid, (7* vulfactor - 13.1)/2.3  from popoliforpostgres""")

        except:
            print "I can't SELECT from popoli for postgres"


        sqllist = []

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:

            try:

                print "Row 1 " + str(row[0])

                if str(row[0])=='None':
                   valor = 0
                else:
                   valor = row[0]
            except:
                valor = -1


    except :
        import sys
        print "I am unable to connect to the database.", sys.exc_info()[0]
        raise

    return valor









