import logging
import random
import Writes

from Database import Directory

path_denug = Directory.getPathTempDir() + "seismicrisk.log"
logging.basicConfig(filename=path_denug, level=logging.INFO)

from Database.Connection import Connection

import conectarpostgres


def populateValutazione(databasename):
    numberofstructures = calculatenumberofstructures(databasename)
    logging.debug("numberofstructures")
    logging.debug(numberofstructures)
    # get the active layer
    # layer = iface.activeLayer()


    '''
        init postgres
        http://gis.stackexchange.com/questions/86983/how-to-properly-establish-a-postgresql-connection-using-qgscredentials
        '''

    sqllist = []

    for idstructura in range(0, numberofstructures):
        for param in range(1, 15):
            x = random.sample([0, 1], 1)
            # z= random.sample([0,1], 1)
            z = x
            # f = random.sample([0,1.5], 1)  ## dont know the ranges of values
            h1 = random.uniform(0, 1.5)
            h = round(h1, 2)
            f = [h]
            w1 = random.sample([1, 2], 1)
            # w2= random.sample([1,2], 1)

            h1 = random.uniform(0, 1.5)
            h = round(h1, 2)
            n = [h]

            idstructura = str(idstructura)
            param = str(param)

            x = x[0]

            z = z[0]
            w1 = w1[0]
            f = f[0]
            # w2=  w2[0]
            n = n[0]
            w2 = w1

            z = x
            # n = f

            # vki = Z* W * F
            vki_factor = w1 * z * f
            vki_float = round(vki_factor)

            # vkp = wz*m
            vkp_factor = w2 * z * n
            vkp_float = round(vkp_factor)

            x = str(x)
            z = str(z)

            f = str(f)
            w1 = str(w1)
            w2 = str(w2)

            n = str(n)

            # vki = Z* W * F
            vki = str(vki_float)

            # vkp = wz*m
            vkp = str(vkp_float)

            '''


idstructure integer NOT NULL,
idparam integer NOT NULL,
x integer,
z integer,
f integer,
w1 integer,
w2 integer,
n integer,
vkimportance integer,
vkprotection integer,
paramvalue real,
            '''

            sql = " insert into valutazione values (" + idstructura + "," + param + "," + x + ", " + z + ", " + f + "," + w1 + "," + w2 + ", " + n + "," + vki + "," + vkp + ", 0)"
            # sql = sql + ";"

            # print sql


            # cur.execute(otrosql)

            sqllist.append(sql)
    # cur.execute(otrosql)


    sql = "update valutazione set  paramvalue='1' where (idparam=4 or idparam=5 or idparam=6 or idparam=7 )"
    print sql

    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='0.5' where idparam=9"
    print sql

    # cur.execute(otrosql)
    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='1' where idparam=10"
    print sql

    # cur.executd(otrosql)

    sql = "update valutazione set  paramvalue='0.8' where (idparam=11 or idparam=8)"

    # cur.execute(otrosql)
    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='0.5' where idparam=12"
    print sql

    # cur.execute(otrosql)
    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='1.5' where idparam=13"
    print sql

    # cur.execute(otrosql)
    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='0.3' where idparam=14"
    print sql

    # cur.execute(otrosql)
    sqllist.append(sql)

    logging.debug(" PredictiveModel 137 ")
    for sql in sqllist:
        logging.debug(sql)

    conectarpostgres.executeSQL(sqllist)

    print " valutation populated"


def calculatenumberofstructures(databasename):
    try:
        # logging.debug(" calculating number of structures in database: " + databasename)

        import psycopg2
        import numpy

        con2 = Connection()

        con = con2.getConnection()

        strcon = con2.getStringToConnect(con.database)
        logging.debug(" string de connection")

        print "strcon"
        print strcon
        logging.debug(strcon)

        conn = psycopg2.connect(strcon)

        cur = conn.cursor()
        try:
            cur.execute("SELECT count(gid) from popoliforpostgres")
            # cur.execute("""SELECT gid, (7* vulfactor - 13.1)/2.3  from popoliforpostgres""")

        except:
            print "I can't SELECT from popoli for postgres"

        sqllist = []

        rows = cur.fetchall()
        print "\nRows: \n"
        for row in rows:

            try:

                print "Row 1 " + str(row[0])

                if str(row[0]) == 'None':
                    valor = 0
                else:
                    valor = row[0]
            except:
                valor = -1


    except:
        import sys
        print "I am unable to connect to the database.", sys.exc_info()[0]
        raise
        valor =0

    return valor



