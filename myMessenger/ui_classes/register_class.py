from PyQt5.QtWidgets import QLineEdit

from ui.register import Ui_RegisterWindow
from PyQt5 import QtWidgets
import requests
import re
import utilits.constants
from ui_classes.error_dialog_class import Error

username_pattern = r'[\w\d\s\.\-_"@#$&!?%+,=<>/;]+'
password_pattern = r'[\w\d\.\-_@#$&!?%+,=<>/;]+'


class Register(Ui_RegisterWindow, QtWidgets.QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(utilits.constants.window_width, utilits.constants.window_height)

        self.label_username_exists.hide()
        self.label_wrong_confirm.hide()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_confirm_password.setEchoMode(QLineEdit.Password)

        self.url = url
        self.error_dialog = Error()
        self.success_register = False

        self.button_register.pressed.connect(self.register_button_pressed)

    def register_button_pressed(self):
        self.label_username_exists.hide()
        self.label_wrong_confirm.hide()

        if not self.check_fields():
            return

        if self.input_password.text() == self.input_confirm_password.text():
            register_info = {
                'username': self.input_username.text(),
                'password': self.input_password.text()
            }

            try:
                response = requests.post(self.url + '/register', json=register_info)
                if response.status_code != 200:
                    self.error_dialog.show()
                    return

                if response.json()['error']:
                    self.label_username_exists.setText("Такое имя пользователя уже существует")
                    self.label_username_exists.show()
                    self.success_register = False
                else:
                    self.success_register = True
                    self.clear_fields()
                    self.button_register_back.click()
            except:
                self.error_dialog.show()

        else:
            self.label_wrong_confirm.setText("Введенные пароли не совпадают")
            self.label_wrong_confirm.show()
            self.success_register = False

    def clear_fields(self):
        self.input_username.setText("")
        self.input_password.setText("")
        self.input_confirm_password.setText("")

    def check_fields(self):
        usrnm = re.findall(username_pattern, self.input_username.text(), re.IGNORECASE)
        psswd = re.findall(password_pattern, self.input_password.text(), re.IGNORECASE)

        if not (len(usrnm) > 0 and usrnm[0] == self.input_username.text()):
            self.label_username_exists.setText("Использованы недопустимые символы")
            self.label_username_exists.show()
            return False

        if not (len(psswd) > 0 and psswd[0] == self.input_password.text()):
            self.label_wrong_confirm.setText("Использованы недопустимые символы")
            self.label_wrong_confirm.show()
            return False

        if len(self.input_username.text()) < 1 or len(self.input_username.text()) > 20:
            self.label_username_exists.setText("Неверная длина. Допустимая длина 1-20")
            self.label_username_exists.show()
            return False

        if len(self.input_password.text()) < 8 or len(self.input_password.text()) > 32:
            self.label_wrong_confirm.setText("Неверная длина. Допустимая длина 8-32")
            self.label_wrong_confirm.show()
            return False

        return True
