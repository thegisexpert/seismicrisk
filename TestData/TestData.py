
import Writes as w

def poputateFragilitiesCurvesToBuildings(databasename):
    import os, subprocess

    from Connection import Connection

    maquina = " -h 127.0.0.1 -p 5434"

    con2 = Connection()

    con = con2.getConnection()


    sql = "delete from fragility_curve_structure "

    file = "C:/Data/Python/sql_temporal.txt"

    w.writefile(file, sql)

    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > C:/Data/Python/errores.txt"

    print cmd
    subprocess.call(cmd, shell=True)

    from Logic import Common

    number_of_structures = Common.calculatenumberofstructures(databasename)

    for x in range(0, number_of_structures):
        # Y =  divmov(x, 3)
        y = x % 2
        sqlinsert = "insert into fragility_curve_structure values('" + str(x) + "', '" + str(y + 1) + "');\n"
        #sqlinsert = "insert into fragility_curve_structure values('" + str(x) + "', '0');\n"
        #
        #print sql
        sql += sqlinsert

    print " sql assing fragility " + sql

    file = "C:/Data/Python/sql_temporal.txt"

    w.writefile(file, sql)


    cmd = "psql -U " + con.user + maquina + " " + databasename + " < " + file + " > C:/Data/Python/errores.txt"

    print cmd
    subprocess.call(cmd, shell=True)




def populateValutazione(databasename):
    from Logic.PredictiveModel import PredictiveModel
    PredictiveModel.populateValutazione(databasename)

databasename = "popoli"
populateValutazione(databasename)


#poputateFragilitiesCurvesToBuildings(databasename)