def updatevulnerabilityparamaters(namedatabase):
    '''update popoliforpostgres
    set vulindex = (select   (sum(paramvalue*(vkimportance-vkprotection))/sum(paramvalue))/6 + 0.5 from valutazione where idstructure=17)
    where gid=17

    '''
    sqllist = []

    sql = "update valutazione set  paramvalue='1' where (idparam=4 or idparam=5 or idparam=6 or idparam=7 )"
    print sql

    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='0.5' where idparam=9"
    print sql

    # cur.execute(otrosql)
    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='1' where idparam=10"
    print sql

    # cur.executd(otrosql)

    sql = "update valutazione set  paramvalue='0.8' where (idparam=11 or idparam=8)"

    # cur.execute(otrosql)
    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='0.5' where idparam=12"
    print sql

    # cur.execute(otrosql)
    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='1.5' where idparam=13"
    print sql

    # cur.execute(otrosql)
    sqllist.append(sql)

    sql = "update valutazione set  paramvalue='0.3' where idparam=14"
    print sql

    # cur.execute(otrosql)
    sqllist.append(sql)

    logging.debug(" PredictiveModel 137 ")
    for sql in sqllist:
        logging.debug(sql)

    conectarpostgres.executeSQL(sqllist)
# otrosql del vki

# select  (vkimportance-vkprotection)*(select param from misparam where idparam=8)*(1/6)*(1/14)+ 0.5 from valutazione;

def updatevulnerabilityindex(namedatabase):
    '''update popoliforpostgres
    set vulindex = (select   (sum(paramvalue*(vkimportance-vkprotection))/sum(paramvalue))/6 + 0.5 from valutazione where idstructure=17)
    where gid=17

    '''
    sqllist = []

    numberofstructures = calculatenumberofstructures(namedatabase)

    # vki = Z* W * F

    # vkp = wz*m

    sql = "update valutazione set vkimportance = w1*z*f, vkprotection=w2*z*n"

    sqllist.append(sql)

    for idstructura in range(1, numberofstructures):
        # otrosql = "update popolispatial set vulnerab = (select  sum(paramvalue*(vkimportance-vkprotection))*(1/6)*(1/(select sum(paramvalue) from valutazione where idstructure= " + str(idstructura) + "))+ 0.5 from valutazione where idstructure= " + str(idstructura) +" ) where ogc_fid= " + str(idstructura) + ""

        sql = "update popoliforpostgres set vulindex = "
        sql = sql + "(select   (sum(paramvalue*(vkimportance-vkprotection))/sum(paramvalue))/6 + 0.5 "
        sql = sql + "from valutazione where idstructure='" + str(idstructura) + "'"
        sql = sql + ") "
        sql = sql + "where gid='" + str(idstructura) + "'"

        print sql
        sqllist.append(sql)

    conectarpostgres.executeSQL(sqllist)


def updatevulnerabilityfactor(namedatabase):
    sqllist = []

    sql = "update popoliforpostgres set vulfactor = 0.53 + 1.15*vulindex -4*vulindex*vulindex + 4.21*vulindex*vulindex*vulindex"

    # print otrosql

    sqllist.append(sql)

    conectarpostgres.executeSQL(sqllist)


'''
def exportValutazioneToExcel(filename, databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # sql = "Copy (Select * From valutazione order by idstructure, idparam) To  '" + filename+ "' With CSV DELIMITER ','  HEADER;"
    sql = "Copy (Select * From valutazione order by idstructure, idparam) To  '" + filename + "' With CSV DELIMITER ',';"

    from Utils import Directory2

    dir = Directory2.getPathScripts()

    # file = "C:/Data/Python/sql_temporal.txt"
    file = dir + "sql_temporal.txt"

    Writes.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)

    from Utils import XLSConverterDefinitivo

    XLSConverterDefinitivo.convertToXLS(filename)

'''


def exportValutazioneToExcelv2(filename):
    sqllist = ["select * from valutazione order by idstructure, idparam"]

    writeSQLtoFile(sqllist, filename)


def importValutazioneFromExcelv2(filename, database):

    sqllist = readFromExcel(filename)

    #import connectdb

    import conectarpostgres

    conectarpostgres.executeSQL(sqllist)

    updatevulnerabilityparamaters(database)
    updatevulnerabilityindex(database)



    updatevulnerabilityfactor(database)




