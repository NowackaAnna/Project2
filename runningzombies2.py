import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random
from PyQt5 import QtCore, QtGui, QtWidgets
import math
class Ui_Przewidywania(object):
    def nCzasT(self):
        h1 = self.godziny_1.text()
        m1 = self.minuty_1.text()
        s1 = self.sekundy_1.text()
        h1 = str(h1)
        m1 = str(m1)
        s1 = str(s1)
        h2 = self.godziny_2.text()
        m2 = self.minuty_2.text()
        s2 = self.sekundy_2.text()
        h2 = str(h2)
        m2 = str(m2)
        s2 = str(s2)
        h3 = self.godziny_3.text()
        m3 = self.minuty_3.text()
        s3 = self.sekundy_3.text()
        h3 = str(h3)
        m3 = str(m3)
        s3 = str(s3)
        try:
            int(h2)
            int(m2)
            int(s2)
            int(h2)
            int(m2)
            int(s2)
            int(h3)
            int(m3)
            int(s3)
            if ((float(h1)) >= 0 and (float(m1) in range(0, 60)) and (float(s1) in range(0, 60)) and (float(h2)) >= 0 and (float(m2) in range(0, 60)) and (float(s2) in range(0, 60)) and (float(h3)) >= 0 and (float(m3) in range(0, 60)) and (float(s3) in range(0, 60))):
                hpomoc = float(h1)*3600+ float(h2)*3600+float(h3)*3600
                mpomoc = float(m1)*60 + float(m2)*60 + float(m3)*60
                spomoc = float(s1)+float(s2)+float(s3)
                wspolczynnik = 6
                sr = (hpomoc + mpomoc + spomoc + wspolczynnik)/3
                hr = sr%3600
                hrezultat = (sr - hr)/3600
                mr = hr%60
                mrezultat = (hr-mr)/60
                srezultat = math.floor(mr)
                czas = "Przewidywany czas to: " + str(int(hrezultat)) + "h : " + str(int(mrezultat)) + "m : " + str(int(srezultat)) + "s \n"
                self.listWidget.clear()
                self.listWidget.addItem(czas)

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.listWidget.clear()
                self.listWidget.addItem(komunikat)

        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.listWidget.clear()
            self.listWidget.addItem(komunikat)



    def nCzasP(self):
        h1 = self.godziny_1.text()
        m1 = self.minuty_1.text()
        s1 = self.sekundy_1.text()
        h1 = str(h1)
        m1 = str(m1)
        s1 = str(s1)
        h2 = self.godziny_2.text()
        m2 = self.minuty_2.text()
        s2 = self.sekundy_2.text()
        h2 = str(h2)
        m2 = str(m2)
        s2 = str(s2)
        h3 = self.godziny_3.text()
        m3 = self.minuty_3.text()
        s3 = self.sekundy_3.text()
        h3 = str(h3)
        m3 = str(m3)
        s3 = str(s3)
        try:
            int(h2)
            int(m2)
            int(s2)
            int(h2)
            int(m2)
            int(s2)
            int(h3)
            int(m3)
            int(s3)
            if ((float(h1)) >= 0 and (float(m1) in range(0, 60)) and (float(s1) in range(0, 60)) and (float(h2)) >= 0 and (float(m2) in range(0, 60)) and (float(s2) in range(0, 60)) and (float(h3)) >= 0 and (float(m3) in range(0, 60)) and (float(s3) in range(0, 60))):
                hpomoc = float(h1)*3600+ float(h2)*3600+float(h3)*3600
                mpomoc = float(m1)*60 + float(m2)*60 + float(m3)*60
                spomoc = float(s1)+float(s2)+float(s3)
                wspolczynnik = 4
                sr = (hpomoc + mpomoc + spomoc + wspolczynnik)/3
                hr = sr%3600
                hrezultat = (sr - hr)/3600
                mr = hr%60
                mrezultat = (hr-mr)/60
                srezultat = math.floor(mr)
                czas = "Przewidywany czas to: " + str(int(hrezultat)) + "h : " + str(int(mrezultat)) + "m : " + str(int(srezultat)) + "s \n"
                self.listWidget.clear()
                self.listWidget.addItem(czas)

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.listWidget.clear()
                self.listWidget.addItem(komunikat)

        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.listWidget.clear()
            self.listWidget.addItem(komunikat)

    def nCzasD(self):
        h1 = self.godziny_1.text()
        m1 = self.minuty_1.text()
        s1 = self.sekundy_1.text()
        h1 = str(h1)
        m1 = str(m1)
        s1 = str(s1)
        h2 = self.godziny_2.text()
        m2 = self.minuty_2.text()
        s2 = self.sekundy_2.text()
        h2 = str(h2)
        m2 = str(m2)
        s2 = str(s2)
        h3 = self.godziny_3.text()
        m3 = self.minuty_3.text()
        s3 = self.sekundy_3.text()
        h3 = str(h3)
        m3 = str(m3)
        s3 = str(s3)
        try:
            int(h2)
            int(m2)
            int(s2)
            int(h2)
            int(m2)
            int(s2)
            int(h3)
            int(m3)
            int(s3)
            if ((float(h1)) >= 0 and (float(m1) in range(0, 60)) and (float(s1) in range(0, 60)) and (float(h2)) >= 0 and (float(m2) in range(0, 60)) and (float(s2) in range(0, 60)) and (float(h3)) >= 0 and (float(m3) in range(0, 60)) and (float(s3) in range(0, 60))):
                hpomoc = float(h1)*3600+ float(h2)*3600+float(h3)*3600
                mpomoc = float(m1)*60 + float(m2)*60 + float(m3)*60
                spomoc = float(s1)+float(s2)+float(s3)
                wspolczynnik = -10
                sr = (hpomoc + mpomoc + spomoc + wspolczynnik)/3
                hr = sr%3600
                hrezultat = (sr - hr)/3600
                mr = hr%60
                mrezultat = (hr-mr)/60
                srezultat = math.floor(mr)
                czas = "Przewidywany czas to: " + str(int(hrezultat)) + "h : " + str(int(mrezultat)) + "m : " + str(int(srezultat)) + "s \n"
                self.listWidget.clear()
                self.listWidget.addItem(czas)

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.listWidget.clear()
                self.listWidget.addItem(komunikat)

        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.listWidget.clear()
            self.listWidget.addItem(komunikat)


    def nCzasH(self):
        h1 = self.godziny_1.text()
        m1 = self.minuty_1.text()
        s1 = self.sekundy_1.text()
        h1 = str(h1)
        m1 = str(m1)
        s1 = str(s1)
        h2 = self.godziny_2.text()
        m2 = self.minuty_2.text()
        s2 = self.sekundy_2.text()
        h2 = str(h2)
        m2 = str(m2)
        s2 = str(s2)
        h3 = self.godziny_3.text()
        m3 = self.minuty_3.text()
        s3 = self.sekundy_3.text()
        h3 = str(h3)
        m3 = str(m3)
        s3 = str(s3)
        try:
            int(h2)
            int(m2)
            int(s2)
            int(h2)
            int(m2)
            int(s2)
            int(h3)
            int(m3)
            int(s3)
            if ((float(h1)) >= 0 and (float(m1) in range(0, 60)) and (float(s1) in range(0, 60)) and (float(h2)) >= 0 and (float(m2) in range(0, 60)) and (float(s2) in range(0, 60)) and (float(h3)) >= 0 and (float(m3) in range(0, 60)) and (float(s3) in range(0, 60))):
                hpomoc = float(h1)*3600+ float(h2)*3600+float(h3)*3600
                mpomoc = float(m1)*60 + float(m2)*60 + float(m3)*60
                spomoc = float(s1)+float(s2)+float(s3)
                wspolczynnik = -15
                sr = (hpomoc + mpomoc + spomoc + wspolczynnik)/3
                hr = sr%3600
                hrezultat = (sr - hr)/3600
                mr = hr%60
                mrezultat = (hr-mr)/60
                srezultat = math.floor(mr)
                czas = "Przewidywany czas to: " + str(int(hrezultat)) + "h : " + str(int(mrezultat)) + "m : " + str(int(srezultat)) + "s \n"
                self.listWidget.clear()
                self.listWidget.addItem(czas)

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.listWidget.clear()
                self.listWidget.addItem(komunikat)

        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.listWidget.clear()
            self.listWidget.addItem(komunikat)

    def nCzasM(self):
        h1 = self.godziny_1.text()
        m1 = self.minuty_1.text()
        s1 = self.sekundy_1.text()
        h1 = str(h1)
        m1 = str(m1)
        s1 = str(s1)
        h2 = self.godziny_2.text()
        m2 = self.minuty_2.text()
        s2 = self.sekundy_2.text()
        h2 = str(h2)
        m2 = str(m2)
        s2 = str(s2)
        h3 = self.godziny_3.text()
        m3 = self.minuty_3.text()
        s3 = self.sekundy_3.text()
        h3 = str(h3)
        m3 = str(m3)
        s3 = str(s3)
        try:
            int(h2)
            int(m2)
            int(s2)
            int(h2)
            int(m2)
            int(s2)
            int(h3)
            int(m3)
            int(s3)
            if ((float(h1)) >= 0 and (float(m1) in range(0, 60)) and (float(s1) in range(0, 60)) and (float(h2)) >= 0 and (float(m2) in range(0, 60)) and (float(s2) in range(0, 60)) and (float(h3)) >= 0 and (float(m3) in range(0, 60)) and (float(s3) in range(0, 60))):
                hpomoc = float(h1)*3600+ float(h2)*3600+float(h3)*3600
                mpomoc = float(m1)*60 + float(m2)*60 + float(m3)*60
                spomoc = float(s1)+float(s2)+float(s3)
                wspolczynnik = -25
                sr = (hpomoc + mpomoc + spomoc + wspolczynnik)/3
                hr = sr%3600
                hrezultat = (sr - hr)/3600
                mr = hr%60
                mrezultat = (hr-mr)/60
                srezultat = math.floor(mr)
                czas = "Przewidywany czas to: " + str(int(hrezultat)) + "h : " + str(int(mrezultat)) + "m : " + str(int(srezultat)) + "s \n"
                self.listWidget.clear()
                self.listWidget.addItem(czas)

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.listWidget.clear()
                self.listWidget.addItem(komunikat)

        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.listWidget.clear()
            self.listWidget.addItem(komunikat)


    def nowyCzas(self):
        if (len(self.godziny_1.text()) == 0) and (len(self.minuty_1.text()) == 0) and (len(self.sekundy_1.text()) == 0) and (len(self.godziny_2.text()) == 0) and (len(self.minuty_2.text()) == 0) and (len(self.sekundy_2.text()) == 0) and (len(self.godziny_3.text()) == 0) and (len(self.minuty_3.text()) == 0) and (len(self.sekundy_3.text()) == 0):
            komunikat = "Podaj czas"

            self.listWidget.clear()
            self.listWidget.addItem(komunikat)
        else:
            if self.TpButton.isChecked():
                self.nCzasT()
            elif self.PpButton.isChecked():
                self.nCzasP()
            elif self.DpButton.isChecked():
                self.nCzasD()
            elif self.HpButton.isChecked():
                self.nCzasH()
            elif self.MpButton.isChecked():
                self.nCzasM()
    def setupUi(self, Przewidywania):
        Przewidywania.setObjectName("Przewidywania")
        Przewidywania.resize(753, 377)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 213, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 149, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 213, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 149, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 213, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 149, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Przewidywania.setPalette(palette)
        Przewidywania.setAutoFillBackground(False)
        self.widgetycentralne = QtWidgets.QWidget(Przewidywania)
        self.widgetycentralne.setObjectName("widgetycentralne")
        self.TpButton = QtWidgets.QRadioButton(self.widgetycentralne)
        self.TpButton.setGeometry(QtCore.QRect(30, 70, 82, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.TpButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TpButton.setFont(font)
        self.TpButton.setObjectName("TpButton")
        self.PpButton = QtWidgets.QRadioButton(self.widgetycentralne)
        self.PpButton.setGeometry(QtCore.QRect(30, 100, 82, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.PpButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PpButton.setFont(font)
        self.PpButton.setObjectName("PpButton")
        self.DpButton = QtWidgets.QRadioButton(self.widgetycentralne)
        self.DpButton.setGeometry(QtCore.QRect(30, 130, 82, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.DpButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DpButton.setFont(font)
        self.DpButton.setObjectName("DpButton")
        self.HpButton = QtWidgets.QRadioButton(self.widgetycentralne)
        self.HpButton.setGeometry(QtCore.QRect(30, 160, 101, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.HpButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.HpButton.setFont(font)
        self.HpButton.setObjectName("HpButton")
        self.MpButton = QtWidgets.QRadioButton(self.widgetycentralne)
        self.MpButton.setGeometry(QtCore.QRect(30, 190, 101, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.MpButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MpButton.setFont(font)
        self.MpButton.setObjectName("MpButton")
        self.labelD = QtWidgets.QLabel(self.widgetycentralne)
        self.labelD.setGeometry(QtCore.QRect(30, 40, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelD.setFont(font)
        self.labelD.setObjectName("labelD")
        self.label_PB = QtWidgets.QLabel(self.widgetycentralne)
        self.label_PB.setGeometry(QtCore.QRect(160, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_PB.setFont(font)
        self.label_PB.setObjectName("label_PB")
        self.label_G1 = QtWidgets.QLabel(self.widgetycentralne)
        self.label_G1.setGeometry(QtCore.QRect(160, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_G1.setFont(font)
        self.label_G1.setObjectName("label_G1")
        self.label_M1 = QtWidgets.QLabel(self.widgetycentralne)
        self.label_M1.setGeometry(QtCore.QRect(160, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_M1.setFont(font)
        self.label_M1.setObjectName("label_M1")
        self.label_S1 = QtWidgets.QLabel(self.widgetycentralne)
        self.label_S1.setGeometry(QtCore.QRect(160, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_S1.setFont(font)
        self.label_S1.setObjectName("label_S1")
        self.godziny_1 = QtWidgets.QLineEdit(self.widgetycentralne)
        self.godziny_1.setGeometry(QtCore.QRect(230, 70, 113, 20))
        self.godziny_1.setObjectName("godziny_1")
        self.minuty_1 = QtWidgets.QLineEdit(self.widgetycentralne)
        self.minuty_1.setGeometry(QtCore.QRect(230, 100, 113, 20))
        self.minuty_1.setObjectName("minuty_1")
        self.sekundy_1 = QtWidgets.QLineEdit(self.widgetycentralne)
        self.sekundy_1.setGeometry(QtCore.QRect(230, 130, 113, 20))
        self.sekundy_1.setObjectName("sekundy_1")
        self.scrollArea1 = QtWidgets.QScrollArea(self.widgetycentralne)
        self.scrollArea1.setGeometry(QtCore.QRect(140, 230, 261, 31))
        self.scrollArea1.setWidgetResizable(True)
        self.scrollArea1.setObjectName("scrollArea1")
        self.scrollAreaWidgetContents1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents1.setGeometry(QtCore.QRect(0, 0, 281, 29))
        self.scrollAreaWidgetContents1.setObjectName("scrollAreaWidgetContents1")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents1)
        self.listWidget.setGeometry(QtCore.QRect(-5, 0, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.scrollArea1.setWidget(self.scrollAreaWidgetContents1)
        self.rezultatButton = QtWidgets.QPushButton(self.widgetycentralne)
        self.rezultatButton.setGeometry(QtCore.QRect(430, 220, 151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.rezultatButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.rezultatButton.setFont(font)
        self.rezultatButton.setObjectName("rezultatButton")
        self.label_M2 = QtWidgets.QLabel(self.widgetycentralne)
        self.label_M2.setGeometry(QtCore.QRect(350, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_M2.setFont(font)
        self.label_M2.setObjectName("label_M2")
        self.minuty_2 = QtWidgets.QLineEdit(self.widgetycentralne)
        self.minuty_2.setGeometry(QtCore.QRect(420, 100, 113, 20))
        self.minuty_2.setObjectName("minuty_2")
        self.label_G2 = QtWidgets.QLabel(self.widgetycentralne)
        self.label_G2.setGeometry(QtCore.QRect(350, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_G2.setFont(font)
        self.label_G2.setObjectName("label_G2")
        self.sekundy_2 = QtWidgets.QLineEdit(self.widgetycentralne)
        self.sekundy_2.setGeometry(QtCore.QRect(420, 130, 113, 20))
        self.sekundy_2.setObjectName("sekundy_2")
        self.godziny_2 = QtWidgets.QLineEdit(self.widgetycentralne)
        self.godziny_2.setGeometry(QtCore.QRect(420, 70, 113, 20))
        self.godziny_2.setObjectName("godziny_2")
        self.label_SB = QtWidgets.QLabel(self.widgetycentralne)
        self.label_SB.setGeometry(QtCore.QRect(350, 40, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_SB.setFont(font)
        self.label_SB.setObjectName("label_SB")
        self.label_S2 = QtWidgets.QLabel(self.widgetycentralne)
        self.label_S2.setGeometry(QtCore.QRect(350, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_S2.setFont(font)
        self.label_S2.setObjectName("label_S2")
        self.label_M3 = QtWidgets.QLabel(self.widgetycentralne)
        self.label_M3.setGeometry(QtCore.QRect(540, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_M3.setFont(font)
        self.label_M3.setObjectName("label_M3")
        self.minuty_3 = QtWidgets.QLineEdit(self.widgetycentralne)
        self.minuty_3.setGeometry(QtCore.QRect(610, 100, 113, 20))
        self.minuty_3.setObjectName("minuty_3")
        self.label_G3 = QtWidgets.QLabel(self.widgetycentralne)
        self.label_G3.setGeometry(QtCore.QRect(540, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_G3.setFont(font)
        self.label_G3.setObjectName("label_G3")
        self.sekundy_3 = QtWidgets.QLineEdit(self.widgetycentralne)
        self.sekundy_3.setGeometry(QtCore.QRect(610, 130, 113, 20))
        self.sekundy_3.setObjectName("sekundy_3")
        self.godziny_3 = QtWidgets.QLineEdit(self.widgetycentralne)
        self.godziny_3.setGeometry(QtCore.QRect(610, 70, 113, 20))
        self.godziny_3.setObjectName("godziny_3")
        self.label_Or = QtWidgets.QLabel(self.widgetycentralne)
        self.label_Or.setGeometry(QtCore.QRect(540, 40, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Or.setFont(font)
        self.label_Or.setObjectName("label_Or")
        self.label_S3 = QtWidgets.QLabel(self.widgetycentralne)
        self.label_S3.setGeometry(QtCore.QRect(540, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_S3.setFont(font)
        self.label_S3.setObjectName("label_S3")
        self.TpButton.raise_()
        self.PpButton.raise_()
        self.DpButton.raise_()
        self.HpButton.raise_()
        self.MpButton.raise_()
        self.labelD.raise_()
        self.label_PB.raise_()
        self.label_G1.raise_()
        self.label_M1.raise_()
        self.label_S1.raise_()
        self.godziny_1.raise_()
        self.minuty_1.raise_()
        self.sekundy_1.raise_()
        self.scrollArea1.raise_()
        self.rezultatButton.raise_()
        self.label_M2.raise_()
        self.minuty_2.raise_()
        self.label_G2.raise_()
        self.sekundy_2.raise_()
        self.godziny_2.raise_()
        self.label_SB.raise_()
        self.label_S2.raise_()
        self.label_M3.raise_()
        self.minuty_3.raise_()
        self.label_G3.raise_()
        self.sekundy_3.raise_()
        self.godziny_3.raise_()
        self.label_Or.raise_()
        self.label_S3.raise_()
        Przewidywania.setCentralWidget(self.widgetycentralne)
        self.menubar1 = QtWidgets.QMenuBar(Przewidywania)
        self.menubar1.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar1.setObjectName("menubar1")
        Przewidywania.setMenuBar(self.menubar1)
        self.statusbar1 = QtWidgets.QStatusBar(Przewidywania)
        self.statusbar1.setObjectName("statusbar1")
        Przewidywania.setStatusBar(self.statusbar1)
        self.rezultatButton.clicked.connect(self.nowyCzas)

        self.retranslateUi(Przewidywania)
        QtCore.QMetaObject.connectSlotsByName(Przewidywania)

    def retranslateUi(self, Przewidywania):
        _translate = QtCore.QCoreApplication.translate
        Przewidywania.setWindowTitle(_translate("Przewidywania", "MainWindow"))
        self.TpButton.setText(_translate("Przewidywania", "3 km"))
        self.PpButton.setText(_translate("Przewidywania", "5 km"))
        self.DpButton.setText(_translate("Przewidywania", "10 km"))
        self.HpButton.setText(_translate("Przewidywania", "21, 097 km"))
        self.MpButton.setText(_translate("Przewidywania", "42,195 km"))
        self.labelD.setText(_translate("Przewidywania", "DYSTANS"))
        self.label_PB.setText(_translate("Przewidywania", "Personal Best"))
        self.label_G1.setText(_translate("Przewidywania", "Godziny:"))
        self.label_M1.setText(_translate("Przewidywania", "Minuty:"))
        self.label_S1.setText(_translate("Przewidywania", "Sekundy:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Przewidywania", ""))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.rezultatButton.setText(_translate("Przewidywania", "Przewidywany Rezultat"))
        self.label_M2.setText(_translate("Przewidywania", "Minuty:"))
        self.label_G2.setText(_translate("Przewidywania", "Godziny:"))
        self.label_SB.setText(_translate("Przewidywania", "Season Best"))
        self.label_S2.setText(_translate("Przewidywania", "Sekundy:"))
        self.label_M3.setText(_translate("Przewidywania", "Minuty:"))
        self.label_G3.setText(_translate("Przewidywania", "Godziny:"))
        self.label_Or.setText(_translate("Przewidywania", "Ostatni wynik"))
        self.label_S3.setText(_translate("Przewidywania", "Sekundy:"))
class Ui_runningzombies(object):


    def okno(self):
        self.Przewidywania = QtWidgets.QMainWindow()
        self.ui     = Ui_Przewidywania()
        self.ui.setupUi(self.Przewidywania)
        self.Przewidywania.show()

    def staleT(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 3
                h_result = math.floor(x)
                h_pomoc = (float(h) % 3) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 3)
                m_ppomoc = (m_pomoc % 3) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 3)

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh]

                for i in range((len(sekundy))):
                    if sekundy[i - 1] + (s_result) < 60:
                        sekundy[i] = sekundy[i - 1] + s_result
                    elif (sekundy[i - 1] + s_result == 60):
                        sekundy[i] = 0
                        minuty[i] += 1
                    else:
                        sekundy[i] = sekundy[i - 1] + s_result - 60
                        minuty[i] += 1

                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + m_result + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1] + m_result
                    elif (minuty[i - 1] + m_result + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + m_result + minuty[i] - 60
                        godziny[i] += 1

                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1] + h_result


                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(sekundy[2]) + "s \n"
                rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci
                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)
    def staleP(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 5
                h_result = math.floor(x)
                h_pomoc = (float(h) % 5) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 5)
                m_ppomoc = (m_pomoc % 5) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 5)

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh]

                for i in range((len(sekundy))):
                    if sekundy[i - 1] + (s_result) < 60:
                        sekundy[i] = sekundy[i - 1] + s_result
                    elif (sekundy[i - 1] + s_result == 60):
                        sekundy[i] = 0
                        minuty[i] += 1
                    else:
                        sekundy[i] = sekundy[i - 1] + s_result - 60
                        minuty[i] += 1

                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + m_result + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1] + m_result
                    elif (minuty[i - 1] + m_result + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + m_result + minuty[i] - 60
                        godziny[i] += 1

                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1] + h_result

                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(sekundy[4]) + "s \n"
                rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty
                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty,
                              miedzyczas_piaty]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)

    def staleD(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 10
                h_result = math.floor(x)
                h_pomoc = (float(h) % 10) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 10)
                m_ppomoc = (m_pomoc % 10) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 10)

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                szosty_kms = 0
                szosty_kmm = 0
                szosty_kmh = 0
                siodmy_kms = 0
                siodmy_kmm = 0
                siodmy_kmh = 0
                osmy_kms = 0
                osmy_kmm = 0
                osmy_kmh = 0
                dziewiaty_kms = 0
                dziewiaty_kmm = 0
                dziewiaty_kmh = 0
                dziesiaty_kms = 0
                dziesiaty_kmm = 0
                dziesiaty_kmh = 0
                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms, szosty_kms, siodmy_kms,osmy_kms, dziewiaty_kms, dziesiaty_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm, szosty_kmm, siodmy_kmm, osmy_kmm,dziewiaty_kmm, dziesiaty_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh, szosty_kmh, siodmy_kmh,osmy_kmh, dziewiaty_kmh, dziesiaty_kmh]

                for i in range((len(sekundy))):
                    if sekundy[i - 1] + (s_result) < 60:
                        sekundy[i] = sekundy[i - 1] + s_result
                    elif (sekundy[i - 1] + s_result == 60):
                        sekundy[i] = 0
                        minuty[i] += 1
                    else:
                        sekundy[i] = sekundy[i - 1] + s_result - 60
                        minuty[i] += 1

                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + m_result + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1] + m_result
                    elif (minuty[i - 1] + m_result + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + m_result + minuty[i] - 60
                        godziny[i] += 1

                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1] + h_result

                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(sekundy[4]) + "s \n"
                miedzyczas_szosty = "6km: " + str(godziny[5]) + "h : " + str(minuty[5]) + "m : " + str(sekundy[5]) + "s \n"
                miedzyczas_siodmy = "7km: " + str(godziny[6]) + "h : " + str(minuty[6]) + "m : " + str(sekundy[6]) + "s \n"
                miedzyczas_osmy = "8km: " + str(godziny[7]) + "h : " + str(minuty[7]) + "m : " + str(sekundy[7]) + "s \n"
                miedzyczas_dziewiaty = "9km: " + str(godziny[8]) + "h : " + str(minuty[8]) + "m : " + str(sekundy[8]) + "s \n"
                miedzyczas_dziesiaty = "10km: " + str(godziny[9]) + "h : " + str(minuty[9]) + "m : " + str(sekundy[9]) + "s \n"
                rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty + miedzyczas_szosty + miedzyczas_siodmy + miedzyczas_osmy + miedzyczas_dziewiaty + miedzyczas_dziesiaty
                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty,
                              miedzyczas_piaty, miedzyczas_szosty, miedzyczas_siodmy, miedzyczas_osmy,
                              miedzyczas_dziewiaty, miedzyczas_dziesiaty]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)

    def staleH(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 21.097
                h_result = math.floor(x)
                h_pomoc = (float(h) % 21.097) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 21.097)
                m_ppomoc = (m_pomoc % 21.097) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 21.097)

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                szosty_kms = 0
                szosty_kmm = 0
                szosty_kmh = 0
                siodmy_kms = 0
                siodmy_kmm = 0
                siodmy_kmh = 0
                osmy_kms = 0
                osmy_kmm = 0
                osmy_kmh = 0
                dziewiaty_kms = 0
                dziewiaty_kmm = 0
                dziewiaty_kmh = 0
                dziesiaty_kms = 0
                dziesiaty_kmm = 0
                dziesiaty_kmh = 0
                jedenasty_kms = 0
                jedenasty_kmm = 0
                jedenasty_kmh = 0
                dwunasty_kms = 0
                dwunasty_kmm = 0
                dwunasty_kmh = 0
                trzynasty_kms = 0
                trzynasty_kmm = 0
                trzynasty_kmh = 0
                czternasty_kms = 0
                czternasty_kmm = 0
                czternasty_kmh = 0
                pietnasty_kms = 0
                pietnasty_kmm = 0
                pietnasty_kmh = 0
                szesnasty_kms = 0
                szesnasty_kmm = 0
                szesnasty_kmh = 0
                siedemnasty_kms = 0
                siedemnasty_kmm = 0
                siedemnasty_kmh = 0
                osiemnasty_kms = 0
                osiemnasty_kmm = 0
                osiemnasty_kmh = 0
                dziewietnasty_kms = 0
                dziewietnasty_kmm = 0
                dziewietnasty_kmh = 0
                dwudziesty_kms = 0
                dwudziesty_kmm = 0
                dwudziesty_kmh = 0
                djeden_kms = 0
                djeden_kmm = 0
                djeden_kmh = 0

                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms, szosty_kms, siodmy_kms,
                           osmy_kms, dziewiaty_kms, dziesiaty_kms, jedenasty_kms, dwunasty_kms, trzynasty_kms, czternasty_kms, pietnasty_kms, szesnasty_kms, siedemnasty_kms, osiemnasty_kms, dziewietnasty_kms, dwudziesty_kms, djeden_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm, szosty_kmm, siodmy_kmm, osmy_kmm,
                          dziewiaty_kmm, dziesiaty_kmm, jedenasty_kmm, dwunasty_kmm, trzynasty_kmm, czternasty_kmm, pietnasty_kmm, szesnasty_kmm, siedemnasty_kmm, osiemnasty_kmm, dziewietnasty_kmm, dwudziesty_kmm, djeden_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh, szosty_kmh, siodmy_kmh,
                           osmy_kmh, dziewiaty_kmh, dziesiaty_kmh, jedenasty_kmh, dwunasty_kmh, trzynasty_kmh, czternasty_kmh, pietnasty_kmh, szesnasty_kmh, siedemnasty_kmh, osiemnasty_kmh, dziewietnasty_kmh, dwudziesty_kmh, djeden_kmh]

                for i in range((len(sekundy))):
                    if sekundy[i - 1] + (s_result) < 60:
                        sekundy[i] = sekundy[i - 1] + s_result
                    elif (sekundy[i - 1] + s_result == 60):
                        sekundy[i] = 0
                        minuty[i] += 1
                    else:
                        sekundy[i] = sekundy[i - 1] + s_result - 60
                        minuty[i] += 1

                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + m_result + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1] + m_result
                    elif (minuty[i - 1] + m_result + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + m_result + minuty[i] - 60
                        godziny[i] += 1

                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1] + h_result


                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(
                    sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(
                    sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(
                    sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(
                    sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(
                    sekundy[4]) + "s \n"
                miedzyczas_szosty = "6km: " + str(godziny[5]) + "h : " + str(minuty[5]) + "m : " + str(
                    sekundy[5]) + "s \n"
                miedzyczas_siodmy = "7km: " + str(godziny[6]) + "h : " + str(minuty[6]) + "m : " + str(
                    sekundy[6]) + "s \n"
                miedzyczas_osmy = "8km: " + str(godziny[7]) + "h : " + str(minuty[7]) + "m : " + str(
                    sekundy[7]) + "s \n"
                miedzyczas_dziewiaty = "9km: " + str(godziny[8]) + "h : " + str(minuty[8]) + "m : " + str(
                    sekundy[8]) + "s \n"
                miedzyczas_dziesiaty = "10km: " + str(godziny[9]) + "h : " + str(minuty[9]) + "m : " + str(
                    sekundy[9]) + "s \n"
                miedzyczas_jedenasty = "11km: " + str(godziny[10]) + "h : " + str(minuty[10]) + "m : " + str(
                    sekundy[10]) + "s \n"
                miedzyczas_dwunasty = "12km: " + str(godziny[11]) + "h : " + str(minuty[11]) + "m : " + str(
                    sekundy[11]) + "s \n"
                miedzyczas_trzynasty = "13km: " + str(godziny[12]) + "h : " + str(minuty[12]) + "m : " + str(
                    sekundy[12]) + "s \n"
                miedzyczas_czternasty = "14km: " + str(godziny[13]) + "h : " + str(minuty[13]) + "m : " + str(
                    sekundy[13]) + "s \n"
                miedzyczas_pietnasty = "15km: " + str(godziny[14]) + "h : " + str(minuty[14]) + "m : " + str(
                    sekundy[14]) + "s \n"
                miedzyczas_szesnasty = "16km: " + str(godziny[15]) + "h : " + str(minuty[15]) + "m : " + str(
                    sekundy[15]) + "s \n"
                miedzyczas_siedemnasty = "17km: " + str(godziny[16]) + "h : " + str(minuty[16]) + "m : " + str(
                    sekundy[16]) + "s \n"
                miedzyczas_osiemnasty = "18km: " + str(godziny[17]) + "h : " + str(minuty[17]) + "m : " + str(
                    sekundy[17]) + "s \n"
                miedzyczas_dziewietnasty = "19km: " + str(godziny[18]) + "h : " + str(minuty[18]) + "m : " + str(
                    sekundy[18]) + "s \n"
                miedzyczas_dwudziesty = "20km: " + str(godziny[19]) + "h : " + str(minuty[19]) + "m : " + str(
                    sekundy[19]) + "s \n"
                miedzyczas_djeden = "21km: " + str(godziny[20]) + "h : " + str(minuty[20]) + "m : " + str(
                    sekundy[20]) + "s \n"

                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty, miedzyczas_piaty, miedzyczas_szosty, miedzyczas_siodmy, miedzyczas_osmy, miedzyczas_dziewiaty, miedzyczas_dziesiaty,miedzyczas_jedenasty, miedzyczas_dwunasty, miedzyczas_trzynasty, miedzyczas_czternasty, miedzyczas_pietnasty, miedzyczas_szesnasty, miedzyczas_siedemnasty, miedzyczas_osiemnasty, miedzyczas_dziewietnasty, miedzyczas_dwudziesty, miedzyczas_djeden]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)

    def staleM(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 42.195
                h_result = math.floor(x)
                h_pomoc = (float(h) % 42.195) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 42.195)
                m_ppomoc = (m_pomoc % 42.195) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 42.195)

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                szosty_kms = 0
                szosty_kmm = 0
                szosty_kmh = 0
                siodmy_kms = 0
                siodmy_kmm = 0
                siodmy_kmh = 0
                osmy_kms = 0
                osmy_kmm = 0
                osmy_kmh = 0
                dziewiaty_kms = 0
                dziewiaty_kmm = 0
                dziewiaty_kmh = 0
                dziesiaty_kms = 0
                dziesiaty_kmm = 0
                dziesiaty_kmh = 0
                jedenasty_kms = 0
                jedenasty_kmm = 0
                jedenasty_kmh = 0
                dwunasty_kms = 0
                dwunasty_kmm = 0
                dwunasty_kmh = 0
                trzynasty_kms = 0
                trzynasty_kmm = 0
                trzynasty_kmh = 0
                czternasty_kms = 0
                czternasty_kmm = 0
                czternasty_kmh = 0
                pietnasty_kms = 0
                pietnasty_kmm = 0
                pietnasty_kmh = 0
                szesnasty_kms = 0
                szesnasty_kmm = 0
                szesnasty_kmh = 0
                siedemnasty_kms = 0
                siedemnasty_kmm = 0
                siedemnasty_kmh = 0
                osiemnasty_kms = 0
                osiemnasty_kmm = 0
                osiemnasty_kmh = 0
                dziewietnasty_kms = 0
                dziewietnasty_kmm = 0
                dziewietnasty_kmh = 0
                dwudziesty_kms = 0
                dwudziesty_kmm = 0
                dwudziesty_kmh = 0
                djeden_kms = 0
                djeden_kmm = 0
                djeden_kmh = 0
                ddwa_kms = 0
                ddwa_kmm = 0
                ddwa_kmh = 0
                dtrzy_kms = 0
                dtrzy_kmm = 0
                dtrzy_kmh = 0
                dcztery_kms = 0
                dcztery_kmm = 0
                dcztery_kmh = 0
                dpiec_kms = 0
                dpiec_kmm = 0
                dpiec_kmh = 0
                dszesc_kms = 0
                dszesc_kmm = 0
                dszesc_kmh = 0
                dsiedem_kms = 0
                dsiedem_kmm = 0
                dsiedem_kmh = 0
                dosiem_kms = 0
                dosiem_kmm = 0
                dosiem_kmh = 0
                ddziewiec_kms = 0
                ddziewiec_kmm = 0
                ddziewiec_kmh = 0
                trzydziesci_kms = 0
                trzydziesci_kmm = 0
                trzydziesci_kmh = 0
                tjeden_kms = 0
                tjeden_kmm = 0
                tjeden_kmh = 0
                tdwa_kms = 0
                tdwa_kmm = 0
                tdwa_kmh = 0
                ttrzy_kms = 0
                ttrzy_kmm = 0
                ttrzy_kmh = 0
                tcztery_kms = 0
                tcztery_kmm = 0
                tcztery_kmh = 0
                tpiec_kms = 0
                tpiec_kmm = 0
                tpiec_kmh = 0
                tszesc_kms = 0
                tszesc_kmm = 0
                tszesc_kmh = 0
                tsiedem_kms = 0
                tsiedem_kmm = 0
                tsiedem_kmh = 0
                tosiem_kms = 0
                tosiem_kmm = 0
                tosiem_kmh = 0
                tdziewiec_kms = 0
                tdziewiec_kmm = 0
                tdziewiec_kmh = 0
                czterdziesci_kms = 0
                czterdziesci_kmm = 0
                czterdziesci_kmh = 0
                cjeden_kms = 0
                cjeden_kmm = 0
                cjeden_kmh = 0
                cdwa_kms = 0
                cdwa_kmm = 0
                cdwa_kmh = 0

                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms, szosty_kms, siodmy_kms,
                           osmy_kms, dziewiaty_kms, dziesiaty_kms, jedenasty_kms, dwunasty_kms, trzynasty_kms, czternasty_kms, pietnasty_kms, szesnasty_kms, siedemnasty_kms, osiemnasty_kms, dziewietnasty_kms, dwudziesty_kms, djeden_kms,
                           ddwa_kms, dtrzy_kms, dcztery_kms, dpiec_kms, dszesc_kms, dsiedem_kms,dosiem_kms,ddziewiec_kms,trzydziesci_kms, tjeden_kms, tdwa_kms, ttrzy_kms,
                           tcztery_kms,tpiec_kms,tszesc_kms, tsiedem_kms, tosiem_kms,tdziewiec_kms, czterdziesci_kms, cjeden_kms,cdwa_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm, szosty_kmm, siodmy_kmm, osmy_kmm,
                          dziewiaty_kmm, dziesiaty_kmm, jedenasty_kmm, dwunasty_kmm, trzynasty_kmm, czternasty_kmm, pietnasty_kmm, szesnasty_kmm, siedemnasty_kmm, osiemnasty_kmm, dziewietnasty_kmm, dwudziesty_kmm, djeden_kmm,
                          ddwa_kmm, dtrzy_kmm, dcztery_kmm, dpiec_kmm, dszesc_kmm, dsiedem_kmm, dosiem_kmm, ddziewiec_kmm, trzydziesci_kmm, tjeden_kmm, tdwa_kmm,
                          ttrzy_kmm, tcztery_kmm, tpiec_kmm, tszesc_kmm, tsiedem_kmm,tosiem_kmm, tdziewiec_kmm, czterdziesci_kmm, cjeden_kmm, cdwa_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh, szosty_kmh, siodmy_kmh,
                           osmy_kmh, dziewiaty_kmh, dziesiaty_kmh, jedenasty_kmh, dwunasty_kmh, trzynasty_kmh, czternasty_kmh, pietnasty_kmh, szesnasty_kmh, siedemnasty_kmh, osiemnasty_kmh, dziewietnasty_kmh, dwudziesty_kmh, djeden_kmh,
                           ddwa_kmh, dtrzy_kmh, dcztery_kmh, dpiec_kmh, dszesc_kmh, dsiedem_kmh, dosiem_kmh, ddziewiec_kmh, ddziewiec_kmh, trzydziesci_kmh, tjeden_kmh, tdwa_kmh,
                           ttrzy_kmh, tcztery_kmh, tpiec_kmh, tszesc_kmh, tsiedem_kmh, tosiem_kmh, tdziewiec_kmh, czterdziesci_kmh, cjeden_kmh, cdwa_kmh]


                for i in range((len(sekundy))):
                    if sekundy[i - 1] + (s_result) < 60:
                        sekundy[i] = sekundy[i - 1] + s_result
                    elif (sekundy[i - 1] + s_result == 60):
                        sekundy[i] = 0
                        minuty[i] += 1
                    else:
                        sekundy[i] = sekundy[i - 1] + s_result - 60
                        minuty[i] += 1

                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + m_result + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1] + m_result
                    elif (minuty[i - 1] + m_result + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + m_result + minuty[i] - 60
                        godziny[i] += 1

                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1] + h_result


                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(
                    sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(
                    sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(
                    sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(
                    sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(
                    sekundy[4]) + "s \n"
                miedzyczas_szosty = "6km: " + str(godziny[5]) + "h : " + str(minuty[5]) + "m : " + str(
                    sekundy[5]) + "s \n"
                miedzyczas_siodmy = "7km: " + str(godziny[6]) + "h : " + str(minuty[6]) + "m : " + str(
                    sekundy[6]) + "s \n"
                miedzyczas_osmy = "8km: " + str(godziny[7]) + "h : " + str(minuty[7]) + "m : " + str(
                    sekundy[7]) + "s \n"
                miedzyczas_dziewiaty = "9km: " + str(godziny[8]) + "h : " + str(minuty[8]) + "m : " + str(
                    sekundy[8]) + "s \n"
                miedzyczas_dziesiaty = "10km: " + str(godziny[9]) + "h : " + str(minuty[9]) + "m : " + str(
                    sekundy[9]) + "s \n"
                miedzyczas_jedenasty = "11km: " + str(godziny[10]) + "h : " + str(minuty[10]) + "m : " + str(
                    sekundy[10]) + "s \n"
                miedzyczas_dwunasty = "12km: " + str(godziny[11]) + "h : " + str(minuty[11]) + "m : " + str(
                    sekundy[11]) + "s \n"
                miedzyczas_trzynasty = "13km: " + str(godziny[12]) + "h : " + str(minuty[12]) + "m : " + str(
                    sekundy[12]) + "s \n"
                miedzyczas_czternasty = "14km: " + str(godziny[13]) + "h : " + str(minuty[13]) + "m : " + str(
                    sekundy[13]) + "s \n"
                miedzyczas_pietnasty = "15km: " + str(godziny[14]) + "h : " + str(minuty[14]) + "m : " + str(
                    sekundy[14]) + "s \n"
                miedzyczas_szesnasty = "16km: " + str(godziny[15]) + "h : " + str(minuty[15]) + "m : " + str(
                    sekundy[15]) + "s \n"
                miedzyczas_siedemnasty = "17km: " + str(godziny[16]) + "h : " + str(minuty[16]) + "m : " + str(
                    sekundy[16]) + "s \n"
                miedzyczas_osiemnasty = "18km: " + str(godziny[17]) + "h : " + str(minuty[17]) + "m : " + str(
                    sekundy[17]) + "s \n"
                miedzyczas_dziewietnasty = "19km: " + str(godziny[18]) + "h : " + str(minuty[18]) + "m : " + str(
                    sekundy[18]) + "s \n"
                miedzyczas_dwudziesty = "20km: " + str(godziny[19]) + "h : " + str(minuty[19]) + "m : " + str(
                    sekundy[19]) + "s \n"
                miedzyczas_djeden = "21km: " + str(godziny[20]) + "h : " + str(minuty[20]) + "m : " + str(
                    sekundy[20]) + "s \n"
                miedzyczas_ddwa = "22km: " + str(godziny[21]) + "h : " + str(minuty[21]) + "m : " + str(
                    sekundy[21]) + "s \n"
                miedzyczas_dtrzy = "23km: " + str(godziny[22]) + "h : " + str(minuty[22]) + "m : " + str(
                    sekundy[22]) + "s \n"
                miedzyczas_dcztery = "24km: " + str(godziny[23]) + "h : " + str(minuty[23]) + "m : " + str(
                    sekundy[23]) + "s \n"
                miedzyczas_dpiec = "25km: " + str(godziny[24]) + "h : " + str(minuty[24]) + "m : " + str(
                    sekundy[24]) + "s \n"
                miedzyczas_dszesc = "26km: " + str(godziny[25]) + "h : " + str(minuty[25]) + "m : " + str(
                    sekundy[25]) + "s \n"
                miedzyczas_dsiedem = "27km: " + str(godziny[26]) + "h : " + str(minuty[26]) + "m : " + str(
                    sekundy[26]) + "s \n"
                miedzyczas_dosiem = "28km: " + str(godziny[27]) + "h : " + str(minuty[27]) + "m : " + str(
                    sekundy[27]) + "s \n"
                miedzyczas_ddziewiec = "29km: " + str(godziny[28]) + "h : " + str(minuty[28]) + "m : " + str(
                    sekundy[28]) + "s \n"
                miedzyczas_trzydziesci = "30km: " + str(godziny[29]) + "h : " + str(minuty[29]) + "m : " + str(
                    sekundy[29]) + "s \n"
                miedzyczas_tjeden = "31km: " + str(godziny[30]) + "h : " + str(minuty[30]) + "m : " + str(
                    sekundy[30]) + "s \n"
                miedzyczas_tdwa = "32km: " + str(godziny[31]) + "h : " + str(minuty[31]) + "m : " + str(
                    sekundy[31]) + "s \n"
                miedzyczas_ttrzy = "33km: " + str(godziny[32]) + "h : " + str(minuty[32]) + "m : " + str(
                    sekundy[32]) + "s \n"
                miedzyczas_tcztery = "34km: " + str(godziny[33]) + "h : " + str(minuty[33]) + "m : " + str(
                    sekundy[33]) + "s \n"
                miedzyczas_tpiec = "35km: " + str(godziny[34]) + "h : " + str(minuty[34]) + "m : " + str(
                    sekundy[34]) + "s \n"
                miedzyczas_tszesc = "36km: " + str(godziny[35]) + "h : " + str(minuty[35]) + "m : " + str(
                    sekundy[35]) + "s \n"
                miedzyczas_tsiedem = "37km: " + str(godziny[36]) + "h : " + str(minuty[36]) + "m : " + str(
                    sekundy[36]) + "s \n"
                miedzyczas_tosiem = "38km: " + str(godziny[37]) + "h : " + str(minuty[37]) + "m : " + str(
                    sekundy[37]) + "s \n"
                miedzyczas_tdziewiec = "39km: " + str(godziny[38]) + "h : " + str(minuty[38]) + "m : " + str(
                    sekundy[38]) + "s \n"
                miedzyczas_czterdziesci = "40km: " + str(godziny[39]) + "h : " + str(minuty[39]) + "m : " + str(
                    sekundy[39]) + "s \n"
                miedzyczas_cjeden = "41km: " + str(godziny[40]) + "h : " + str(minuty[40]) + "m : " + str(
                    sekundy[40]) + "s \n"
                miedzyczas_cdwa = "42km: " + str(godziny[41]) + "h : " + str(minuty[41]) + "m : " + str(
                    sekundy[41]) + "s \n"

                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty, miedzyczas_piaty, miedzyczas_szosty, miedzyczas_siodmy, miedzyczas_osmy, miedzyczas_dziewiaty, miedzyczas_dziesiaty,miedzyczas_jedenasty, miedzyczas_dwunasty, miedzyczas_trzynasty, miedzyczas_czternasty, miedzyczas_pietnasty, miedzyczas_szesnasty, miedzyczas_siedemnasty, miedzyczas_osiemnasty, miedzyczas_dziewietnasty, miedzyczas_dwudziesty, miedzyczas_djeden,
                              miedzyczas_ddwa, miedzyczas_dtrzy, miedzyczas_dcztery, miedzyczas_dpiec, miedzyczas_dszesc, miedzyczas_dsiedem, miedzyczas_dosiem, miedzyczas_ddziewiec, miedzyczas_trzydziesci, miedzyczas_tjeden,
                              miedzyczas_tdwa, miedzyczas_ttrzy, miedzyczas_tcztery, miedzyczas_tpiec, miedzyczas_tszesc, miedzyczas_tsiedem, miedzyczas_tosiem, miedzyczas_tdziewiec, miedzyczas_czterdziesci, miedzyczas_cjeden, miedzyczas_cdwa]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)

    def timeCheck(self):
        if (len(self.godziny.text()) == 0) and (len(self.minuty.text()) == 0) and (len(self.sekundy.text()) == 0):
            komunikat = "Podaj czas"

            self.result.clear()
            self.result.addItem(komunikat)
        else:
            if self.TButton.isChecked():
                self.staleT()


            elif self.PButton.isChecked():
                self.staleP()
            elif self.DButton.isChecked():
                self.staleD()
            elif self.HButton.isChecked():
                self.staleH()
            elif self.MButton.isChecked():
                self.staleM()

    def progresT(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 3
                h_result = math.floor(x)
                h_pomoc = (float(h) % 3) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 3)
                m_ppomoc = (m_pomoc % 3) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 3)
                wspolczynnik = 5

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh]
                if (s_result + wspolczynnik) < 60:
                    sekundy[0] = s_result + wspolczynnik
                elif (s_result + wspolczynnik) == 60:
                    sekundy[0] = 0
                    minuty[0] += 1
                else:
                    sekundy[0] = (s_result + wspolczynnik) - 60
                    minuty[0] += 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] - wspolczynnik >0:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik
                    elif (sekundy[i - 1] - wspolczynnik == 0):
                        sekundy[i] = 0

                    else:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik + 60
                        minuty[i] -= 1



                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1


                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]

                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(sekundy[2]) + "s \n"
                rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci
                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])


                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)

        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)

    def progresP(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 5
                h_result = math.floor(x)
                h_pomoc = (float(h) % 5) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 5)
                m_ppomoc = (m_pomoc % 5) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 5)
                wspolczynnik = 4

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh]

                if (s_result + 2*wspolczynnik) < 60:
                    sekundy[0] = s_result + 2*wspolczynnik
                elif (s_result + 2*wspolczynnik) == 60:
                    sekundy[0] = 0
                    minuty[0] += 1
                else:
                    sekundy[0] = (s_result + 2*wspolczynnik) - 60
                    minuty[0] += 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] - wspolczynnik > 0:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik
                    elif (sekundy[i - 1] - wspolczynnik == 0):
                        sekundy[i] = 0

                    else:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik + 60
                        minuty[i] -= 1

                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1

                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]

                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)
                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(sekundy[4]) + "s \n"
                rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty
                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty,
                              miedzyczas_piaty]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)

    def progresD(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 10
                h_result = math.floor(x)
                h_pomoc = (float(h) % 10) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 10)
                m_ppomoc = (m_pomoc % 10) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 10)
                wspolczynnik = 3

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                szosty_kms = 0
                szosty_kmm = 0
                szosty_kmh = 0
                siodmy_kms = 0
                siodmy_kmm = 0
                siodmy_kmh = 0
                osmy_kms = 0
                osmy_kmm = 0
                osmy_kmh = 0
                dziewiaty_kms = 0
                dziewiaty_kmm = 0
                dziewiaty_kmh = 0
                dziesiaty_kms = 0
                dziesiaty_kmm = 0
                dziesiaty_kmh = 0
                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms, szosty_kms, siodmy_kms,osmy_kms, dziewiaty_kms, dziesiaty_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm, szosty_kmm, siodmy_kmm, osmy_kmm,dziewiaty_kmm, dziesiaty_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh, szosty_kmh, siodmy_kmh,osmy_kmh, dziewiaty_kmh, dziesiaty_kmh]

                if (s_result + 4.5 * wspolczynnik) < 60:
                    sekundy[0] = math.floor(s_result + 4.5 * wspolczynnik)
                elif (s_result + 4.5 * wspolczynnik) == 60:
                    sekundy[0] = 0
                    minuty[0] += 1
                else:
                    sekundy[0] = math.floor(s_result + 4.5 * wspolczynnik) - 60
                    minuty[0] += 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] - wspolczynnik > 0:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik
                    elif (sekundy[i - 1] - wspolczynnik == 0):
                        sekundy[i] = 0

                    else:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik + 60
                        minuty[i] -= 1

                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1

                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]
                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(sekundy[4]) + "s \n"
                miedzyczas_szosty = "6km: " + str(godziny[5]) + "h : " + str(minuty[5]) + "m : " + str(sekundy[5]) + "s \n"
                miedzyczas_siodmy = "7km: " + str(godziny[6]) + "h : " + str(minuty[6]) + "m : " + str(sekundy[6]) + "s \n"
                miedzyczas_osmy = "8km: " + str(godziny[7]) + "h : " + str(minuty[7]) + "m : " + str(sekundy[7]) + "s \n"
                miedzyczas_dziewiaty = "9km: " + str(godziny[8]) + "h : " + str(minuty[8]) + "m : " + str(sekundy[8]) + "s \n"
                miedzyczas_dziesiaty = "10km: " + str(godziny[9]) + "h : " + str(minuty[9]) + "m : " + str(sekundy[9]) + "s \n"
                rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty + miedzyczas_szosty + miedzyczas_siodmy + miedzyczas_osmy + miedzyczas_dziewiaty + miedzyczas_dziesiaty
                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty,
                              miedzyczas_piaty, miedzyczas_szosty, miedzyczas_siodmy, miedzyczas_osmy,
                              miedzyczas_dziewiaty, miedzyczas_dziesiaty]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)


    def progresH(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 21.097
                h_result = math.floor(x)
                h_pomoc = (float(h) % 21.097) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 21.097)
                m_ppomoc = (m_pomoc % 21.097) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 21.097)
                wspolczynnik = 2

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                szosty_kms = 0
                szosty_kmm = 0
                szosty_kmh = 0
                siodmy_kms = 0
                siodmy_kmm = 0
                siodmy_kmh = 0
                osmy_kms = 0
                osmy_kmm = 0
                osmy_kmh = 0
                dziewiaty_kms = 0
                dziewiaty_kmm = 0
                dziewiaty_kmh = 0
                dziesiaty_kms = 0
                dziesiaty_kmm = 0
                dziesiaty_kmh = 0
                jedenasty_kms = 0
                jedenasty_kmm = 0
                jedenasty_kmh = 0
                dwunasty_kms = 0
                dwunasty_kmm = 0
                dwunasty_kmh = 0
                trzynasty_kms = 0
                trzynasty_kmm = 0
                trzynasty_kmh = 0
                czternasty_kms = 0
                czternasty_kmm = 0
                czternasty_kmh = 0
                pietnasty_kms = 0
                pietnasty_kmm = 0
                pietnasty_kmh = 0
                szesnasty_kms = 0
                szesnasty_kmm = 0
                szesnasty_kmh = 0
                siedemnasty_kms = 0
                siedemnasty_kmm = 0
                siedemnasty_kmh = 0
                osiemnasty_kms = 0
                osiemnasty_kmm = 0
                osiemnasty_kmh = 0
                dziewietnasty_kms = 0
                dziewietnasty_kmm = 0
                dziewietnasty_kmh = 0
                dwudziesty_kms = 0
                dwudziesty_kmm = 0
                dwudziesty_kmh = 0
                djeden_kms = 0
                djeden_kmm = 0
                djeden_kmh = 0

                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms, szosty_kms, siodmy_kms,
                           osmy_kms, dziewiaty_kms, dziesiaty_kms, jedenasty_kms, dwunasty_kms, trzynasty_kms, czternasty_kms, pietnasty_kms, szesnasty_kms, siedemnasty_kms, osiemnasty_kms, dziewietnasty_kms, dwudziesty_kms, djeden_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm, szosty_kmm, siodmy_kmm, osmy_kmm,
                          dziewiaty_kmm, dziesiaty_kmm, jedenasty_kmm, dwunasty_kmm, trzynasty_kmm, czternasty_kmm, pietnasty_kmm, szesnasty_kmm, siedemnasty_kmm, osiemnasty_kmm, dziewietnasty_kmm, dwudziesty_kmm, djeden_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh, szosty_kmh, siodmy_kmh,
                           osmy_kmh, dziewiaty_kmh, dziesiaty_kmh, jedenasty_kmh, dwunasty_kmh, trzynasty_kmh, czternasty_kmh, pietnasty_kmh, szesnasty_kmh, siedemnasty_kmh, osiemnasty_kmh, dziewietnasty_kmh, dwudziesty_kmh, djeden_kmh]

                if (s_result + (9+(11/21)) * wspolczynnik) < 60:
                    sekundy[0] = math.floor(s_result + (9+(11/21)) * wspolczynnik)
                elif (s_result + (9+(11/21)) * wspolczynnik) == 60:
                    sekundy[0] = 0
                    minuty[0] += 1
                else:
                    sekundy[0] = math.floor(s_result + (9+(11/21)) * wspolczynnik) - 60
                    minuty[0] += 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] - wspolczynnik > 0:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik
                    elif (sekundy[i - 1] - wspolczynnik == 0):
                        sekundy[i] = 0

                    else:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik + 60
                        minuty[i] -= 1

                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1

                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]
                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(
                    sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(
                    sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(
                    sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(
                    sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(
                    sekundy[4]) + "s \n"
                miedzyczas_szosty = "6km: " + str(godziny[5]) + "h : " + str(minuty[5]) + "m : " + str(
                    sekundy[5]) + "s \n"
                miedzyczas_siodmy = "7km: " + str(godziny[6]) + "h : " + str(minuty[6]) + "m : " + str(
                    sekundy[6]) + "s \n"
                miedzyczas_osmy = "8km: " + str(godziny[7]) + "h : " + str(minuty[7]) + "m : " + str(
                    sekundy[7]) + "s \n"
                miedzyczas_dziewiaty = "9km: " + str(godziny[8]) + "h : " + str(minuty[8]) + "m : " + str(
                    sekundy[8]) + "s \n"
                miedzyczas_dziesiaty = "10km: " + str(godziny[9]) + "h : " + str(minuty[9]) + "m : " + str(
                    sekundy[9]) + "s \n"
                miedzyczas_jedenasty = "11km: " + str(godziny[10]) + "h : " + str(minuty[10]) + "m : " + str(
                    sekundy[10]) + "s \n"
                miedzyczas_dwunasty = "12km: " + str(godziny[11]) + "h : " + str(minuty[11]) + "m : " + str(
                    sekundy[11]) + "s \n"
                miedzyczas_trzynasty = "13km: " + str(godziny[12]) + "h : " + str(minuty[12]) + "m : " + str(
                    sekundy[12]) + "s \n"
                miedzyczas_czternasty = "14km: " + str(godziny[13]) + "h : " + str(minuty[13]) + "m : " + str(
                    sekundy[13]) + "s \n"
                miedzyczas_pietnasty = "15km: " + str(godziny[14]) + "h : " + str(minuty[14]) + "m : " + str(
                    sekundy[14]) + "s \n"
                miedzyczas_szesnasty = "16km: " + str(godziny[15]) + "h : " + str(minuty[15]) + "m : " + str(
                    sekundy[15]) + "s \n"
                miedzyczas_siedemnasty = "17km: " + str(godziny[16]) + "h : " + str(minuty[16]) + "m : " + str(
                    sekundy[16]) + "s \n"
                miedzyczas_osiemnasty = "18km: " + str(godziny[17]) + "h : " + str(minuty[17]) + "m : " + str(
                    sekundy[17]) + "s \n"
                miedzyczas_dziewietnasty = "19km: " + str(godziny[18]) + "h : " + str(minuty[18]) + "m : " + str(
                    sekundy[18]) + "s \n"
                miedzyczas_dwudziesty = "20km: " + str(godziny[19]) + "h : " + str(minuty[19]) + "m : " + str(
                    sekundy[19]) + "s \n"
                miedzyczas_djeden = "21km: " + str(godziny[20]) + "h : " + str(minuty[20]) + "m : " + str(
                    sekundy[20]) + "s \n"

                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty,
                              miedzyczas_piaty, miedzyczas_szosty, miedzyczas_siodmy, miedzyczas_osmy,
                              miedzyczas_dziewiaty, miedzyczas_dziesiaty, miedzyczas_jedenasty, miedzyczas_dwunasty,
                              miedzyczas_trzynasty, miedzyczas_czternasty, miedzyczas_pietnasty,
                              miedzyczas_szesnasty, miedzyczas_siedemnasty, miedzyczas_osiemnasty,
                              miedzyczas_dziewietnasty, miedzyczas_dwudziesty, miedzyczas_djeden]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)

    def progresM(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 42.195
                h_result = math.floor(x)
                h_pomoc = (float(h) % 42.195) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 42.195)
                m_ppomoc = (m_pomoc % 42.195) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 42.195)
                wspolczynnik = 1

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                szosty_kms = 0
                szosty_kmm = 0
                szosty_kmh = 0
                siodmy_kms = 0
                siodmy_kmm = 0
                siodmy_kmh = 0
                osmy_kms = 0
                osmy_kmm = 0
                osmy_kmh = 0
                dziewiaty_kms = 0
                dziewiaty_kmm = 0
                dziewiaty_kmh = 0
                dziesiaty_kms = 0
                dziesiaty_kmm = 0
                dziesiaty_kmh = 0
                jedenasty_kms = 0
                jedenasty_kmm = 0
                jedenasty_kmh = 0
                dwunasty_kms = 0
                dwunasty_kmm = 0
                dwunasty_kmh = 0
                trzynasty_kms = 0
                trzynasty_kmm = 0
                trzynasty_kmh = 0
                czternasty_kms = 0
                czternasty_kmm = 0
                czternasty_kmh = 0
                pietnasty_kms = 0
                pietnasty_kmm = 0
                pietnasty_kmh = 0
                szesnasty_kms = 0
                szesnasty_kmm = 0
                szesnasty_kmh = 0
                siedemnasty_kms = 0
                siedemnasty_kmm = 0
                siedemnasty_kmh = 0
                osiemnasty_kms = 0
                osiemnasty_kmm = 0
                osiemnasty_kmh = 0
                dziewietnasty_kms = 0
                dziewietnasty_kmm = 0
                dziewietnasty_kmh = 0
                dwudziesty_kms = 0
                dwudziesty_kmm = 0
                dwudziesty_kmh = 0
                djeden_kms = 0
                djeden_kmm = 0
                djeden_kmh = 0
                ddwa_kms = 0
                ddwa_kmm = 0
                ddwa_kmh = 0
                dtrzy_kms = 0
                dtrzy_kmm = 0
                dtrzy_kmh = 0
                dcztery_kms = 0
                dcztery_kmm = 0
                dcztery_kmh = 0
                dpiec_kms = 0
                dpiec_kmm = 0
                dpiec_kmh = 0
                dszesc_kms = 0
                dszesc_kmm = 0
                dszesc_kmh = 0
                dsiedem_kms = 0
                dsiedem_kmm = 0
                dsiedem_kmh = 0
                dosiem_kms = 0
                dosiem_kmm = 0
                dosiem_kmh = 0
                ddziewiec_kms = 0
                ddziewiec_kmm = 0
                ddziewiec_kmh = 0
                trzydziesci_kms = 0
                trzydziesci_kmm = 0
                trzydziesci_kmh = 0
                tjeden_kms = 0
                tjeden_kmm = 0
                tjeden_kmh = 0
                tdwa_kms = 0
                tdwa_kmm = 0
                tdwa_kmh = 0
                ttrzy_kms = 0
                ttrzy_kmm = 0
                ttrzy_kmh = 0
                tcztery_kms = 0
                tcztery_kmm = 0
                tcztery_kmh = 0
                tpiec_kms = 0
                tpiec_kmm = 0
                tpiec_kmh = 0
                tszesc_kms = 0
                tszesc_kmm = 0
                tszesc_kmh = 0
                tsiedem_kms = 0
                tsiedem_kmm = 0
                tsiedem_kmh = 0
                tosiem_kms = 0
                tosiem_kmm = 0
                tosiem_kmh = 0
                tdziewiec_kms = 0
                tdziewiec_kmm = 0
                tdziewiec_kmh = 0
                czterdziesci_kms = 0
                czterdziesci_kmm = 0
                czterdziesci_kmh = 0
                cjeden_kms = 0
                cjeden_kmm = 0
                cjeden_kmh = 0
                cdwa_kms = 0
                cdwa_kmm = 0
                cdwa_kmh = 0

                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms, szosty_kms, siodmy_kms,
                           osmy_kms, dziewiaty_kms, dziesiaty_kms, jedenasty_kms, dwunasty_kms, trzynasty_kms, czternasty_kms, pietnasty_kms, szesnasty_kms, siedemnasty_kms, osiemnasty_kms, dziewietnasty_kms, dwudziesty_kms, djeden_kms,
                           ddwa_kms, dtrzy_kms, dcztery_kms, dpiec_kms, dszesc_kms, dsiedem_kms,dosiem_kms,ddziewiec_kms,trzydziesci_kms, tjeden_kms, tdwa_kms, ttrzy_kms,
                           tcztery_kms,tpiec_kms,tszesc_kms, tsiedem_kms, tosiem_kms,tdziewiec_kms, czterdziesci_kms, cjeden_kms,cdwa_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm, szosty_kmm, siodmy_kmm, osmy_kmm,
                          dziewiaty_kmm, dziesiaty_kmm, jedenasty_kmm, dwunasty_kmm, trzynasty_kmm, czternasty_kmm, pietnasty_kmm, szesnasty_kmm, siedemnasty_kmm, osiemnasty_kmm, dziewietnasty_kmm, dwudziesty_kmm, djeden_kmm,
                          ddwa_kmm, dtrzy_kmm, dcztery_kmm, dpiec_kmm, dszesc_kmm, dsiedem_kmm, dosiem_kmm, ddziewiec_kmm, trzydziesci_kmm, tjeden_kmm, tdwa_kmm,
                          ttrzy_kmm, tcztery_kmm, tpiec_kmm, tszesc_kmm, tsiedem_kmm,tosiem_kmm, tdziewiec_kmm, czterdziesci_kmm, cjeden_kmm, cdwa_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh, szosty_kmh, siodmy_kmh,
                           osmy_kmh, dziewiaty_kmh, dziesiaty_kmh, jedenasty_kmh, dwunasty_kmh, trzynasty_kmh, czternasty_kmh, pietnasty_kmh, szesnasty_kmh, siedemnasty_kmh, osiemnasty_kmh, dziewietnasty_kmh, dwudziesty_kmh, djeden_kmh,
                           ddwa_kmh, dtrzy_kmh, dcztery_kmh, dpiec_kmh, dszesc_kmh, dsiedem_kmh, dosiem_kmh, ddziewiec_kmh, ddziewiec_kmh, trzydziesci_kmh, tjeden_kmh, tdwa_kmh,
                           ttrzy_kmh, tcztery_kmh, tpiec_kmh, tszesc_kmh, tsiedem_kmh, tosiem_kmh, tdziewiec_kmh, czterdziesci_kmh, cjeden_kmh, cdwa_kmh]


                if (s_result + (20.5) * wspolczynnik) < 60:
                    sekundy[0] = math.floor(s_result + (20.5) * wspolczynnik)
                elif (s_result + (20.5) * wspolczynnik) == 60:
                    sekundy[0] = 0
                    minuty[0] += 1
                else:
                    sekundy[0] = math.floor(s_result + (20.5) * wspolczynnik) - 60
                    minuty[0] += 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] - wspolczynnik > 0:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik
                    elif (sekundy[i - 1] - wspolczynnik == 0):
                        sekundy[i] = 0

                    else:
                        sekundy[i] = sekundy[i - 1] - wspolczynnik + 60
                        minuty[i] -= 1

                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1

                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]


                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(
                    sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(
                    sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(
                    sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(
                    sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(
                    sekundy[4]) + "s \n"
                miedzyczas_szosty = "6km: " + str(godziny[5]) + "h : " + str(minuty[5]) + "m : " + str(
                    sekundy[5]) + "s \n"
                miedzyczas_siodmy = "7km: " + str(godziny[6]) + "h : " + str(minuty[6]) + "m : " + str(
                    sekundy[6]) + "s \n"
                miedzyczas_osmy = "8km: " + str(godziny[7]) + "h : " + str(minuty[7]) + "m : " + str(
                    sekundy[7]) + "s \n"
                miedzyczas_dziewiaty = "9km: " + str(godziny[8]) + "h : " + str(minuty[8]) + "m : " + str(
                    sekundy[8]) + "s \n"
                miedzyczas_dziesiaty = "10km: " + str(godziny[9]) + "h : " + str(minuty[9]) + "m : " + str(
                    sekundy[9]) + "s \n"
                miedzyczas_jedenasty = "11km: " + str(godziny[10]) + "h : " + str(minuty[10]) + "m : " + str(
                    sekundy[10]) + "s \n"
                miedzyczas_dwunasty = "12km: " + str(godziny[11]) + "h : " + str(minuty[11]) + "m : " + str(
                    sekundy[11]) + "s \n"
                miedzyczas_trzynasty = "13km: " + str(godziny[12]) + "h : " + str(minuty[12]) + "m : " + str(
                    sekundy[12]) + "s \n"
                miedzyczas_czternasty = "14km: " + str(godziny[13]) + "h : " + str(minuty[13]) + "m : " + str(
                    sekundy[13]) + "s \n"
                miedzyczas_pietnasty = "15km: " + str(godziny[14]) + "h : " + str(minuty[14]) + "m : " + str(
                    sekundy[14]) + "s \n"
                miedzyczas_szesnasty = "16km: " + str(godziny[15]) + "h : " + str(minuty[15]) + "m : " + str(
                    sekundy[15]) + "s \n"
                miedzyczas_siedemnasty = "17km: " + str(godziny[16]) + "h : " + str(minuty[16]) + "m : " + str(
                    sekundy[16]) + "s \n"
                miedzyczas_osiemnasty = "18km: " + str(godziny[17]) + "h : " + str(minuty[17]) + "m : " + str(
                    sekundy[17]) + "s \n"
                miedzyczas_dziewietnasty = "19km: " + str(godziny[18]) + "h : " + str(minuty[18]) + "m : " + str(
                    sekundy[18]) + "s \n"
                miedzyczas_dwudziesty = "20km: " + str(godziny[19]) + "h : " + str(minuty[19]) + "m : " + str(
                    sekundy[19]) + "s \n"
                miedzyczas_djeden = "21km: " + str(godziny[20]) + "h : " + str(minuty[20]) + "m : " + str(
                    sekundy[20]) + "s \n"
                miedzyczas_ddwa = "22km: " + str(godziny[21]) + "h : " + str(minuty[21]) + "m : " + str(
                    sekundy[21]) + "s \n"
                miedzyczas_dtrzy = "23km: " + str(godziny[22]) + "h : " + str(minuty[22]) + "m : " + str(
                    sekundy[22]) + "s \n"
                miedzyczas_dcztery = "24km: " + str(godziny[23]) + "h : " + str(minuty[23]) + "m : " + str(
                    sekundy[23]) + "s \n"
                miedzyczas_dpiec = "25km: " + str(godziny[24]) + "h : " + str(minuty[24]) + "m : " + str(
                    sekundy[24]) + "s \n"
                miedzyczas_dszesc = "26km: " + str(godziny[25]) + "h : " + str(minuty[25]) + "m : " + str(
                    sekundy[25]) + "s \n"
                miedzyczas_dsiedem = "27km: " + str(godziny[26]) + "h : " + str(minuty[26]) + "m : " + str(
                    sekundy[26]) + "s \n"
                miedzyczas_dosiem = "28km: " + str(godziny[27]) + "h : " + str(minuty[27]) + "m : " + str(
                    sekundy[27]) + "s \n"
                miedzyczas_ddziewiec = "29km: " + str(godziny[28]) + "h : " + str(minuty[28]) + "m : " + str(
                    sekundy[28]) + "s \n"
                miedzyczas_trzydziesci = "30km: " + str(godziny[29]) + "h : " + str(minuty[29]) + "m : " + str(
                    sekundy[29]) + "s \n"
                miedzyczas_tjeden = "31km: " + str(godziny[30]) + "h : " + str(minuty[30]) + "m : " + str(
                    sekundy[30]) + "s \n"
                miedzyczas_tdwa = "32km: " + str(godziny[31]) + "h : " + str(minuty[31]) + "m : " + str(
                    sekundy[31]) + "s \n"
                miedzyczas_ttrzy = "33km: " + str(godziny[32]) + "h : " + str(minuty[32]) + "m : " + str(
                    sekundy[32]) + "s \n"
                miedzyczas_tcztery = "34km: " + str(godziny[33]) + "h : " + str(minuty[33]) + "m : " + str(
                    sekundy[33]) + "s \n"
                miedzyczas_tpiec = "35km: " + str(godziny[34]) + "h : " + str(minuty[34]) + "m : " + str(
                    sekundy[34]) + "s \n"
                miedzyczas_tszesc = "36km: " + str(godziny[35]) + "h : " + str(minuty[35]) + "m : " + str(
                    sekundy[35]) + "s \n"
                miedzyczas_tsiedem = "37km: " + str(godziny[36]) + "h : " + str(minuty[36]) + "m : " + str(
                    sekundy[36]) + "s \n"
                miedzyczas_tosiem = "38km: " + str(godziny[37]) + "h : " + str(minuty[37]) + "m : " + str(
                    sekundy[37]) + "s \n"
                miedzyczas_tdziewiec = "39km: " + str(godziny[38]) + "h : " + str(minuty[38]) + "m : " + str(
                    sekundy[38]) + "s \n"
                miedzyczas_czterdziesci = "40km: " + str(godziny[39]) + "h : " + str(minuty[39]) + "m : " + str(
                    sekundy[39]) + "s \n"
                miedzyczas_cjeden = "41km: " + str(godziny[40]) + "h : " + str(minuty[40]) + "m : " + str(
                    sekundy[40]) + "s \n"
                miedzyczas_cdwa = "42km: " + str(godziny[41]) + "h : " + str(minuty[41]) + "m : " + str(
                    sekundy[41]) + "s \n"

                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty, miedzyczas_piaty, miedzyczas_szosty, miedzyczas_siodmy, miedzyczas_osmy, miedzyczas_dziewiaty, miedzyczas_dziesiaty,miedzyczas_jedenasty, miedzyczas_dwunasty, miedzyczas_trzynasty, miedzyczas_czternasty, miedzyczas_pietnasty, miedzyczas_szesnasty, miedzyczas_siedemnasty, miedzyczas_osiemnasty, miedzyczas_dziewietnasty, miedzyczas_dwudziesty, miedzyczas_djeden,
                              miedzyczas_ddwa, miedzyczas_dtrzy, miedzyczas_dcztery, miedzyczas_dpiec, miedzyczas_dszesc, miedzyczas_dsiedem, miedzyczas_dosiem, miedzyczas_ddziewiec, miedzyczas_trzydziesci, miedzyczas_tjeden,
                              miedzyczas_tdwa, miedzyczas_ttrzy, miedzyczas_tcztery, miedzyczas_tpiec, miedzyczas_tszesc, miedzyczas_tsiedem, miedzyczas_tosiem, miedzyczas_tdziewiec, miedzyczas_czterdziesci, miedzyczas_cjeden, miedzyczas_cdwa]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)


    def timeProgres(self):
        if (len(self.godziny.text()) == 0) and (len(self.minuty.text()) == 0) and (len(self.sekundy.text()) == 0):
            komunikat = "Podaj czas"

            self.result.clear()
            self.result.addItem(komunikat)
        else:
            if self.TButton.isChecked():
                self.progresT()


            elif self.PButton.isChecked():
                self.progresP()
            elif self.DButton.isChecked():
                self.progresD()
            elif self.HButton.isChecked():
                self.progresH()
            elif self.MButton.isChecked():
                self.progresM()

    def regresT(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 3
                h_result = math.floor(x)
                h_pomoc = (float(h) % 3) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 3)
                m_ppomoc = (m_pomoc % 3) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 3)
                wspolczynnik = 5

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh]
                if (s_result - wspolczynnik) > 0:
                    sekundy[0] = s_result - wspolczynnik
                elif (s_result - wspolczynnik) == 0:
                    sekundy[0] = 0

                else:
                    sekundy[0] = (s_result - wspolczynnik) + 60
                    minuty[0] -= 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] + wspolczynnik <60:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik
                    elif (sekundy[i - 1] + wspolczynnik == 60):
                        sekundy[i] = 0
                        minuty[i] += 1

                    else:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik - 60
                        minuty[i] += 1



                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1


                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]

                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(sekundy[2]) + "s \n"
                rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci
                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)

        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)

    def regresP(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 5
                h_result = math.floor(x)
                h_pomoc = (float(h) % 5) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 5)
                m_ppomoc = (m_pomoc % 5) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 5)
                wspolczynnik = 4

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh]

                if (s_result - 2*wspolczynnik) > 0:
                    sekundy[0] = s_result - 2*wspolczynnik
                elif (s_result - 2*wspolczynnik) == 0:
                    sekundy[0] = 0

                else:
                    sekundy[0] = (s_result - 2*wspolczynnik) + 60
                    minuty[0] -= 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] + wspolczynnik <60:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik
                    elif (sekundy[i - 1] + wspolczynnik == 60):
                        sekundy[i] = 0
                        minuty[i] += 1

                    else:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik - 60
                        minuty[i] += 1



                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1


                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]

                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)
                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(sekundy[4]) + "s \n"
                rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty
                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty,
                              miedzyczas_piaty]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)



    def regresD(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 10
                h_result = math.floor(x)
                h_pomoc = (float(h) % 10) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 10)
                m_ppomoc = (m_pomoc % 10) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 10)
                wspolczynnik = 3

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                szosty_kms = 0
                szosty_kmm = 0
                szosty_kmh = 0
                siodmy_kms = 0
                siodmy_kmm = 0
                siodmy_kmh = 0
                osmy_kms = 0
                osmy_kmm = 0
                osmy_kmh = 0
                dziewiaty_kms = 0
                dziewiaty_kmm = 0
                dziewiaty_kmh = 0
                dziesiaty_kms = 0
                dziesiaty_kmm = 0
                dziesiaty_kmh = 0
                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms, szosty_kms, siodmy_kms,osmy_kms, dziewiaty_kms, dziesiaty_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm, szosty_kmm, siodmy_kmm, osmy_kmm,dziewiaty_kmm, dziesiaty_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh, szosty_kmh, siodmy_kmh,osmy_kmh, dziewiaty_kmh, dziesiaty_kmh]

                if (s_result - 4.5 * wspolczynnik) > 0:
                    sekundy[0] = math.floor(s_result - 4.5 * wspolczynnik)
                elif (s_result - 4.5 * wspolczynnik) == 0:
                    sekundy[0] = 0
                else:
                    sekundy[0] = math.floor(s_result - 4.5 * wspolczynnik) + 60
                    minuty[0] -= 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] + wspolczynnik <60:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik
                    elif (sekundy[i - 1] + wspolczynnik == 60):
                        sekundy[i] = 0
                        minuty[i] += 1

                    else:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik - 60
                        minuty[i] += 1



                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1


                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]

                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(sekundy[4]) + "s \n"
                miedzyczas_szosty = "6km: " + str(godziny[5]) + "h : " + str(minuty[5]) + "m : " + str(sekundy[5]) + "s \n"
                miedzyczas_siodmy = "7km: " + str(godziny[6]) + "h : " + str(minuty[6]) + "m : " + str(sekundy[6]) + "s \n"
                miedzyczas_osmy = "8km: " + str(godziny[7]) + "h : " + str(minuty[7]) + "m : " + str(sekundy[7]) + "s \n"
                miedzyczas_dziewiaty = "9km: " + str(godziny[8]) + "h : " + str(minuty[8]) + "m : " + str(sekundy[8]) + "s \n"
                miedzyczas_dziesiaty = "10km: " + str(godziny[9]) + "h : " + str(minuty[9]) + "m : " + str(sekundy[9]) + "s \n"
                rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty + miedzyczas_szosty + miedzyczas_siodmy + miedzyczas_osmy + miedzyczas_dziewiaty + miedzyczas_dziesiaty
                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty,
                              miedzyczas_piaty, miedzyczas_szosty, miedzyczas_siodmy, miedzyczas_osmy,
                              miedzyczas_dziewiaty, miedzyczas_dziesiaty]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)


    def regresH(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 21.097
                h_result = math.floor(x)
                h_pomoc = (float(h) % 21.097) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 21.097)
                m_ppomoc = (m_pomoc % 21.097) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 21.097)
                wspolczynnik = 2

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                szosty_kms = 0
                szosty_kmm = 0
                szosty_kmh = 0
                siodmy_kms = 0
                siodmy_kmm = 0
                siodmy_kmh = 0
                osmy_kms = 0
                osmy_kmm = 0
                osmy_kmh = 0
                dziewiaty_kms = 0
                dziewiaty_kmm = 0
                dziewiaty_kmh = 0
                dziesiaty_kms = 0
                dziesiaty_kmm = 0
                dziesiaty_kmh = 0
                jedenasty_kms = 0
                jedenasty_kmm = 0
                jedenasty_kmh = 0
                dwunasty_kms = 0
                dwunasty_kmm = 0
                dwunasty_kmh = 0
                trzynasty_kms = 0
                trzynasty_kmm = 0
                trzynasty_kmh = 0
                czternasty_kms = 0
                czternasty_kmm = 0
                czternasty_kmh = 0
                pietnasty_kms = 0
                pietnasty_kmm = 0
                pietnasty_kmh = 0
                szesnasty_kms = 0
                szesnasty_kmm = 0
                szesnasty_kmh = 0
                siedemnasty_kms = 0
                siedemnasty_kmm = 0
                siedemnasty_kmh = 0
                osiemnasty_kms = 0
                osiemnasty_kmm = 0
                osiemnasty_kmh = 0
                dziewietnasty_kms = 0
                dziewietnasty_kmm = 0
                dziewietnasty_kmh = 0
                dwudziesty_kms = 0
                dwudziesty_kmm = 0
                dwudziesty_kmh = 0
                djeden_kms = 0
                djeden_kmm = 0
                djeden_kmh = 0

                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms, szosty_kms, siodmy_kms,
                           osmy_kms, dziewiaty_kms, dziesiaty_kms, jedenasty_kms, dwunasty_kms, trzynasty_kms, czternasty_kms, pietnasty_kms, szesnasty_kms, siedemnasty_kms, osiemnasty_kms, dziewietnasty_kms, dwudziesty_kms, djeden_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm, szosty_kmm, siodmy_kmm, osmy_kmm,
                          dziewiaty_kmm, dziesiaty_kmm, jedenasty_kmm, dwunasty_kmm, trzynasty_kmm, czternasty_kmm, pietnasty_kmm, szesnasty_kmm, siedemnasty_kmm, osiemnasty_kmm, dziewietnasty_kmm, dwudziesty_kmm, djeden_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh, szosty_kmh, siodmy_kmh,
                           osmy_kmh, dziewiaty_kmh, dziesiaty_kmh, jedenasty_kmh, dwunasty_kmh, trzynasty_kmh, czternasty_kmh, pietnasty_kmh, szesnasty_kmh, siedemnasty_kmh, osiemnasty_kmh, dziewietnasty_kmh, dwudziesty_kmh, djeden_kmh]


                if (s_result - (9 + (11 / 21)) * wspolczynnik) > 0:
                    sekundy[0] = math.floor(s_result - (9 + (11 / 21)) * wspolczynnik)
                elif (s_result - (9 + (11 / 21)) * wspolczynnik) == 0:
                    sekundy[0] = 0
                else:
                    sekundy[0] = math.floor(s_result - (9 + (11 / 21)) * wspolczynnik) + 60
                    minuty[0] -= 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] + wspolczynnik <60:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik
                    elif (sekundy[i - 1] + wspolczynnik == 60):
                        sekundy[i] = 0
                        minuty[i] += 1

                    else:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik - 60
                        minuty[i] += 1



                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1


                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]

                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(
                    sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(
                    sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(
                    sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(
                    sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(
                    sekundy[4]) + "s \n"
                miedzyczas_szosty = "6km: " + str(godziny[5]) + "h : " + str(minuty[5]) + "m : " + str(
                    sekundy[5]) + "s \n"
                miedzyczas_siodmy = "7km: " + str(godziny[6]) + "h : " + str(minuty[6]) + "m : " + str(
                    sekundy[6]) + "s \n"
                miedzyczas_osmy = "8km: " + str(godziny[7]) + "h : " + str(minuty[7]) + "m : " + str(
                    sekundy[7]) + "s \n"
                miedzyczas_dziewiaty = "9km: " + str(godziny[8]) + "h : " + str(minuty[8]) + "m : " + str(
                    sekundy[8]) + "s \n"
                miedzyczas_dziesiaty = "10km: " + str(godziny[9]) + "h : " + str(minuty[9]) + "m : " + str(
                    sekundy[9]) + "s \n"
                miedzyczas_jedenasty = "11km: " + str(godziny[10]) + "h : " + str(minuty[10]) + "m : " + str(
                    sekundy[10]) + "s \n"
                miedzyczas_dwunasty = "12km: " + str(godziny[11]) + "h : " + str(minuty[11]) + "m : " + str(
                    sekundy[11]) + "s \n"
                miedzyczas_trzynasty = "13km: " + str(godziny[12]) + "h : " + str(minuty[12]) + "m : " + str(
                    sekundy[12]) + "s \n"
                miedzyczas_czternasty = "14km: " + str(godziny[13]) + "h : " + str(minuty[13]) + "m : " + str(
                    sekundy[13]) + "s \n"
                miedzyczas_pietnasty = "15km: " + str(godziny[14]) + "h : " + str(minuty[14]) + "m : " + str(
                    sekundy[14]) + "s \n"
                miedzyczas_szesnasty = "16km: " + str(godziny[15]) + "h : " + str(minuty[15]) + "m : " + str(
                    sekundy[15]) + "s \n"
                miedzyczas_siedemnasty = "17km: " + str(godziny[16]) + "h : " + str(minuty[16]) + "m : " + str(
                    sekundy[16]) + "s \n"
                miedzyczas_osiemnasty = "18km: " + str(godziny[17]) + "h : " + str(minuty[17]) + "m : " + str(
                    sekundy[17]) + "s \n"
                miedzyczas_dziewietnasty = "19km: " + str(godziny[18]) + "h : " + str(minuty[18]) + "m : " + str(
                    sekundy[18]) + "s \n"
                miedzyczas_dwudziesty = "20km: " + str(godziny[19]) + "h : " + str(minuty[19]) + "m : " + str(
                    sekundy[19]) + "s \n"
                miedzyczas_djeden = "21km: " + str(godziny[20]) + "h : " + str(minuty[20]) + "m : " + str(
                    sekundy[20]) + "s \n"

                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty,
                              miedzyczas_piaty, miedzyczas_szosty, miedzyczas_siodmy, miedzyczas_osmy,
                              miedzyczas_dziewiaty, miedzyczas_dziesiaty, miedzyczas_jedenasty, miedzyczas_dwunasty,
                              miedzyczas_trzynasty, miedzyczas_czternasty, miedzyczas_pietnasty,
                              miedzyczas_szesnasty, miedzyczas_siedemnasty, miedzyczas_osiemnasty,
                              miedzyczas_dziewietnasty, miedzyczas_dwudziesty, miedzyczas_djeden]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)



    def regresM(self):
        h = self.godziny.text()
        m = self.minuty.text()
        s = self.sekundy.text()
        h = str(h)
        m = str(m)
        s = str(s)
        try:
            int(h)
            int(m)
            int(s)
            if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                x = float(h) / 42.195
                h_result = math.floor(x)
                h_pomoc = (float(h) % 42.195) * 60
                m_pomoc = float(m) + h_pomoc
                m_result = math.floor(m_pomoc / 42.195)
                m_ppomoc = (m_pomoc % 42.195) * 60
                s_pomoc = m_ppomoc + float(s)
                s_result = math.floor(s_pomoc / 42.195)
                wspolczynnik = 1

                pierwszy_kms = s_result
                pierwszy_kmm = m_result
                pierwszy_kmh = h_result
                drugi_kms = 0
                drugi_kmm = 0
                drugi_kmh = 0
                trzeci_kms = 0
                trzeci_kmm = 0
                trzeci_kmh = 0
                czwarty_kms = 0
                czwarty_kmm = 0
                czwarty_kmh = 0
                piaty_kms = 0
                piaty_kmm = 0
                piaty_kmh = 0
                szosty_kms = 0
                szosty_kmm = 0
                szosty_kmh = 0
                siodmy_kms = 0
                siodmy_kmm = 0
                siodmy_kmh = 0
                osmy_kms = 0
                osmy_kmm = 0
                osmy_kmh = 0
                dziewiaty_kms = 0
                dziewiaty_kmm = 0
                dziewiaty_kmh = 0
                dziesiaty_kms = 0
                dziesiaty_kmm = 0
                dziesiaty_kmh = 0
                jedenasty_kms = 0
                jedenasty_kmm = 0
                jedenasty_kmh = 0
                dwunasty_kms = 0
                dwunasty_kmm = 0
                dwunasty_kmh = 0
                trzynasty_kms = 0
                trzynasty_kmm = 0
                trzynasty_kmh = 0
                czternasty_kms = 0
                czternasty_kmm = 0
                czternasty_kmh = 0
                pietnasty_kms = 0
                pietnasty_kmm = 0
                pietnasty_kmh = 0
                szesnasty_kms = 0
                szesnasty_kmm = 0
                szesnasty_kmh = 0
                siedemnasty_kms = 0
                siedemnasty_kmm = 0
                siedemnasty_kmh = 0
                osiemnasty_kms = 0
                osiemnasty_kmm = 0
                osiemnasty_kmh = 0
                dziewietnasty_kms = 0
                dziewietnasty_kmm = 0
                dziewietnasty_kmh = 0
                dwudziesty_kms = 0
                dwudziesty_kmm = 0
                dwudziesty_kmh = 0
                djeden_kms = 0
                djeden_kmm = 0
                djeden_kmh = 0
                ddwa_kms = 0
                ddwa_kmm = 0
                ddwa_kmh = 0
                dtrzy_kms = 0
                dtrzy_kmm = 0
                dtrzy_kmh = 0
                dcztery_kms = 0
                dcztery_kmm = 0
                dcztery_kmh = 0
                dpiec_kms = 0
                dpiec_kmm = 0
                dpiec_kmh = 0
                dszesc_kms = 0
                dszesc_kmm = 0
                dszesc_kmh = 0
                dsiedem_kms = 0
                dsiedem_kmm = 0
                dsiedem_kmh = 0
                dosiem_kms = 0
                dosiem_kmm = 0
                dosiem_kmh = 0
                ddziewiec_kms = 0
                ddziewiec_kmm = 0
                ddziewiec_kmh = 0
                trzydziesci_kms = 0
                trzydziesci_kmm = 0
                trzydziesci_kmh = 0
                tjeden_kms = 0
                tjeden_kmm = 0
                tjeden_kmh = 0
                tdwa_kms = 0
                tdwa_kmm = 0
                tdwa_kmh = 0
                ttrzy_kms = 0
                ttrzy_kmm = 0
                ttrzy_kmh = 0
                tcztery_kms = 0
                tcztery_kmm = 0
                tcztery_kmh = 0
                tpiec_kms = 0
                tpiec_kmm = 0
                tpiec_kmh = 0
                tszesc_kms = 0
                tszesc_kmm = 0
                tszesc_kmh = 0
                tsiedem_kms = 0
                tsiedem_kmm = 0
                tsiedem_kmh = 0
                tosiem_kms = 0
                tosiem_kmm = 0
                tosiem_kmh = 0
                tdziewiec_kms = 0
                tdziewiec_kmm = 0
                tdziewiec_kmh = 0
                czterdziesci_kms = 0
                czterdziesci_kmm = 0
                czterdziesci_kmh = 0
                cjeden_kms = 0
                cjeden_kmm = 0
                cjeden_kmh = 0
                cdwa_kms = 0
                cdwa_kmm = 0
                cdwa_kmh = 0

                sekundy = [pierwszy_kms, drugi_kms, trzeci_kms, czwarty_kms, piaty_kms, szosty_kms, siodmy_kms,
                           osmy_kms, dziewiaty_kms, dziesiaty_kms, jedenasty_kms, dwunasty_kms, trzynasty_kms, czternasty_kms, pietnasty_kms, szesnasty_kms, siedemnasty_kms, osiemnasty_kms, dziewietnasty_kms, dwudziesty_kms, djeden_kms,
                           ddwa_kms, dtrzy_kms, dcztery_kms, dpiec_kms, dszesc_kms, dsiedem_kms,dosiem_kms,ddziewiec_kms,trzydziesci_kms, tjeden_kms, tdwa_kms, ttrzy_kms,
                           tcztery_kms,tpiec_kms,tszesc_kms, tsiedem_kms, tosiem_kms,tdziewiec_kms, czterdziesci_kms, cjeden_kms,cdwa_kms]
                minuty = [pierwszy_kmm, drugi_kmm, trzeci_kmm, czwarty_kmm, piaty_kmm, szosty_kmm, siodmy_kmm, osmy_kmm,
                          dziewiaty_kmm, dziesiaty_kmm, jedenasty_kmm, dwunasty_kmm, trzynasty_kmm, czternasty_kmm, pietnasty_kmm, szesnasty_kmm, siedemnasty_kmm, osiemnasty_kmm, dziewietnasty_kmm, dwudziesty_kmm, djeden_kmm,
                          ddwa_kmm, dtrzy_kmm, dcztery_kmm, dpiec_kmm, dszesc_kmm, dsiedem_kmm, dosiem_kmm, ddziewiec_kmm, trzydziesci_kmm, tjeden_kmm, tdwa_kmm,
                          ttrzy_kmm, tcztery_kmm, tpiec_kmm, tszesc_kmm, tsiedem_kmm,tosiem_kmm, tdziewiec_kmm, czterdziesci_kmm, cjeden_kmm, cdwa_kmm]
                godziny = [pierwszy_kmh, drugi_kmh, trzeci_kmh, czwarty_kmh, piaty_kmh, szosty_kmh, siodmy_kmh,
                           osmy_kmh, dziewiaty_kmh, dziesiaty_kmh, jedenasty_kmh, dwunasty_kmh, trzynasty_kmh, czternasty_kmh, pietnasty_kmh, szesnasty_kmh, siedemnasty_kmh, osiemnasty_kmh, dziewietnasty_kmh, dwudziesty_kmh, djeden_kmh,
                           ddwa_kmh, dtrzy_kmh, dcztery_kmh, dpiec_kmh, dszesc_kmh, dsiedem_kmh, dosiem_kmh, ddziewiec_kmh, ddziewiec_kmh, trzydziesci_kmh, tjeden_kmh, tdwa_kmh,
                           ttrzy_kmh, tcztery_kmh, tpiec_kmh, tszesc_kmh, tsiedem_kmh, tosiem_kmh, tdziewiec_kmh, czterdziesci_kmh, cjeden_kmh, cdwa_kmh]


                if (s_result - 20.5 * wspolczynnik) > 0:
                    sekundy[0] = math.floor(s_result - 20.5 * wspolczynnik)
                elif (s_result - 20.5 * wspolczynnik) == 0:
                    sekundy[0] = 0
                else:
                    sekundy[0] = math.floor(s_result - 20.5 * wspolczynnik) + 60
                    minuty[0] -= 1

                for i in range(1, len(sekundy)):
                    if sekundy[i - 1] + wspolczynnik <60:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik
                    elif (sekundy[i - 1] + wspolczynnik == 60):
                        sekundy[i] = 0
                        minuty[i] += 1

                    else:
                        sekundy[i] = sekundy[i - 1] + wspolczynnik - 60
                        minuty[i] += 1



                for i in range(1, (len(minuty))):
                    if (minuty[i - 1] + minuty[i]) < 60:
                        minuty[i] += minuty[i - 1]
                    elif (minuty[i - 1] + minuty[i]) == 60:
                        minuty[i] = 0
                        godziny[i] += 1
                    else:
                        minuty[i] = minuty[i - 1] + minuty[i] - 60
                        godziny[i] += 1


                for i in range(1, len(godziny)):
                    godziny[i] += godziny[i - 1]


                h_result = str(h_result)
                m_result = str(m_result)
                s_result = str(s_result)

                czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                miedzyczas_pierwszy = "1 km: " + str(godziny[0]) + "h : " + str(minuty[0]) + "m : " + str(
                    sekundy[0]) + "s \n"
                miedzyczas_drugi = "2 km: " + str(godziny[1]) + "h : " + str(minuty[1]) + "m : " + str(
                    sekundy[1]) + "s \n"
                miedzyczas_trzeci = "3 km: " + str(godziny[2]) + "h : " + str(minuty[2]) + "m : " + str(
                    sekundy[2]) + "s \n"
                miedzyczas_czwarty = "4km: " + str(godziny[3]) + "h : " + str(minuty[3]) + "m : " + str(
                    sekundy[3]) + "s \n"
                miedzyczas_piaty = "5km: " + str(godziny[4]) + "h : " + str(minuty[4]) + "m : " + str(
                    sekundy[4]) + "s \n"
                miedzyczas_szosty = "6km: " + str(godziny[5]) + "h : " + str(minuty[5]) + "m : " + str(
                    sekundy[5]) + "s \n"
                miedzyczas_siodmy = "7km: " + str(godziny[6]) + "h : " + str(minuty[6]) + "m : " + str(
                    sekundy[6]) + "s \n"
                miedzyczas_osmy = "8km: " + str(godziny[7]) + "h : " + str(minuty[7]) + "m : " + str(
                    sekundy[7]) + "s \n"
                miedzyczas_dziewiaty = "9km: " + str(godziny[8]) + "h : " + str(minuty[8]) + "m : " + str(
                    sekundy[8]) + "s \n"
                miedzyczas_dziesiaty = "10km: " + str(godziny[9]) + "h : " + str(minuty[9]) + "m : " + str(
                    sekundy[9]) + "s \n"
                miedzyczas_jedenasty = "11km: " + str(godziny[10]) + "h : " + str(minuty[10]) + "m : " + str(
                    sekundy[10]) + "s \n"
                miedzyczas_dwunasty = "12km: " + str(godziny[11]) + "h : " + str(minuty[11]) + "m : " + str(
                    sekundy[11]) + "s \n"
                miedzyczas_trzynasty = "13km: " + str(godziny[12]) + "h : " + str(minuty[12]) + "m : " + str(
                    sekundy[12]) + "s \n"
                miedzyczas_czternasty = "14km: " + str(godziny[13]) + "h : " + str(minuty[13]) + "m : " + str(
                    sekundy[13]) + "s \n"
                miedzyczas_pietnasty = "15km: " + str(godziny[14]) + "h : " + str(minuty[14]) + "m : " + str(
                    sekundy[14]) + "s \n"
                miedzyczas_szesnasty = "16km: " + str(godziny[15]) + "h : " + str(minuty[15]) + "m : " + str(
                    sekundy[15]) + "s \n"
                miedzyczas_siedemnasty = "17km: " + str(godziny[16]) + "h : " + str(minuty[16]) + "m : " + str(
                    sekundy[16]) + "s \n"
                miedzyczas_osiemnasty = "18km: " + str(godziny[17]) + "h : " + str(minuty[17]) + "m : " + str(
                    sekundy[17]) + "s \n"
                miedzyczas_dziewietnasty = "19km: " + str(godziny[18]) + "h : " + str(minuty[18]) + "m : " + str(
                    sekundy[18]) + "s \n"
                miedzyczas_dwudziesty = "20km: " + str(godziny[19]) + "h : " + str(minuty[19]) + "m : " + str(
                    sekundy[19]) + "s \n"
                miedzyczas_djeden = "21km: " + str(godziny[20]) + "h : " + str(minuty[20]) + "m : " + str(
                    sekundy[20]) + "s \n"
                miedzyczas_ddwa = "22km: " + str(godziny[21]) + "h : " + str(minuty[21]) + "m : " + str(
                    sekundy[21]) + "s \n"
                miedzyczas_dtrzy = "23km: " + str(godziny[22]) + "h : " + str(minuty[22]) + "m : " + str(
                    sekundy[22]) + "s \n"
                miedzyczas_dcztery = "24km: " + str(godziny[23]) + "h : " + str(minuty[23]) + "m : " + str(
                    sekundy[23]) + "s \n"
                miedzyczas_dpiec = "25km: " + str(godziny[24]) + "h : " + str(minuty[24]) + "m : " + str(
                    sekundy[24]) + "s \n"
                miedzyczas_dszesc = "26km: " + str(godziny[25]) + "h : " + str(minuty[25]) + "m : " + str(
                    sekundy[25]) + "s \n"
                miedzyczas_dsiedem = "27km: " + str(godziny[26]) + "h : " + str(minuty[26]) + "m : " + str(
                    sekundy[26]) + "s \n"
                miedzyczas_dosiem = "28km: " + str(godziny[27]) + "h : " + str(minuty[27]) + "m : " + str(
                    sekundy[27]) + "s \n"
                miedzyczas_ddziewiec = "29km: " + str(godziny[28]) + "h : " + str(minuty[28]) + "m : " + str(
                    sekundy[28]) + "s \n"
                miedzyczas_trzydziesci = "30km: " + str(godziny[29]) + "h : " + str(minuty[29]) + "m : " + str(
                    sekundy[29]) + "s \n"
                miedzyczas_tjeden = "31km: " + str(godziny[30]) + "h : " + str(minuty[30]) + "m : " + str(
                    sekundy[30]) + "s \n"
                miedzyczas_tdwa = "32km: " + str(godziny[31]) + "h : " + str(minuty[31]) + "m : " + str(
                    sekundy[31]) + "s \n"
                miedzyczas_ttrzy = "33km: " + str(godziny[32]) + "h : " + str(minuty[32]) + "m : " + str(
                    sekundy[32]) + "s \n"
                miedzyczas_tcztery = "34km: " + str(godziny[33]) + "h : " + str(minuty[33]) + "m : " + str(
                    sekundy[33]) + "s \n"
                miedzyczas_tpiec = "35km: " + str(godziny[34]) + "h : " + str(minuty[34]) + "m : " + str(
                    sekundy[34]) + "s \n"
                miedzyczas_tszesc = "36km: " + str(godziny[35]) + "h : " + str(minuty[35]) + "m : " + str(
                    sekundy[35]) + "s \n"
                miedzyczas_tsiedem = "37km: " + str(godziny[36]) + "h : " + str(minuty[36]) + "m : " + str(
                    sekundy[36]) + "s \n"
                miedzyczas_tosiem = "38km: " + str(godziny[37]) + "h : " + str(minuty[37]) + "m : " + str(
                    sekundy[37]) + "s \n"
                miedzyczas_tdziewiec = "39km: " + str(godziny[38]) + "h : " + str(minuty[38]) + "m : " + str(
                    sekundy[38]) + "s \n"
                miedzyczas_czterdziesci = "40km: " + str(godziny[39]) + "h : " + str(minuty[39]) + "m : " + str(
                    sekundy[39]) + "s \n"
                miedzyczas_cjeden = "41km: " + str(godziny[40]) + "h : " + str(minuty[40]) + "m : " + str(
                    sekundy[40]) + "s \n"
                miedzyczas_cdwa = "42km: " + str(godziny[41]) + "h : " + str(minuty[41]) + "m : " + str(
                    sekundy[41]) + "s \n"

                miedzyczas = [miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci, miedzyczas_czwarty, miedzyczas_piaty, miedzyczas_szosty, miedzyczas_siodmy, miedzyczas_osmy, miedzyczas_dziewiaty, miedzyczas_dziesiaty,miedzyczas_jedenasty, miedzyczas_dwunasty, miedzyczas_trzynasty, miedzyczas_czternasty, miedzyczas_pietnasty, miedzyczas_szesnasty, miedzyczas_siedemnasty, miedzyczas_osiemnasty, miedzyczas_dziewietnasty, miedzyczas_dwudziesty, miedzyczas_djeden,
                              miedzyczas_ddwa, miedzyczas_dtrzy, miedzyczas_dcztery, miedzyczas_dpiec, miedzyczas_dszesc, miedzyczas_dsiedem, miedzyczas_dosiem, miedzyczas_ddziewiec, miedzyczas_trzydziesci, miedzyczas_tjeden,
                              miedzyczas_tdwa, miedzyczas_ttrzy, miedzyczas_tcztery, miedzyczas_tpiec, miedzyczas_tszesc, miedzyczas_tsiedem, miedzyczas_tosiem, miedzyczas_tdziewiec, miedzyczas_czterdziesci, miedzyczas_cjeden, miedzyczas_cdwa]
                self.result.clear()
                self.result.addItem(czas)
                for i in range(len(sekundy)):
                    self.result.addItem(miedzyczas[i])
                self.dowykresupts = sekundy
                self.dowykresuptm = minuty
                self.dowykresupth = godziny

                return self.dowykresupts, self.dowykresuptm, self.dowykresupth

            else:
                komunikat = "Sprawdź, czy dobrze podałeś wartości."
                self.result.clear()
                self.result.addItem(komunikat)
        except:
            komunikat = "Podane wartości nie są liczbami całkowitymi"
            self.result.clear()
            self.result.addItem(komunikat)



    def timeRegres(self):
        if (len(self.godziny.text()) == 0) and (len(self.minuty.text()) == 0) and (len(self.sekundy.text()) == 0):
            komunikat = "Podaj czas"

            self.result.clear()
            self.result.addItem(komunikat)
        else:
            if self.TButton.isChecked():
                self.regresT()
            elif self.PButton.isChecked():
                self.regresP()
            elif self.DButton.isChecked():
                self.regresD()
            elif self.HButton.isChecked():
                self.regresH()
            elif self.MButton.isChecked():
                self.regresM()

    def Wykres(self):
        if (len(self.godziny.text()) == 0) and (len(self.minuty.text()) == 0) and (len(self.sekundy.text()) == 0):
            komunikat = "Podaj czas"

            self.result.clear()
            self.result.addItem(komunikat)
        else:
            h = self.godziny.text()
            m = self.minuty.text()
            s = self.sekundy.text()
            h = str(h)
            m = str(m)
            s = str(s)
            try:
                int(h)
                int(m)
                int(s)
                if ((float(h)) >= 0 and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                    if self.TButton.isChecked():
                        if self.doWykresuS.isChecked():
                            self.staleT()
                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)
                            Km = [1, 2, 3]

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności całkowitego czasu na danym kilometrze od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Całkowity czas w sekunach na danym kilometrze')
                            plt.grid()
                            plt.show()

                        elif self.doWykresuP.isChecked():
                            self.progresT()


                            rysujWykres= []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i]+((self.dowykresuptm[i])*60)+((self.dowykresupth[i])*3600)
                                rysujWykres.append(x)


                            Km = [1, 2, 3]




                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()


                        elif self.doWykresuR.isChecked():
                            self.regresT()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = [1, 2, 3]

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()
                    elif self.PButton.isChecked():
                        if self.doWykresuS.isChecked():
                            self.staleP()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 6):
                                Km.append(i)


                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności całkowitego czasu na danym kilometrze od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Całkowity czas w sekunach na danym kilometrze')
                            plt.grid()
                            plt.show()


                        elif self.doWykresuP.isChecked():
                            self.progresP()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 6):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()
                        elif self.doWykresuR.isChecked():
                            self.regresP()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 6):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()
                    elif self.DButton.isChecked():
                        if self.doWykresuS.isChecked():
                            self.staleD()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 11):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności całkowitego czasu na danym kilometrze od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Całkowity czas w sekunach na danym kilometrze')
                            plt.grid()
                            plt.show()
                        elif self.doWykresuP.isChecked():
                            self.progresD()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 11):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()
                        elif self.doWykresuR.isChecked():
                            self.regresD()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 11):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()
                    elif self.HButton.isChecked():
                        if self.doWykresuS.isChecked():
                            self.staleH()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 22):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności całkowitego czasu na danym kilometrze od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Całkowity czas w sekunach na danym kilometrze')
                            plt.grid()
                            plt.show()
                        elif self.doWykresuP.isChecked():
                            self.progresH()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 22):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()
                        elif self.doWykresuR.isChecked():
                            self.regresH()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 22):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()
                    elif self.MButton.isChecked():
                        if self.doWykresuS.isChecked():
                            self.staleM()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 43):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności całkowitego czasu na danym kilometrze od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Całkowity czas w sekunach na danym kilometrze')
                            plt.grid()
                            plt.show()
                        elif self.doWykresuP.isChecked():
                            self.progresM()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 43):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()
                        elif self.doWykresuR.isChecked():
                            self.regresM()

                            rysujWykres = []
                            for i in range(0, len(self.dowykresupts)):
                                x = self.dowykresupts[i] + ((self.dowykresuptm[i]) * 60) + (
                                            (self.dowykresupth[i]) * 3600)
                                rysujWykres.append(x)


                            Km = []
                            for i in range(1, 43):
                                Km.append(i)

                            plt.scatter(Km, rysujWykres)
                            plt.title('Wykres zależności kolejnych międzyczasów od kilometra')
                            plt.xlabel('Kilometry')
                            plt.ylabel('Międzyczas, jaki należy uzyskać na danym kilometrze w sekunach')
                            plt.grid()
                            plt.show()


                else:
                    komunikat = "Sprawdź, czy dobrze podałeś wartości."
                    self.result.clear()
                    self.result.addItem(komunikat)
            except:
                komunikat = "Podane wartości nie są liczbami całkowitymi"
                self.result.clear()
                self.result.addItem(komunikat)





    def setupUi(self, runningzombies):
        runningzombies.setObjectName("runningzombies")
        runningzombies.resize(640, 400)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 213, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 149, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 213, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 149, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(213, 213, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(149, 149, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        runningzombies.setPalette(palette)
        runningzombies.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(runningzombies)
        self.centralwidget.setObjectName("centralwidget")
        self.TButton = QtWidgets.QRadioButton(self.centralwidget)
        self.TButton.setGeometry(QtCore.QRect(30, 70, 82, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.TButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TButton.setFont(font)
        self.TButton.setObjectName("TButton")
        self.PButton = QtWidgets.QRadioButton(self.centralwidget)
        self.PButton.setGeometry(QtCore.QRect(30, 100, 82, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.PButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PButton.setFont(font)
        self.PButton.setObjectName("PButton")
        self.DButton = QtWidgets.QRadioButton(self.centralwidget)
        self.DButton.setGeometry(QtCore.QRect(30, 130, 82, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.DButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DButton.setFont(font)
        self.DButton.setObjectName("DButton")
        self.HButton = QtWidgets.QRadioButton(self.centralwidget)
        self.HButton.setGeometry(QtCore.QRect(30, 160, 101, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.HButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.HButton.setFont(font)
        self.HButton.setObjectName("HButton")
        self.MButton = QtWidgets.QRadioButton(self.centralwidget)
        self.MButton.setGeometry(QtCore.QRect(30, 190, 101, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.MButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MButton.setFont(font)
        self.MButton.setObjectName("MButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 40, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.godziny = QtWidgets.QLineEdit(self.centralwidget)
        self.godziny.setGeometry(QtCore.QRect(270, 70, 113, 20))
        self.godziny.setObjectName("godziny")
        self.minuty = QtWidgets.QLineEdit(self.centralwidget)
        self.minuty.setGeometry(QtCore.QRect(270, 100, 113, 20))
        self.minuty.setObjectName("minuty")
        self.sekundy = QtWidgets.QLineEdit(self.centralwidget)
        self.sekundy.setGeometry(QtCore.QRect(270, 130, 113, 20))
        self.sekundy.setObjectName("sekundy")
        self.StaleButton = QtWidgets.QPushButton(self.centralwidget)
        self.StaleButton.setGeometry(QtCore.QRect(10, 250, 141, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.StaleButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.StaleButton.setFont(font)
        self.StaleButton.setObjectName("StaleButton")
        self.ProgresButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProgresButton.setGeometry(QtCore.QRect(150, 250, 141, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.ProgresButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ProgresButton.setFont(font)
        self.ProgresButton.setObjectName("ProgresButton")
        self.RegresButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegresButton.setGeometry(QtCore.QRect(290, 250, 141, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.RegresButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.RegresButton.setFont(font)
        self.RegresButton.setObjectName("RegresButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(420, 10, 201, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 199, 229))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.result = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.result.setGeometry(QtCore.QRect(-5, 0, 207, 231))
        self.result.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.result.setObjectName("result")
        item = QtWidgets.QListWidgetItem()
        self.result.addItem(item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.ProgresButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ProgresButton_2.setGeometry(QtCore.QRect(480, 250, 141, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.ProgresButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.ProgresButton_2.setFont(font)
        self.ProgresButton_2.setObjectName("ProgresButton_2")
        self.doWykresuS = QtWidgets.QRadioButton(self.centralwidget)
        self.doWykresuS.setGeometry(QtCore.QRect(150, 310, 82, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.doWykresuS.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.doWykresuS.setFont(font)
        self.doWykresuS.setObjectName("doWykresuS")
        self.buttonGroup = QtWidgets.QButtonGroup(runningzombies)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.doWykresuS)
        self.doWykresuP = QtWidgets.QRadioButton(self.centralwidget)
        self.doWykresuP.setGeometry(QtCore.QRect(290, 310, 101, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.doWykresuP.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.doWykresuP.setFont(font)
        self.doWykresuP.setObjectName("doWykresuP")
        self.buttonGroup.addButton(self.doWykresuP)
        self.doWykresuR = QtWidgets.QRadioButton(self.centralwidget)
        self.doWykresuR.setGeometry(QtCore.QRect(430, 310, 91, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.doWykresuR.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.doWykresuR.setFont(font)
        self.doWykresuR.setObjectName("doWykresuR")
        self.buttonGroup.addButton(self.doWykresuR)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        runningzombies.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(runningzombies)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        runningzombies.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(runningzombies)
        self.statusbar.setObjectName("statusbar")
        runningzombies.setStatusBar(self.statusbar)
        self.Przewidywaniaaa = QtWidgets.QPushButton(self.centralwidget)
        self.Przewidywaniaaa.setGeometry(QtCore.QRect(480, 335, 141, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(86, 86, 86))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(14, 46, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(254, 255, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 175, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.Przewidywaniaaa.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Przewidywaniaaa.setFont(font)
        self.Przewidywaniaaa.setObjectName("Przewidywaniaaa")

        ###Evenet to przelicz button###
        self.StaleButton.clicked.connect(self.timeCheck)
        self.ProgresButton.clicked.connect(self.timeProgres)
        self.RegresButton.clicked.connect(self.timeRegres)
        self.ProgresButton_2.clicked.connect(self.Wykres)
        self.Przewidywaniaaa.clicked.connect(self.okno)
        ##


        self.retranslateUi(runningzombies)
        QtCore.QMetaObject.connectSlotsByName(runningzombies)

    def retranslateUi(self, runningzombies):
        _translate = QtCore.QCoreApplication.translate
        runningzombies.setWindowTitle(_translate("runningzombies", "RunningZombies"))
        self.TButton.setText(_translate("runningzombies", "3 km"))
        self.PButton.setText(_translate("runningzombies", "5 km"))
        self.DButton.setText(_translate("runningzombies", "10 km"))
        self.HButton.setText(_translate("runningzombies", "21, 097 km"))
        self.MButton.setText(_translate("runningzombies", "42,195 km"))
        self.label.setText(_translate("runningzombies", "DYSTANS"))
        self.label_2.setText(_translate("runningzombies", "CZAS"))
        self.label_3.setText(_translate("runningzombies", "Godziny:"))
        self.label_4.setText(_translate("runningzombies", "Minuty:"))
        self.label_5.setText(_translate("runningzombies", "Sekundy:"))
        self.StaleButton.setText(_translate("runningzombies", "Tempo stałe"))
        self.ProgresButton.setText(_translate("runningzombies", "Tempo progresywne"))
        self.RegresButton.setText(_translate("runningzombies", "Tempo regresywne"))
        __sortingEnabled = self.result.isSortingEnabled()
        self.result.setSortingEnabled(False)
        item = self.result.item(0)
        item.setText(_translate("runningzombies", ""))
        self.result.setSortingEnabled(__sortingEnabled)
        self.ProgresButton_2.setText(_translate("runningzombies", "Wykres"))
        self.Przewidywaniaaa.setText(_translate("runningzombies", "Przewidywanie"))
        self.doWykresuS.setText(_translate("runningzombies", "STAŁE"))
        self.doWykresuP.setText(_translate("runningzombies", "PROGRES"))
        self.doWykresuR.setText(_translate("runningzombies", "REGRES"))
        self.label_6.setText(_translate("runningzombies", "WYKRES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    runningzombies = QtWidgets.QMainWindow()
    ui = Ui_runningzombies()
    ui.setupUi(runningzombies)
    runningzombies.show()
    sys.exit(app.exec_())

