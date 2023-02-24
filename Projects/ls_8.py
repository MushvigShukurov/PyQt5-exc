from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from sys import argv, exit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1000,800)
        self.start()
        
    def start(self):
        self.input = QtWidgets.QLineEdit()
        self.clear = QtWidgets.QPushButton("Təmizlə")
        self.type = QtWidgets.QPushButton("Yaz")
        
        v_layout = QtWidgets.QVBoxLayout(self)

        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.input)
        h_layout.addWidget(self.clear)
        h_layout.addWidget(self.type)

        v_layout.addLayout(h_layout)
        v_layout.addStretch()

        self.show()

    

app = QApplication(argv)
window = Window()
exit(app.exec_())