class Writes():


    def readFile(self, filename):

        content = ""

        try:

        # filename = "C:/Data/Python/archivometodologia.txt"
            if (filename != ""):
                infile = open(filename, "r")
                lines = infile.readlines()
                infile.close()

                # self.tableViewMethodology.setRowCount(len(lines))
                # self.tableViewMethodology.setColumnCount(3)
                content = lines[0]
        except:
            content = ""


        return str(content)


    def writefile(self, filename, content ):

        out_file = open(filename, "w")
        if (filename != ""):

            infile = open(filename, "r")
            lines = infile.readlines()
            infile.close()

            try:

                out_file.write(content)

            except:
                print ""

        out_file.close()