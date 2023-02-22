from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QIcon 
from sys import argv, exit
def OurNewApp():
    app = QApplication(argv)
    window = QWidget()
    window.setWindowTitle("Sixth App")
    window.setGeometry(200,200,1000,468)
    button = QPushButton(window)
    button.setText("Subscribe To My Channel")
    button.setGeometry(10,10,300,36)
    button.setStyleSheet("""
                            QPushButton{
                                background:rgb(10,113,254);
                                color:#fff;
                                padding:3px;
                                line-height:30px;
                                font-size:18px;
                                outline:none;
                                border:none;
                                }
                            QPushButton:hover{
                                background:#000;
                            }
                        """)
    button.setToolTip("Youtube kanalıma abunə olun.")

    window.show()
    exit(app.exec_())
    


OurNewApp()