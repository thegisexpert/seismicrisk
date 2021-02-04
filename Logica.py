 # inicio spatial litle
        # importing pyspatialite


from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import string
import random

import connectdb
import sys
import psycopg2
import updatedatabase
import conectarpostgres

from Connection import Connection
con2 = Connection()

def addBuildings():
    updatedatabase.addBuildings()





def readData(id, databasename):
        # creating/connecting the test_db
        #conn = db.connect('test_db.sqlite')

        msg = ""

        #for the case it not exist the  iid


        print "Inside code code ... with id " + str(id)
        #conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')


        conn=psycopg2.connect(con2.getStringToConnect(databasename))


        # creating a Cursor
        cur = conn.cursor()

        # testing library versions
        #atritt = readNamesAttributesData()

        #rint atritt

        table = "popoliforpostgres"
        clave = "gid"

        #otrosql = 'SELECT ' +atritt  +' from ' + table +' where ' + clave +'=' + "'" + str(id) + "'"

        sql = 'SELECT vulindex, vulfactor, damage from ' + table + ' where ' + clave + '=' + "'" + str(id) + "'"

        sql =  sql.replace('\n', ' ')

        print sql

        rs = cur.execute(sql)

        existe = False

        rows = cur.fetchall()

        for row in rows:

            existe = True
            #msg = str(row[0])  + " ," + str(row[1]) + " ," + str(row[2]) + " ," + str(row[3]) + " ," + str(row[4]) + " ," + str(row[5]) + " ," + str(row[6]) + " ," + str(row[7]) + " ," + str(row[8]) + " ," + str(row[9]) + " ," + str(row[10])
            msg = str(row[0])  + " ," + str(row[1]) + " ," + str(row[2])

            msg = msg + "," + msg  + "," + msg
            print msg




        conn.commit()

        #rs.close()
        conn.close()



        if existe:
            print "existe el item"
        else:
            msg ="0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"
        return msg

        # fin spatial litle

        #quit()




def readIds():
        # creating/connecting the test_db
        #conn = db.connect('test_db.sqlite')

        msg = ""

        #for the case it not exist the  iid


        print "Inside code code ... with id " + str(id)


        existe = False

        try:

            sql = 'SELECT gid, name from popoliforpostgres order by gid '
            sql =  sql.replace('\n', ' ')

            print sql

            conn=psycopg2.connect(con2.getStringToConnect())
                # creating a Cursor
            cur = conn.cursor()

            # testing library versions
            #atritt = readNamesAttributesData()



            cur.execute(sql)

            for record in cur:
                #print "  " +record
                existe = True
                msg1 = str(record[0])  + " ," + str(record[1]) + " "
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
            msg ="0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"


        return msg

        # fin spatial litle

        #quit()





def readGeometry(id):
        # creating/connecting the test_db
        #conn = db.connect('test_db.sqlite')

        geom = ""

        #for the case it not exist the  iid


        print "Inside code code ... with id " + str(id)
        #conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')


        conn=psycopg2.connect(con2.getStringToConnect2())


        # creating a Cursor
        cur = conn.cursor()

        # testing library versions
        #atritt = readNamesAttributesData()

        ## print atritt

        table = "popoliforpostgres"
        clave = "gid"

        sql = 'SELECT geom from popoliforpostgres where gid=' + str(id) + ''
        sql =  sql.replace('\n', ' ')

        print sql

        rs = cur.execute(sql)

        existe = False

        rows = cur.fetchall()

        for row in rows:

            existe = True
            #msg = str(row[0])  + " ," + str(row[1]) + " ," + str(row[2]) + " ," + str(row[3]) + " ," + str(row[4]) + " ," + str(row[5]) + " ," + str(row[6]) + " ," + str(row[7]) + " ," + str(row[8]) + " ," + str(row[9]) + " ," + str(row[10])
            geom = str(row[0])




        conn.commit()

        #rs.close()
        conn.close()



        if existe:
            print "existe el item"
        else:
            geom ="00000000000000000000"
        return geom

        # fin spatial litle

        #quit()



def readGeometry(id):
        # creating/connecting the test_db
        #conn = db.connect('test_db.sqlite')

        geom = ""

        #for the case it not exist the  iid


        print "Inside code code ... with id " + str(id)
        #conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')


        conn=psycopg2.connect(con2.getStringToConnect2())


        # creating a Cursor
        cur = conn.cursor()

        # testing library versions
        #atritt = readNamesAttributesData()

        ## print atritt

        table = "popoliforpostgres"
        clave = "gid"

        sql = 'SELECT geom from popoliforpostgres where gid=' + str(id) + ''
        sql =  sql.replace('\n', ' ')

        print sql

        rs = cur.execute(sql)

        existe = False

        rows = cur.fetchall()

        for row in rows:

            existe = True
            #msg = str(row[0])  + " ," + str(row[1]) + " ," + str(row[2]) + " ," + str(row[3]) + " ," + str(row[4]) + " ," + str(row[5]) + " ," + str(row[6]) + " ," + str(row[7]) + " ," + str(row[8]) + " ," + str(row[9]) + " ," + str(row[10])
            geom = str(row[0])




        conn.commit()

        #rs.close()
        conn.close()



        if existe:
            print "existe el item"
        else:
            geom ="00000000000000000000"
        return geom

        # fin spatial litle

        #quit()


