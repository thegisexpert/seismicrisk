#http://pyqgis.org/blog/2013/04/11/creating-a-postgresql-connection-from-a-qgis-layer-datasource/

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from qgis.core import *


def run_script(iface):
    # get the active layer
    #layer = iface.activeLayer()
    
    '''
        init postgres
        http://gis.stackexchange.com/questions/86983/how-to-properly-establish-a-postgresql-connection-using-qgscredentials
        '''
    
    uri = QgsDataSourceURI()
    # assign this information before you query the QgsCredentials data store
    uri.setConnection("localhost", "5432", "prueba4", "postgres", "postgres")
    connInfo = uri.connectionInfo()
    
    (success, user, passwd) = QgsCredentials.instance().get(connInfo, "postgres", "postgres")
    
    if success:
        uri.setPassword(passwd)
        uri.setUsername(user)
        uri.setDataSource("public", "popoliforpostgres", "geom")
        layer = QgsVectorLayer(uri.uri(), "LYR", "postgres")
        
        
    
    # get the underlying data provider
    provider = layer.dataProvider()
        # get the URI containing the connection parameters
    uri = QgsDataSourceURI(provider.dataSourceUri())
    print uri.uri()
    # create a PostgreSQL connection using QSqlDatabase
    db = QSqlDatabase.addDatabase('QPSQL')
    # check to see if it is valid
    
    if db.isValid():
        print "QPSQL db is valid"
        # set the parameters needed for the connection
        '''db.setHostName(uri.host())
        db.setDatabaseName(uri.database())
        db.setPort(int(uri.port()))
        db.setUserName(uri.username())
        db.setPassword(uri.password())'''
        
        db.setHostName("localhost")
        db.setDatabaseName("prueba4")
        db.setPort(5432)
        db.setUserName("postgres")
        db.setPassword("postgres")
        
        if db.open():
            print "Opened %s" % uri.uri()
            # execute a simple query 
            query = db.exec_("""select * from valutazione""")
            # loop through the result set and print the name
            while query.next():
                #print " while "
                record = query.record()
                #print str(record.field('idstructure').value())
        else:
            err = db.lastError()
            print err.driverText()

        

        sql = "update popoliforpostgres set damage = 0, vulnerab=0"
        
        print sql
        db.exec_(sql)
                      
        db.commit()   
        db.close() 
               

    print "Initializatized vsalues for vulnerablity and damage" 
    
    



def updatevulnerability():

    conn = db.connect('C:/Data/Popoli/popolispatial.sqlite')
    
    # creating a Cursor
    cur = conn.cursor()




    
    # creating a Cursorupdate
    
    table = "popolispatial"
    
    filename = "C:/Data/Python/archivoupdate.txt"
            
    jueego = "0"
   
 
    for idstructura in range(1,55):
    
        sql = "update popolispatial set vulnerab = (select  sum(paramvalue*(vkimportance-vkprotection))*(1/6)*(1/(select sum(paramvalue) from valutazione where idstructure= " + str(idstructura) + "))+ 0.5 from valutazione where idstructure= " + str(idstructura) +" ) where ogc_fid= " + str(idstructura) + ""

        sql = "update popolispatial set vulnerab = "
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
    
   
    sql = "update popoliforpostgres set damage = 0.53 + 1.15*vulnerab -4*vulnerab*vulnerab + 4.21*vulnerab*vulnerab*vulnerab"
    
    try:       
          
            print sql
            cur.execute(sql)
            
            
       
       
    except:
            jueego = "1"
            #print " sentencia  otrosql erronea "

    conn.commit()
    conn.close()
    
    print " juego es " + jueego
    
    
def updatedamage():

    
    
    '''
        init postgres
        http://gis.stackexchange.com/questions/86983/how-to-properly-establish-a-postgresql-connection-using-qgscredentials
        '''
        
    uri = QgsDataSourceURI()
    # assign this information before you query the QgsCredentials data store
    uri.setConnection("localhost", "5432", "prueba4", "postgres", "postgres")
    connInfo = uri.connectionInfo()
    
    (success, user, passwd) = QgsCredentials.instance().get(connInfo, "postgres", "postgres")
    




    
    # creating a Cursorupdate
    
    table = "popolispatial"
    
            
    jueego = "0"
   
 

    
    sql = "update popoliforpostgres set damage = 0.53 + 1.15*vulnerab -4*vulnerab*vulnerab + 4.21*vulnerab*vulnerab*vulnerab"
    
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
    


    


run_script(iface)