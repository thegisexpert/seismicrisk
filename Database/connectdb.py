#/usr/bin/python2.
#
#

import psycopg2
import numpy
import string
import sys

from Connection import Connection


#maquina = " -h 127.0.0.1 -p 5434"

con2 = Connection()


# Try to connect

'''
try:
    conn=psycopg2.connect("dbname='prueba4' userpostgres' password='postgres'")
except:
    print "I am unable to connect to the database."

cur = conn.cursor()
try:
    cur.execute("""SELECT * from popoliforpostgres""")
except:
    print "I can't SELECT from popoli for postgres"

rows = cur.fetchall()
print "\nRows: \n"
for row in rows:
    print "   ", row[1]


updatevulnerability()
populateparameters()
'''

#otrosql del vki

#select  (vkimportance-vkprotection)*(select param from misparam where idparam=8)*(1/6)*(1/14)+ 0.5 from valutazione;

def updatevulnerability():

    try:
        conn=psycopg2.connect(Connection.getStringToConnect(self))
    except:
        print "I am unable to connect to the database."

    # creating a Cursor
    cur = conn.cursor()





    # creating a Cursorupdate

    table = "popoliforpostgres"

    filename = "C:/Data/Python/archivoupdate.txt"

    jueego = "0"

    for idstructura in range(1,55):

        sql = "update popoliforpostgres set vulnerab = (select  sum(paramvalue*(vkimportance-vkprotection))*(1/6)*(1/(select sum(paramvalue) from valutazione where idstructure= " + str(idstructura) + "))+ 0.5 from valutazione where idstructure= " + str(idstructura) +" ) where ogc_fid= " + str(idstructura) + ""

        sql = "update popoliforpostgres set vulnerab = "
        sql = sql + "(select   (sum(paramvalue*(vkimportance-vkprotection))/sum(paramvalue))/6 + 0.5 "
        sql = sql + "from valutazione where idstructure='" + str(idstructura)+"'"
        sql = sql + ")"
        sql = sql + "where idstructure=" + str(idstructura)+"'"

        try:

                print sql
                cur.execute(sql)




        except:
                jueego = "1"
                #print " sentencia  otrosql erronea "


    #rs.close()
    conn.commit()
    conn.close()

    print " juego es " + jueego



def populateparameters():

    ##conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')

    try:
        conn=psycopg2.connect(con2.getStringToConnect())
    except:
        print "I am unable to connect to the database."

    # creating a Cursor
    cur = conn.cursor()





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

    #vki = w1 * z * f

    # vkp = wz*m
    #vkp = w2 * z * n

    cur.execute(sql)
    #cur.execute(otrosql)





    cur.execute("SELECT UpdateLayerStatistics(\'popolispatial\')")
    conn.commit()

    #rs.close()
    conn.close()



def updateValutazioneLot(filrname, databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "delete from valutazione;"
    sql += "copy valutazione(idstructure, idparam, x, z, f, w1, w2,n) FROM 'C:/Data/datos_valutazione.csv' DELIMITER ';' CSV"
    file = "C:/Data/Python/sql_temporal.txt"

    writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)

    sql = "update valutazione set  paramvalue='1.5' where (idparam=1 or idparam=2 or idparam=3 or idparam=13 );"
    print sql

    sql += "update valutazione set  paramvalue='1' where (idparam=4 or idparam=5 or idparam=6 or idparam=7 );"
    print sql



    sql += "update valutazione set  paramvalue='0.5' where idparam=9;"
    print sql


    sql += "update valutazione set  paramvalue='1' where idparam=10;"
    print sql + ";"


    sql += "update valutazione set  paramvalue='0.8' where (idparam=11 or idparam=8);"
    print sql + ";"


    sql += "update valutazione set  paramvalue='0.5' where idparam=12;"
    print sql + ";"

    sql += "update valutazione set  paramvalue='0.3' where idparam=14;"
    print sql + ";"

    '''

    vki = w1 * z * f

    vkp = w2 * z * n
    '''

    sql += "update valutazione set  vkimportance=w1*z*f;"
    print sql + ";"


    sql += "update valutazione set  vkprotection=w2*z*n;"
    print sql + ";"



    writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > C:/Data/Python/errores.txt "
    print cmd
    subprocess.call(cmd, shell=True)

    print sql + ";"

    # cur.execute(otrosql)





    sql="SELECT UpdateLayerStatistics(\'popoliforpostgres\')"


    writefile(file, sql)


    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > C:/Data/Python/errores2.txt "
    print cmd
    subprocess.call(cmd, shell=True)




