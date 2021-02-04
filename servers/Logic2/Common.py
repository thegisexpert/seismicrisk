
def calculatenumberofstructures( databasename):

    valor = -1

    try:
        import logging
        from Database.Connection import Connection
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



def calculatenumberofstructuresinfragilityview( databasename):

    valor = -1

    try:
        import logging
        from Database.Connection import Connection
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
            cur.execute("SELECT count(gid) from view_fragility_curve_structure")
            #cur.execute("""SELECT gid, (7* vulfactor - 13.1)/2.3  from popoliforpostgres""")

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
            print "I can't SELECT from view_fragility_curve_structure"




    except :
        import sys
        print "I am unable to connect to the database.", sys.exc_info()[0]
        raise

    return valor
