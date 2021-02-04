import csv
with open('C:/Data/Popoli/valutazione.cvs', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t') #my example uses the tab as delimiter
    for line in reader
        print '; '.join(line)

#execfile("D:/usbgis/apps/qgis2/qgisconfig/python/plugins/PruebaAutoFields/Otros/readcvs.py")