from PyQt5 import QtWidgets

from ui.error import Ui_Dialog


class Error(Ui_Dialog, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
