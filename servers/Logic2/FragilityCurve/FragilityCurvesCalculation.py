'''

This class uses the fragility curves stored in the databases in order to calculate
the fragility value to be shown in the map

'''
'''
updateVulnerabilityByCurves
'''

'''
OJO DIFERENCUA POR ID
Y DEBE DIFERENCIA POR LA CURVA ASIGNADA A CADA EDIDICIO
'''

import psycopg2
import Writes as w

import sys

import inspect
print inspect.stack()[0][1]
path = inspect.getfile(inspect.currentframe())

path=path.replace("Logic2\FragilityCurve\FragilityCurve.py", "Utils\\")
print " path " + path
sys.path.append(path)

#sys.path.append("C:\Users\AG\.qgis2\python\plugins\SeismicRisk\Database")


def createViewFragilityCurveStructures(idlevel):
    # plugin_dir = "C:\Users\AG\.qgis2\python\plugins\SeismicRisk"

    from Connection import Connection
    import os, subprocess

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    from ..Utils import Directory

    # sql_dir = plugin_dir + "\\Database\\SQL\\"

    sql_dir = Directory.getPathSqlDir()

    file = sql_dir + str("create_or_update_view_fragility_curves.txt")

    sql = "DROP TABLE view_fragility_curve_structure;"

    sql += "create table view_fragility_curve_structure as "
    sql += "select fragility_values.gid, fragility_values.name, fragility_values.geom, idfunction, fragility_curve_structure.idfragility, level, param1, param2, value, hazard "
    sql += "from fragility_values, fragility_curve_structure, fragility_curve_level, hazard "
    sql += "where  hazard.gid =fragility_values.gid and fragility_values.gid=fragility_curve_structure.gid and fragility_curve_level.level='" + str(idlevel) +"' and  "
    sql += "fragility_curve_structure.idfragility=fragility_curve_level.idfragility; "


    print "\n"
    print sql

    print "\n"

    temp_file = Directory.getPathTempDir() + "sql.txt"
    w.writefile(temp_file, sql)

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + temp_file
    print cmd
    subprocess.call(cmd, shell=True)


#FragilityCurvesCalculation.updateVulnerabilityValues(pga, databasename, idfragility, level, idstructure, working_dir)




def updateVulnerabilityValuesLot(databasename):
    import Writes as w


    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()



    #file = "C:/Data/Python/update_vulnerability_values.txt"

    from ..Utils import Directory

    # sql_dir = plugin_dir + "\\Database\\SQL\\"



    sql = "update view_fragility_curve_structure set value=get_pga_value(hazard, param1, param2)"

    temp_dir = Directory.getPathTempDir()

    file =  temp_dir+ str("sql.txt")
    w.writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file

    print "\n"
    print "temp_dir is "
    print temp_dir
    print cmd
    subprocess.call(cmd, shell=True)


def updateVulnerabilityValues(pga, databasename, idfragility, idlevel, gid, working_dir):
    import Writes as w

    print " I must show idfragility   " + str(idfragility) + " and id level " + str(
                idlevel) + " and pga is " + str(pga)
    print " working dir is " + working_dir
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    if (idfragility > 0):
        # parameters_value = readParameters(idfragility, idlevel, databasename)
        parameters_value = readParametersTutto(gid, idlevel, databasename)

        param0 = 0
        param1 = 0

        try:

            print " readed patameter 1 " + parameters_value[0]
            print " readed patameter 2 " + parameters_value[1]
            print " id fragility line 957 " + str(idfragility)

            param0 = parameters_value[0]
            param1 = parameters_value[1]

        except:
            param0 = 0
            param1 = 0



        vulnerabilty = calculateValue(pga, param0, param1)


        # sql ="update fragility set level1='" + str(vulnerabilidad)+"'"




        sql = "update fragility_values set value=  " + str(vulnerabilty) + ""
        sql += " where gid=" + str(gid) + ""  # ojo attenzione ogni structura haa un tipo


        # file = "C:/Data/Python/update_vulnerability_values.txt"

        file = working_dir + str("/update_vulnerability_values.txt")

        w.writefile(file, sql)

        cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
        # print cmd
        subprocess.call(cmd, shell=True)


def readParametersTutto(gid, level, databasename):

    #return the files excel with the loaded fragilitycurves

    # sql ="update fragility set level1='" + str(vulnerabilidad)+"'"

    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # sql = "select param1, param2 from fragility_curve_level where idfragility='" + str(idfragility) + "' and level='" + str(level) + "'"

    sql = "select param1, param2 from fragility_curve_level, fragility_curve_structure  "
    sql += " where fragility_curve_structure.idfragility=fragility_curve_level.idfragility and level='" + str(
        level) + "' and fragility_curve_structure.gid='" + str(gid) + "'"

    print " sql read parameteres  claaa FragilityCurveCalculation 134 "
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
        result = [str(row[0]), str(row[1])]

    conn.commit()

    # rs.close()
    conn.close()

    return result


def readMinMaxFragilitiesValue( databasename):
    '''
    return the files excel with the loaded fragilitycurves
    '''
    # sql ="update fragility set level1='" + str(vulnerabilidad)+"'"

    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # sql = "select param1, param2 from fragility_curve_level where idfragility='" + str(idfragility) + "' and level='" + str(level) + "'"

    sql = "select min(value), max(value) from fragility_values  "
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
        result = [str(row[0]), str(row[1])]

    conn.commit()

    # rs.close()
    conn.close()

    return result



def getHazardValue (databasename, gid):
    '''
    return the files excel with the loaded fragilitycurves
    '''
    # sql ="update fragility set level1='" + str(vulnerabilidad)+"'"

    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # sql = "select param1, param2 from fragility_curve_level where idfragility='" + str(idfragility) + "' and level='" + str(level) + "'"

    sql = "select hazard from hazard where gid=  '" + str(gid) + "'"
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

'''
def readParametersByIdFragility(idfragility, level, databasename):

    #return the files excel with the loaded fragilitycurves
    
    # sql ="update fragility set level1='" + str(vulnerabilidad)+"'"

    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # sql = "select param1, param2 from fragility_curve_level where idfragility='" + str(idfragility) + "' and level='" + str(level) + "'"

    sql = "select param1, param2 from fragility_curve_level, fragility_curve_structure  "
    sql += " where fragility_curve_structure.idfragility=fragility_curve_level.idfragility and level='" + str(
        level) + "' and fragility_curve_structure.idfragility='" + str(idfragility) + "'"

    print " sql read parameteres Logica 1118 "
    print sql


    # read parameters again not by formulas but using database


    conn = psycopg2.connect(con2.getStringToConnect(darabasename), con2.user, con2.password)

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
        result = [str(row[0]), str(row[1])]

    conn.commit()

    # rs.close()
    conn.close()

    return result
    
    '''


def calculateValue(pga, mu0, sigma0):
    # http://www.statisticshowto.com/lognormal-distribution/
    import math
    import numpy as np

    '''
    sigma = 0.5
    mu = 0.1
    x = 0.8
    '''

    try:

        sigma = float(sigma0)
        mu = float(mu0)
        x = float(pga)

        y = - (math.log(x) - mu) * (math.log(x) - mu) / (2 * sigma * sigma)
        N = 1 / sigma * math.sqrt(2 * math.pi) * np.exp(y)
    except:
        N=-1

    return N

'''
def calculateValue(parameter1, parameter2 ):

    print " calculation pf the value  in the class FragilityCurvesCalculation "

    num1 = float(parameter1)
    num2 = float(parameter2)

    return num1
    print " calculate vulnerability values "
'''