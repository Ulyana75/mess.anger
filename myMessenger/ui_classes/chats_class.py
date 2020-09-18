import requests
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QListWidgetItem, QHBoxLayout, QWidget

from ui.chats import Ui_ChatsWindow
import utilits.constants
from ui_classes.error_dialog_class import Error


class Chats(Ui_ChatsWindow, QtWidgets.QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(utilits.constants.window_width, utilits.constants.window_height)

        self.label_wrong_username.hide()
        self.button_search_back.hide()

        self.url = url
        self.error_dialog = Error()

        self.button_search_user.clicked.connect(self.search_button_pressed)
        self.button_search_back.clicked.connect(self.show_chats)

    def show_chats(self):
        self.clear_list()
        try:
            response = requests.get(self.url + '/get_chats', params={'username': utilits.constants.current_username})
            if response.status_code != 200:
                self.error_dialog = Error()
                return
            chats = response.json()['chats']
            for i in chats:
                self.add_item_in_list_widget(i)
        except:
            self.error_dialog = Error()

    def search_button_pressed(self):
        self.listWidget.clear()
        self.button_search_back.show()

        search_info = {
            'username': self.input_search_username.text()
        }

        try:
            response = requests.get(self.url + '/search', json=search_info)

            if response.status_code != 200:
                self.error_dialog.show()
                return

            userdata = response.json()
            if 'error' not in userdata.keys():
                self.add_item_in_list_widget(self.input_search_username.text())
            else:
                self.label_wrong_username.show()
                self.button_search_back.show()
        except:
            self.error_dialog = Error()

    def add_item_in_list_widget(self, text):
        layout = QHBoxLayout()
        wdg = QWidget()

        font = QFont()
        font.setPointSize(12)

        label = QLabel(text)
        label.setObjectName("username")
        label.setFont(font)
        layout.addWidget(label)
        wdg.setLayout(layout)

        item = QListWidgetItem(self.listWidget)
        item.setSizeHint(wdg.sizeHint())
        self.listWidget.setItemWidget(item, wdg)
        self.listWidget.repaint()

    def clear_list(self):
        self.label_wrong_username.hide()
        self.button_search_back.hide()
        self.listWidget.clear()
        self.input_search_username.clear()
