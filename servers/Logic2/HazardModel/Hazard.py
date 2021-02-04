
def createEpicenter( momentum, x, y, parametros, objetos, modelohazard):
    import os, subprocess

    from Database.Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()

    # Choose your PostgreSQL version here
    # os.environ['PATH'] += r';C:\Program Files\PostgreSQL\9.5\bin'
    # D:\usbgis\apps\postgresql93\bin

    db = con2.getPathDatabase()

    # os.environ['PATH'] += r';D:\usbgis\apps\postgresql93\bin'

    # path_database=db["path_database"]

    path_database = con2.getPathDatabase()

    os.environ['PATH'] += "r" + path_database

    # http://www.postgresql.org/docs/current/static/libpq-envars.html

    '''
            os.environ['PGHOST'] = 'localhost'
    os.environ['PGPORT'] = '5432'
    os.environ['PGUSER'] = 'potgres'
    os.environ['PGPASSWORD'] = 'postgres'
    os.environ['PGDATABASE'] = 'prueba4'
    '''

    from Utils import Directory

    sqld = Directory.getPathSqlDir()

    sql_temp = Directory.getPathTempDir()

    print " log path scripts 3502 "
    print sqld

    #cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + sqld + "random_points_in_polygons.txt > " + sql_temp + "errores2.txt"

    #subprocess.call(cmd, shell=True)

    cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + sqld + "Hazard/create_epicenter_hazard1.txt > " + sql_temp + "errores2.txt"

    if (objetos == 1):
        cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + sqld + "Hazard/create_epicenter_hazard.txt > " + sql_temp + "errores1.txt"

    print cmd

    subprocess.call(cmd, shell=True)

    populateEpicenter(momentum, x, y, parametros)

    cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + sqld + "Hazard/update_epicenter.txt > " + sql_temp + "errores3.txt"
    print cmd

    subprocess.call(cmd, shell=True)

    if modelohazard == 0:

        cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + sqld + "Hazard/update_hazard1.txt > " + sql_temp + "errores4.txt"
        print cmd

    else:
        cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + sqld + "Hazard/update_hazard2.txt > " + sql_temp + "errores5.txt"
        print cmd

    subprocess.call(cmd, shell=True)



def populateEpicenter(momemtum, x, y, texto):
    '''
    try:

        parametros = texto.split(",")

        a = parametros[0]
        b = parametros[1]
        c = parametros[2]
        d = parametros[3]

        a = a.replace("a=", "")

        b = b.replace("b=", "")

        c = c.replace("c=", "")

        d = d.replace("d=", "")

        otrosql = "update hazard set  a="+a +", b=" +b +", c=" +c +", d=" + d+""
        otrosql = otrosql.replace("\n", "")

    except :

        import sys
        print "parse  error:", sys.exc_info()[0]

        otrosql = ""



    if (otrosql==""):
        otrosql = "update hazard set  a=random(), b=random() , c=random(), d=random()"

    print " Populate epicenter "
    '''

    # sqllist=[otrosql]

    sqllist = []
    sql = "insert into epicenter values ('0', 'epicenter',  ST_SetSRID(ST_MakePoint(" + str(x) + "," + str(
        y) + "), 4326))"

    sqllist.append(sql)
    sqllist.append("update hazard set momentum = " + momemtum)

    print sql

    executeSQL(sqllist)

    # run the next three sqls by console


    '''

    these instructions are runned by console
    otrosql = "update distance_from_epicenter set geom = (select ST_MakeLine((select geom from hazard where hazard.gid=distance_from_epicenter.gid), (select geom from epicenter where gid='0')))"


    sql2 = "update distance_from_epicenter set distance=ST_Length(geom)"

    sql3 = "update hazard set rdistance=ST_Length((select geom from distance_from_epicenter where distance_from_epicenter.gid=hazard.gid))/1000"

    '''

    # sqllist.append(otrosql)


    # sqllist.append(sql2)

    # sqllist.append(sql3)


    # aqui

    import os, subprocess

    from Database.Connection import Connection

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

    cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < C:/Data/Python/copy_from_cvs.txt"
    print cmd

    subprocess.call(cmd, shell=True)

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


    from Utils import Directory

    dir = Directory.getPathTempDir()

    file = dir + "sqltemporal2.txt"

    file_temp = dir + "errores.txt"

    Writes.writefile(file, s)



    cmd = "psql -d " + con.database + " -U " + con.user + maquina + " < " + file + " >  " + file_temp + ""
    print cmd

    subprocess.call(cmd, shell=True)



