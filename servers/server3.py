import SimpleHTTPServer
import SocketServer
import sys

'''

import sys
sys.path
#sys.path.append('D:/repositorydef/SeismicRisk')
sys.path.append('C:/Users/AG/.qgis2/python/plugins/SeismicRisk/')
sys.path.append('C:/usbgis/apps/python27')

sys.path.append('D:/repositorydef/SeismicRisk/Logic2')
print(sys.path)
'''

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler


def escribirfecha():
    import datetime
    datetime_object = datetime.datetime.now()

    str_d = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    print(datetime_object)

    file = "D:/Bitnami/djangostack-2.2.5-0/apps/django/Scripts/servidor/out.txt"
    f = open(file, 'w+')
    out = ""
    out = str_d + "\n" + sys.path[0] + "\n version" + sys.version

    print("i will close the file")
    f.write(out)

    f.close()

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def escribirfecha(self):
        import datetime
        datetime_object = datetime.datetime.now()

        str_d = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        print(datetime_object)

        file = "D:/Bitnami/djangostack-2.2.5-0/apps/django/Scripts/servidor/out.txt"
        f = open(file, 'w+')
        out = ""
        out = str_d + "\n" + sys.path[0] + "\n version" + sys.version

        print("i will close the file")
        f.write(out)

        f.close()

    def do_GET(self):
        '''
        https://stackoverflow.com/questions/10607621/a-simple-website-with-python-using-simplehttpserver-and-socketserver-how-to-onl
        
        if self.path == '/':
            self.path = '/simplehttpwebpage_content.html'
        '''

        self.escribirfecha()

        from Logic2.HazardModel import Hazard

        Hazard.createEpicenter("7", "8.9", "8.7", "1", "1", "1")

        #D:\repositorydef\SeismicRisk\Logic2\PredictiveModel\PredictiveModel.py
        #C:/Users/AG/.qgis2/python/plugins/SeismicRisk/Logic2/PredictiveModel/

        print(sys.path)

        from Logic2.PredictiveModel import PredictiveModel

        PredictiveModel.populateValutazione("popoli")
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print ("serving at port", PORT)
print ("si sono qua", PORT)

#C:\Users\AG\.qgis2\python\plugins\SeismicRisk\SeismicRiskDockWidget.py

#D:\repositorydef\SeismicRisk\SeismicRiskDockWidget.py


print (sys.path)
'''
from datetime import datetime
now = datetime.now() # current date and time
#date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#print("date and time:",date_time)
out = ""

out = "".join("\ndate and time:").join(date_time)

out = out.join(sys.path)
'''

#import SeismicRiskDockWidget

escribirfecha()
httpd.serve_forever()
