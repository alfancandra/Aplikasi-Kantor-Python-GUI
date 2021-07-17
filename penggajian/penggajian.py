

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from home import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel,QComboBox
from datetime import datetime

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
            """)
        mainLayout = QVBoxLayout()

        self.nama = QComboBox()
        self.bonus = QLineEdit()
        mainLayout.addWidget(self.nama)
        mainLayout.addWidget(self.bonus)

        self.bonus.setPlaceholderText('Bonus')

        self.saveButton = QPushButton('Simpan')
        self.saveButton.clicked.connect(self.simpanPenggajian)
        self.saveButton.clicked.connect(self.close)
        mainLayout.addWidget(self.saveButton)

        self.setLayout(mainLayout)
        try:
            
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="kantor"

            )

            mycursor = mydb.cursor()
            query = "SELECT * FROM pegawai"
            mycursor.execute(query)
            result = mycursor.fetchall()
            
        except mc.Error as e:
            print('gagal')
        self.names =[]
        for i in result:
            self.names.append(i[1])
            self.nama.addItem(i[1])
        
        print(self.names)

    def displayInfo(self):
        self.show()

    def simpanPenggajian(self):
        try:
            nama2 = str(self.nama.currentText())
            bonus = self.bonus.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="kantor"

            )

            mycursor = mydb.cursor()
            cekpegawai = "SELECT * FROM pegawai WHERE nama_pegawai = %s"
            values = (nama2,)
            mycursor.execute(cekpegawai,values)
            result = mycursor.fetchall()
            for i in result:
                id_pegawainya = i[0]
            print(id_pegawainya)
            now = datetime.now()
            datenow = now.strftime("%Y-%m-%d")
            print(datenow)
            query = "INSERT INTO penggajian (id_pegawai,bonus,tanggal) VALUES (%s,%s,%s)"
            value = (id_pegawainya,bonus,datenow)
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
            """)
        mainLayout = QVBoxLayout()

        self.inputid = QLineEdit()
        self.input1 = QLineEdit()
        self.input2 = QComboBox()
        self.input3 = QLineEdit()
        mainLayout.addWidget(self.inputid)
        mainLayout.addWidget(self.input1)
        mainLayout.addWidget(self.input2)
        mainLayout.addWidget(self.input3)

        self.inputid.setEnabled(False)

        self.saveButton = QPushButton('Simpan')
        self.saveButton.clicked.connect(self.simpanData)
        self.saveButton.clicked.connect(self.close)
        mainLayout.addWidget(self.saveButton)

        self.setLayout(mainLayout)

        try:
            
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="kantor"

            )

            mycursor = mydb.cursor()
            query = "SELECT * FROM jabatan"
            mycursor.execute(query)
            result = mycursor.fetchall()

        except mc.Error as e:
            print('gagal')
        self.names =[]
        for i in result:
            self.names.append(i[1])
            self.input2.addItem(i[1])
        print(self.names)

    def displayInfo(self):
        self.show()

    def simpanData(self):
        try:
            id_pegawai = self.inputid.text()
            nama = self.input1.text()
            jabatan2 = str(self.input2.currentText())
            alamat = self.input3.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="kantor"

            )

            mycursor = mydb.cursor()
            cekjabatan = "SELECT * FROM jabatan WHERE jabatan = %s"
            values = (jabatan2,)
            mycursor.execute(cekjabatan,values)
            result = mycursor.fetchall()
            for i in result:
                id_jabatannya = i[0]
            print(id_jabatannya)
            query = """UPDATE pegawai SET nama_pegawai = %s, id_jabatan = %s, alamat = %s WHERE id = %s"""
            value = (nama,id_jabatannya,alamat,id_pegawai)
            mycursor.execute(query,value)
            mydb.commit()
        except mc.Error as e:
            print('gagal')

class Penggajian(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(746, 561)
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
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(['id','Nama', 'Jabatan', 'Gaji','Bonus','Tanggal'])
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

        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setText('DATA GAJI')
        self.label2.setGeometry(QtCore.QRect(300, 80, 101, 31))
        self.label2.setFont(QtGui.QFont('Arial', 20))
        self.label2.setObjectName("label2")
        self.label2.adjustSize()

        self.buttonKembali = QtWidgets.QPushButton(Form)
        self.buttonKembali.setGeometry(QtCore.QRect(20, 80, 101, 31))
        self.buttonKembali.setObjectName("buttonKembali")
        self.buttonKembali.clicked.connect(Form.close)

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
        mycursor.execute("SELECT penggajian.id,pegawai.nama_pegawai,jabatan.jabatan,gaji.gaji,penggajian.bonus,penggajian.tanggal FROM penggajian inner join pegawai on penggajian.id_pegawai = pegawai.id inner join jabatan on pegawai.id_jabatan = jabatan.id inner join gaji on jabatan.id_gaji = gaji.id")
        
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
            thing2 = self.tableWidget.item(row,3)
            if thing is not None or thing1 is not None or thing2 is not None and thing.text() != '':
                currentid = (self.tableWidget.item(row, 0).text() )
                currentNama = (self.tableWidget.item(row, 1).text() )
                currentAlamat = (self.tableWidget.item(row, 3).text() )
                self.updateWindow.inputid.setText(currentid)
                self.updateWindow.input1.setText(currentNama)
                self.updateWindow.input3.setText(currentAlamat)
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
        mycursor.execute("SELECT penggajian.id,pegawai.nama_pegawai,jabatan.jabatan,gaji.gaji,penggajian.bonus,penggajian.tanggal FROM penggajian inner join pegawai on penggajian.id_pegawai = pegawai.id inner join jabatan on pegawai.id_jabatan = jabatan.id inner join gaji on jabatan.id_gaji = gaji.id")
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
            thing2 = self.tableWidget.item(row,3)
            if thing is not None or thing1 is not None or thing2 is not None and thing.text() != '':
                currentid = (self.tableWidget.item(row, 0).text() )
                mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="kantor"
                )

                mycursor = mydb.cursor()
                query = "DELETE FROM penggajian WHERE id=%s"
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
        self.pushButton.setText(_translate("Form", "Tambah"))
        self.hapusButton.setText(_translate("Form", "Hapus"))
        self.refreshButton.setText(_translate("Form", "Refresh"))
        self.buttonKembali.setText(_translate("Form", "Kembali"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Penggajian()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
