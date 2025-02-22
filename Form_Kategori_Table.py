# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_Kategori_Table.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout1.setObjectName("verticalLayout1")

        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName("label1")

        self.verticalLayout1.addWidget(self.label1)

        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label2.setObjectName("label2")

        self.verticalLayout1.addWidget(self.label2)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 20, 331, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout2.setObjectName("verticalLayout2")

        self.lineEdit1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit1.setObjectName("lineEdit1")

        self.verticalLayout2.addWidget(self.lineEdit1)

        self.lineEdit2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit2.setObjectName("lineEdit2")

        self.verticalLayout2.addWidget(self.lineEdit2)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 170, 491, 181))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.verticalLayout3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout3.setObjectName("verticalLayout3")

        self.tableWidget1 = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(2)
        self.tableWidget1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget1.setHorizontalHeaderItem(1, item)
        self.verticalLayout3.addWidget(self.tableWidget1)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 501, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout1.setObjectName("horizontalLayout1")

        self.pushButtonDelete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonDelete.setObjectName("pushButtonDelete")

        self.horizontalLayout1.addWidget(self.pushButtonDelete)

        self.pushButtonUpdate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.horizontalLayout1.addWidget(self.pushButtonUpdate)


        self.pushButtonInsert = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonInsert.setObjectName("pushButtonInsert")
        self.horizontalLayout1.addWidget(self.pushButtonInsert)

        self.pushButtonLoad = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout1.addWidget(self.pushButtonLoad)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 360, 501, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")

        self.line3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.line3.setObjectName("line3")

        self.horizontalLayout2.addWidget(self.line3)
        self.pushButtonSearch = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.horizontalLayout2.addWidget(self.pushButtonSearch)

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(20, 146, 481, 20))
        self.label3.setObjectName("label3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #event
        self.pushButtonInsert.clicked.connect(self.deletekategori)
        self.pushButtonLoad.clicked.connect(self.loadkategori)
        self.pushButtonUpdate.clicked.connect(self.updatekategori)
        self.pushButtonDelete.clicked.connect(self.insertkategori)
        self.pushButtonSearch.clicked.connect(self.searchkategori)


    def insertkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                port=3307,
                database="db_penjualan"
            )

            cursor = mydb.cursor()
            idkat = self.lineEdit1.text()
            namekat = self.lineEdit2.text()

            sql = "INSERT INTO kategori (id,name) VALUES (%s,%s)"
            val = (idkat, namekat)
            cursor.execute(sql, val)
            mydb.commit()
            self.label3.setText("Data Kategori Berhasil Disimpan")

            self.lineEdit1.setText("")
            self.lineEdit2.setText("")
        except mc.Error as e:
            self.label3.setText("Data Kategori Gagal Disimpan")

    def updatekategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                port=3307,
                database="db_penjualan"
            )

            cursor = mydb.cursor()
            idkat = self.lineEdit1.text()
            namekat = self.lineEdit2.text()

            sql = "UPDATE kategori set name = %s where id = %s"
            val = (namekat, idkat)
            cursor.execute(sql, val)
            mydb.commit()
            self.label3.setText("Data Kategori Berhasil DiUpdate")

            self.lineEdit1.setText("")
            self.lineEdit2.setText("")
        except mc.Error as e:
            print(sql)
            self.label3.setText("Data Kategori Gagal DiUpdate")

    def deletekategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                port=3307,
                database="db_penjualan_visual"
            )

            cursor = mydb.cursor()
            idkat = self.lineEdit1.text()

            sql = "DELETE FROM kategori where id = %s"
            val = (idkat,)
            cursor.execute(sql, val)
            mydb.commit()

            self.label3.setText("Data Kategori Berhasil Dihapus")

            self.lineEdit1.setText("")
        except mc.Error as e:
            print(sql)
            self.label3.setText("Data Kategori Gagal DiHapus")

    def searchkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                port="3307",
                database="db_penjualan"
            )

            mycursor = mydb.cursor()
            namekat = self.line3.text()

            mycursor.execute(f"SELECT * from kategori where name like '{namekat}%' ")
            result = mycursor.fetchall()
            self.tableWidget1.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget1.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget1.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.label3.setText("Data Kategori Berhasil Ditampilkan")

        except mc.Error as err:
            self.label3.setText("Data Kategori Gagal DiLoad")


    def loadkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                port="3307",
                database="db_penjualan"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM kategori ORDER BY ID ASC")
            result = mycursor.fetchall()
            self.tableWidget1.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget1.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget1.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.label3.setText("Data Kategori Berhasil Ditampilkan")

        except mc.Error as err:
            self.label3.setText("Data Kategori Gagal DiLoad")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "ID"))
        self.label2.setText(_translate("MainWindow", "Kategori"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nama Kategori"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Insert"))
        self.pushButtonUpdate.setText(_translate("MainWindow", "Update"))
        self.pushButtonInsert.setText(_translate("MainWindow", "Delete"))
        self.pushButtonLoad.setText(_translate("MainWindow", "Load"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search"))
        self.label3.setText(_translate("MainWindow", "TextLabel"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())