
def exportToXLS(filenamein, filenameout):
    import glob, csv, xlwt, os
    wb = xlwt.Workbook()

    #filename = "D:\Data\Python\export\\fragilities2.txt"

    f_short_name = "Sheet1.xls"
    ws = wb.add_sheet(f_short_name)
    #spamReader = csv.reader(open(filenamein, 'rb'))

    spamReader = csv.reader(x.replace('\0', '') for x in filenamein)

    for rowx, row in enumerate(spamReader):
        for colx, value in enumerate(row):
            ws.write(rowx, colx, value)

    #wb.save("D:\Data\Python\export\\fragilities2.xls")
    wb.save(filenameout)

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