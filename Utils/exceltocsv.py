def convertXLS2CSV(aFile):
    '''converts a MS Excel file to csv w/ the same name in the same directory'''

    print "------ beginning to convert XLS to CSV ------"

    try:
        import win32com.client, os
        from win32com.client import constants as c
        excel = win32com.client.Dispatch('Excel.Application')

        fileDir, fileName = os.path.split(aFile)
        nameOnly = os.path.splitext(fileName)
        newName = nameOnly[0] + ".csv"
        outCSV = os.path.join(fileDir, newName)
        workbook = excel.Workbooks.Open(aFile)
        workbook.SaveAs(outCSV, c.xlCSVMSDOS) # 24 represents xlCSVMSDOS
        workbook.Close(False)
        excel.Quit()
        del excel

        print "...Converted " + nameOnly + " to CSV"
    except:
        print ">>>>>>> FAILED to convert " + aFile + " to CSV!"

filename = "D:\Data\Python\export\\fragilities2.xls"

convertXLS2CSV(filename)