import sys
sys.path.append('../../')

import inspect
print inspect.stack()[0][1]
path = inspect.getfile(inspect.currentframe())

path=path.replace("Logic2\FragilityCurve\FragilityCurve.py", "Utils\\")
print " path " + path
sys.path.append(path)

#sys.path.append("C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database")
print sys.path

import logging

import Directory
path_denug = Directory.getPathTempDir() + "seismicrisk.log"


logging.basicConfig(filename=path_denug,level=logging.INFO)
logging.debug('This message should go to the log file')


import Writes as w
from Connection import Connection
import psycopg2
from ..Utils import  Directory


def imprime():
    print "OK; from subfolder"

    from Database import MyDatabase
    MyDatabase.imprime()


def insertFragilityCurves(databasename, id):
    import os, subprocess

    from Connection import Connection




    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    sql = "insert into fragility_curve (idfragility, name) values('" + str(id)+"','curva')"

    print " sql fragility insert " + sql

    temp_dir = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"
    file = temp_dir + "sql.txt"

    w.writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file

    print cmd
    subprocess.call(cmd, shell=True)


def updateFragilityCurves(databasename, idfragility, idlevel, param1, param2):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    print "Id fragility is " + str(idfragility)

    if (idfragility > 0):
        vulnerabilty = calculateValue(param1, param2)

        frsagility = "1"

        # sql ="update fragility set level1='" + str(vulnerabilidad)+"'

        '''
        sql = "insert into fragility_curve (name) values('curva')"

        print " sql fragility insert " + sql

        file = "C:/Data/Python/sql.txt"

        writefile(file, sql)

        cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
        subprocess.call(cmd, shell=True)

        '''

        # vulnerabilty = 0.5

        # sql = "update fragility_curves set param1='" + str(param1) + "', param2='" + str(param2) + "' where idfragility='" + str(idfragility) + "'"

        '''

        sql = "delete from fragility_curve_level where idfragility='" + str(
            idfragility) + "' and level='" + str(idlevel) + "'"

        sql = "delete from fragility_curve_level where idfragility=currval('fragility_curve_seq') and level='" + str(idlevel) + "'"

        print " sql fragility delete " + sql

        file = "C:/Data/Python/sql.txt"

        writefile(file, sql)


        cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
        subprocess.call(cmd, shell=True)
        '''

        sql = "insert into fragility_curve_level (idfragility, level, param1, param2) values ('" + str(
            idfragility) + "','" + str(idlevel) + "','" + str(param1) + "','" + str(param2) + "')"

        sql2 = "update fragility_curve_level set param1='" + str(param1) + "', param2='" + str(param2) + "'"
        sql2 += " where idfragility =  '" + str(idfragility) + "' and level ='" + str(idlevel) + "'"

        print " sql fragility insert " + sql


        print " sql fragility insert sql2 " + sql2

        temp_dir = Directory.getPathTempDir()

        #file = "C:/Data/Python/sql.txt"
        file = temp_dir + "sql.txt"

        w.writefile(file, sql)

        cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
        print cmd
        subprocess.call(cmd, shell=True)

        w.writefile(file, sql2)

        cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
        print cmd
        subprocess.call(cmd, shell=True)

        ''' if it is not posible to update because the curve does not exit
            then insert

        '''

        #file = "C:/Data/Python/sql.txt"
        file = temp_dir + "sql.txt"

        w.writefile(file, sql2)

        cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
        print cmd
        subprocess.call(cmd, shell=True)

def calculateValue(parameter1, parameter2):
        num1 = float(parameter1)
        num2 = float(parameter2)

        return num1
        print " calculate vulnerability values "


