# Scrive un file.
import string


def writePoint(coord):
    out_file = open("C:/Data/Python/coordinates_of_proof.txt","a")
    out_file.write(coord)
    out_file.close()


def fromPointsToQueries(filename):
    #filename = "C:/Data/Python/coordinates_of_proof.txt"

    '''
    query as example
    
    SELECT    ST_SetSRID(ST_Multi(ST_MakePolygon( ST_GeomFromEWKT('LINESTRING(
1539876.23141 5187076.02848 1,
1539897.50032 5187079.00155 1,
1539908.93521 5187033.71936 1,
1539895.44204 5187030.28889 1,
1539876.23141 5187076.02848 1)'))), 3857) as geom

SELECT    ST_SetSRID(ST_Multi(ST_MakePolygon( ST_GeomFromEWKT('LINESTRING(
PUNTOS)'))), 3857) as geom
    '''

    sql1 ="drop table if exists addstructures;\n"

    sql2 ="create table  addstructures as \n"
    sql_to_generate = " SELECT  '' as name, '' as despriptio,   ST_SetSRID(ST_Multi(ST_ConvexHull(ST_MakePolygon( ST_GeomFromEWKT('LINESTRING(PUNTOS)')))), 4326) as geom \n"

    #filename = "C:/Data/Python/coordinates_of_proof.txt"


    if (filename != ""):

        out_file = open("C:\Data\Python\create_new_structures.txt", "w")

        out_file.write(sql1)
        out_file.write(sql2)

        infile = open(filename,"r")
        lines = infile.readlines()
        infile.close()

        for i in range(0, len(lines)):
            print " iiii " +  str(i)
            tokens = lines[i]
            my_sql = sql_to_generate

            try:
                pos_of_comma = tokens.index(",")
                primera_coordenada = tokens[0: pos_of_comma]


                tokens = tokens.replace("fin", primera_coordenada)

                my_sql = my_sql.replace("PUNTOS", tokens )

                #print " union \n"
                print my_sql

                if i>0:
                    out_file.write("union \n")
                out_file.write(my_sql)

            except :
                print " 51 format of points not valid"

    out_file.close()


filename =  "C:/Data/Python/coordinates_of_proof.txt"
fromPointsToQueries(filename)
execfile("C:\Users\AG\.qgis2\python\plugins\PruebaAutoFields\Otros\merge_shapefiles_method_add_new_structures.py");


