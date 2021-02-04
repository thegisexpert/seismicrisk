import xlrd
#uri = 'path_to_the_file/test.xlsx'
uri = "C:/Data/datos_hazard.xls"
workbook = xlrd.open_workbook(uri)
wrksht1 = workbook.sheet_by_index(0)  #assuming you mean the first sheet in Excel

offset = 0   #set to 1 if there's 1 header line
rows = []
for i, row in enumerate(range(wrksht1.nrows)):
    if i <= offset: continue
    r = []
    try:
        r.append(wrksht1.cell_value(i, 0))   #First column
        r.append(wrksht1.cell_value(i, 1))   #Second column
        r.append(wrksht1.cell_value(i, 2))   #Third column
        rows.append(r)

        print rows
    except ValueError:
        pass

xlsxDict = {}  #Dictionary to store your excel data
for aRow in rows:
    try:
        xlsxDict[aRow[0]]=[aRow[1], aRow[2]]  #first column is key, 2nd/3rd columns are the values
    except:
        raise
print len(xlsxDict.keys())