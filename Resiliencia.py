  # inicio spatial litle
        # importing pyspatialite
        
from pyspatialite import dbapi2 as db
        
        
     def setData():   
        # creating/connecting the test_db
        #conn = db.connect('test_db.sqlite')
        print "Inside code code ..."
        conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')
        
        # creating a Cursor
        cur = conn.cursor()
        
        # testing library versions
        rs = cur.execute('SELECT sqlite_version(), spatialite_version()')
        for row in rs:
            msg = "> SQLite v%s Spatialite v%s" % (row[0], row[1])
            print msg
        
        rs = cur.execute('SELECT sqlite_version(), spatialite_version()')
        for row in rs:
            msg = "> SQLite v%s Spatialite v%s" % (row[0], row[1])
            print msg
        
        #cur.execute("INSERT INTO popolispatial('descriptio') VALUES ('NUOVO 2 ')");
        
        #cur.execute("UPDATE popolispatial SET descriptio = 'my  descriptio plugin'  WHERE ogc_fid = '1'");
        
        cur.execute("DELETE FROM popolispatial  WHERE ogc_fid = '77'");
        
        conn.commit()
        
        rs.close()
        conn.close()
        
        # fin spatial litle
        
        #quit()