def exportFragilityValuesToExcel(filename, filename2, databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "Copy (Select idfragility, level, param1, param2 From fragility_curve_level order by idfragility, level) To  '" + filename+ "' With CSV DELIMITER ','  HEADER;"
    file = "C:/Data/Python/sql_temporal.txt"

    writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)



    sql = "Copy (Select * from fragility_curve_structure order by type_structure) To  '" + filename2+ "' With CSV DELIMITER ','  HEADER;"
    file = "C:/Data/Python/sql_temporal.txt"

    writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file
    print cmd
    subprocess.call(cmd, shell=True)


def updateValutazioneFromExcel(idstructura, filename, nombretabla):

    ##conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')

    sqllist = []




    # creating a Cursorupdate


    print filename + " is "

    if (filename != ""):
            infile = open(filename,"r")
            lines = infile.readlines()
            infile.close()

            #cur = conn.cursor()


            tokens = ""

            #params = ["param10", "param20", "param30", "param40", "param50", "param60", "param70", "param80",  "param90"]
            #params.append(["param11", "param12", "param13", "param14", "param15", "param16", "param17", "param18",  "param19"])

            params = ["param10", "param20", "param30", "param40", "param50", "param60", "param70", "param80",  "param90", "param11", "param12", "param13", "param14", "param15", "param16", "param17", "param18",  "param19"]

            for i in range(0, len(lines)):
                values =  lines[i];

                print values

                tokens = values.split(";")
                '''cur.execute(otrosql)'''

                param = tokens[0]
                x= float(tokens[1])
                z= float(tokens[2])
                f = float(tokens[3]) ## dont know the ranges of values
                w1= float(tokens[4])
                w2= float(tokens[5])
                n = float(tokens[6])  ## dont know the ranges of values

                       #vki = Z* W * F
                vki = w1*z*f

            #vkp = wz*m
                vkp = w2*z*n



                x= str(tokens[1])
                z= str(tokens[2])
                f = str(tokens[3])  ## dont know the ranges of values
                w1= str(tokens[4])
                w2= str(tokens[5])
                n = str(tokens[6])  ## dont know the ranges of values

                vki = str(vki)
                vkp = str(vkp)


            #try:

                sql = " insert into valutazione values (" + str(idstructura) + "," + param + "," + x + ", " + z + ", " + f + "," + w1 + "," + w2 + ", " + n + "," + vki + "," + vkp +", 0)"

                print sql + ";"
                ##cur.execute(otrosql)
                sqllist.append(sql)




            #except:
            #    jueego = 1
                        #print " sentencia  otrosql erronea "


            sql = "update valutazione set  paramvalue='1.5' where (idparam=1 or idparam=2 or idparam=3 or idparam=13 )"
            print sql

            #cur.execute(otrosql)

            sqllist.append(sql)


            sql = "update valutazione set  paramvalue='1' where (idparam=4 or idparam=5 or idparam=6 or idparam=7 )"
            print sql


            #cur.execute(otrosql)
            sqllist.append(sql)


            sql = "update valutazione set  paramvalue='0.5' where idparam=9"
            print sql

            #cur.execute(otrosql)
            sqllist.append(sql)

            sql = "update valutazione set  paramvalue='1' where idparam=10"
            print sql + ";"

