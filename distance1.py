from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def timeCheck(self):
        if (len(self.lineEdit.text())==0) and (len(self.lineEdit_2.text())==0) and (len(self.lineEdit_3.text())==0):
            print("podaj czas")
        else:
            if self.radioButton_6.isChecked():
                h = self.lineEdit.text()
                m = self.lineEdit_2.text()
                s = self.lineEdit_3.text()
                print(h,":",m,":",s)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.distance = QtWidgets.QListWidget(self.centralwidget)
        self.distance.setGeometry(QtCore.QRect(90, 80, 121, 192))
        self.distance.setObjectName("distance")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(110, 120, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 150, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 180, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(110, 210, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(110, 240, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(110, 90, 82, 17))
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 101, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        #########
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 290, 111, 31))
        self.pushButton.setObjectName("pushButton")
        ###Evenet to przelicz button###
        self.pushButton.clicked.connect(self.timeCheck)
        ######
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 101, 31))
        self.label_2.setObjectName("label_2")
        ###
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 110, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 140, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 70, 31, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 100, 31, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 130, 31, 31))
        self.label_5.setObjectName("label_5")
        ###
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "3 km"))
        self.radioButton_2.setText(_translate("MainWindow", "5 km"))
        self.radioButton_3.setText(_translate("MainWindow", "10 km"))
        self.radioButton_4.setText(_translate("MainWindow", "21,097 km"))
        self.radioButton_5.setText(_translate("MainWindow", "42,195 km"))
        self.radioButton_6.setText(_translate("MainWindow", "1 km"))
        self.label.setText(_translate("MainWindow", "Czas:"))
        self.pushButton.setText(_translate("MainWindow", "Przelicz"))
        self.label_2.setText(_translate("MainWindow", "Dystans:"))
        self.label_3.setText(_translate("MainWindow", "Godziny:"))
        self.label_4.setText(_translate("MainWindow", "Minuty:"))
        self.label_5.setText(_translate("MainWindow", "Sekundy:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

