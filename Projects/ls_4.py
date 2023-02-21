import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
BASE_DIR = os.getcwd()

def OurApp():
    app = QtWidgets.QApplication(sys.argv)

    t_window = QtWidgets.QWidget()
    t_window.setWindowTitle("Third App")
    t_window.setGeometry(200,200,1000,768)
    full_path = os.path.join(BASE_DIR,"Projects","Images","scooby-doo.jpg")
    label_image = QtWidgets.QLabel(t_window)
    pix_map = QPixmap(full_path)
    # # set image size
    # label_image.setPixmap(pix_map)    
    # label_image.resize(300,300)
    """
        Şəkil 300-300 pəncərəyə sığması üçün contain olmalıdır
        Bunun üçün 15,16,17 sətirləri şərh sətrinə çevirdim
        23, 24 -ü əlavə etdim.
    """
    pix_map = pix_map.scaled(300,300)
    label_image.setPixmap(pix_map)    


    t_window.show()
    sys.exit(app.exec_())

OurApp()