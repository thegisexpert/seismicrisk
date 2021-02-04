

def refactor_py(x, y):

    a = (x-1, y+1)
    b = (x+1, y+1)
    c=  (x-1, y-1)
    d =  (x+1, y-1)


    geom = '''(((X, Y, W, Z)))
    '''

    geom = geom.replace("X", str(a[0]) + " "  +str(a[1]) )
    geom = geom.replace("Y", str(b[0]) + " " + str(b[1]))
    geom = geom.replace("W", str(c[0]) + " " + str(d[1]))
    geom = geom.replace("Z", str(d[0]) + " " + str(d[1]))

    geom = "MULTIPOLYGON" + geom

    print geom

    insert = "insert into popoliforpostgres (name, geom) values ( 'generated', ST_GeomFromText(" + geom +"))"

    print insert

    #return geom

refactor_py(2, 1)
