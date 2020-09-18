from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore

from ui.single_chat import Ui_SingleChatWindow
import utilits.constants
from ui_classes.error_dialog_class import Error


class SingleChat(Ui_SingleChatWindow, QtWidgets.QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(utilits.constants.window_width, utilits.constants.window_height)

        self.url = url
        self.dialog_with = ''
        self.after_timestamp = -1
        self.error_dialog = Error()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)

        self.button_send.clicked.connect(self.send_message)

    def send_message(self):
        if len(self.input_message.toPlainText()) != 0:
            message_data = {
                'from': utilits.constants.current_username,
                'to': self.dialog_with,
                'text': self.input_message.toPlainText()
            }

            try:
                response = requests.post(self.url + '/send_message', json=message_data)

                if response.status_code == 200:
                    self.input_message.clear()
                else:
                    self.error_dialog.show()

            except:
                self.error_dialog.show()

    def update_messages(self):
        response = None

        data = {
            'user1': utilits.constants.current_username,
            'user2': self.dialog_with,
            'after_timestamp': self.after_timestamp
        }

        try:
            response = requests.get(self.url + '/get_messages', json=data)
            if response.status_code != 200:
                self.error_dialog.show()
                return
        except:
            self.error_dialog.show()

        if response and response.status_code == 200:
            messages = response.json()['messages']
            for message in messages:
                self.print_message(message)
                self.after_timestamp = message['timestamp']
            return messages

    def show_messages(self):
        while self.update_messages():
            pass

    def print_message(self, message):
        """
        15.09.2020 10:23:30 user
        Text

        """
        dt = datetime.fromtimestamp(message['timestamp'])
        dt = dt.strftime('%d.%m.%Y %H:%M:%S')

        if message['from'] == utilits.constants.current_username:
            font = '#800080'
        else:
            font = '#000080'

        self.messages_browser.append("<font color = " + font + ">" + dt + ' ' + '<b>' + message['from'] + "<\\font></b>")
        self.messages_browser.append(message['text'] + '\n')
