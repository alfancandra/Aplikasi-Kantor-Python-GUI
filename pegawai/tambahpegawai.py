# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tambah-pegawai.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Tambah(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(406, 328)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 321, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.nama = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.nama.setObjectName("nama")
        self.horizontalLayout.addWidget(self.nama)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 60, 321, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.jabatan = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.jabatan.setObjectName("jabatan")
        self.horizontalLayout_3.addWidget(self.jabatan)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 100, 321, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.alamat = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.alamat.setObjectName("alamat")
        self.horizontalLayout_4.addWidget(self.alamat)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(40, 140, 321, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(40, 180, 321, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        
        
        self.simpan = QtWidgets.QPushButton(Form)
        self.simpan.setGeometry(QtCore.QRect(160, 280, 75, 23))
        self.simpan.setObjectName("simpan")
        self.simpan.clicked.connect(self.simpanpegawai)
        self.simpan.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

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
            self.jabatan.addItem(i[1])
        print(self.names)
    

    def simpanpegawai(self):
        try:
            nama = self.nama.text()
            jabatan2 = str(self.jabatan.currentText())
            alamat = self.alamat.text()
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
            query = "INSERT INTO pegawai (nama_pegawai,id_jabatan,alamat) VALUES (%s,%s,%s)"
            value = (nama,id_jabatannya,alamat)
            mycursor.execute(query,value)
            mydb.commit()
        except mc.Error as e:
            print('gagal')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tambah Pegawai"))
        self.label.setText(_translate("Form", "Nama    "))
        self.label_3.setText(_translate("Form", ":"))
        self.label_4.setText(_translate("Form", "Jabatan"))
        self.label_5.setText(_translate("Form", ":"))
        self.label_6.setText(_translate("Form", "Alamat  "))
        self.label_7.setText(_translate("Form", ":"))
        
        self.simpan.setText(_translate("Form", "Simpan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Tambah()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())