def readRoads():
        # creating/connecting the test_db
        #conn = db.connect('test_db.sqlite')

        msg = ""

        #for the case it not exist the  iid


        print "Inside code code ... with id " + str(id)


        existe = False

        try:

            sql = 'SELECT gid, name, geom from popoliforpostgres order by gid '
            sql =  sql.replace('\n', ' ')

            print sql

            conn=psycopg2.connect(con2.getStringToConnect2(), con2.user, con2.password)
                # creating a Cursor
            cur = conn.cursor()

            # testing library versions
            #atritt = readNamesAttributesData()



            cur.execute(sql)

            for record in cur:
                #print "  " +record
                existe = True
                msg1 = str(record[0]) + " ," + str(record[1]) +  " ," + str(record[2]) + " "

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

            rs.close()
            conn.close()

        except Exception as e:
            print str(e)

        if existe:
            print "existe el item"
        else:
            msg ="0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"


        return msg

        # fin spatial litle

        #quit()




        # fin spatial litle

        #quit()


def readTypeOfBuilding():
        # creating/connecting the test_db
        # conn = db.connect('test_db.sqlite')

        msg = ""

        # for the case it not exist the  iid


        print "Inside code code ... with id " + str(id)

        existe = False

        try:

            #update type of buildings
            sql = 'SELECT gid, name from fragility_values order by gid '
            sql = sql.replace('\n', ' ')

            print sql

            conn = psycopg2.connect(con2.getStringToConnect(), con2.user, con2.password)
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

            cur.close()
            conn.close()

        except Exception as e:
            print str(e)

        if existe:
            print "existe el item"
        else:
            msg = "0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0"

        return msg

     # fin spatial litle

     # quit()



def addAttributesData():
    conectarpostgres.addAttributesData()

def addVulnerabilityColumns():


    # creating a Cursor

    table = "popoliforpostgres";

    filename = "C:/Data/Python/metodologia.txt"

    sql = ""
    sqllist = []

    if (filename != ""):
            infile = open(filename,"r")
            lines = infile.readlines()
            infile.close()


            for i in range(0, len(lines)):
                tokens  = lines[i];

                if (len(sql))>1:
                    #otrosql =  otrosql + ", " + tokens
                    sql = "alter table popoliforpostgres add column " + tokens
                    print "Logica 525 \n  " + sql

                    sqllist.append(sql)
                else:

                    #otrosql =  tokens
                    sql = ""


            conectarpostgres.executeSQL(sqllist)


    return sql
#quit()

def setmydata(self, data):

        horHeaders = []

        for n, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)


def populateTableMethodology():
        self.tableViewMethodology = QtGui.QTableWidget(1,3)
        #self.tableViewMethodology.setGeometry(QtCore.QRect(40, 210, 211, 131))
        #self.tableViewMethodology.setObjectName(_fromUtf8("tableViewMethodology"))

        ''' data methodologia
        '''



        filename = "C:/Data/Python/archivolectura.txt"
        if (filename != ""):
            infile = open(filename,"r")
            lines = infile.readlines()
            infile.close()
            self.tableViewMethodology.setRowCount(len(lines))
            for i in range(0, len(lines)):
                tokens = lines[i].strip().split(",")
                make = QtGui.QTableWidgetItem(tokens[0])
                model = QtGui.QTableWidgetItem(tokens[1])
                price = QtGui.QTableWidgetItem(tokens[2])
                self.tableViewMethodology.setItem(i,0,make)
                self.tableViewMethodology.setItem(i,1,model)
                self.tableViewMethodology.setItem(i,2,price)
            self.tableViewMethodology.resizeColumnsToContents()
        #self.tableViewMethodology.data = data

        self.tableViewMethodology.resizeColumnsToContents()
        self.tableViewMethodology.resizeRowsToContents()

        ''' fin data methodologia '''

def mytablewidget2():
        self.tableViewMethodology = QtGui.QTableWidget(1,3)
        #self.tableViewMethodology.setGeometry(QtCore.QRect(40, 210, 211, 131))
        #self.tableViewMethodology.setObjectName(_fromUtf8("tableViewMethodology"))

        ''' data methodologia
        '''



        filename = "C:/Data/Python/archivolectura.txt"
        if (filename != ""):
            infile = open(filename,"r")
            lines = infile.readlines()
            infile.close()
            self.tableWidget.setRowCount(len(lines))
            for i in range(0, len(lines)):
                tokens = lines[i].strip().split(",")
                make = QtGui.QTableWidgetItem(tokens[0])
                model = QtGui.QTableWidgetItem(tokens[1])
                price = QtGui.QTableWidgetItem(tokens[2])
                self.tableWidget.setItem(i,0,make)
                self.tableWidget.setItem(i,1,model)
                self.tableWidget.setItem(i,2,price)
            self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.data = data

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

        ''' fin data methodologia '''