def writeSQLtoFile(sqllist, filename):
    ##conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')

    import psycopg2

    import xlwt


    wb = xlwt.Workbook()
    ws = wb.add_sheet('Valutations indicatores')

    rowNum = 0
    #colNum = 0

    ws.write(rowNum, 0, 'idstructure')
    ws.write(rowNum, 1, 'idparam')
    ws.write(rowNum, 2, 'x')
    ws.write(rowNum, 4, 'z')
    ws.write(rowNum, 5, 'f')
    ws.write(rowNum, 6, 'w1')
    ws.write(rowNum, 7, 'w2')
    ws.write(rowNum, 8, 'n')

    rowNum = 1




    con = Connection()

    con2 = con.getConnection()

    database = con2.database

    print " database is " + database

    conn = psycopg2.connect(con2.getStringToConnect(database))
    # creating a Cursor


    cur = conn.cursor()

    for sql in sqllist:
        # execute a simple query
        # query = db.exec_(str)
        # cur.execute(otrosql)


        cur.execute(sql)

        print " sql iside write "
        print sql

        try:
            rows = cur.fetchall()

            print('Total Row(s):', cur.rowcount)
            for row in rows:
                #print(row)

                ws.write(rowNum, 0, row[0])  # row, column, value
                ws.write(rowNum, 1, row[1])
                ws.write(rowNum, 2, row[2])
                ws.write(rowNum, 3, row[3])
                ws.write(rowNum, 4, row[4])
                ws.write(rowNum, 5, row[5])
                ws.write(rowNum, 6, row[6])
                ws.write(rowNum, 7, row[7])
                ws.write(rowNum, 8, row[8])

                rowNum = rowNum + 1
                #colNum = colNum + 1

        except:
            import sys
            print("Exception running PredictiveModel.writeSQLtoFile.", sys.exc_info())

    conn.commit()

    # rs.close()
    conn.close()

    wb.save(filename)

    #wb.save('C:/Data/example.xls')




def readFromExcel(filename):
    ##conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')

    sqllist = []

    import psycopg2

    import xlrd

    #filename = "python_excel_test.xls"
    #excel_file = xlwt.Workbook()

    wb = xlrd.open_workbook(filename)

    table = wb.sheet_by_index(0)  # Gets the index order

    nrows = table.nrows

    print " nrows " + str(nrows)

    rowNum = 1

    for rowNum in range(1,nrows):

        print " rowNum " + str(rowNum)


        #colNum = i

        idstructure= table.cell(rowNum,0).value


        idparam = table.cell( rowNum, 1).value
        x = table.cell(rowNum, 2).value
        z = table.cell(rowNum, 3).value
        f = table.cell(rowNum, 4).value
        w1 = table.cell( rowNum, 5).value
        w2 = table.cell( rowNum, 6).value
        n = table.cell( rowNum, 7).value

        sql = " insert into valutazione values( "
        sql +=  str(idstructure) + "," + str(idparam) + ", " + str(x)  + ", "+ str(z) + ", " + str(f)
        sql +=  ", " + str(w1) +  ", "+ str(w2) +  ", "+str(n)
        sql += ")"

        #print "\n"
        #print sql
        sqllist.append(sql)





    return sqllist
    # creating a Cursor



def importValutazioneFromText(filename, databasename):
    import os, subprocess

    from Connection import Connection

    #maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    sql = "Copy   valutazione from '" + filename + "' delimiter ','"

    print "\n"
    print sql

    from Utils import Directory2

    dir = Directory2.getPathScripts()

    # file = "C:/Data/Python/sql_temporal.txt"
    file = dir + "sql_temporal.txt"

    Writes.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    maquina = " -h " + con.host+ " -p " + con.port

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)


def deleteValutazione(databasename):
    import os, subprocess

    from Connection import Connection


    con2 = Connection()

    con = con2.getConnection()

    sql = "delete from valutazione "

    #maquina = " -h 127.0.0.1 -p 5434"
    maquina = " -h " + con.host + " -p " + con.port

    from Utils import Directory2

    dir = Directory2.getPathScripts()

    # file = "C:/Data/Python/sql_temporal.txt"
    file = dir + "sql_temporal.txt"

    Writes.writefile(file, sql)

    logging.debug("sql")
    logging.debug(sql)

    cmd = "psql -U " + con.user + maquina + " " + con.database + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)


def updatedamage(earthquakeintensity, databasename):
    conectarpostgres.calculatedamage(earthquakeintensity, databasename)

def checkdatabase(databasename):

    valor = 1
    try:
        # logging.debug(" calculating number of structures in database: " + databasename)

        import psycopg2
        import numpy

        con2 = Connection()

        con = con2.getConnection()

        #strcon = con2.getStringToConnect(con.database)

        name_data0base = "test"

        strcon = con2.getStringToConnect(databasename)

        logging.debug(" string de connection")

        print "strcon"
        print strcon
        logging.debug(strcon)

        try:

            conn = psycopg2.connect(strcon)

            '''
            cur = conn.cursor()

            cur.execute("SELECT count(gid) from p+")
            # cur.execute("""SELECT gid, (7* vulfactor - 13.1)/2.3  from popoliforpostgres""")

            sqllist = []

            rows = cur.fetchall()
            print "\nRows: \n"
            for row in rows:

                try:

                    print "Row 1 " + str(row[0])

                    if str(row[0]) == 'None':
                        valor = 0
                    else:
                        valor = row[0]
                except:
                    valor = -1
                '''


        except:
            print "I can't SELECT from popoli for postgres"
            valor =-1




    except:
        import sys
        print "I am unable to connect to the database.", sys.exc_info()[0]
        raise
        valor =-1

    return valor

