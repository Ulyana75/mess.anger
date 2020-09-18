import sys

from PyQt5 import QtWidgets, QtCore

from ui_classes.authorize_class import Authorize
from ui_classes.chats_class import Chats
from ui_classes.register_class import Register
from ui_classes.single_chat_class import SingleChat


# Class for changing windows

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, url):
        super().__init__()

        self.url = url

        self.authorizeWindow = Authorize(self.url)
        self.registerWindow = Register(self.url)
        self.chatsWindow = Chats(self.url)
        self.singleChatWindow = SingleChat(self.url)

        self.chatsWindow.listWidget.itemClicked.connect(self.open_single_chat)
        self.chatsWindow.listWidget.itemClicked.connect(self.chatsWindow.close)

        self.chatsWindow.button_exit.clicked.connect(self.show_authorize_window)
        self.chatsWindow.button_exit.clicked.connect(self.chatsWindow.close)

    def show_authorize_window(self):
        if self.registerWindow.success_register:
            self.authorizeWindow.label_success_register.show()
        else:
            self.authorizeWindow.label_success_register.hide()

        self.authorizeWindow.button_register.clicked.connect(self.show_register_window)
        self.authorizeWindow.button_register.clicked.connect(self.authorizeWindow.close)

        self.authorizeWindow.button_enter.clicked.connect(self.show_chats_window)

        self.authorizeWindow.label_wrong_username.hide()
        self.authorizeWindow.label_wrong_password.hide()

        self.authorizeWindow.show()

    def show_register_window(self):
        self.registerWindow.show()
        self.registerWindow.label_username_exists.hide()
        self.registerWindow.label_wrong_confirm.hide()
        self.registerWindow.clear_fields()
        self.registerWindow.button_register_back.clicked.connect(self.show_authorize_window)
        self.registerWindow.button_register_back.clicked.connect(self.registerWindow.close)

    def show_chats_window(self):
        if self.authorizeWindow.enter_button_pressed():
            self.chatsWindow.show()
            self.chatsWindow.show_chats()
            self.authorizeWindow.close()

    def open_single_chat(self, item):
        widget = self.chatsWindow.listWidget.itemWidget(item)
        for i in widget.children():
            if i.objectName() == "username":
                self.singleChatWindow.show()
                self.singleChatWindow.messages_browser.clear()
                self.singleChatWindow.after_timestamp = -1
                self.singleChatWindow.label_dialog_with.setText("Диалог с " + i.text())
                self.singleChatWindow.dialog_with = i.text()
                self.singleChatWindow.show_messages()
                self.chatsWindow.clear_list()
                self.singleChatWindow.button_back.clicked.connect(self.show_chats_window)
                self.singleChatWindow.button_back.clicked.connect(self.singleChatWindow.close)
                self.singleChatWindow.button_back.clicked.connect(self.singleChatWindow.timer.stop)
                self.singleChatWindow.timer.start(1000)
                break


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow("https://myserverlol.herokuapp.com")
    window.show_authorize_window()
    sys.exit(app.exec_())
