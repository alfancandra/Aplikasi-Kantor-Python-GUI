# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import mysql.connector as mc
from home import *

class Login(object):
    def koneksi(self):
        con = pymysql.connect(db='kantor', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        if(cur):
            self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
            self.messagebox("Koneksi", "Koneksi Gagal")

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(746, 561)
        Form.setFixedSize(746,561)
        Form.setStyleSheet("#Form{border-image:url(images/bg.jpg)}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:white}")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(120, 140, 461, 271))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(120, 100, 211, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(120, 150, 211, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(120, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setObjectName("label_3")
        self.loginButton = QtWidgets.QPushButton(self.groupBox)
        self.loginButton.setGeometry(QtCore.QRect(190, 190, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login)

        font2 = QtGui.QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(60)

        
        self.label_2.setFont(font2)
        self.label_3.setFont(font2)
        self.label_2.setStyleSheet("QLabel{color:white}")
        self.label_3.setStyleSheet("QLabel{color:white}")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def login(self):
        try:
            username = self.username.text()
            password = self.password.text()

            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="kantor"

            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT username,password from users where username like '"+username + "'and password like '"+password+"'")
            result = mycursor.fetchone()

            if result == None:
                self.messagebox("Login", "Username atau password salah")

            else:
                self.Form = QtWidgets.QDialog()
                self.ui = Home()
                self.ui.setupUi(self.Form)
                self.Form.show()
                Form.hide()

                
        except mc.Error as e:
            self.labelResult.setText("Error")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "LOGIN"))
        self.label_2.setText(_translate("Form", "Username"))
        self.label_3.setText(_translate("Form", "Password"))
        self.loginButton.setText(_translate("Form", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