#            cur.execute(otrosql)
            sqllist.append(sql)

            sql = "update valutazione set  paramvalue='0.8' where (idparam=11 or idparam=8)"
            print sql + ";"

            #cur.execute(otrosql)
            sqllist.append(sql)

            sql = "update valutazione set  paramvalue='0.5' where idparam=12"
            print sql + ";"

            #cur.execute(otrosql)
            sqllist.append(sql)

            sql = "update valutazione set  paramvalue='1.5' where idparam=13"
            print sql + ";"

            #cur.execute(otrosql)
            sqllist.append(sql)

            sql = "update valutazione set  paramvalue='0.3' where idparam=14"
            print sql + ";"

            #cur.execute(otrosql)
            #cur.execute(otrosql)
            sqllist.append(sql)



            for sql in sqllist:
                # execute a simple query
                   #query = db.exec_(str)
                   print sql

            executeSQL(sqllist)


    #rs.close()
    #conn.close()




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



def deleteValutazioneStructucture(idstructura):

    ##conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')




    try:
        conn=psycopg2.connect(con2.getStringToConnect())
    except:
        print "I am unable to connect to the database."

    # creating a Cursor
    cur = conn.cursor()



    sql = "delete from valutazione where idstructure = '" + str(idstructura) + "'"

    sqllist = []
    #print otrosql
    #cur.execute(otrosql)

    sqllist.append(sql)

    executeSQL(sqllist)

    # creating a Cursorupdate



    #rs.close()

    conn.close()


def executeSQL(sqllist):

    ##conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')

    try:
        conn=psycopg2.connect(con2.getStringToConnect())
            # creating a Cursor
        cur = conn.cursor()





        # creating a Cursorupdate


        table = "popolispatial"

        filename = "C:/Data/Python/archivoupdate.txt"

        cur = conn.cursor()

        for sql in sqllist:
                    # execute a simple query
                       #query = db.exec_(str)
                       #cur.execute(otrosql)

                try:
                    cur.execute(sql)
                except:
                    print( "Exception running otrosql.", sys.exc_info())


        conn.commit()

        #rs.close()
        conn.close()
    except:
        print ("I am unable to connect to the database.", sys.exc_info())





def calculatedamage(earthquakeintesity):

    try:
        conn=psycopg2.connect(con2.getStringToConnect())

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

                print "Row 1 " + str(row[1])

                if str(row[1])=='None':
                   valor = 2.5*(1+ numpy.tanh(0))
                else:
                   valor = 2.5*(1 + numpy.tanh(float(str(row[1]))))
            except:
                valor = 2.5*(1+ numpy.tanh(0))


            sql = "update popoliforpostgres set damage = '" + str(valor) + "' where gid= '" + str(row[0]) + "'"

            #otrosql = "update damage set damage = '" + str(valor) + "' where gid= '" + str(row[0]) + "'"

            sqllist.append(sql)




        executeSQL(sqllist)
    except:
        print "I am unable to connect to the database."




def calculateinterdependencies(geom):

    createinterdependency(geom)
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # Choose your PostgreSQL version here
    # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
    # D:\usbgis\apps\postgresql93\bin

    os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

    # http://www.postgresql.org/docs/current/static/libpq-envars.html
    os.environ['PGHOST'] = 'localhost'
    os.environ['PGPORT'] = '5432'
    os.environ['PGUSER'] = 'potgres'
    os.environ['PGPASSWORD'] = 'postgres'
    os.environ['PGDATABASE'] = 'roads'



    cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < D:/Data/Python/create_interdependencies.txt"
    print cmd

    subprocess.call(cmd, shell=True)

def createinterdependency(geom):

    try:

        sql2 = "drop table interdependencies; "

        sql = '''
SELECT gid, name, geom,
ST_Distance_Sphere(geom,  ST_GeomFromText( ST_AsText('param'))
) INTO interdependencies
FROM popoliforpostgres
WHERE ST_Distance_Sphere(geom,
ST_GeomFromText(ST_AsText('param'))) < 20
        '''

        sql = sql.replace('param', geom.strip())
        print sql
        f = open('D:/Data/Python/create_interdependencies.txt', 'w')

        f.write(sql2)

        f.write(sql)
        f.close()


    except:
        print "I am unable to connect to the database." , sys.exc_info()


def populatehazard():

    print " in conndect db populate hazard 581"


    sqllist = ["update hazard set  momentum= get_random_number(0, 9), soilfactor= get_random_number(0, 1)"]

    sql2 = "update hazard set rdistance=(select distance from distance_from_epicenter where distance_from_epicenter.gid=hazard.gid)/1000"

    sqllist.append(sql2)

    executeSQL(sqllist)

