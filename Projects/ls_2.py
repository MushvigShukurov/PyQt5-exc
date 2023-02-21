import sys
from PyQt5 import QtWidgets

def OurWindow():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Second App")
    # Position
    """
        Birinci və ikinci parametr 200, 200 - Açılan pəncərənin sol yuxarı küncünün
        dayandığı kordinatlardır deyə bilərik
        ---------------------------------------------------------------------------
        Üçüncü və dördüncü parametrlər isə uyğun olaraq pəncərənin soldan-sağa uzunluğu və
        yuxarıdan aşağıya enidir.
    """
    window.setGeometry(200,200,1000,768)
    window.show()
    sys.exit(app.exec_())

OurWindow()