import xlrd

from xlwt import Workbook, Formula

path = r"D:\Data\Python\export\fichier.xls"


classeur = Workbook()
# On ajoute une feuille au classeur
feuille = classeur.add_sheet("OCB")

feuille.write(0, 0, 1)
feuille.write(0, 1, 2)
feuille.write(0, 2, Formula('A1+B1'))

classeur.save(path)

print u"Fichier cree: {}".format(path)


'''
import glob, csv, xlwt, os
wb = xlwt.Workbook()
for filename in glob.glob("c:/xxx/*.csv"):
    (f_path, f_name) = os.path.split(filename)
    (f_short_name, f_extension) = os.path.splitext(f_name)
    ws = wb.add_sheet(f_short_name)
    spamReader = csv.reader(open(filename, 'rb'))
    for rowx, row in enumerate(spamReader):
        for colx, value in enumerate(row):
            ws.write(rowx, colx, value)
wb.save("c:/xxx/compiled.xls")
'''