def updateHazardParameters(momentum, texto):

    parametros = texto.split(",")

    sqlhazard = ""
    try:

        a = parametros[0]
        b = parametros[1]
        c = parametros[2]
        d = parametros[3]

        a = a.replace("a=", "")

        b = b.replace("b=", "")

        c = c.replace("c=", "")

        d = d.replace("d=", "")

        sql = "update hazard set  a="+a +",b=" +b +",c=" +c +",d=" + d+""
        sql = sql.replace("\n", "")
        sqlhazard = sql

    except :

        print "parse  error:", sys.exc_info()[0]

        sql = ""



    print sql





    if sql!="":
        sqllist0 = ["update hazard set momentum=" + momentum]


        #executeSQL(sqllist0)



        sqllist = [sql]
        sqllist.append("update hazard set hazard=a + b*momentum + c*rdistance + d*soilfactor")

        #executeSQL(sqllist)

        #"update hazard set momentum = get_random_number(0, 9), soilfactor = get_random_number(0, 1)"

        #"update hazard set rdistance = (select distance from distance_from_epicenter where distance_from_epicenter.gid = hazard.gid) / 1000"



        out_file = open("C:\Data\qgis\updatehazard.txt", "w")

        out_file.write(sqlhazard + ";\n")

        out_file.write("update hazard set momentum=" + momentum +";\n")
        out_file.write("update hazard set soilfactor = get_random_number(0, 1);\n")
        out_file.write("update hazard set rdistance = (select distance from distance_from_epicenter where distance_from_epicenter.gid = hazard.gid) / 1000;\n")
        out_file.write("update hazard set hazard=a + b*momentum + c*rdistance + d*soilfactor;\n")






        out_file.close()

        import os, subprocess

        from Connection import Connection


        maquina = " -h 127.0.0.1 -p 5434"

        con2 = Connection()

        con = con2.getConnection()

        # Choose your PostgreSQL version here
        # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
        # D:\usbgis\apps\postgresql93\bin

        os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

        # http://www.postgresql.org/docs/current/static/libpq-envars.html
        os.environ['PGHOST'] = 'localhost'
        os.environ['PGPORT'] = '5432'
        os.environ['PGUSER'] = 'potgres'
        os.environ['PGPASSWORD'] = 'postgres'
        os.environ['PGDATABASE'] = 'prueba7'

        #cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < C:/Data/Python/copy_from_cvs.txt"


        cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < C:\Data\Python\update_epicenter.txt > C:\Data\Python\errores.txt"
        print cmd

        subprocess.call(cmd, shell=True)

        cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < C:\Data\qgis\updatehazard.txt > C:\Data\Python\errores.txt"
        print cmd

        subprocess.call(cmd, shell=True)




def removeALLLayers():
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "drop database prueba7"
    file = "C:/Data/Python/sql_temporal.txt"

    writefile(file, sql)

    databasename = "template1"

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > 'C:/Data/Python/errores.txt'"
    subprocess.call(cmd, shell=True)





def assignFragilitiesCurvesToBuildings(databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = ""

    for x in range(0, 8800):
        # Y =  divmov(x, 3)
        y = x % 2
        sqlinsert = "insert into fragility_curve_structure values('" + str(x) + "', '" + str(y + 1) + "');\n"
        #print sql
        sql += sqlinsert

    file = "C:/Data/Python/sql_temporal.txt"

    writefile(file, sql)


    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > C:/Data/Python/errores.txt"

    print cmd
    subprocess.call(cmd, shell=True)




def deleteFragilitiesCurves(databasename, idfragility):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    sql = "delete from fragility_curve_structure where idfragility='" + str(idfragility) + "';\n"
    sql += "delete from fragility_curve_level where idfragility='" + str(idfragility) + "';\n"

    sql += "delete from fragility_curve where idfragility='" + str(idfragility) + "';\n"

    file = "C:/Data/Python/sql_temporal.txt"

    writefile(file, sql)


    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > C:/Data/Python/errores.txt"

    print cmd
    subprocess.call(cmd, shell=True)
