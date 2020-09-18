from PyQt5 import QtWidgets
import requests

from PyQt5.QtWidgets import QLineEdit

from ui.authorize import Ui_AuthorizeWindow
import utilits.constants
from ui_classes.error_dialog_class import Error


class Authorize(Ui_AuthorizeWindow, QtWidgets.QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(utilits.constants.window_width, utilits.constants.window_height)

        self.label_success_register.hide()
        self.label_wrong_password.hide()
        self.label_wrong_username.hide()

        self.input_password.setEchoMode(QLineEdit.Password)

        self.url = url
        self.error_dialog = Error()

    def enter_button_pressed(self):

        authorize_info = {
            'username': self.input_username.text(),
            'password': self.input_password.text()
        }

        try:
            response = requests.post(self.url + '/authorize', json=authorize_info)

            if response.status_code != 200:
                self.error_dialog.show()
                return False

            if not response.json()['error']:
                utilits.constants.current_username = authorize_info['username']
                return True

            if response.json()['error'] == 'no such username':
                self.label_wrong_username.show()

            if response.json()['error'] == 'wrong password':
                self.label_wrong_password.show()
        except:
            self.error_dialog.show()
        return False
