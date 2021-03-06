# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\authorize.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthorizeWindow(object):
    def setupUi(self, AuthorizeWindow):
        AuthorizeWindow.setObjectName("AuthorizeWindow")
        AuthorizeWindow.resize(636, 761)
        font = QtGui.QFont()
        font.setPointSize(20)
        AuthorizeWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(AuthorizeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_welcome = QtWidgets.QLabel(self.centralwidget)
        self.label_welcome.setGeometry(QtCore.QRect(60, 130, 561, 91))
        self.label_welcome.setObjectName("label_welcome")
        self.input_username = QtWidgets.QLineEdit(self.centralwidget)
        self.input_username.setGeometry(QtCore.QRect(250, 271, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_username.setFont(font)
        self.input_username.setObjectName("input_username")
        self.input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_password.setGeometry(QtCore.QRect(250, 360, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_password.setFont(font)
        self.input_password.setObjectName("input_password")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(20, 280, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(20, 370, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(250, 447, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_enter.setFont(font)
        self.button_enter.setObjectName("button_enter")
        self.button_register = QtWidgets.QPushButton(self.centralwidget)
        self.button_register.setGeometry(QtCore.QRect(250, 530, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_register.setFont(font)
        self.button_register.setObjectName("button_register")
        self.label_success_register = QtWidgets.QLabel(self.centralwidget)
        self.label_success_register.setGeometry(QtCore.QRect(110, 610, 561, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_success_register.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_success_register.setFont(font)
        self.label_success_register.setObjectName("label_success_register")
        self.label_wrong_username = QtWidgets.QLabel(self.centralwidget)
        self.label_wrong_username.setGeometry(QtCore.QRect(250, 250, 271, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_wrong_username.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_wrong_username.setFont(font)
        self.label_wrong_username.setAutoFillBackground(False)
        self.label_wrong_username.setObjectName("label_wrong_username")
        self.label_wrong_password = QtWidgets.QLabel(self.centralwidget)
        self.label_wrong_password.setGeometry(QtCore.QRect(250, 410, 271, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_wrong_password.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_wrong_password.setFont(font)
        self.label_wrong_password.setAutoFillBackground(False)
        self.label_wrong_password.setObjectName("label_wrong_password")
        AuthorizeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AuthorizeWindow)
        self.statusbar.setObjectName("statusbar")
        AuthorizeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthorizeWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthorizeWindow)

    def retranslateUi(self, AuthorizeWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthorizeWindow.setWindowTitle(_translate("AuthorizeWindow", "Authorization"))
        self.label_welcome.setText(_translate("AuthorizeWindow", "Добро пожаловать в Mess.anger"))
        self.input_username.setPlaceholderText(_translate("AuthorizeWindow", "username"))
        self.input_password.setPlaceholderText(_translate("AuthorizeWindow", "password"))
        self.label_username.setText(_translate("AuthorizeWindow", "Имя пользователя"))
        self.label_password.setText(_translate("AuthorizeWindow", "Пароль"))
        self.button_enter.setText(_translate("AuthorizeWindow", "Войти"))
        self.button_register.setText(_translate("AuthorizeWindow", "Зарегестрироваться"))
        self.label_success_register.setText(_translate("AuthorizeWindow", "Регистрация прошла успешно!"))
        self.label_wrong_username.setText(_translate("AuthorizeWindow", "Пользователя с таким именем не существует"))
        self.label_wrong_password.setText(_translate("AuthorizeWindow", "Неверный пароль"))
