
def readFile(filename):

    #filename = "C:/Data/Python/archivometodologia.txt"
    if (filename != ""):
        infile = open(filename ,"r")
        lines = infile.readlines()
        infile.close()

        #self.tableViewMethodology.setRowCount(len(lines))
        #self.tableViewMethodology.setColumnCount(3)


    return lines

def readFileAsString(filename):
    contentsbeforestr = readFile(filename)

    contentsbefore =""

    for i in contentsbeforestr:
            contentsbefore = contentsbefore + i

    return contentsbefore


def writefile(filename, content ):

    out_file = open(filename, "w")
    if (filename != ""):

        infile = open(filename, "r")
        lines = infile.readlines()
        infile.close()

        try:

            out_file.write(content)

        except:
            print (" not possible to write the file ")

    out_file.close()