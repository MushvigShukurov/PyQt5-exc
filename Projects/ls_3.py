import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
"""
    Şəkil əlavə etmək üçün bir dənə label yaratdım
    Eyni zamanda QtGui -dan QPixmap-i import etməliyəm (sətir 3 də)
    ---------------------------------------------------------------
    Şəklin full path-ini tapmaq üçün sətir-1 də os modulunu əlavə
    etdim
    ---------------------------------------------------------------
    os.path.join() daxil etdiyimiz path-leri uyğun əməliyyat siste-
    minə görə birləşdirir
    (sətir-24)
"""
BASE_DIR = os.getcwd() # C:\Users\User\Desktop\Projects\PyQt5-exc

def OurApp():
    app = QtWidgets.QApplication(sys.argv)

    t_window = QtWidgets.QWidget()
    t_window.setWindowTitle("Third App")
    t_window.setGeometry(200,200,1000,768)
    # first label for image
    full_path = os.path.join(BASE_DIR,"Projects","Images","scooby-doo.jpg")
    label_image = QtWidgets.QLabel(t_window)
    label_image.setPixmap(QPixmap(full_path))


    t_window.show()
    sys.exit(app.exec_())

OurApp()