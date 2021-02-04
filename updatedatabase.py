#http://gis.stackexchange.com/questions/90085/import-shp-to-postgis-using-python-and-ogrhttp://gis.stackexchange.com/questions/90085/import-shp-to-postgis-using-python-and-ogr

import os.path  
import psycopg2
import osgeo.ogr as ogr

def addBuildings():  
    #connection = psycopg2.connect("dbname=... user=...") 
    
    try:
        connection=psycopg2.connect("dbname='prueba4' user='postgres' password='postgres'")
    except:
        print "I am unable to connect to the database."
 
    cursor = connection.cursor()  
    #cursor.execute("DELETE FROM countries")  
    #srcFile = os.path.join("DISTAL-data", "TM_WORLD_BORDERS-0.3","TM_WORLD_BORDERS-0.3.shp")  
   
    #https://pcjericks.github.io/py-gdalogr-cookbook/vector_layers.html
    
    #daShapefile = r"C:\Temp\Voting_Centers_and_Ballot_Sites.shp"
    
    daShapefile = r"C:\Data\Popoli\popoli.shp"
    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    
    dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.
    
    # Check to see if shapefile is found.
    if dataSource is None:
        print 'Could not open %s' % (daShapefile)
    else:
        print 'Opened %s' % (daShapefile)
        layer = dataSource.GetLayer()
        featureCount = layer.GetFeatureCount()
        print "Number of features in %s: %d" % (os.path.basename(daShapefile),featureCount)
        
    #fin https://pcjericks.github.io/py-gdalogr-cookbook/vector_layers.html
        
    #shapefile = osgeo.ogr.Open(srcFile)   ojo no lee el shapefile con osgeo  
    #layer = shapefile.GetLayer(0)    
    for i in range(layer.GetFeatureCount()):  
        feature = layer.GetFeature(i)  
        #name = feature.GetField("NAME").decode("Latin-1")  
        name = feature.GetField("name")  
        
        #wkt = feature.GetGeometryRef().ExportToWkt()     #original with ExportToWkt()
        
        wkt = feature.GetGeometryRef()
        
        geom = ogr.CreateGeometryFromWkt(str(wkt))
        #cursor.execute("INSERT INTO popoliforpostgres (name,outline) " +"VALUES (%s, ST_GeometryFromText(%s, " +"4326))", (name.encode("utf8"), wkt))  
        
        sql = "INSERT INTO popoliforpostgres (name,geom) " +"VALUES ('" +  str(name) +"', ST_GeometryFromText('" + str(geom) + "')"
        
        print sql
        
        #cursor.execute("INSERT INTO popoliforpostgres (name,geom) " +"VALUES (" +  str(name) +", ST_GeometryFromText(" + str(wkt) + "))")  
    
    connection.commit()  