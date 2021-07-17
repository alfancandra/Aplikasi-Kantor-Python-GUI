

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from pegawai.tambahpegawai import *
from home import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel,QComboBox,QSpinBox

class TambahWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('second window')
        self.setFixedWidth(500)
        self.setStyleSheet("""
            QLineEdit{
                font-size: 30px
            }
            QPushButton{
                font-size: 30px
            }
            QComboBox{
                font-size: 30px
            }
            QSpinBox{
                font-size: 30px
            }
            """)
        mainLayout = QVBoxLayout()

        self.gaji = QSpinBox()
        mainLayout.addWidget(self.gaji)
        self.gaji.setMaximum(999999999)

        self.saveButton = QPushButton('Simpan')
        self.saveButton.clicked.connect(self.simpangaji)
        self.saveButton.clicked.connect(self.close)
        mainLayout.addWidget(self.saveButton)

        self.setLayout(mainLayout)
        

    def displayInfo(self):
        self.show()

    def simpangaji(self):
        try:
            gaji = self.gaji.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="kantor"

            )

            mycursor = mydb.cursor()
            query = "INSERT INTO gaji (gaji) VALUES (%s)"
            value = (gaji,)
            mycursor.execute(query,value)
            mydb.commit()
        except mc.Error as e:
            print('gagal')

class UpdateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('second window')
        self.setFixedWidth(500)
        self.setStyleSheet("""
            QLineEdit{
                font-size: 30px
            }
            QPushButton{
                font-size: 30px
            }
            QComboBox{
                font-size: 30px
            }
            QSpinBox{
                font-size: 30px
            }
            """)
        mainLayout = QVBoxLayout()

        self.inputid = QLineEdit()
        self.gaji = QSpinBox()
        mainLayout.addWidget(self.inputid)
        mainLayout.addWidget(self.gaji)

        self.gaji.setMaximum(999999999)

        self.inputid.setEnabled(False)

        self.saveButton = QPushButton('Simpan')
        self.saveButton.clicked.connect(self.simpanData)
        self.saveButton.clicked.connect(self.close)
        mainLayout.addWidget(self.saveButton)

        self.setLayout(mainLayout)


    def displayInfo(self):
        self.show()

    def simpanData(self):
        try:
            id_gaji = self.inputid.text()
            gaji = self.gaji.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="kantor"

            )

            mycursor = mydb.cursor()
            
            query = """UPDATE gaji SET gaji = %s WHERE id = %s"""
            value = (gaji,id_gaji)
            mycursor.execute(query,value)
            mydb.commit()
        except mc.Error as e:
            print('gagal')

class Gaji(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(746, 561)
        self.updateWindow = UpdateWindow()
        self.tambahWindow = TambahWindow()
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 701, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 160, 701, 381))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget_4)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(['id','Gaji'])
        self.horizontalLayout_7.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(620, 122, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tambah)
        self.hapusButton = QtWidgets.QPushButton(Form)
        self.hapusButton.setGeometry(QtCore.QRect(20, 122, 101, 31))
        self.hapusButton.setObjectName("hapusButton")
        self.hapusButton.clicked.connect(self.hapus)
        self.hapusButton.clicked.connect(self.selectData)
        self.refreshButton = QtWidgets.QPushButton(Form)
        self.refreshButton.setGeometry(QtCore.QRect(320, 122, 101, 31))
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(self.selectData)

        self.updatebutton = QtWidgets.QPushButton(Form)
        self.updatebutton.setGeometry(QtCore.QRect(150, 122, 101, 31))
        self.updatebutton.setObjectName("updatebutton")
        self.updatebutton.clicked.connect(self.updatedata)

        self.buttonKembali = QtWidgets.QPushButton(Form)
        self.buttonKembali.setGeometry(QtCore.QRect(20, 80, 101, 31))
        self.buttonKembali.setObjectName("buttonKembali")
        self.buttonKembali.clicked.connect(Form.close)

        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setText('DATA JABATAN')
        self.label2.setGeometry(QtCore.QRect(280, 80, 101, 31))
        self.label2.setFont(QtGui.QFont('Arial', 20))
        self.label2.setObjectName("label2")
        self.label2.adjustSize()

        QtCore.QTimer.singleShot(10000, self.selectData)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # retrieve data
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="kantor"

        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT gaji.id,gaji.gaji FROM gaji")
        result = mycursor.fetchall()
        self.tableWidget.setRowCount(0)

        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        # close 

    def kehome(self):
        self.FormHome = QtWidgets.QDialog()
        self.ui = Home()
        self.ui.setupUi(self.FormHome)
        self.FormHome.show()

    def updatedata(self):
        try:
            row = self.tableWidget.currentRow()
            thing = self.tableWidget.item(row,0)
            thing1 = self.tableWidget.item(row,1)
            if thing is not None or thing1 is not None or thing2 is not None and thing.text() != '':
                currentid = (self.tableWidget.item(row, 0).text() )
                currentGaji = (self.tableWidget.item(row, 1).text() )
                self.updateWindow.inputid.setText(currentid)
                self.updateWindow.gaji.setValue(int(currentGaji))
                self.updateWindow.displayInfo()
            
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass
        

    def tambah(self):
        self.tambahWindow.displayInfo()

    def selectData(self):
        # retrieve data
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="kantor"

        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT gaji.id,gaji.gaji FROM gaji")
        result = mycursor.fetchall()
        self.tableWidget.setRowCount(0)

        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        # close 
    def hapus(self):
        
        try:
            row = self.tableWidget.currentRow()
            thing = self.tableWidget.item(row,0)
            thing1 = self.tableWidget.item(row,1)
            if thing is not None or thing1 is not None or thing2 is not None and thing.text() != '':
                currentid = (self.tableWidget.item(row, 0).text() )
                mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="kantor"
                )

                mycursor = mydb.cursor()
                query = "DELETE FROM gaji WHERE id=%s"
                value = (currentid,)
                mycursor.execute(query,value)
                mydb.commit()
        except mc.Error as e:
            print('gagal')
            

    def pageTambah(self):
        self.Form2 = QtWidgets.QDialog()
        self.ui = Tambah()
        self.ui.setupUi(self.Form2)
        self.Form2.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PT. BEJO ABADI Tbk"))
        self.label2.setText(_translate("Form", "DATA GAJI"))
        self.pushButton.setText(_translate("Form", "Tambah"))
        self.hapusButton.setText(_translate("Form", "Hapus"))
        self.refreshButton.setText(_translate("Form", "Refresh"))
        self.updatebutton.setText(_translate("Form", "Update"))
        self.buttonKembali.setText(_translate("Form", "Kembali"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Gaji()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