def getNewIdFragility(databasename):
    '''
    return the files excel with the loaded fragilitycurves
    '''
    # sql ="update fragility set level1='" + str(vulnerabilidad)+"'"

    import os, subprocess



    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # sql = "select param1, param2 from fragility_curve_level where idfragility='" + str(idfragility) + "' and level='" + str(level) + "'"

    sql = "select nextval('fragility_curve_seq');"

    print sql

    '''

    print "sql \n"
    print sql

    file = "C:/Data/Python/file_sql.txt"


    file2 = "C:/Data/Python/sql_output.txt"


    writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > " +  file2
    print cmd
    subprocess.call(cmd, shell=True)

    init of reading the quary by hard drive fils

    finish of doing the consult by files
    '''

    # read parameters again not by formulas but using database


    #conn = psycopg2.connect(con2.getStringToConnect(databasename), con2.user, con2.password)

    conn = psycopg2.connect(con2.getStringToConnect(databasename))

    # creating a Cursor
    cur = conn.cursor()

    # testing library versions
    # atritt = readNamesAttributesData()

    # print atritt

    table = "popoliforpostgres"
    clave = "gid"

    # sql = 'SELECT geom from popoliforpostgres where gid=' + str(id) + ''
    sql = sql.replace('\n', ' ')

    print sql

    rs = cur.execute(sql)

    existe = False

    rows = cur.fetchall()

    result = ""

    for row in rows:
        existe = True
        # msg = str(row[0])  + " ," + str(row[1]) + " ," + str(row[2]) + " ," + str(row[3]) + " ," + str(row[4]) + " ," + str(row[5]) + " ," + str(row[6]) + " ," + str(row[7]) + " ," + str(row[8]) + " ," + str(row[9]) + " ," + str(row[10])
        result = str(row[0])

    conn.commit()

    # rs.close()
    conn.close()

    return result


def deleteFragilitiesCurves(databasename, idfragility):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    sql = "delete from fragility_curve_structure where idfragility='" + str(idfragility) + "';\n"
    sql += "delete from fragility_curve_level where idfragility='" + str(idfragility) + "';\n"

    sql += "delete from fragility_curve where idfragility='" + str(idfragility) + "';\n"


    temp_dir = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql_temporal.txt"
    file = temp_dir + "sql_temporal.txt"

    w.writefile(file, sql)

    sql_temp = Directory.getPathTempDir()
    file_err = sql_temp + "errores.txt"

    #cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > C:/Data/Python/errores.txt"
    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file + " > " + file_err

    print cmd
    subprocess.call(cmd, shell=True)



