class Table():
    def populateTable(self, tableWidgetParam ):
        self.tableWidget=tableWidgetParam
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)

        item = QTableWidgetItem("Cell (1,1)")
        item.setFlags(QtCore.Qt.ItemIsEnabled)

        item2 = QTableWidgetItem("Cell (1,2)")
        item2.setFlags(QtCore.Qt.ItemIsEnabled)

        item.setFlags(QtCore.Qt.ItemIsEnabled)

        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.setItem(0, 1, item2)
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,11)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,22)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,11)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,22)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,11)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,22)"))
        self.tableWidget.move(0, 0)