def initvalues():

    conectarpostgres.initvalues()



#otrosql del vki

#select  (vkimportance-vkprotection)*(select param from misparam where idparam=8)*(1/6)*(1/14)+ 0.5 from valutazione;

'''
Assing some values to hazards calculations
'''
def populatehazard():

    connectdb.populatehazard()

def updateHazardParameters(momentum, texto):

    connectdb.updateHazardParameters(momentum, texto)






def updateValutazioneFromExcel(idstructura, filename, nombretabla):

          print " filename is " + filename

          connectdb.deleteValutazioneStructucture(idstructura)

          connectdb.updateValutazioneFromExcel(idstructura, filename, nombretabla)


def updateValutazioneLot(filename, database):
    print " filename is " + filename

    connectdb.updateValutazioneLot( filename, database)

def calculateinterdependency(geom):

          connectdb.calculateinterdependencies(geom)


def calculateinterdependencyById(id):
    # creating/connecting the test_db
    # conn = db.connect('test_db.sqlite')

    geom = ""

    # for the case it not exist the  iid


    print "Inside code code with id " + str(id)
    # conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')


    conn = psycopg2.connect(con2.getStringToConnect2(), con2.user, con2.password)

    # creating a Cursor
    cur = conn.cursor()

    # testing library versions
    #atritt = readNamesAttributesData()

    #print atritt

    table = "popoliforpostgres"
    clave = "gid"

    sql = 'SELECT geom from popoliforpostgres where gid=' + str(id) + ''
    sql = sql.replace('\n', ' ')

    print sql

    rs = cur.execute(sql)

    existe = False

    rows = cur.fetchall()

    for row in rows:
        existe = True
        # msg = str(row[0])  + " ," + str(row[1]) + " ," + str(row[2]) + " ," + str(row[3]) + " ," + str(row[4]) + " ," + str(row[5]) + " ," + str(row[6]) + " ," + str(row[7]) + " ," + str(row[8]) + " ," + str(row[9]) + " ," + str(row[10])
        geom = str(row[0])

    conn.commit()

    # rs.close()
    conn.close()

    if existe:
        print "existe el item"
    else:
        geom = "00000000000000000000"


    connectdb.calculateinterdependencies(geom)





def assignFragilitiesCurvesToBuildings(databasename):

    databasename ="prueba7"
    connectdb.assignFragilitiesCurvesToBuildings(databasename)


def deleteFragilitiesCurves(databasename, idfragility):

    connectdb.deleteFragilitiesCurves(databasename, idfragility)


def removeALLLayers():
    connectdb.removeALLLayers()

def exportFragilityValuesToExcel(filename, filename2, databasename):
    connectdb.exportFragilityValuesToExcel(filename, filename2,  databasename)







'''
read all the data as fragility curves,
and writes in excel
'''
def readAllDaraFragilityCurve(idfragility, databasename):
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

    sql = "select level, param1, param2 from fragility_curve_level  where idfragility='"+ str(idfragility)+"' order by level"

    print " sql read parameteres Logica 1237 "
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


    conn = psycopg2.connect(con2.getStringToConnect(), con2.user, con2.password)

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

    import csv

    name = 'D:/Data/Python/OtherFiles/somefile4.csv'

    row = cur.fetchall()
    f = open(name, 'w')
    writer = csv.writer(f)

    for element in row:
       writer.writerow(element)
    f.close()




    conn.commit()

    # rs.close()
    conn.close()






def writefile(filename, content ):

    out_file = open(filename, "w")
    if (filename != ""):

        infile = open(filename, "r")
        lines = infile.readlines()
        infile.close()

        try:

            out_file.write(content)

        except:
            print ""

    out_file.close()




'''
def readFragilityCurveData(idfragility, databasename):
    import csv

    records = readAllDaraFragilityCurve(idfragility, databasename)

    print " RECORDS ARE " + str(records)

    with open('D:/Data/Python/OtherFiles/somefile.csv', 'w') as csvfile:
        fieldnames = ['level', 'param1', 'param2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'level': records[0], 'param1': records[1], 'param2': records[2]})
        writer.writerow({'level': records[0], 'param1': records[1], 'param2': records[2]})
        writer.writerow({'level': records[0], 'param1': records[1], 'param2': records[2]})

def writeRows(rows):
    import csv

    records = readAllDaraFragilityCurve(idfragility, databasename)

    with open('D:/Data/Python/OtherFiles/somefile.csv', 'w') as csvfile:
        fieldnames = ['level', 'param1', 'param2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'level': records[0], 'param1': records[1], 'param2': records[2]})
        writer.writerow({'level': records[0], 'param1': records[1], 'param2': records[2]})
        writer.writerow({'level': records[0], 'param1': records[1], 'param2': records[2]})
'''