def poputateFragilitiesCurvesToBuildings(databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = ""

    from Logic import Common

    number_of_structures = Common.calculatenumberofstructures(databasename)

    for x in range(0, number_of_structures):
        # Y =  divmov(x, 3)
        y = x % 2
        #sqlinsert = "insert into fragility_curve_structure values('" + str(x) + "', '" + str(y + 1) + "');\n"
        sqlinsert = "insert into fragility_curve_structure values('" + str(x) + "', '0');\n"
        #
        #print sql
        sql += sqlinsert

    print " sql assing fragility " + sql

    temp_dir = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql.txt"
    file = temp_dir + "sql_temporal.txt"

    w.writefile(file, sql)

    sql_temp = Directory.getPathTempDir()
    file_err = sql_temp + "errores.txt"

    #cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > C:/Data/Python/errores.txt"
    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file + " > " + file_err

    print cmd
    subprocess.call(cmd, shell=True)

def readFragilityCurves(databasename):
    from Connection import Connection
    con2 = Connection()

    con = con2.getConnection()

    # creating/connecting the test_db
    # conn = db.connect('test_db.sqlite')

    msg = ""

    # for the case it not exist the  iid



    print "Inside code code ... with id " + str(id)

    existe = False

    try:

        sql = 'SELECT idfragility, name from fragility_curve order by idfragility '
        sql = sql.replace('\n', ' ')

        print sql

        #conn = psycopg2.connect(con2.getStringToConnect(databasename), con2.user, con2.password)

        conn = psycopg2.connect(con2.getStringToConnect(databasename))

        #C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Logic\FragilityCurve\FragilityCurve.py

        #conn = psycopg2.connect(dbname="test", user="postgres", password="secret")

        # creating a Cursor
        cur = conn.cursor()

        # testing library versions
        # atritt = readNamesAttributesData()



        cur.execute(sql)

        for record in cur:
            # print "  " +record
            existe = True
            msg1 = str(record[0]) + " ," + str(record[1]) + " "


            msg = msg1 + ";" + msg

        '''try:
            existe = False
            for row in rs:

                existe = True
                msg1 = str(row[0])  + " ," + str(row[1]) + " "
                msg = msg1 + ";" + msg
                print msg

        except:
            msg= "Except "
        '''

        conn.commit()

        #rs.close()
        conn.close()

    except Exception as e:
        print str(e)

    if existe:
        print "existe el item"
    else:
        # msg ="0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"
        msg = "FragilityCurve 368 Not loaded any fragility curve"

    return msg



def createFragilityTable(databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()





    sql_dir = Directory.getPathSqlDir()

    #file = "C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database\SQL\create_fragility.txt"
    file = sql_dir + "create_fragility.txt"

    sql_temp = Directory.getPathTempDir()
    file_err = sql_temp + "errores.txt"

    #cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > C:/Data/Python/errores.txt"

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file + " > " + file_err

    print " Fragility Curves 435 "

    print cmd

    logging.debug(cmd)
    subprocess.call(cmd, shell=True)



def exportFragilitiesAssignationToExcel(filename,  databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    #sql = "Copy (Select * From valutazione order by idstructure, idparam) To  '" + filename+ "' With CSV DELIMITER ','  HEADER;"
    sql = "Copy (Select * From fragility_curve_structure order by type_structure, idfragility) To  '" + filename + "' With CSV DELIMITER ',';"

    print sql

    temp_dir = Directory.getPathSqlDir()


    file = temp_dir + "sql_temporal.txt"


    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)

    from Utils import XLSConverterDefinitivo

    XLSConverterDefinitivo.convertToXLS(filename)






def importFragilitiesAssignationFromText(filename, databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "Copy   fragility_curve_structure from '" + filename+ "' delimiter ','"
    print sql

    temp_dir = Directory.getPathTempDir()



    file = temp_dir + "sql_temporal.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)



def importFragilitiesAssignationFromInput():

    '''
    read these values from the community of study
    
    :param filename: 
    :param databasename: 
    :return: 
    
    the databasename is taken from the class Connection
    '''
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "drop  table if exists fragility_curve_structure  "
    print sql

    temp_dir = Directory.getPathTempDir()



    file = temp_dir + "sql_temporal.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file


    #subprocess.call(cmd, shell=True)

    sql0 = "drop  table if exists fragility_curve_structure;  "

    sql = "create table fragility_curve_structure as  "
    sql += "select gid, idfragility from communitytostudy ; "

    sql2 = "alter  table fragility_curve_structure add primary key (gid, idfragility); "

    print sql



    temp_dir = Directory.getPathTempDir()



    file = temp_dir + "sql_temporal4.txt"

    all_sql = sql0 + sql + sql2

    w.writefile(file, all_sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file

    print cmd


    subprocess.call(cmd, shell=True)



    temp_dir = Directory.getPathTempDir()



    file = temp_dir + "sql_temporal.txt"

    #w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
    print cmd
    #subprocess.call(cmd, shell=True)


    sql = "alter  table add primary key fragility_curve_structure_pkey  "
    sql += " fragility_curve_structure(gid, id_fragility) "
    print sql

    temp_dir = Directory.getPathTempDir()



    file = temp_dir + "sql_temporal.txt"

    #w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
    print cmd
    #subprocess.call(cmd, shell=True)


def deleteFragilitiesAssignation(databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "delete from fragility_curve_structure "

    temp_dir = Directory.getPathTempDir()

    #file = "C:/Data/Python/sql_temporal.txt"
    file = temp_dir + "sql_temporal.txt"

    w.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)


