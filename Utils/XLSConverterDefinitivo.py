#https://stackoverflow.com/questions/19677104/convert-text-files-to-excel-files-using-python

# mypath should be the complete path for the directory containing the input text files
#mypath = raw_input("Please enter the directory path for the input files: ")

def convertToXLS(myfullpathfile):




    from os import listdir
    from os.path import isfile, join
    #textfiles = [ join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f)) and '.txt' in  f]

    #textfiles = [ mypath + "fragilities.txt" ]myfullpathfile

    textfiles = [myfullpathfile]
    def is_number(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    import xlwt
    import xlrd

    style = xlwt.XFStyle()
    #style.num_format_str = '#,###0.00'

    style.num_format_str = '0'

    for textfile in textfiles:
        f = open(textfile, 'r+')
        row_list = []
        for row in f:
            row_list.append(row.split('|'))
        column_list = zip(*row_list)
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Sheet1')
        i = 0
        for column in column_list:
            for item in range(len(column)):
                value = column[item].strip()


                if is_number(value):
                    worksheet.write(item, i, float(value), style=style)
                else:
                    worksheet.write(item, i, value)
            i+=1
        workbook.save(textfile.replace('.txt', '.xls'))






#https://stackoverflow.com/questions/24969274/converting-xls-file-into-csv-txt-file-in-python
def xls_to_csv(mypath):
    import xlrd
    import csv

    x =  xlrd.open_workbook(mypath)
    x1 = x.sheet_by_name('Sheet1')
    csvfile = open('data.csv', 'wb')
    writecsv = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    for rownum in xrange(x1.nrows): #To determine the total rows.
        writecsv.writerow(x1.row_values(rownum))

    csvfile.close()

'''


mypath = "C:/Data/Python/workspace2/"

myfullpathfile = mypath + "fragilities.txt"
convertToXLS(myfullpathfile)
'''
