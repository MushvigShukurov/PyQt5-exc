import sys
from PyQt5 import QtWidgets

def OurWindow():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("First App")
    window.show()
    sys.exit(app.exec_())

OurWindow()
