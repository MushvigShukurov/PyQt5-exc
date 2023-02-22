from PyQt5 import QtWidgets
from PyQt5 import QtCore
from sys import argv,exit
from PyQt5.QtGui import QFont

def OurApp():
    app = QtWidgets.QApplication(argv)
    app_window = QtWidgets.QWidget()
    app_window.setWindowTitle("Fifth App")
    app_window.setGeometry(100,100,1000,768)

    # text label
    label_text = QtWidgets.QLabel(app_window)
    label_text.setText("#codewithmushvig")

    label_text.setGeometry(10,10,980,50)
    label_text.setStyleSheet("""
                                background :black;color:rgb(10,113,254);
                                padding :10px;
                                border-top-left-radius :25px;
                                border-top-right-radius : 25px; 
                                border-bottom-left-radius : 25px; 
                                border-bottom-right-radius : 25px;
                            """)
    
    label_text.setAlignment(QtCore.Qt.AlignCenter)
    label_text.setFont(QFont('Times',15))


    app_window.show()
    exit(app.exec_())

OurApp()