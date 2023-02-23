from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from sys import argv, exit

def type_to_console():
    print("Hello World!")

def OurApp():
    app = QApplication(argv)
    window = QWidget()
    window.setWindowTitle("Seventh App")
    window.setGeometry(200,200,1000,468)

    button_1 = QtWidgets.QPushButton(window)
    button_2 = QtWidgets.QPushButton(window)

    button_1.setText("Print Hello")
    button_2.setText("Ele Bele")

    button_1.clicked.connect(type_to_console)

    
    h_layout = QtWidgets.QHBoxLayout()
    h_layout.addWidget(button_1)
    h_layout.addWidget(button_2)
    h_layout.addStretch()
    

    v_layout = QtWidgets.QVBoxLayout(window)
    v_layout.addLayout(h_layout)
    v_layout.addStretch()

    window.show()
    exit(app.exec_())

OurApp()