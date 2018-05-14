from PyQt5 import QtCore, QtGui, QtWidgets
import math
class Ui_MainWindow(object):
    def timeCheck(self):
        if (len(self.godziny.text())==0) and (len(self.minuty.text())==0) and (len(self.sekundy.text())==0):
            komunikat = "Podaj czas"
            self.result.setText(komunikat)
        else:
            if self.JkmButton.isChecked():
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h)>=0) and (float(m) in range(0,60)) and (float(s) in range(0,60))):
                        czas = "Średni czas na 1 km: "+h+"h : "+m+"m : "+s+"s"
                        self.result.setText(czas)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane wartości nie są liczbami całkowitymi")
            elif self.TkmButton.isChecked():
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h)/3
                        h_result = math.floor(x)
                        h_pomoc = (float(h)%3)*60
                        m_pomoc = float(m)+h_pomoc
                        m_result = math.floor(m_pomoc/3)
                        m_ppomoc = (m_pomoc%3)*60
                        s_pomoc = m_ppomoc+float(s)
                        s_result = math.floor(s_pomoc/3)

                        pierwszy_kms = s_result
                        pierwszy_kmm = m_result
                        pierwszy_kmh = h_result
                        drugi_kms = 0
                        drugi_kmm = 0
                        drugi_kmh = 0
                        trzeci_kms = 0
                        trzeci_kmm = 0
                        trzeci_kmh = 0
                        if (pierwszy_kms + (s_result))< 60:
                            drugi_kms = pierwszy_kms + (s_result)
                        elif (pierwszy_kms + (s_result)==60):
                            drugi_kms = 0
                            drugi_kmm += 1
                        else:
                            drugi_kms = (pierwszy_kms + (s_result)) - 60
                            drugi_kmm += 1

                        if (drugi_kms + (s_result)) <60:
                            trzeci_kms = drugi_kms + (s_result)
                        elif (drugi_kms + (s_result) == 60):
                            trzeci_kms = 0
                            trzeci_kmm += 1
                        else:
                            trzeci_kms = (drugi_kms + (s_result)) - 60
                            trzeci_kmm +=1

                        if (pierwszy_kmm + (m_result)+drugi_kmm)<60:
                            drugi_kmm += (pierwszy_kmm + (m_result))
                        elif (pierwszy_kmm + (m_result)+drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh += 1
                        else:
                            drugi_kmm = (pierwszy_kmm + (m_result)+drugi_kmm)-60
                            drugi_kmh +=1

                        if (drugi_kmm + (m_result)+trzeci_kmm)<60:
                            trzeci_kmm += (drugi_kmm + (m_result))
                        elif (drugi_kmm + (m_result)+trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh += 1
                        else:
                            trzeci_kmm = (drugi_kmm + (m_result)+trzeci_kmm)-60
                            trzeci_kmh +=1

                        drugi_kmh += pierwszy_kmh+h_result
                        trzeci_kmh += drugi_kmh +h_result

                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result= str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)

                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \n"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \n"
                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")
                    #print(miedzyczas_pierwszy, miedzyczas_drugi, miedzyczas_trzeci)

            elif self.PkmButton.isChecked():
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h)/5
                        h_result = math.floor(x)
                        h_pomoc = (float(h)%5)*60
                        m_pomoc = float(m)+h_pomoc
                        m_result = math.floor(m_pomoc/5)
                        m_ppomoc = (m_pomoc%5)*60
                        s_pomoc = m_ppomoc+float(s)
                        s_result = math.floor(s_pomoc/5)

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


                        if (pierwszy_kms + (s_result))< 60:
                            drugi_kms = pierwszy_kms + (s_result)
                        elif (pierwszy_kms + (s_result)==60):
                            drugi_kms = 0
                            drugi_kmm += 1
                        else:
                            drugi_kms = (pierwszy_kms + (s_result)) - 60
                            drugi_kmm += 1

                        if (drugi_kms + (s_result)) <60:
                            trzeci_kms = drugi_kms + (s_result)
                        elif (drugi_kms + (s_result) == 60):
                            trzeci_kms = 0
                            trzeci_kmm += 1
                        else:
                            trzeci_kms = (drugi_kms + (s_result)) - 60
                            trzeci_kmm +=1

                        if (trzeci_kms + (s_result))<60:
                            czwarty_kms = trzeci_kms + (s_result)
                        elif (trzeci_kms + (s_result))==60:
                            czwarty_kms = 0
                            czwarty_kmm +=1
                        else:
                            czwarty_kms = (trzeci_kms + (s_result))-60
                            czwarty_kmm +=1

                        if (czwarty_kms + (s_result))<60:
                            piaty_kms = czwarty_kms + (s_result)
                        elif (czwarty_kms + (s_result))==60:
                            piaty_kms = 0
                            piaty_kmm +=1
                        else:
                            piaty_kms = (czwarty_kms + (s_result))-60
                            piaty_kmm +=1

                        if (pierwszy_kmm + (m_result)+drugi_kmm)<60:
                            drugi_kmm += (pierwszy_kmm + (m_result))
                        elif (pierwszy_kmm + (m_result)+drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh +=1
                        else:
                            drugi_kmm = (pierwszy_kmm + (m_result)+drugi_kmm)-60
                            drugi_kmh +=1

                        if (drugi_kmm + (m_result)+trzeci_kmm)<60:
                            trzeci_kmm += (drugi_kmm + (m_result))
                        elif (drugi_kmm + (m_result)+trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh +=1
                        else:
                            trzeci_kmm = (drugi_kmm + (m_result)+trzeci_kmm)-60
                            trzeci_kmh +=1

                        if (trzeci_kmm + (m_result)+ czwarty_kmm)<60:
                            czwarty_kmm += (trzeci_kmm + (m_result))
                        elif (trzeci_kmm + (m_result)+ czwarty_kmm)==60:
                            czwarty_kmm = 0
                            czwarty_kmh +=1
                        else:
                            czwarty_kmm = (trzeci_kmm + (m_result)+czwarty_kmm)-60
                            czwarty_kmh +=1

                        if (czwarty_kmm + (m_result)+ piaty_kmm)<60:
                            piaty_kmm += (czwarty_kmm + (m_result))
                        elif (czwarty_kmm + (m_result)+ piaty_kmm)==60:
                            piaty_kmm = 0
                            piaty_kmh += 1
                        else:
                            piaty_kmm = (czwarty_kmm + (m_result)+piaty_kmm)-60
                            piaty_kmh +=1


                        drugi_kmh += pierwszy_kmh + h_result
                        trzeci_kmh += drugi_kmh + h_result
                        czwarty_kmh += trzeci_kmh + h_result
                        piaty_kmh += czwarty_kmh + h_result

                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result = str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        czwarty_kms = str(czwarty_kms)
                        piaty_kms = str(piaty_kms)
                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        czwarty_kmm = str(czwarty_kmm)
                        piaty_kmm = str(piaty_kmm)
                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)
                        czwarty_kmh = str(czwarty_kmh)
                        piaty_kmh = str(piaty_kmh)


                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \n"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \n"
                        miedzyczas_czwarty = "4 km: " + czwarty_kmh + "h : " + czwarty_kmm + "m : " + czwarty_kms + "s \n"
                        miedzyczas_piaty = "5 km: " + piaty_kmh + "h : " + piaty_kmm + "m : " + piaty_kms + "s \n"

                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")
            elif self.DkmButton.isChecked():
                MainWindow.resize(480, 580)
                self.pushButton.setGeometry(QtCore.QRect(180, 490, 111, 31))
                self.pushButton_2.setGeometry(QtCore.QRect(180, 530, 111, 31))
                self.result.setGeometry(QtCore.QRect(220, 170, 300, 305))
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h)/10
                        h_result = math.floor(x)
                        h_pomoc = (float(h)%10)*60
                        m_pomoc = float(m)+h_pomoc
                        m_result = math.floor(m_pomoc/10)
                        m_ppomoc = (m_pomoc%10)*60
                        s_pomoc = m_ppomoc+float(s)
                        s_result = math.floor(s_pomoc/10)

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
                        osmy_kms =0
                        osmy_kmm = 0
                        osmy_kmh = 0
                        dziewiaty_kms = 0
                        dziewiaty_kmm = 0
                        dziewiaty_kmh = 0
                        dziesiaty_kms = 0
                        dziesiaty_kmm = 0
                        dziesiaty_kmh = 0

                        if (pierwszy_kms + (s_result)) < 60:
                            drugi_kms = pierwszy_kms + (s_result)
                        elif (pierwszy_kms + (s_result) == 60):
                            drugi_kms = 0
                            drugi_kmm += 1
                        else:
                            drugi_kms = (pierwszy_kms + (s_result)) - 60
                            drugi_kmm += 1

                        if (drugi_kms + (s_result)) < 60:
                            trzeci_kms = drugi_kms + (s_result)
                        elif (drugi_kms + (s_result) == 60):
                            trzeci_kms = 0
                            trzeci_kmm += 1
                        else:
                            trzeci_kms = (drugi_kms + (s_result)) - 60
                            trzeci_kmm += 1

                        if (trzeci_kms + (s_result)) < 60:
                            czwarty_kms = trzeci_kms + (s_result)
                        elif (trzeci_kms + (s_result)) == 60:
                            czwarty_kms = 0
                            czwarty_kmm += 1
                        else:
                            czwarty_kms = (trzeci_kms + (s_result)) - 60
                            czwarty_kmm += 1

                        if (czwarty_kms + (s_result)) < 60:
                            piaty_kms = czwarty_kms + (s_result)
                        elif (czwarty_kms + (s_result)) == 60:
                            piaty_kms = 0
                            piaty_kmm += 1
                        else:
                            piaty_kms = (czwarty_kms + (s_result)) - 60
                            piaty_kmm += 1

                        if(piaty_kms + (s_result)) <60:
                            szosty_kms = (piaty_kms + (s_result))
                        elif (piaty_kms + (s_result))==60:
                            szosty_kms = 0
                            szosty_kmm +=1
                        else:
                            szosty_kms = (piaty_kms + (s_result))-60
                            szosty_kmm +=1

                        if(szosty_kms +(s_result))<60:
                            siodmy_kms = (szosty_kms +(s_result))
                        elif (szosty_kms +(s_result))==60:
                            siodmy_kms = 0
                            siodmy_kmm +=1
                        else:
                            siodmy_kms = (szosty_kms +(s_result))-60
                            siodmy_kmm +=1

                        if(siodmy_kms + (s_result))<60:
                            osmy_kms = (siodmy_kms + (s_result))
                        elif(siodmy_kms + (s_result))==60:
                            osmy_kms = 0
                            osmy_kmm +=1
                        else:
                            osmy_kms = (siodmy_kms + (s_result))-60
                            osmy_kmm+=1

                        if(osmy_kms+(s_result))<60:
                            dziewiaty_kms = (osmy_kms+(s_result))
                        elif(osmy_kms+(s_result))==60:
                            dziewiaty_kms = 0
                            dziewiaty_kmm +=1
                        else:
                            dziewiaty_kms = (osmy_kms+(s_result))-60
                            dziewiaty_kmm +=1

                        if(dziewiaty_kms+(s_result))<60:
                            dziesiaty_kms = (dziewiaty_kms+(s_result))
                        elif((dziewiaty_kms+(s_result)))==60:
                            dziesiaty_kms = 0
                            dziesiaty_kmm +=1
                        else:
                            dziesiaty_kms = (dziewiaty_kms+(s_result))-60
                            dziesiaty_kmm +=1


                        if (pierwszy_kmm + (m_result) + drugi_kmm) < 60:
                            drugi_kmm += (pierwszy_kmm + (m_result))
                        elif (pierwszy_kmm + (m_result) + drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh += 1
                        else:
                            drugi_kmm = (pierwszy_kmm + (m_result) + drugi_kmm) - 60
                            drugi_kmh += 1

                        if (drugi_kmm + (m_result) + trzeci_kmm) < 60:
                            trzeci_kmm += (drugi_kmm + (m_result))
                        elif (drugi_kmm + (m_result) + trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh += 1
                        else:
                            trzeci_kmm = (drugi_kmm + (m_result) + trzeci_kmm) - 60
                            trzeci_kmh += 1

                        if (trzeci_kmm + (m_result) + czwarty_kmm) < 60:
                            czwarty_kmm += (trzeci_kmm + (m_result))
                        elif (trzeci_kmm + (m_result) + czwarty_kmm) == 60:
                            czwarty_kmm = 0
                            czwarty_kmh += 1
                        else:
                            czwarty_kmm = (trzeci_kmm + (m_result) + czwarty_kmm) - 60
                            czwarty_kmh += 1

                        if (czwarty_kmm + (m_result) + piaty_kmm) < 60:
                            piaty_kmm += (czwarty_kmm + (m_result))
                        elif (czwarty_kmm + (m_result) + piaty_kmm) == 60:
                            piaty_kmm = 0
                            piaty_kmh += 1
                        else:
                            piaty_kmm = (czwarty_kmm + (m_result) + piaty_kmm) - 60
                            piaty_kmh += 1

                        if (piaty_kmm + (m_result) + szosty_kmm)<60:
                            szosty_kmm += piaty_kmm + (m_result)
                        elif (piaty_kmm + (m_result) + szosty_kmm)==60:
                            szosty_kmm = 0
                            szosty_kmh += 1
                        else:
                            szosty_kmm = (piaty_kmm + (m_result) + szosty_kmm)-60
                            szosty_kmh +=1

                        if (szosty_kmm + (m_result) + siodmy_kmm)<60:
                            siodmy_kmm+= szosty_kmm+ (m_result)
                        elif (szosty_kmm + (m_result) + siodmy_kmm)==60:
                            siodmy_kmm = 0
                            siodmy_kmh +=1
                        else:
                            siodmy_kmm = (szosty_kmm + (m_result) + siodmy_kmm)-60
                            siodmy_kmh +=1

                        if (siodmy_kmm + (m_result)+osmy_kmm)<60:
                            osmy_kmm += siodmy_kmm + (m_result)
                        elif (siodmy_kmm + (m_result)+osmy_kmm)==60:
                            osmy_kmm = 0
                            osmy_kmh +=1
                        else:
                            osmy_kmm = (siodmy_kmm + (m_result)+osmy_kmm)-60
                            osmy_kmh+=1

                        if (osmy_kmm + (m_result)+dziewiaty_kmm)<60:
                            dziewiaty_kmm += osmy_kmm + (m_result)
                        elif (osmy_kmm + (m_result)+dziewiaty_kmm)==60:
                            dziewiaty_kmm = 0
                            dziewiaty_kmh+=1
                        else:
                            dziewiaty_kmm = (osmy_kmm + (m_result)+dziewiaty_kmm)-60
                            dziewiaty_kmh +=1

                        if (dziewiaty_kmm + (m_result)+dziesiaty_kmm)<60:
                            dziesiaty_kmm += dziewiaty_kmm + (m_result)
                        elif (dziewiaty_kmm + (m_result)+dziesiaty_kmm)==60:
                            dziesiaty_kmm = 0
                            dziesiaty_kmh +=1
                        else:
                            dziesiaty_kmm = (dziewiaty_kmm + (m_result)+dziesiaty_kmm)-60
                            dziesiaty_kmh +=1

                        drugi_kmh += pierwszy_kmh + h_result
                        trzeci_kmh += drugi_kmh + h_result
                        czwarty_kmh += trzeci_kmh + h_result
                        piaty_kmh += czwarty_kmh + h_result
                        szosty_kmh += piaty_kmh + h_result
                        siodmy_kmh += szosty_kmh + h_result
                        osmy_kmh += siodmy_kmh + h_result
                        dziewiaty_kmh += osmy_kmh + h_result
                        dziesiaty_kmh += dziewiaty_kmh + h_result


                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result = str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        czwarty_kms = str(czwarty_kms)
                        piaty_kms = str(piaty_kms)
                        szosty_kms = str(szosty_kms)
                        siodmy_kms = str(siodmy_kms)
                        osmy_kms = str(osmy_kms)
                        dziewiaty_kms = str(dziewiaty_kms)
                        dziesiaty_kms = str(dziesiaty_kms)
                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        czwarty_kmm = str(czwarty_kmm)
                        piaty_kmm = str(piaty_kmm)
                        szosty_kmm = str(szosty_kmm)
                        siodmy_kmm = str(siodmy_kmm)
                        osmy_kmm = str(osmy_kmm)
                        dziewiaty_kmm = str(dziewiaty_kmm)
                        dziesiaty_kmm = str(dziesiaty_kmm)
                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)
                        czwarty_kmh = str(czwarty_kmh)
                        piaty_kmh = str(piaty_kmh)
                        szosty_kmh = str(szosty_kmh)
                        siodmy_kmh = str(siodmy_kmh)
                        osmy_kmh = str(osmy_kmh)
                        dziewiaty_kmh = str(dziewiaty_kmh)
                        dziesiaty_kmh = str(dziesiaty_kmh)

                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \n"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \n"
                        miedzyczas_czwarty = "4 km: " + czwarty_kmh + "h : " + czwarty_kmm + "m : " + czwarty_kms + "s \n"
                        miedzyczas_piaty = "5 km: " + piaty_kmh + "h : " + piaty_kmm + "m : " + piaty_kms + "s \n"
                        miedzyczas_szosty = "6 km: " + szosty_kmh + "h : " + szosty_kmm + "m : " + szosty_kms + "s \n"
                        miedzyczas_siodmy = "7 km: " + siodmy_kmh + "h : " + siodmy_kmm + "m : " + siodmy_kms + "s \n"
                        miedzyczas_osmy = "8 km: " + osmy_kmh + "h : " + osmy_kmm + "m : " + osmy_kms + "s \n"
                        miedzyczas_dziewiaty = "9 km: " + dziewiaty_kmh + "h : " + dziewiaty_kmm + "m : " + dziewiaty_kms + "s \n"
                        miedzyczas_dziesiaty = "10 km: " + dziesiaty_kmh + "h : " + dziesiaty_kmm + "m : " + dziesiaty_kms + "s \n"


                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty + miedzyczas_szosty + miedzyczas_siodmy + miedzyczas_osmy + miedzyczas_dziewiaty + miedzyczas_dziesiaty

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")
            elif self.HkmButton.isChecked():
                MainWindow.resize(480, 580)
                self.pushButton.setGeometry(QtCore.QRect(180, 490, 111, 31))
                self.pushButton_2.setGeometry(QtCore.QRect(180, 530, 111, 31))
                self.result.setGeometry(QtCore.QRect(220, 170, 300, 305))

                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h)/21.097
                        h_result = math.floor(x)
                        h_pomoc = (float(h)%21.097)*60
                        m_pomoc = float(m)+h_pomoc
                        m_result = math.floor(m_pomoc/21.097)
                        m_ppomoc = (m_pomoc%21.097)*60
                        s_pomoc = m_ppomoc+float(s)
                        s_result = math.floor(s_pomoc/21.097)


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
                        f_kms = 0
                        f_kmm = 0
                        f_kmh = 0

                        if ((pierwszy_kms + (s_result)) < 60):
                            drugi_kms = pierwszy_kms + (s_result)
                        elif ((pierwszy_kms + (s_result)) == 60):
                            drugi_kms = 0
                            drugi_kmm += 1
                        else:
                            drugi_kms = (pierwszy_kms + (s_result)) - 60
                            drugi_kmm += 1

                        if ((drugi_kms + (s_result)) < 60):
                            trzeci_kms = drugi_kms + (s_result)
                        elif ((drugi_kms + (s_result)) == 60):
                            trzeci_kms = 0
                            trzeci_kmm += 1
                        else:
                            trzeci_kms = (drugi_kms + (s_result)) - 60
                            trzeci_kmm += 1

                        if ((trzeci_kms + (s_result)) < 60):
                            czwarty_kms = trzeci_kms + (s_result)
                        elif (trzeci_kms + (s_result)) == 60:
                            czwarty_kms = 0
                            czwarty_kmm += 1
                        else:
                            czwarty_kms = (trzeci_kms + (s_result)) - 60
                            czwarty_kmm += 1

                        if ((czwarty_kms + (s_result)) < 60):
                            piaty_kms = czwarty_kms + (s_result)
                        elif (czwarty_kms + (s_result)) == 60:
                            piaty_kms = 0
                            piaty_kmm += 1
                        else:
                            piaty_kms = (czwarty_kms + (s_result)) - 60
                            piaty_kmm += 1

                        if ((piaty_kms + (s_result)) < 60):
                            szosty_kms = (piaty_kms + (s_result))
                        elif (piaty_kms + (s_result)) == 60:
                            szosty_kms = 0
                            szosty_kmm += 1
                        else:
                            szosty_kms = (piaty_kms + (s_result)) - 60
                            szosty_kmm += 1

                        if (szosty_kms + (s_result)) < 60:
                            siodmy_kms = (szosty_kms + (s_result))
                        elif (szosty_kms + (s_result)) == 60:
                            siodmy_kms = 0
                            siodmy_kmm += 1
                        else:
                            siodmy_kms = (szosty_kms + (s_result)) - 60
                            siodmy_kmm += 1

                        if (siodmy_kms + (s_result)) < 60:
                            osmy_kms = (siodmy_kms + (s_result))
                        elif (siodmy_kms + (s_result)) == 60:
                            osmy_kms = 0
                            osmy_kmm += 1
                        else:
                            osmy_kms = (siodmy_kms + (s_result)) - 60
                            osmy_kmm += 1

                        if (osmy_kms + (s_result)) < 60:
                            dziewiaty_kms = (osmy_kms + (s_result))
                        elif (osmy_kms + (s_result)) == 60:
                            dziewiaty_kms = 0
                            dziewiaty_kmm += 1
                        else:
                            dziewiaty_kms = (osmy_kms + (s_result)) - 60
                            dziewiaty_kmm += 1

                        if (dziewiaty_kms + (s_result)) < 60:
                            dziesiaty_kms = (dziewiaty_kms + (s_result))
                        elif ((dziewiaty_kms + (s_result))) == 60:
                            dziesiaty_kms = 0
                            dziesiaty_kmm += 1
                        else:
                            dziesiaty_kms = (dziewiaty_kms + (s_result)) - 60
                            dziesiaty_kmm += 1
                        if (dziesiaty_kms + (s_result)) < 60:
                            jedenasty_kms = (dziesiaty_kms + (s_result))
                        elif (dziesiaty_kms + (s_result)) == 60:
                            jedenasty_kms = 0
                            jedenasty_kmm += 1
                        else:
                            jedenasty_kms = (dziesiaty_kms + (s_result)) - 60
                            jedenasty_kmm += 1

                        if (jedenasty_kms + (s_result)) < 60:
                            dwunasty_kms = (jedenasty_kms + (s_result))
                        elif (jedenasty_kms + (s_result)) == 60:
                            dwunasty_kms = 0
                            dwunasty_kmm += 1
                        else:
                            dwunasty_kms = (jedenasty_kms + (s_result)) - 60
                            dwunasty_kmm += 1
                        if (dwunasty_kms + (s_result)) < 60:
                            trzynasty_kms = (dwunasty_kms + (s_result))
                        elif (dwunasty_kms + (s_result)) == 60:
                            trzynasty_kms = 0
                            trzynasty_kmm += 1
                        else:
                            trzynasty_kms = (dwunasty_kms + (s_result)) - 60
                            trzynasty_kmm += 1

                        if (trzynasty_kms + (s_result)) < 60:
                            czternasty_kms = (trzynasty_kms + (s_result))
                        elif (trzynasty_kms + (s_result)) == 60:
                            czternasty_kms = 0
                            czternasty_kmm += 1
                        else:
                            czternasty_kms = (trzynasty_kms + (s_result)) - 60
                            czternasty_kmm += 1
                        if (czternasty_kms + (s_result)) < 60:
                            pietnasty_kms = (czternasty_kms + (s_result))
                        elif (czternasty_kms + (s_result)) == 60:
                            pietnasty_kms = 0
                            pietnasty_kmm += 1
                        else:
                            pietnasty_kms = (czternasty_kms + (s_result)) - 60
                            pietnasty_kmm += 1

                        if (pietnasty_kms + (s_result)) < 60:
                            szesnasty_kms = (pietnasty_kms + (s_result))
                        elif (pietnasty_kms + (s_result)) == 60:
                            szesnasty_kms = 0
                            szesnasty_kmm += 1
                        else:
                            szesnasty_kms = (pietnasty_kms + (s_result)) - 60
                            szesnasty_kmm += 1

                        if (szesnasty_kms + (s_result)) < 60:
                            siedemnasty_kms = (szesnasty_kms + (s_result))
                        elif (szesnasty_kms + (s_result)) == 60:
                            siedemnasty_kms = 0
                            siedemnasty_kmm += 1
                        else:
                            siedemnasty_kms = (szesnasty_kms + (s_result)) - 60
                            siedemnasty_kmm += 1

                        if (siedemnasty_kms + (s_result)) < 60:
                            osiemnasty_kms = (siedemnasty_kms + (s_result))
                        elif (siedemnasty_kms + (s_result)) == 60:
                            osiemnasty_kms = 0
                            osiemnasty_kmm += 1
                        else:
                            osiemnasty_kms = (siedemnasty_kms + (s_result)) - 60
                            osiemnasty_kmm += 1

                        if (osiemnasty_kms + (s_result)) < 60:
                            dziewietnasty_kms = (osiemnasty_kms + (s_result))
                        elif (osiemnasty_kms + (s_result)) == 60:
                            dziewietnasty_kms = 0
                            dziewietnasty_kmm += 1
                        else:
                            dziewietnasty_kms = (osiemnasty_kms + (s_result)) - 60
                            dziewietnasty_kmm += 1

                        if (dziewietnasty_kms + (s_result)) < 60:
                            dwudziesty_kms = (dziewietnasty_kms + (s_result))
                        elif (dziewietnasty_kms + (s_result)) == 60:
                            dwudziesty_kms = 0
                            dwudziesty_kmm += 1
                        else:
                            dwudziesty_kms = (dziewietnasty_kms + (s_result)) - 60
                            dwudziesty_kmm += 1

                        if (dwudziesty_kms + (s_result)) < 60:
                            djeden_kms = (dwudziesty_kms + (s_result))
                        elif (dwudziesty_kms + (s_result)) == 60:
                            djeden_kms = 0
                            djeden_kmm += 1
                        else:
                            djeden_kms = (dwudziesty_kms + (s_result)) - 60
                            djeden_kmm += 1



                        if (pierwszy_kmm + (m_result) + drugi_kmm) < 60:
                            drugi_kmm += (pierwszy_kmm + (m_result))
                        elif (pierwszy_kmm + (m_result) + drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh += 1
                        else:
                            drugi_kmm = (pierwszy_kmm + (m_result) + drugi_kmm) - 60
                            drugi_kmh += 1

                        if (drugi_kmm + (m_result) + trzeci_kmm) < 60:
                            trzeci_kmm += (drugi_kmm + (m_result))
                        elif (drugi_kmm + (m_result) + trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh += 1
                        else:
                            trzeci_kmm = (drugi_kmm + (m_result) + trzeci_kmm) - 60
                            trzeci_kmh += 1

                        if (trzeci_kmm + (m_result) + czwarty_kmm) < 60:
                            czwarty_kmm += (trzeci_kmm + (m_result))
                        elif (trzeci_kmm + (m_result) + czwarty_kmm) == 60:
                            czwarty_kmm = 0
                            czwarty_kmh += 1
                        else:
                            czwarty_kmm = (trzeci_kmm + (m_result) + czwarty_kmm) - 60
                            czwarty_kmh += 1

                        if (czwarty_kmm + (m_result) + piaty_kmm) < 60:
                            piaty_kmm += (czwarty_kmm + (m_result))
                        elif (czwarty_kmm + (m_result) + piaty_kmm) == 60:
                            piaty_kmm = 0
                            piaty_kmh += 1
                        else:
                            piaty_kmm = (czwarty_kmm + (m_result) + piaty_kmm) - 60
                            piaty_kmh += 1

                        if (piaty_kmm + (m_result) + szosty_kmm) < 60:
                            szosty_kmm += piaty_kmm + (m_result)
                        elif (piaty_kmm + (m_result) + szosty_kmm) == 60:
                            szosty_kmm = 0
                            szosty_kmh += 1
                        else:
                            szosty_kmm = (piaty_kmm + (m_result) + szosty_kmm) - 60
                            szosty_kmh += 1

                        if (szosty_kmm + (m_result) + siodmy_kmm) < 60:
                            siodmy_kmm += szosty_kmm + (m_result)
                        elif (szosty_kmm + (m_result) + siodmy_kmm) == 60:
                            siodmy_kmm = 0
                            siodmy_kmh += 1
                        else:
                            siodmy_kmm = (szosty_kmm + (m_result) + siodmy_kmm) - 60
                            siodmy_kmh += 1

                        if (siodmy_kmm + (m_result) + osmy_kmm) < 60:
                            osmy_kmm += siodmy_kmm + (m_result)
                        elif (siodmy_kmm + (m_result) + osmy_kmm) == 60:
                            osmy_kmm = 0
                            osmy_kmh += 1
                        else:
                            osmy_kmm = (siodmy_kmm + (m_result) + osmy_kmm) - 60
                            osmy_kmh += 1

                        if (osmy_kmm + (m_result) + dziewiaty_kmm) < 60:
                            dziewiaty_kmm += osmy_kmm + (m_result)
                        elif (osmy_kmm + (m_result) + dziewiaty_kmm) == 60:
                            dziewiaty_kmm = 0
                            dziewiaty_kmh += 1
                        else:
                            dziewiaty_kmm = (osmy_kmm + (m_result) + dziewiaty_kmm) - 60
                            dziewiaty_kmh += 1

                        if (dziewiaty_kmm + (m_result) + dziesiaty_kmm) < 60:
                            dziesiaty_kmm += dziewiaty_kmm + (m_result)
                        elif (dziewiaty_kmm + (m_result) + dziesiaty_kmm) == 60:
                            dziesiaty_kmm = 0
                            dziesiaty_kmh += 1
                        else:
                            dziesiaty_kmm = (dziewiaty_kmm + (m_result) + dziesiaty_kmm) - 60
                            dziesiaty_kmh += 1
                        if (dziesiaty_kmm + (m_result) + jedenasty_kmm) < 60:
                            jedenasty_kmm += dziesiaty_kmm + (m_result)
                        elif (dziesiaty_kmm + (m_result) + jedenasty_kmm) == 60:
                            jedenasty_kmm = 0
                            jedenasty_kmh += 1
                        else:
                            jedenasty_kmm = (dziesiaty_kmm + (m_result) + jedenasty_kmm) - 60
                            jedenasty_kmh += 1
                        if (jedenasty_kmm + (m_result) + dwunasty_kmm) < 60:
                            dwunasty_kmm += jedenasty_kmm + (m_result)
                        elif (jedenasty_kmm + (m_result) + dwunasty_kmm) == 60:
                            dwunasty_kmm = 0
                            dwunasty_kmh += 1
                        else:
                            dwunasty_kmm = (jedenasty_kmm + (m_result) + dwunasty_kmm) - 60
                            dwunasty_kmh += 1
                        if (dwunasty_kmm + (m_result) + trzynasty_kmm) < 60:
                            trzynasty_kmm += dwunasty_kmm + (m_result)
                        elif (dwunasty_kmm + (m_result) + trzynasty_kmm) == 60:
                            trzynasty_kmm = 0
                            trzynasty_kmh += 1
                        else:
                            trzynasty_kmm = (dwunasty_kmm + (m_result) + trzynasty_kmm) - 60
                            trzynasty_kmh += 1

                        if (trzynasty_kmm + (m_result) + czternasty_kmm) < 60:
                            czternasty_kmm += trzynasty_kmm + (m_result)
                        elif (trzynasty_kmm + (m_result) + czternasty_kmm) == 60:
                            czternasty_kmm = 0
                            czternasty_kmh += 1
                        else:
                            czternasty_kmm = (trzynasty_kmm + (m_result) + czternasty_kmm) - 60
                            czternasty_kmh += 1
                        if (czternasty_kmm + (m_result) + pietnasty_kmm) < 60:
                            pietnasty_kmm += czternasty_kmm + (m_result)
                        elif (czternasty_kmm + (m_result) + pietnasty_kmm) == 60:
                            pietnasty_kmm = 0
                            pietnasty_kmh += 1
                        else:
                            pietnasty_kmm = (czternasty_kmm + (m_result) + pietnasty_kmm) - 60
                            pietnasty_kmh += 1

                        if (pietnasty_kmm + (m_result) + szesnasty_kmm) < 60:
                            szesnasty_kmm += pietnasty_kmm + (m_result)
                        elif (pietnasty_kmm + (m_result) + szesnasty_kmm) == 60:
                            szesnasty_kmm = 0
                            szesnasty_kmh += 1
                        else:
                            szesnasty_kmm = (pietnasty_kmm + (m_result) + szesnasty_kmm) - 60
                            szesnasty_kmh += 1
                        if (szesnasty_kmm + (m_result) + siedemnasty_kmm) < 60:
                            siedemnasty_kmm += szesnasty_kmm + (m_result)
                        elif (szesnasty_kmm + (m_result) + siedemnasty_kmm) == 60:
                            siedemnasty_kmm = 0
                            siedemnasty_kmh += 1
                        else:
                            siedemnasty_kmm = (szesnasty_kmm + (m_result) + siedemnasty_kmm) - 60
                            siedemnasty_kmh += 1

                        if (siedemnasty_kmm + (m_result) + osiemnasty_kmm) < 60:
                            osiemnasty_kmm += siedemnasty_kmm + (m_result)
                        elif (siedemnasty_kmm + (m_result) + osiemnasty_kmm) == 60:
                            osiemnasty_kmm = 0
                            osiemnasty_kmh += 1
                        else:
                            osiemnasty_kmm = (siedemnasty_kmm + (m_result) + osiemnasty_kmm) - 60
                            osiemnasty_kmh += 1

                        if (osiemnasty_kmm + (m_result) + dziewietnasty_kmm) < 60:
                            dziewietnasty_kmm += osiemnasty_kmm + (m_result)
                        elif (osiemnasty_kmm + (m_result) + dziewietnasty_kmm) == 60:
                            dziewietnasty_kmm = 0
                            dziewietnasty_kmh += 1
                        else:
                            dziewietnasty_kmm = (osiemnasty_kmm + (m_result) + dziewietnasty_kmm) - 60
                            dziewietnasty_kmh += 1

                        if (dziewietnasty_kmm + (m_result) + dwudziesty_kmm) < 60:
                            dwudziesty_kmm += dziewietnasty_kmm + (m_result)
                        elif (dziewietnasty_kmm + (m_result) + dwudziesty_kmm) == 60:
                            dwudziesty_kmm = 0
                            dwudziesty_kmh += 1
                        else:
                            dwudziesty_kmm = (dziewietnasty_kmm + (m_result) + dwudziesty_kmm) - 60
                            dwudziesty_kmh += 1

                        if (dwudziesty_kmm + (m_result) + djeden_kmm) < 60:
                            djeden_kmm += dwudziesty_kmm + (m_result)
                        elif (dwudziesty_kmm + (m_result) + djeden_kmm) == 60:
                            djeden_kmm = 0
                            djeden_kmh += 1
                        else:
                            djeden_kmm = (dwudziesty_kmm + (m_result) + djeden_kmm) - 60
                            djeden_kmh += 1




                        drugi_kmh += pierwszy_kmh + h_result
                        trzeci_kmh += drugi_kmh + h_result
                        czwarty_kmh += trzeci_kmh + h_result
                        piaty_kmh += czwarty_kmh + h_result
                        szosty_kmh += piaty_kmh + h_result
                        siodmy_kmh += szosty_kmh + h_result
                        osmy_kmh += siodmy_kmh + h_result
                        dziewiaty_kmh += osmy_kmh + h_result
                        dziesiaty_kmh += dziewiaty_kmh + h_result
                        jedenasty_kmh += dziesiaty_kmh + h_result
                        dwunasty_kmh += jedenasty_kmh + h_result
                        trzynasty_kmh += dwunasty_kmh + h_result
                        czternasty_kmh += trzynasty_kmh + h_result
                        pietnasty_kmh += czternasty_kmh + h_result
                        szesnasty_kmh += pietnasty_kmh + h_result
                        siedemnasty_kmh += szesnasty_kmh + h_result
                        osiemnasty_kmh += siedemnasty_kmh + h_result
                        dziewietnasty_kmh += osiemnasty_kmh + h_result
                        dwudziesty_kmh += dziewietnasty_kmh + h_result
                        djeden_kmh += dwudziesty_kmh + h_result


                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result = str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        czwarty_kms = str(czwarty_kms)
                        piaty_kms = str(piaty_kms)
                        szosty_kms = str(szosty_kms)
                        siodmy_kms = str(siodmy_kms)
                        osmy_kms = str(osmy_kms)
                        dziewiaty_kms = str(dziewiaty_kms)
                        dziesiaty_kms = str(dziesiaty_kms)
                        jedenasty_kms = str(jedenasty_kms)
                        dwunasty_kms = str(dwunasty_kms)
                        trzynasty_kms = str(trzynasty_kms)
                        czternasty_kms = str(czternasty_kms)
                        pietnasty_kms = str(pietnasty_kms)
                        szesnasty_kms = str(szesnasty_kms)
                        siedemnasty_kms = str(siedemnasty_kms)
                        osiemnasty_kms = str(osiemnasty_kms)
                        dziewietnasty_kms = str(dziewietnasty_kms)
                        dwudziesty_kms = str(dwudziesty_kms)
                        djeden_kms = str(djeden_kms)

                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        czwarty_kmm = str(czwarty_kmm)
                        piaty_kmm = str(piaty_kmm)
                        szosty_kmm = str(szosty_kmm)
                        siodmy_kmm = str(siodmy_kmm)
                        osmy_kmm = str(osmy_kmm)
                        dziewiaty_kmm = str(dziewiaty_kmm)
                        dziesiaty_kmm = str(dziesiaty_kmm)
                        jedenasty_kmm = str(jedenasty_kmm)
                        dwunasty_kmm = str(dwunasty_kmm)
                        trzynasty_kmm = str(trzynasty_kmm)
                        czternasty_kmm = str(czternasty_kmm)
                        pietnasty_kmm = str(pietnasty_kmm)
                        szesnasty_kmm = str(szesnasty_kmm)
                        siedemnasty_kmm = str(siedemnasty_kmm)
                        osiemnasty_kmm = str(osiemnasty_kmm)
                        dziewietnasty_kmm = str(dziewietnasty_kmm)
                        dwudziesty_kmm = str(dwudziesty_kmm)
                        djeden_kmm = str(djeden_kmm)

                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)
                        czwarty_kmh = str(czwarty_kmh)
                        piaty_kmh = str(piaty_kmh)
                        szosty_kmh = str(szosty_kmh)
                        siodmy_kmh = str(siodmy_kmh)
                        osmy_kmh = str(osmy_kmh)
                        dziewiaty_kmh = str(dziewiaty_kmh)
                        dziesiaty_kmh = str(dziesiaty_kmh)
                        jedenasty_kmh = str(jedenasty_kmh)
                        dwunasty_kmh = str(dwunasty_kmh)
                        trzynasty_kmh = str(trzynasty_kmh)
                        czternasty_kmh = str(czternasty_kmh)
                        pietnasty_kmh = str(pietnasty_kmh)
                        szesnasty_kmh = str(szesnasty_kmh)
                        siedemnasty_kmh = str(siedemnasty_kmh)
                        osiemnasty_kmh = str(osiemnasty_kmh)
                        dziewietnasty_kmh = str(dziewietnasty_kmh)
                        dwudziesty_kmh = str(dwudziesty_kmh)
                        djeden_kmh = str(djeden_kmh)


                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \n"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \n"
                        miedzyczas_czwarty = "4 km: " + czwarty_kmh + "h : " + czwarty_kmm + "m : " + czwarty_kms + "s \n"
                        miedzyczas_piaty = "5 km: " + piaty_kmh + "h : " + piaty_kmm + "m : " + piaty_kms + "s \n"
                        miedzyczas_szosty = "6 km: " + szosty_kmh + "h : " + szosty_kmm + "m : " + szosty_kms + "s \n"
                        miedzyczas_siodmy = "7 km: " + siodmy_kmh + "h : " + siodmy_kmm + "m : " + siodmy_kms + "s \n"
                        miedzyczas_osmy = "8 km: " + osmy_kmh + "h : " + osmy_kmm + "m : " + osmy_kms + "s \n"
                        miedzyczas_dziewiaty = "9 km: " + dziewiaty_kmh + "h : " + dziewiaty_kmm + "m : " + dziewiaty_kms + "s \n"
                        miedzyczas_dziesiaty = "10 km: " + dziesiaty_kmh + "h : " + dziesiaty_kmm + "m : " + dziesiaty_kms + "s \n"
                        miedzyczas_jedenasty = "11 km: " + jedenasty_kmh + "h : " + jedenasty_kmm + "m : " + jedenasty_kms + "s \n"
                        miedzyczas_dwunasty = "12 km: " + dwunasty_kmh + "h : " + dwunasty_kmm + "m : " + dwunasty_kms + "s \n"
                        miedzyczas_trzynasty = "13 km: " + trzynasty_kmh + "h : " + trzynasty_kmm + "m : " + trzynasty_kms + "s \n"
                        miedzyczas_czternasty = "14 km: " + czternasty_kmh + "h : " + czternasty_kmm + "m : " + czternasty_kms + "s \n"
                        miedzyczas_pietnasty = "15 km: " + pietnasty_kmh + "h : " + pietnasty_kmm + "m : " + pietnasty_kms + "s \n"
                        miedzyczas_szesnasty = "16 km: " + szesnasty_kmh + "h : " + szesnasty_kmm + "m : " + szesnasty_kms + "s \n"
                        miedzyczas_siedemnasty = "17 km: " + siedemnasty_kmh + "h : " + siedemnasty_kmm + "m : " + siedemnasty_kms + "s \n"
                        miedzyczas_osiemnasty = "18 km: " + osiemnasty_kmh + "h : " + osiemnasty_kmm + "m : " + osiemnasty_kms + "s \n"
                        miedzyczas_dziewietnasty = "19 km: " + dziewietnasty_kmh + "h : " + dziewietnasty_kmm + "m : " + dziewietnasty_kms + "s \n"
                        miedzyczas_dwudziesty = "20 km: " + dwudziesty_kmh + "h : " + dwudziesty_kmm + "m : " + dwudziesty_kms + "s \n"
                        miedzyczas_djeden = "21 km: " + djeden_kmh + "h : " + djeden_kmm + "m : " + djeden_kms + "s \n"

                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty + miedzyczas_szosty + miedzyczas_siodmy + miedzyczas_osmy + miedzyczas_dziewiaty + miedzyczas_dziesiaty + miedzyczas_jedenasty + miedzyczas_dwunasty + miedzyczas_trzynasty + miedzyczas_czternasty + miedzyczas_pietnasty + miedzyczas_szesnasty + miedzyczas_siedemnasty + miedzyczas_osiemnasty + miedzyczas_dziewietnasty + miedzyczas_dwudziesty + miedzyczas_djeden

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")
            elif self.MkmButton.isChecked():
                MainWindow.resize(580, 580)
                self.pushButton.setGeometry(QtCore.QRect(180, 490, 111, 31))
                self.pushButton_2.setGeometry(QtCore.QRect(180, 530, 111, 31))
                self.result.setGeometry(QtCore.QRect(220, 170, 400, 305))
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h)/42.195
                        h_result = math.floor(x)
                        h_pomoc = (float(h)%42.195)*60
                        m_pomoc = float(m)+h_pomoc
                        m_result = math.floor(m_pomoc/42.195)
                        m_ppomoc = (m_pomoc%42.195)*60
                        s_pomoc = m_ppomoc+float(s)
                        s_result = math.floor(s_pomoc/42.195)

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
                        f_kms = 0
                        f_kmm = 0
                        f_kmh = 0

                        if ((pierwszy_kms + (s_result)) < 60):
                            drugi_kms = pierwszy_kms + (s_result)
                        elif ((pierwszy_kms + (s_result)) == 60):
                            drugi_kms = 0
                            drugi_kmm += 1
                        else:
                            drugi_kms = (pierwszy_kms + (s_result)) - 60
                            drugi_kmm += 1

                        if ((drugi_kms + (s_result)) < 60):
                            trzeci_kms = drugi_kms + (s_result)
                        elif ((drugi_kms + (s_result)) == 60):
                            trzeci_kms = 0
                            trzeci_kmm += 1
                        else:
                            trzeci_kms = (drugi_kms + (s_result)) - 60
                            trzeci_kmm += 1

                        if ((trzeci_kms + (s_result)) < 60):
                            czwarty_kms = trzeci_kms + (s_result)
                        elif (trzeci_kms + (s_result)) == 60:
                            czwarty_kms = 0
                            czwarty_kmm += 1
                        else:
                            czwarty_kms = (trzeci_kms + (s_result)) - 60
                            czwarty_kmm += 1

                        if ((czwarty_kms + (s_result)) < 60):
                            piaty_kms = czwarty_kms + (s_result)
                        elif (czwarty_kms + (s_result)) == 60:
                            piaty_kms = 0
                            piaty_kmm += 1
                        else:
                            piaty_kms = (czwarty_kms + (s_result)) - 60
                            piaty_kmm += 1

                        if ((piaty_kms + (s_result)) < 60):
                            szosty_kms = (piaty_kms + (s_result))
                        elif (piaty_kms + (s_result)) == 60:
                            szosty_kms = 0
                            szosty_kmm += 1
                        else:
                            szosty_kms = (piaty_kms + (s_result)) - 60
                            szosty_kmm += 1

                        if (szosty_kms + (s_result)) < 60:
                            siodmy_kms = (szosty_kms + (s_result))
                        elif (szosty_kms + (s_result)) == 60:
                            siodmy_kms = 0
                            siodmy_kmm += 1
                        else:
                            siodmy_kms = (szosty_kms + (s_result)) - 60
                            siodmy_kmm += 1

                        if (siodmy_kms + (s_result)) < 60:
                            osmy_kms = (siodmy_kms + (s_result))
                        elif (siodmy_kms + (s_result)) == 60:
                            osmy_kms = 0
                            osmy_kmm += 1
                        else:
                            osmy_kms = (siodmy_kms + (s_result)) - 60
                            osmy_kmm += 1

                        if (osmy_kms + (s_result)) < 60:
                            dziewiaty_kms = (osmy_kms + (s_result))
                        elif (osmy_kms + (s_result)) == 60:
                            dziewiaty_kms = 0
                            dziewiaty_kmm += 1
                        else:
                            dziewiaty_kms = (osmy_kms + (s_result)) - 60
                            dziewiaty_kmm += 1

                        if (dziewiaty_kms + (s_result)) < 60:
                            dziesiaty_kms = (dziewiaty_kms + (s_result))
                        elif ((dziewiaty_kms + (s_result))) == 60:
                            dziesiaty_kms = 0
                            dziesiaty_kmm += 1
                        else:
                            dziesiaty_kms = (dziewiaty_kms + (s_result)) - 60
                            dziesiaty_kmm += 1
                        if (dziesiaty_kms + (s_result)) < 60:
                            jedenasty_kms = (dziesiaty_kms + (s_result))
                        elif (dziesiaty_kms + (s_result)) == 60:
                            jedenasty_kms = 0
                            jedenasty_kmm += 1
                        else:
                            jedenasty_kms = (dziesiaty_kms + (s_result)) - 60
                            jedenasty_kmm += 1

                        if (jedenasty_kms + (s_result)) < 60:
                            dwunasty_kms = (jedenasty_kms + (s_result))
                        elif (jedenasty_kms + (s_result)) == 60:
                            dwunasty_kms = 0
                            dwunasty_kmm += 1
                        else:
                            dwunasty_kms = (jedenasty_kms + (s_result)) - 60
                            dwunasty_kmm += 1
                        if (dwunasty_kms + (s_result)) < 60:
                            trzynasty_kms = (dwunasty_kms + (s_result))
                        elif (dwunasty_kms + (s_result)) == 60:
                            trzynasty_kms = 0
                            trzynasty_kmm += 1
                        else:
                            trzynasty_kms = (dwunasty_kms + (s_result)) - 60
                            trzynasty_kmm += 1

                        if (trzynasty_kms + (s_result)) < 60:
                            czternasty_kms = (trzynasty_kms + (s_result))
                        elif (trzynasty_kms + (s_result)) == 60:
                            czternasty_kms = 0
                            czternasty_kmm += 1
                        else:
                            czternasty_kms = (trzynasty_kms + (s_result)) - 60
                            czternasty_kmm += 1
                        if (czternasty_kms + (s_result)) < 60:
                            pietnasty_kms = (czternasty_kms + (s_result))
                        elif (czternasty_kms + (s_result)) == 60:
                            pietnasty_kms = 0
                            pietnasty_kmm += 1
                        else:
                            pietnasty_kms = (czternasty_kms + (s_result)) - 60
                            pietnasty_kmm += 1

                        if (pietnasty_kms + (s_result)) < 60:
                            szesnasty_kms = (pietnasty_kms + (s_result))
                        elif (pietnasty_kms + (s_result)) == 60:
                            szesnasty_kms = 0
                            szesnasty_kmm += 1
                        else:
                            szesnasty_kms = (pietnasty_kms + (s_result)) - 60
                            szesnasty_kmm += 1

                        if (szesnasty_kms + (s_result)) < 60:
                            siedemnasty_kms = (szesnasty_kms + (s_result))
                        elif (szesnasty_kms + (s_result)) == 60:
                            siedemnasty_kms = 0
                            siedemnasty_kmm += 1
                        else:
                            siedemnasty_kms = (szesnasty_kms + (s_result)) - 60
                            siedemnasty_kmm += 1

                        if (siedemnasty_kms + (s_result)) < 60:
                            osiemnasty_kms = (siedemnasty_kms + (s_result))
                        elif (siedemnasty_kms + (s_result)) == 60:
                            osiemnasty_kms = 0
                            osiemnasty_kmm += 1
                        else:
                            osiemnasty_kms = (siedemnasty_kms + (s_result)) - 60
                            osiemnasty_kmm += 1

                        if (osiemnasty_kms + (s_result)) < 60:
                            dziewietnasty_kms = (osiemnasty_kms + (s_result))
                        elif (osiemnasty_kms + (s_result)) == 60:
                            dziewietnasty_kms = 0
                            dziewietnasty_kmm += 1
                        else:
                            dziewietnasty_kms = (osiemnasty_kms + (s_result)) - 60
                            dziewietnasty_kmm += 1

                        if (dziewietnasty_kms + (s_result)) < 60:
                            dwudziesty_kms = (dziewietnasty_kms + (s_result))
                        elif (dziewietnasty_kms + (s_result)) == 60:
                            dwudziesty_kms = 0
                            dwudziesty_kmm += 1
                        else:
                            dwudziesty_kms = (dziewietnasty_kms + (s_result)) - 60
                            dwudziesty_kmm += 1

                        if (dwudziesty_kms + (s_result)) < 60:
                            djeden_kms = (dwudziesty_kms + (s_result))
                        elif (dwudziesty_kms + (s_result)) == 60:
                            djeden_kms = 0
                            djeden_kmm += 1
                        else:
                            djeden_kms = (dwudziesty_kms + (s_result)) - 60
                            djeden_kmm += 1

                        if(djeden_kms + (s_result))<60:
                            ddwa_kms = (djeden_kms + (s_result))
                        elif (djeden_kms + (s_result))==60:
                            ddwa_kms = 0
                            ddwa_kmm +=1
                        else:
                            ddwa_kms = (djeden_kms + (s_result))-60
                            ddwa_kmm +=1

                        if(ddwa_kms+(s_result))<60:
                            dtrzy_kms = (ddwa_kms+(s_result))
                        elif (ddwa_kms+(s_result))==60:
                            dtrzy_kms = 0
                            dtrzy_kmm +=1
                        else:
                            dtrzy_kms = (ddwa_kms + (s_result))-60
                            dtrzy_kmm +=1

                        if(dtrzy_kms+(s_result))<60:
                            dcztery_kms = (dtrzy_kms+(s_result))
                        elif (dtrzy_kms+(s_result))==60:
                            dcztery_kms = 0
                            dcztery_kmm +=1
                        else:
                            dcztery_kms = (dtrzy_kms+(s_result))-60
                            dcztery_kmm +=1

                        if(dcztery_kms + (s_result))<60:
                            dpiec_kms = (dcztery_kms + (s_result))
                        elif (dcztery_kms + (s_result)) == 60:
                            dpiec_kms = 0
                            dpiec_kmm +=1
                        else:
                            dpiec_kms = (dcztery_kms + (s_result))-60
                            dpiec_kmm +=1

                        if(dpiec_kms + (s_result))<60:
                            dszesc_kms = (dpiec_kms + (s_result))
                        elif (dpiec_kms + (s_result))==60:
                            dszesc_kms = 0
                            dszesc_kmm +=1
                        else:
                            dszesc_kms = (dpiec_kms + (s_result))-60
                            dszesc_kmm +=1

                        if (dszesc_kms + (s_result))<60:
                            dsiedem_kms = (dszesc_kms + (s_result))
                        elif (dszesc_kms + (s_result))==60:
                            dsiedem_kms = 0
                            dsiedem_kmm +=1
                        else:
                            dsiedem_kms = (dszesc_kms + (s_result))-60
                            dsiedem_kmm +=1

                        if(dsiedem_kms + (s_result))<60:
                            dosiem_kms = (dsiedem_kms + (s_result))
                        elif (dsiedem_kms + (s_result))==60:
                            dosiem_kms = 0
                            dosiem_kmm +=1
                        else:
                            dosiem_kms = (dsiedem_kms + (s_result))-60
                            dosiem_kmm +=1

                        if(dosiem_kms + (s_result))<60:
                            ddziewiec_kms = (dosiem_kms + (s_result))
                        elif (dosiem_kms + (s_result))==60:
                            ddziewiec_kms = 0
                            ddziewiec_kmm +=1
                        else:
                            ddziewiec_kms = (dosiem_kms + (s_result))-60
                            ddziewiec_kmm +=1

                        if(ddziewiec_kms + (s_result))<60:
                            trzydziesci_kms = (ddziewiec_kms + (s_result))
                        elif (ddziewiec_kms + (s_result))==60:
                            trzydziesci_kms = 0
                            trzydziesci_kmm +=1
                        else:
                            trzydziesci_kms = (ddziewiec_kms + (s_result))-60
                            trzydziesci_kmm +=1

                        if(trzydziesci_kms + s_result)<60:
                            tjeden_kms = (trzydziesci_kms + s_result)
                        elif (trzydziesci_kms + s_result)==60:
                            tjeden_kms = 0
                            tjeden_kmm +=1
                        else:
                            tjeden_kms = (trzydziesci_kms + s_result)-60
                            tjeden_kmm +=1

                        if(tjeden_kms + s_result)<60:
                            tdwa_kms = (tjeden_kms + s_result)
                        elif (tjeden_kms + s_result)==60:
                            tdwa_kms = 0
                            tdwa_kmm +=1
                        else:
                            tdwa_kms = (tjeden_kms + s_result)-60
                            tdwa_kmm +=1

                        if(tdwa_kms + s_result)<60:
                            ttrzy_kms = (tdwa_kms + s_result)
                        elif (tdwa_kms + s_result)==60:
                            ttrzy_kms = 0
                            ttrzy_kmm +=1
                        else:
                            ttrzy_kms = (tdwa_kms + s_result)-60
                            ttrzy_kmm +=1

                        if(ttrzy_kms + s_result)<60:
                            tcztery_kms = (ttrzy_kms + s_result)
                        elif (ttrzy_kms + s_result)==60:
                            tcztery_kms = 0
                            tcztery_kmm +=1
                        else:
                            tcztery_kms = (ttrzy_kms + s_result)-60
                            tcztery_kmm +=1

                        if(tcztery_kms + s_result)<60:
                            tpiec_kms = (tcztery_kms + s_result)
                        elif (tcztery_kms + s_result)==60:
                            tpiec_kms = 0
                            tpiec_kmm+=1
                        else:
                            tpiec_kms = (tcztery_kms + s_result)-60
                            tpiec_kmm +=1

                        if(tpiec_kms + s_result)<60:
                            tszesc_kms = (tpiec_kms + s_result)
                        elif (tpiec_kms + s_result)==60:
                            tszesc_kms = 0
                            tszesc_kmm +=1
                        else:
                            tszesc_kms = (tpiec_kms + s_result)-60
                            tszesc_kmm +=1

                        if(tszesc_kms + s_result)<60:
                            tsiedem_kms = (tszesc_kms + s_result)
                        elif (tszesc_kms + s_result)==60:
                            tsiedem_kms = 0
                            tsiedem_kmm +=1
                        else:
                            tsiedem_kms = (tszesc_kms + s_result)-60
                            tsiedem_kmm +=1

                        if(tsiedem_kms + s_result)<60:
                            tosiem_kms = (tsiedem_kms + s_result)
                        elif (tsiedem_kms + s_result)==60:
                            tosiem_kms = 0
                            tosiem_kmm +=1
                        else:
                            tosiem_kms = tsiedem_kms + s_result- -60
                            tosiem_kmm +=1

                        if(tosiem_kms + s_result)<60:
                            tdziewiec_kms = (tosiem_kms + s_result)
                        elif (tosiem_kms + s_result)==60:
                            tdziewiec_kms = 0
                            tdziewiec_kmm +=1
                        else:
                            tdziewiec_kms = (tosiem_kms + s_result)-60
                            tdziewiec_kmm +=1

                        if (tdziewiec_kms + s_result)<60:
                            czterdziesci_kms = (tdziewiec_kms + s_result)
                        elif (tdziewiec_kms + s_result)==60:
                            czterdziesci_kms = 0
                            czterdziesci_kmm +=1
                        else:
                            czterdziesci_kms = (tdziewiec_kms + s_result)-60
                            czterdziesci_kmm +=1

                        if(czterdziesci_kms + s_result)<60:
                            cjeden_kms = (czterdziesci_kms + s_result)
                        elif (czterdziesci_kms + s_result) == 60:
                            cjeden_kms = 0
                            cjeden_kmm +=1
                        else:
                            cjeden_kms = czterdziesci_kms + s_result -60
                            cjeden_kmm +=1

                        if(cjeden_kms + s_result)<60:
                            cdwa_kms = (cjeden_kms + s_result)
                        elif (cjeden_kms + s_result)==60:
                            cdwa_kms = 0
                            cdwa_kmm +=1
                        else:
                            cdwa_kms = (cjeden_kms + s_result) -60
                            cdwa_kmm +=1


                        if (pierwszy_kmm + (m_result) + drugi_kmm) < 60:
                            drugi_kmm += (pierwszy_kmm + (m_result))
                        elif (pierwszy_kmm + (m_result) + drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh += 1
                        else:
                            drugi_kmm = (pierwszy_kmm + (m_result) + drugi_kmm) - 60
                            drugi_kmh += 1

                        if (drugi_kmm + (m_result) + trzeci_kmm) < 60:
                            trzeci_kmm += (drugi_kmm + (m_result))
                        elif (drugi_kmm + (m_result) + trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh += 1
                        else:
                            trzeci_kmm = (drugi_kmm + (m_result) + trzeci_kmm) - 60
                            trzeci_kmh += 1

                        if (trzeci_kmm + (m_result) + czwarty_kmm) < 60:
                            czwarty_kmm += (trzeci_kmm + (m_result))
                        elif (trzeci_kmm + (m_result) + czwarty_kmm) == 60:
                            czwarty_kmm = 0
                            czwarty_kmh += 1
                        else:
                            czwarty_kmm = (trzeci_kmm + (m_result) + czwarty_kmm) - 60
                            czwarty_kmh += 1

                        if (czwarty_kmm + (m_result) + piaty_kmm) < 60:
                            piaty_kmm += (czwarty_kmm + (m_result))
                        elif (czwarty_kmm + (m_result) + piaty_kmm) == 60:
                            piaty_kmm = 0
                            piaty_kmh += 1
                        else:
                            piaty_kmm = (czwarty_kmm + (m_result) + piaty_kmm) - 60
                            piaty_kmh += 1

                        if (piaty_kmm + (m_result) + szosty_kmm) < 60:
                            szosty_kmm += piaty_kmm + (m_result)
                        elif (piaty_kmm + (m_result) + szosty_kmm) == 60:
                            szosty_kmm = 0
                            szosty_kmh += 1
                        else:
                            szosty_kmm = (piaty_kmm + (m_result) + szosty_kmm) - 60
                            szosty_kmh += 1

                        if (szosty_kmm + (m_result) + siodmy_kmm) < 60:
                            siodmy_kmm += szosty_kmm + (m_result)
                        elif (szosty_kmm + (m_result) + siodmy_kmm) == 60:
                            siodmy_kmm = 0
                            siodmy_kmh += 1
                        else:
                            siodmy_kmm = (szosty_kmm + (m_result) + siodmy_kmm) - 60
                            siodmy_kmh += 1

                        if (siodmy_kmm + (m_result) + osmy_kmm) < 60:
                            osmy_kmm += siodmy_kmm + (m_result)
                        elif (siodmy_kmm + (m_result) + osmy_kmm) == 60:
                            osmy_kmm = 0
                            osmy_kmh += 1
                        else:
                            osmy_kmm = (siodmy_kmm + (m_result) + osmy_kmm) - 60
                            osmy_kmh += 1

                        if (osmy_kmm + (m_result) + dziewiaty_kmm) < 60:
                            dziewiaty_kmm += osmy_kmm + (m_result)
                        elif (osmy_kmm + (m_result) + dziewiaty_kmm) == 60:
                            dziewiaty_kmm = 0
                            dziewiaty_kmh += 1
                        else:
                            dziewiaty_kmm = (osmy_kmm + (m_result) + dziewiaty_kmm) - 60
                            dziewiaty_kmh += 1

                        if (dziewiaty_kmm + (m_result) + dziesiaty_kmm) < 60:
                            dziesiaty_kmm += dziewiaty_kmm + (m_result)
                        elif (dziewiaty_kmm + (m_result) + dziesiaty_kmm) == 60:
                            dziesiaty_kmm = 0
                            dziesiaty_kmh += 1
                        else:
                            dziesiaty_kmm = (dziewiaty_kmm + (m_result) + dziesiaty_kmm) - 60
                            dziesiaty_kmh += 1
                        if (dziesiaty_kmm + (m_result) + jedenasty_kmm) < 60:
                            jedenasty_kmm += dziesiaty_kmm + (m_result)
                        elif (dziesiaty_kmm + (m_result) + jedenasty_kmm) == 60:
                            jedenasty_kmm = 0
                            jedenasty_kmh += 1
                        else:
                            jedenasty_kmm = (dziesiaty_kmm + (m_result) + jedenasty_kmm) - 60
                            jedenasty_kmh += 1
                        if (jedenasty_kmm + (m_result) + dwunasty_kmm) < 60:
                            dwunasty_kmm += jedenasty_kmm + (m_result)
                        elif (jedenasty_kmm + (m_result) + dwunasty_kmm) == 60:
                            dwunasty_kmm = 0
                            dwunasty_kmh += 1
                        else:
                            dwunasty_kmm = (jedenasty_kmm + (m_result) + dwunasty_kmm) - 60
                            dwunasty_kmh += 1
                        if (dwunasty_kmm + (m_result) + trzynasty_kmm) < 60:
                            trzynasty_kmm += dwunasty_kmm + (m_result)
                        elif (dwunasty_kmm + (m_result) + trzynasty_kmm) == 60:
                            trzynasty_kmm = 0
                            trzynasty_kmh += 1
                        else:
                            trzynasty_kmm = (dwunasty_kmm + (m_result) + trzynasty_kmm) - 60
                            trzynasty_kmh += 1

                        if (trzynasty_kmm + (m_result) + czternasty_kmm) < 60:
                            czternasty_kmm += trzynasty_kmm + (m_result)
                        elif (trzynasty_kmm + (m_result) + czternasty_kmm) == 60:
                            czternasty_kmm = 0
                            czternasty_kmh += 1
                        else:
                            czternasty_kmm = (trzynasty_kmm + (m_result) + czternasty_kmm) - 60
                            czternasty_kmh += 1
                        if (czternasty_kmm + (m_result) + pietnasty_kmm) < 60:
                            pietnasty_kmm += czternasty_kmm + (m_result)
                        elif (czternasty_kmm + (m_result) + pietnasty_kmm) == 60:
                            pietnasty_kmm = 0
                            pietnasty_kmh += 1
                        else:
                            pietnasty_kmm = (czternasty_kmm + (m_result) + pietnasty_kmm) - 60
                            pietnasty_kmh += 1

                        if (pietnasty_kmm + (m_result) + szesnasty_kmm) < 60:
                            szesnasty_kmm += pietnasty_kmm + (m_result)
                        elif (pietnasty_kmm + (m_result) + szesnasty_kmm) == 60:
                            szesnasty_kmm = 0
                            szesnasty_kmh += 1
                        else:
                            szesnasty_kmm = (pietnasty_kmm + (m_result) + szesnasty_kmm) - 60
                            szesnasty_kmh += 1
                        if (szesnasty_kmm + (m_result) + siedemnasty_kmm) < 60:
                            siedemnasty_kmm += szesnasty_kmm + (m_result)
                        elif (szesnasty_kmm + (m_result) + siedemnasty_kmm) == 60:
                            siedemnasty_kmm = 0
                            siedemnasty_kmh += 1
                        else:
                            siedemnasty_kmm = (szesnasty_kmm + (m_result) + siedemnasty_kmm) - 60
                            siedemnasty_kmh += 1

                        if (siedemnasty_kmm + (m_result) + osiemnasty_kmm) < 60:
                            osiemnasty_kmm += siedemnasty_kmm + (m_result)
                        elif (siedemnasty_kmm + (m_result) + osiemnasty_kmm) == 60:
                            osiemnasty_kmm = 0
                            osiemnasty_kmh += 1
                        else:
                            osiemnasty_kmm = (siedemnasty_kmm + (m_result) + osiemnasty_kmm) - 60
                            osiemnasty_kmh += 1

                        if (osiemnasty_kmm + (m_result) + dziewietnasty_kmm) < 60:
                            dziewietnasty_kmm += osiemnasty_kmm + (m_result)
                        elif (osiemnasty_kmm + (m_result) + dziewietnasty_kmm) == 60:
                            dziewietnasty_kmm = 0
                            dziewietnasty_kmh += 1
                        else:
                            dziewietnasty_kmm = (osiemnasty_kmm + (m_result) + dziewietnasty_kmm) - 60
                            dziewietnasty_kmh += 1

                        if (dziewietnasty_kmm + (m_result) + dwudziesty_kmm) < 60:
                            dwudziesty_kmm += dziewietnasty_kmm + (m_result)
                        elif (dziewietnasty_kmm + (m_result) + dwudziesty_kmm) == 60:
                            dwudziesty_kmm = 0
                            dwudziesty_kmh += 1
                        else:
                            dwudziesty_kmm = (dziewietnasty_kmm + (m_result) + dwudziesty_kmm) - 60
                            dwudziesty_kmh += 1

                        if (dwudziesty_kmm + (m_result) + djeden_kmm) < 60:
                            djeden_kmm += dwudziesty_kmm + (m_result)
                        elif (dwudziesty_kmm + (m_result) + djeden_kmm) == 60:
                            djeden_kmm = 0
                            djeden_kmh += 1
                        else:
                            djeden_kmm = (dwudziesty_kmm + (m_result) + djeden_kmm) - 60
                            djeden_kmh += 1

                        if(djeden_kmm + m_result + ddwa_kmm) <60:
                            ddwa_kmm += djeden_kmm + m_result
                        elif (djeden_kmm + m_result + ddwa_kmm)==60:
                            ddwa_kmm = 0
                            ddwa_kmh +=1
                        else:
                            ddwa_kmm = (djeden_kmm + m_result + ddwa_kmm)-60
                            ddwa_kmh +=1

                        if(ddwa_kmm + m_result + dtrzy_kmm)<60:
                            dtrzy_kmm += ddwa_kmm + m_result
                        elif (ddwa_kmm + m_result + dtrzy_kmm)==60:
                            dtrzy_kmm= 0
                            dtrzy_kmh +=1
                        else:
                            dtrzy_kmm = (ddwa_kmm + m_result + dtrzy_kmm)-60
                            dtrzy_kmh +=1

                        if(dtrzy_kmm + m_result + dcztery_kmm)<60:
                            dcztery_kmm += dtrzy_kmm + m_result
                        elif (dtrzy_kmm + m_result + dcztery_kmm) ==60:
                            dcztery_kmm = 0
                            dcztery_kmh +=1
                        else:
                            dcztery_kmm = (dtrzy_kmm + m_result + dcztery_kmm)-60
                            dcztery_kmh +=1

                        if(dcztery_kmm + m_result + dpiec_kmm)<60:
                            dpiec_kmm += dcztery_kmm + m_result
                        elif (dcztery_kmm + m_result + dpiec_kmm) ==60:
                            dpiec_kmm = 0
                            dpiec_kmh +=1
                        else:
                            dpiec_kmm = (dcztery_kmm + m_result + dpiec_kmm)-60
                            dpiec_kmh +=1

                        if (dpiec_kmm + m_result + dszesc_kmm)<60:
                            dszesc_kmm += dpiec_kmm + m_result
                        elif (dpiec_kmm + m_result + dszesc_kmm)==60:
                            dszesc_kmm = 0
                            dszesc_kmh +=1
                        else:
                            dszesc_kmm = (dpiec_kmm + m_result + dszesc_kmm)-60
                            dszesc_kmh +=1

                        if (dszesc_kmm + m_result + dsiedem_kmm)<60:
                            dsiedem_kmm += dszesc_kmm + m_result
                        elif (dszesc_kmm + m_result + dsiedem_kmm)==60:
                            dsiedem_kmm = 0
                            dsiedem_kmh +=1
                        else:
                            dsiedem_kmm = (dszesc_kmm + m_result + dsiedem_kmm)-60
                            dsiedem_kmh +=1

                        if(dsiedem_kmm + m_result + dosiem_kmm)<60:
                            dosiem_kmm += dsiedem_kmm + m_result
                        elif (dsiedem_kmm + m_result + dosiem_kmm)==60:
                            dosiem_kmm = 0
                            dosiem_kmh +=1
                        else:
                            dosiem_kmm = (dsiedem_kmm + m_result + dosiem_kmm)-60
                            dosiem_kmh +=1

                        if(dosiem_kmm + m_result + ddziewiec_kmm)<60:
                            ddziewiec_kmm += dosiem_kmm + m_result
                        elif (dosiem_kmm + m_result + ddziewiec_kmm)==60:
                            ddziewiec_kmm = 0
                            ddziewiec_kmh +=1
                        else:
                            ddziewiec_kmm = (dosiem_kmm + m_result + ddziewiec_kmm)-60
                            ddziewiec_kmh +=1

                        if(ddziewiec_kmm + m_result + trzydziesci_kmm) <60:
                            trzydziesci_kmm += ddziewiec_kmm + m_result
                        elif (ddziewiec_kmm + m_result + trzydziesci_kmm)==60:
                            trzydziesci_kmm = 0
                            trzydziesci_kmh +=1
                        else:
                            trzydziesci_kmm = (ddziewiec_kmm + m_result + trzydziesci_kmm)-60
                            trzydziesci_kmh +=1

                        if(trzydziesci_kmm + m_result + tjeden_kmm)<60:
                            tjeden_kmm += trzydziesci_kmm + m_result
                        elif (trzydziesci_kmm + m_result + tjeden_kmm)==60:
                            tjeden_kmm = 0
                            tjeden_kmh+=1
                        else:
                            tjeden_kmm =  (trzydziesci_kmm + m_result + tjeden_kmm)-60
                            tjeden_kmh +=1

                        if(tjeden_kmm + m_result + tdwa_kmm)<60:
                            tdwa_kmm += tjeden_kmm + m_result
                        elif (tjeden_kmm + m_result + tdwa_kmm)==60:
                            tdwa_kmm = 0
                            tdwa_kmh +=1
                        else:
                            tdwa_kmm=(tjeden_kmm + m_result + tdwa_kmm)-60
                            tdwa_kmh +=1

                        if(tdwa_kmm + m_result + ttrzy_kmm) <60:
                            ttrzy_kmm += tdwa_kmm + m_result
                        elif (tdwa_kmm + m_result + ttrzy_kmm) == 60:
                            ttrzy_kmm = 0
                            ttrzy_kmh+=1
                        else:
                            ttrzy_kmm = (tdwa_kmm + m_result + ttrzy_kmm)-60
                            ttrzy_kmh +=1

                        if(ttrzy_kmm + m_result + tcztery_kmm) <60:
                            tcztery_kmm += ttrzy_kmm + m_result
                        elif (ttrzy_kmm + m_result + tcztery_kmm) == 60:
                            tcztery_kmm = 0
                            tcztery_kmh +=1
                        else:
                            tcztery_kmm = (ttrzy_kmm + m_result + tcztery_kmm)-60
                            tcztery_kmh +=1

                        if(tcztery_kmm + m_result + tpiec_kmm)<60:
                            tpiec_kmm += tcztery_kmm + m_result
                        elif (tcztery_kmm + m_result + tpiec_kmm) == 60:
                            tpiec_kmm = 0
                            tpiec_kmh +=1
                        else:
                            tpiec_kmm = (tcztery_kmm + m_result + tpiec_kmm) -60
                            tpiec_kmh +=1

                        if (tpiec_kmm + m_result + tszesc_kmm) < 60:
                            tszesc_kmm += tpiec_kmm + m_result
                        elif (tpiec_kmm + m_result + tszesc_kmm)==60:
                            tszesc_kmm = 0
                            tszesc_kmh +=1
                        else:
                            tszesc_kmm = (tpiec_kmm + m_result + tszesc_kmm)-60
                            tszesc_kmh +=1

                        if (tszesc_kmm + m_result + tsiedem_kmm)<60:
                            tsiedem_kmm += tszesc_kmm + m_result
                        elif (tszesc_kmm + m_result + tsiedem_kmm)==60:
                            tsiedem_kmm = 0
                            tsiedem_kmh +=1
                        else:
                            tsiedem_kmm = (tszesc_kmm + m_result + tsiedem_kmm)-60
                            tsiedem_kmh +=1

                        if (tsiedem_kmm + m_result + tosiem_kmm) <60:
                            tosiem_kmm += tsiedem_kmm + m_result
                        elif (tsiedem_kmm + m_result + tosiem_kmm)==60:
                            tosiem_kmm = 0
                            tosiem_kmh +=1
                        else:
                            tosiem_kmm = (tsiedem_kmm + m_result + tosiem_kmm) -60
                            tosiem_kmh +=1

                        if (tosiem_kmm + m_result + tdziewiec_kmm)<60:
                            tdziewiec_kmm += tosiem_kmm + m_result
                        elif (tosiem_kmm + m_result + tdziewiec_kmm)==60:
                            tdziewiec_kmm = 0
                            tdziewiec_kmh +=1
                        else:
                            tdziewiec_kmm = (tosiem_kmm + m_result + tdziewiec_kmm)-60
                            tdziewiec_kmh +=1

                        if(tdziewiec_kmm + m_result + czterdziesci_kmm)<60:
                            czterdziesci_kmm += tdziewiec_kmm + m_result
                        elif (tdziewiec_kmm + m_result + czterdziesci_kmm)==60:
                            czterdziesci_kmm = 0
                            czterdziesci_kmh +=1
                        else:
                            czterdziesci_kmm = (tdziewiec_kmm + m_result + czterdziesci_kmm)-60
                            czterdziesci_kmh +=1

                        if(czterdziesci_kmm + m_result + cjeden_kmm)<60:
                            cjeden_kmm += czterdziesci_kmm + m_result
                        elif (czterdziesci_kmm + m_result + cjeden_kmm)==60:
                            cjeden_kmm = 0
                            cjeden_kmh += 1
                        else:
                            cjeden_kmm = (czterdziesci_kmm + m_result + cjeden_kmm)-60
                            cjeden_kmh +=1

                        if(cjeden_kmm + m_result + cdwa_kmm)<60:
                            cdwa_kmm += cjeden_kmm + m_result
                        elif (cjeden_kmm + m_result + cdwa_kmm)==60:
                            cdwa_kmm = 0
                            cdwa_kmh +=1
                        else:
                            cdwa_kmm = (cjeden_kmm + m_result + cdwa_kmm)-60
                            cdwa_kmh +=1



                        drugi_kmh += pierwszy_kmh + h_result
                        trzeci_kmh += drugi_kmh + h_result
                        czwarty_kmh += trzeci_kmh + h_result
                        piaty_kmh += czwarty_kmh + h_result
                        szosty_kmh += piaty_kmh + h_result
                        siodmy_kmh += szosty_kmh + h_result
                        osmy_kmh += siodmy_kmh + h_result
                        dziewiaty_kmh += osmy_kmh + h_result
                        dziesiaty_kmh += dziewiaty_kmh + h_result
                        jedenasty_kmh += dziesiaty_kmh + h_result
                        dwunasty_kmh += jedenasty_kmh + h_result
                        trzynasty_kmh += dwunasty_kmh + h_result
                        czternasty_kmh += trzynasty_kmh + h_result
                        pietnasty_kmh += czternasty_kmh + h_result
                        szesnasty_kmh += pietnasty_kmh + h_result
                        siedemnasty_kmh += szesnasty_kmh + h_result
                        osiemnasty_kmh += siedemnasty_kmh + h_result
                        dziewietnasty_kmh += osiemnasty_kmh + h_result
                        dwudziesty_kmh += dziewietnasty_kmh + h_result
                        djeden_kmh += dwudziesty_kmh + h_result
                        ddwa_kmh += djeden_kmh + h_result
                        dtrzy_kmh += ddwa_kmh +  h_result
                        dcztery_kmh += dtrzy_kmh + h_result
                        dpiec_kmh += dcztery_kmh + h_result
                        dszesc_kmh += dpiec_kmh + h_result
                        dsiedem_kmh += dszesc_kmh + h_result
                        dosiem_kmh += dsiedem_kmh + h_result
                        ddziewiec_kmh += dosiem_kmh + h_result
                        trzydziesci_kmh += ddziewiec_kmh + h_result
                        tjeden_kmh += trzydziesci_kmh + h_result
                        tdwa_kmh += tjeden_kmh + h_result
                        ttrzy_kmh += tdwa_kmh + h_result
                        tcztery_kmh += ttrzy_kmh + h_result
                        tpiec_kmh += tcztery_kmh + h_result
                        tszesc_kmh += tpiec_kmh + h_result
                        tsiedem_kmh+= tszesc_kmh + h_result
                        tosiem_kmh += tsiedem_kmh + h_result
                        tdziewiec_kmh += tosiem_kmh + h_result
                        czterdziesci_kmh += tdziewiec_kmh + h_result
                        cjeden_kmh += czterdziesci_kmh + h_result
                        cdwa_kmh += cjeden_kmh + h_result

                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result = str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        czwarty_kms = str(czwarty_kms)
                        piaty_kms = str(piaty_kms)
                        szosty_kms = str(szosty_kms)
                        siodmy_kms = str(siodmy_kms)
                        osmy_kms = str(osmy_kms)
                        dziewiaty_kms = str(dziewiaty_kms)
                        dziesiaty_kms = str(dziesiaty_kms)
                        jedenasty_kms = str(jedenasty_kms)
                        dwunasty_kms = str(dwunasty_kms)
                        trzynasty_kms = str(trzynasty_kms)
                        czternasty_kms = str(czternasty_kms)
                        pietnasty_kms = str(pietnasty_kms)
                        szesnasty_kms = str(szesnasty_kms)
                        siedemnasty_kms = str(siedemnasty_kms)
                        osiemnasty_kms = str(osiemnasty_kms)
                        dziewietnasty_kms = str(dziewietnasty_kms)
                        dwudziesty_kms = str(dwudziesty_kms)
                        djeden_kms = str(djeden_kms)
                        ddwa_kms = str(ddwa_kms)
                        dtrzy_kms = str(dtrzy_kms)
                        dcztery_kms = str(dcztery_kms)
                        dpiec_kms = str(dpiec_kms)
                        dszesc_kms = str(dszesc_kms)
                        dsiedem_kms = str(dsiedem_kms)
                        dosiem_kms = str (dosiem_kms)
                        ddziewiec_kms = str(ddziewiec_kms)
                        trzydziesci_kms = str(trzydziesci_kms)
                        tjeden_kms = str(tjeden_kms)
                        tdwa_kms = str(tdwa_kms)
                        ttrzy_kms = str(ttrzy_kms)
                        tcztery_kms = str(tcztery_kms)
                        tpiec_kms = str(tpiec_kms)
                        tszesc_kms = str(tszesc_kms)
                        tsiedem_kms = str(tsiedem_kms)
                        tosiem_kms = str(tosiem_kms)
                        tdziewiec_kms = str(tdziewiec_kms)
                        czterdziesci_kms = str(czterdziesci_kms)
                        cjeden_kms = str(cjeden_kms)
                        cdwa_kms = str(cdwa_kms)

                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        czwarty_kmm = str(czwarty_kmm)
                        piaty_kmm = str(piaty_kmm)
                        szosty_kmm = str(szosty_kmm)
                        siodmy_kmm = str(siodmy_kmm)
                        osmy_kmm = str(osmy_kmm)
                        dziewiaty_kmm = str(dziewiaty_kmm)
                        dziesiaty_kmm = str(dziesiaty_kmm)
                        jedenasty_kmm = str(jedenasty_kmm)
                        dwunasty_kmm = str(dwunasty_kmm)
                        trzynasty_kmm = str(trzynasty_kmm)
                        czternasty_kmm = str(czternasty_kmm)
                        pietnasty_kmm = str(pietnasty_kmm)
                        szesnasty_kmm = str(szesnasty_kmm)
                        siedemnasty_kmm = str(siedemnasty_kmm)
                        osiemnasty_kmm = str(osiemnasty_kmm)
                        dziewietnasty_kmm = str(dziewietnasty_kmm)
                        dwudziesty_kmm = str(dwudziesty_kmm)
                        djeden_kmm = str(djeden_kmm)
                        ddwa_kmm = str(ddwa_kmm)
                        dtrzy_kmm = str(dtrzy_kmm)
                        dcztery_kmm = str(dcztery_kmm)
                        dpiec_kmm = str(dpiec_kmm)
                        dszesc_kmm = str(dszesc_kmm)
                        dsiedem_kmm = str(dsiedem_kmm)
                        dosiem_kmm = str(dosiem_kmm)
                        ddziewiec_kmm = str(ddziewiec_kmm)
                        trzydziesci_kmm = str(trzydziesci_kmm)
                        tjeden_kmm = str(tjeden_kmm)
                        tdwa_kmm = str(tdwa_kmm)
                        ttrzy_kmm = str(ttrzy_kmm)
                        tcztery_kmm = str(tcztery_kmm)
                        tpiec_kmm = str(tpiec_kmm)
                        tszesc_kmm = str(tszesc_kmm)
                        tsiedem_kmm = str(tsiedem_kmm)
                        tosiem_kmm = str(tosiem_kmm)
                        tdziewiec_kmm = str(tdziewiec_kmm)
                        czterdziesci_kmm = str(czterdziesci_kmm)
                        cjeden_kmm = str(cjeden_kmm)
                        cdwa_kmm = str(cdwa_kmm)

                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)
                        czwarty_kmh = str(czwarty_kmh)
                        piaty_kmh = str(piaty_kmh)
                        szosty_kmh = str(szosty_kmh)
                        siodmy_kmh = str(siodmy_kmh)
                        osmy_kmh = str(osmy_kmh)
                        dziewiaty_kmh = str(dziewiaty_kmh)
                        dziesiaty_kmh = str(dziesiaty_kmh)
                        jedenasty_kmh = str(jedenasty_kmh)
                        dwunasty_kmh = str(dwunasty_kmh)
                        trzynasty_kmh = str(trzynasty_kmh)
                        czternasty_kmh = str(czternasty_kmh)
                        pietnasty_kmh = str(pietnasty_kmh)
                        szesnasty_kmh = str(szesnasty_kmh)
                        siedemnasty_kmh = str(siedemnasty_kmh)
                        osiemnasty_kmh = str(osiemnasty_kmh)
                        dziewietnasty_kmh = str(dziewietnasty_kmh)
                        dwudziesty_kmh = str(dwudziesty_kmh)
                        djeden_kmh = str(djeden_kmh)
                        ddwa_kmh = str(ddwa_kmh)
                        dtrzy_kmh = str(dtrzy_kmh)
                        dcztery_kmh = str(dcztery_kmh)
                        dpiec_kmh = str(dpiec_kmh)
                        dszesc_kmh = str(dszesc_kmh)
                        dsiedem_kmh = str(dsiedem_kmh)
                        dosiem_kmh = str(dosiem_kmh)
                        ddziewiec_kmh = str(ddziewiec_kmh)
                        trzydziesci_kmh = str(trzydziesci_kmh)
                        tjeden_kmh = str(tjeden_kmh)
                        tdwa_kmh = str(tdwa_kmh)
                        ttrzy_kmh = str(ttrzy_kmh)
                        tcztery_kmh = str(tcztery_kmh)
                        tpiec_kmh = str(tpiec_kmh)
                        tszesc_kmh = str(tszesc_kmh)
                        tsiedem_kmh = str(tsiedem_kmh)
                        tosiem_kmh = str(tosiem_kmh)
                        tdziewiec_kmh = str(tdziewiec_kmh)
                        czterdziesci_kmh = str(czterdziesci_kmh)
                        cjeden_kmh = str(cjeden_kmh)
                        cdwa_kmh = str(cdwa_kmh)

                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \t"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \t"
                        miedzyczas_czwarty = "4 km: " + czwarty_kmh + "h : " + czwarty_kmm + "m : " + czwarty_kms + "s \n"
                        miedzyczas_piaty = "5 km: " + piaty_kmh + "h : " + piaty_kmm + "m : " + piaty_kms + "s \t"
                        miedzyczas_szosty = "6 km: " + szosty_kmh + "h : " + szosty_kmm + "m : " + szosty_kms + "s \n"
                        miedzyczas_siodmy = "7 km: " + siodmy_kmh + "h : " + siodmy_kmm + "m : " + siodmy_kms + "s \t"
                        miedzyczas_osmy = "8 km: " + osmy_kmh + "h : " + osmy_kmm + "m : " + osmy_kms + "s \n"
                        miedzyczas_dziewiaty = "9 km: " + dziewiaty_kmh + "h : " + dziewiaty_kmm + "m : " + dziewiaty_kms + "s \t"
                        miedzyczas_dziesiaty = "10 km: " + dziesiaty_kmh + "h : " + dziesiaty_kmm + "m : " + dziesiaty_kms + "s \n"
                        miedzyczas_jedenasty = "11 km: " + jedenasty_kmh + "h : " + jedenasty_kmm + "m : " + jedenasty_kms + "s \t"
                        miedzyczas_dwunasty = "12 km: " + dwunasty_kmh + "h : " + dwunasty_kmm + "m : " + dwunasty_kms + "s \n"
                        miedzyczas_trzynasty = "13 km: " + trzynasty_kmh + "h : " + trzynasty_kmm + "m : " + trzynasty_kms + "s \t"
                        miedzyczas_czternasty = "14 km: " + czternasty_kmh + "h : " + czternasty_kmm + "m : " + czternasty_kms + "s \n"
                        miedzyczas_pietnasty = "15 km: " + pietnasty_kmh + "h : " + pietnasty_kmm + "m : " + pietnasty_kms + "s \t"
                        miedzyczas_szesnasty = "16 km: " + szesnasty_kmh + "h : " + szesnasty_kmm + "m : " + szesnasty_kms + "s \n"
                        miedzyczas_siedemnasty = "17 km: " + siedemnasty_kmh + "h : " + siedemnasty_kmm + "m : " + siedemnasty_kms + "s \t"
                        miedzyczas_osiemnasty = "18 km: " + osiemnasty_kmh + "h : " + osiemnasty_kmm + "m : " + osiemnasty_kms + "s \n"
                        miedzyczas_dziewietnasty = "19 km: " + dziewietnasty_kmh + "h : " + dziewietnasty_kmm + "m : " + dziewietnasty_kms + "s \t"
                        miedzyczas_dwudziesty = "20 km: " + dwudziesty_kmh + "h : " + dwudziesty_kmm + "m : " + dwudziesty_kms + "s \n"
                        miedzyczas_djeden = "21 km: " + djeden_kmh + "h : " + djeden_kmm + "m : " + djeden_kms + "s \t"
                        miedzyczas_ddwa = "22 km: " + ddwa_kmh + "h : " + ddwa_kmm + "m : " + ddwa_kms + "s \n"
                        miedzyczas_dtrzy = "23 km: " + dtrzy_kmh + "h : " + dtrzy_kmm + "m : " + dtrzy_kms + "s \t"
                        miedzyczas_dcztery = "24 km: " + dcztery_kmh + "h : " + dcztery_kmm + "m : " + dcztery_kms + "s \n"
                        miedzyczas_dpiec = "25 km: " + dpiec_kmh + "h : " + dpiec_kmm + "m : " + dpiec_kms + "s \t"
                        miedzyczas_dszesc = "26 km: " + dszesc_kmh + "h : " + dszesc_kmm + "m : " + dszesc_kms + "s \n"
                        miedzyczas_dsiedem = "27 km: " + dsiedem_kmh + "h : " + dsiedem_kmm + "m : " + dsiedem_kms + "s \t"
                        miedzyczas_dosiem = "28 km: " + dosiem_kmh + "h : " + dosiem_kmm + "m : " + dosiem_kms + "s \n"
                        miedzyczas_ddziewiec = "29 km: " + ddziewiec_kmh + "h : " + ddziewiec_kmm + "m : " + ddziewiec_kms + "s \t"
                        miedzyczas_trzydziesci = "30 km: " + trzydziesci_kmh + "h : " + trzydziesci_kmm + "m : " + trzydziesci_kms + "s \n"
                        miedzyczas_tjeden = "31 km: " + tjeden_kmh + "h : " + tjeden_kmm + "m : " + tjeden_kms + "s \t"
                        miedzyczas_tdwa = "32 km: " + tdwa_kmh + "h : " + tdwa_kmm + "m : " + tdwa_kms + "s \n"
                        miedzyczas_ttrzy = "33 km: " + ttrzy_kmh + "h : " + ttrzy_kmm + "m : " + ttrzy_kms + "s \t"
                        miedzyczas_tcztery = "34 km: " + tcztery_kmh + "h : " + tcztery_kmm + "m : " + tcztery_kms + "s \n"
                        miedzyczas_tpiec = "35 km: " + tpiec_kmh + "h : " + tpiec_kmm + "m : " + tpiec_kms + "s \t"
                        miedzyczas_tszesc = "36 km: " + tszesc_kmh + "h : " + tszesc_kmm + "m : " + tszesc_kms + "s \n"
                        miedzyczas_tsiedem = "37 km: " + tsiedem_kmh + "h : " + tsiedem_kmm + "m : " + tsiedem_kms + "s \t"
                        miedzyczas_tosiem = "38 km: " + tosiem_kmh + "h : " + tosiem_kmm + "m : " + tosiem_kms + "s \n"
                        miedzyczas_tdziewiec = "39 km: " + tdziewiec_kmh + "h : " + tdziewiec_kmm + "m : " + tdziewiec_kms + "s \t"
                        miedzyczas_czterdziesci = "40 km: " + czterdziesci_kmh + "h : " + czterdziesci_kmm + "m : " + czterdziesci_kms + "s \n"
                        miedzyczas_cjeden = "41 km: " + cjeden_kmh + "h : " + cjeden_kmm + "m : " + cjeden_kms + "s \t"
                        miedzyczas_cdwa = "42 km: " + cdwa_kmh + "h : " + cdwa_kmm + "m : " + cdwa_kms + "s \n"

                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty + miedzyczas_szosty + miedzyczas_siodmy + miedzyczas_osmy + miedzyczas_dziewiaty + miedzyczas_dziesiaty + miedzyczas_jedenasty + miedzyczas_dwunasty + miedzyczas_trzynasty + miedzyczas_czternasty + miedzyczas_pietnasty + miedzyczas_szesnasty + miedzyczas_siedemnasty + miedzyczas_osiemnasty + miedzyczas_dziewietnasty + miedzyczas_dwudziesty + miedzyczas_djeden
                        rezultat += miedzyczas_ddwa + miedzyczas_dtrzy + miedzyczas_dcztery + miedzyczas_dpiec + miedzyczas_dszesc + miedzyczas_dsiedem + miedzyczas_dosiem + miedzyczas_ddziewiec + miedzyczas_trzydziesci
                        rezultat += miedzyczas_tjeden + miedzyczas_tdwa + miedzyczas_ttrzy + miedzyczas_tcztery + miedzyczas_tpiec + miedzyczas_tszesc + miedzyczas_tsiedem + miedzyczas_tosiem + miedzyczas_tdziewiec + miedzyczas_czterdziesci + miedzyczas_cjeden + miedzyczas_cdwa

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")


    def timeProgres(self):
        if (len(self.godziny.text())==0) and (len(self.minuty.text())==0) and (len(self.sekundy.text())==0):
            komunikat = "Podaj czas"
            self.result.setText(komunikat)
        else:
            if self.JkmButton.isChecked():
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h)>=0) and (float(m) in range(0,60)) and (float(s) in range(0,60))):
                        czas = "Średni czas na 1 km: "+h+"h : "+m+"m : "+s+"s"
                        self.result.setText(czas)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane wartości nie są liczbami całkowitymi")
            elif self.TkmButton.isChecked():
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h)/3
                        h_result = math.floor(x)
                        h_pomoc = (float(h)%3)*60
                        m_pomoc = float(m)+h_pomoc
                        m_result = math.floor(m_pomoc/3)
                        m_ppomoc = (m_pomoc%3)*60
                        s_pomoc = m_ppomoc+float(s)
                        s_result = math.floor(s_pomoc/3)
                        wspolczynnik = 5

                        pierwszy_kms = 0
                        pierwszy_kmm = 0
                        pierwszy_kmh = 0
                        drugi_kms = 0
                        drugi_kmm = 0
                        drugi_kmh = 0
                        trzeci_kms = 0
                        trzeci_kmm = 0
                        trzeci_kmh = 0

                        if(s_result + wspolczynnik)<60:
                            pierwszy_kms = s_result + wspolczynnik
                        elif (s_result + wspolczynnik)==60:
                            pierwszy_kms = 0
                            pierwszy_kmm +=1
                        else:
                            pierwszy_kms = (s_result +wspolczynnik)-60
                            pierwszy_kmm +=1

                        if (pierwszy_kms - wspolczynnik)> 0:
                            drugi_kms = (pierwszy_kms - wspolczynnik)
                        elif (pierwszy_kms - wspolczynnik)==0:
                            drugi_kms = 0

                        else:
                            drugi_kms = (pierwszy_kms - wspolczynnik) + 60
                            drugi_kmm -= 1

                        if (drugi_kms - wspolczynnik) >0:
                            trzeci_kms = drugi_kms - wspolczynnik
                        elif (drugi_kms - wspolczynnik == 0):
                            trzeci_kms = 0

                        else:
                            trzeci_kms = (drugi_kms - wspolczynnik) + 60
                            trzeci_kmm -=1

                        if (pierwszy_kmm + m_result) < 60:
                            pierwszy_kmm += m_result
                        elif (pierwszy_kmm + m_result) == 60:
                            pierwszy_kmm = 0
                            pierwszy_kmh += 1
                        else:
                            pierwszy_kmm = (pierwszy_kmm + m_result) - 60
                            pierwszy_kmh += 1

                        if (pierwszy_kmm + drugi_kmm)<60:
                            drugi_kmm += (pierwszy_kmm)
                        elif (pierwszy_kmm + drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh += 1
                        else:
                            drugi_kmm = (pierwszy_kmm+drugi_kmm)-60
                            drugi_kmh +=1

                        if (drugi_kmm +trzeci_kmm)<60:
                            trzeci_kmm += (drugi_kmm)
                        elif (drugi_kmm+trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh += 1
                        else:
                            trzeci_kmm = (drugi_kmm +trzeci_kmm)-60
                            trzeci_kmh +=1

                        drugi_kmh += pierwszy_kmh+h_result
                        trzeci_kmh += drugi_kmh

                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result= str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)

                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \n"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \n"
                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")

            elif self.PkmButton.isChecked():
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)  # tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h) / 5
                        h_result = math.floor(x)
                        h_pomoc = (float(h) % 5) * 60
                        m_pomoc = float(m) + h_pomoc
                        m_result = math.floor(m_pomoc / 5)
                        m_ppomoc = (m_pomoc % 5) * 60
                        s_pomoc = m_ppomoc + float(s)
                        s_result = math.floor(s_pomoc / 5)
                        wspolczynnik = 4

                        pierwszy_kms = 0
                        pierwszy_kmm = 0
                        pierwszy_kmh = 0
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

                        if (s_result + 2 * wspolczynnik) < 60:
                            pierwszy_kms = s_result + 2 * wspolczynnik
                        elif (s_result + 2 * wspolczynnik) == 60:
                            pierwszy_kms = 0
                            pierwszy_kmm += 1
                        else:
                            pierwszy_kms = (s_result + 2 * wspolczynnik) - 60
                            pierwszy_kmm += 1

                        if (pierwszy_kms - wspolczynnik) > 0:
                            drugi_kms = (pierwszy_kms - wspolczynnik)
                        elif (pierwszy_kms - wspolczynnik) == 0:
                            drugi_kms = 0

                        else:
                            drugi_kms = (pierwszy_kms - wspolczynnik) + 60
                            drugi_kmm -= 1

                        if (drugi_kms - wspolczynnik) > 0:
                            trzeci_kms = drugi_kms - wspolczynnik
                        elif (drugi_kms - wspolczynnik == 0):
                            trzeci_kms = 0

                        else:
                            trzeci_kms = (drugi_kms - wspolczynnik) + 60
                            trzeci_kmm -= 1

                        if (trzeci_kms - wspolczynnik) > 0:
                            czwarty_kms = (trzeci_kms - wspolczynnik)
                        elif (trzeci_kms - wspolczynnik) == 0:
                            czwarty_kms = 0

                        else:
                            czwarty_kms = (trzeci_kms - wspolczynnik) + 60
                            czwarty_kmm -= 1

                        if (czwarty_kms - wspolczynnik) > 0:
                            piaty_kms = (czwarty_kms - wspolczynnik)
                        elif (czwarty_kms - wspolczynnik) == 0:
                            piaty_kms = 0

                        else:
                            piaty_kms = (czwarty_kms - wspolczynnik) - 60
                            piaty_kmm -= 1

                        if (pierwszy_kmm + m_result) < 60:
                            pierwszy_kmm += m_result
                        elif (pierwszy_kmm + m_result) == 60:
                            pierwszy_kmm = 0
                            pierwszy_kmh += 1
                        else:
                            pierwszy_kmm = (pierwszy_kmm + m_result) - 60
                            pierwszy_kmh += 1

                        if (pierwszy_kmm + drugi_kmm) < 60:
                            drugi_kmm += (pierwszy_kmm)
                        elif (pierwszy_kmm + drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh += 1
                        else:
                            drugi_kmm = (pierwszy_kmm + drugi_kmm) - 60
                            drugi_kmh += 1

                        if (drugi_kmm + trzeci_kmm) < 60:
                            trzeci_kmm += (drugi_kmm)
                        elif (drugi_kmm + trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh += 1
                        else:
                            trzeci_kmm = (drugi_kmm + trzeci_kmm) - 60
                            trzeci_kmh += 1

                        if (trzeci_kmm + czwarty_kmm) < 60:
                            czwarty_kmm += (trzeci_kmm)
                        elif (trzeci_kmm + czwarty_kmm) == 60:
                            czwarty_kmm = 0
                            czwarty_kmh += 1
                        else:
                            czwarty_kmm = (trzeci_kmm + czwarty_kmm) - 60
                            czwarty_kmh += 1

                        if (czwarty_kmm + piaty_kmm) < 60:
                            piaty_kmm += (czwarty_kmm)
                        elif (czwarty_kmm + piaty_kmm) == 60:
                            piaty_kmm = 0
                            piaty_kmh += 1
                        else:
                            piaty_kmm = (czwarty_kmm + piaty_kmm) - 60
                            piaty_kmh += 1

                        drugi_kmh += pierwszy_kmh + h_result
                        trzeci_kmh += drugi_kmh + h_result
                        czwarty_kmh += trzeci_kmh + h_result
                        piaty_kmh += czwarty_kmh + h_result

                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result = str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        czwarty_kms = str(czwarty_kms)
                        piaty_kms = str(piaty_kms)
                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        czwarty_kmm = str(czwarty_kmm)
                        piaty_kmm = str(piaty_kmm)
                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)
                        czwarty_kmh = str(czwarty_kmh)
                        piaty_kmh = str(piaty_kmh)

                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \n"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \n"
                        miedzyczas_czwarty = "4 km: " + czwarty_kmh + "h : " + czwarty_kmm + "m : " + czwarty_kms + "s \n"
                        miedzyczas_piaty = "5 km: " + piaty_kmh + "h : " + piaty_kmm + "m : " + piaty_kms + "s \n"

                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")
            elif self.DkmButton.isChecked():
                MainWindow.resize(480, 580)
                self.pushButton.setGeometry(QtCore.QRect(180, 490, 111, 31))
                self.pushButton_2.setGeometry(QtCore.QRect(180, 530, 111, 31))
                self.result.setGeometry(QtCore.QRect(220, 170, 300, 305))
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h)/10
                        h_result = math.floor(x)
                        h_pomoc = (float(h)%10)*60
                        m_pomoc = float(m)+h_pomoc
                        m_result = math.floor(m_pomoc/10)
                        m_ppomoc = (m_pomoc%10)*60
                        s_pomoc = m_ppomoc+float(s)
                        s_result = math.floor(s_pomoc/10)
                        wspolczynnik = 3

                        pierwszy_kms = 0
                        pierwszy_kmm = 0
                        pierwszy_kmh = 0
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
                        osmy_kms =0
                        osmy_kmm = 0
                        osmy_kmh = 0
                        dziewiaty_kms = 0
                        dziewiaty_kmm = 0
                        dziewiaty_kmh = 0
                        dziesiaty_kms = 0
                        dziesiaty_kmm = 0
                        dziesiaty_kmh = 0

                        if (s_result + 4.5 * wspolczynnik) < 60:
                            pierwszy_kms = math.floor(s_result + 4.5 * wspolczynnik)
                        elif (s_result + 4.5 * wspolczynnik) == 60:
                            pierwszy_kms = 0
                            pierwszy_kmm += 1
                        else:
                            pierwszy_kms = math.floor(s_result + 4.5 * wspolczynnik) - 60
                            pierwszy_kmm += 1

                        if (pierwszy_kms - wspolczynnik) > 0:
                            drugi_kms = (pierwszy_kms - wspolczynnik)
                        elif (pierwszy_kms - wspolczynnik) == 0:
                            drugi_kms = 0

                        else:
                            drugi_kms = (pierwszy_kms - wspolczynnik) + 60
                            drugi_kmm -= 1

                        if (drugi_kms - wspolczynnik) > 0:
                            trzeci_kms = drugi_kms - wspolczynnik
                        elif (drugi_kms - wspolczynnik == 0):
                            trzeci_kms = 0

                        else:
                            trzeci_kms = (drugi_kms - wspolczynnik) + 60
                            trzeci_kmm -= 1

                        if (trzeci_kms - wspolczynnik) > 0:
                            czwarty_kms = (trzeci_kms - wspolczynnik)
                        elif (trzeci_kms - wspolczynnik) == 0:
                            czwarty_kms = 0

                        else:
                            czwarty_kms = (trzeci_kms - wspolczynnik) + 60
                            czwarty_kmm -= 1

                        if (czwarty_kms - wspolczynnik) > 0:
                            piaty_kms = (czwarty_kms - wspolczynnik)
                        elif (czwarty_kms - wspolczynnik) == 0:
                            piaty_kms = 0

                        else:
                            piaty_kms = (czwarty_kms - wspolczynnik) + 60
                            piaty_kmm -= 1

                        if(piaty_kms - wspolczynnik) >0:
                            szosty_kms = (piaty_kms - wspolczynnik)
                        elif (piaty_kms - wspolczynnik)==0:
                            szosty_kms = 0

                        else:
                            szosty_kms = (piaty_kms -wspolczynnik)+60
                            szosty_kmm -=1

                        if(szosty_kms -wspolczynnik)>0:
                            siodmy_kms = (szosty_kms - wspolczynnik)
                        elif (szosty_kms -wspolczynnik)==0:
                            siodmy_kms = 0

                        else:
                            siodmy_kms = (szosty_kms +wspolczynnik)+60
                            siodmy_kmm -=1

                        if(siodmy_kms - wspolczynnik)>0:
                            osmy_kms = (siodmy_kms - wspolczynnik)
                        elif(siodmy_kms -wspolczynnik)==0:
                            osmy_kms = 0

                        else:
                            osmy_kms = (siodmy_kms - wspolczynnik)+60
                            osmy_kmm-=1

                        if(osmy_kms-wspolczynnik)>0:
                            dziewiaty_kms = (osmy_kms- wspolczynnik)
                        elif(osmy_kms- wspolczynnik)==0:
                            dziewiaty_kms = 0

                        else:
                            dziewiaty_kms = (osmy_kms-wspolczynnik)+60
                            dziewiaty_kmm -=1

                        if(dziewiaty_kms-wspolczynnik)>0:
                            dziesiaty_kms = (dziewiaty_kms-wspolczynnik)
                        elif((dziewiaty_kms- wspolczynnik))==0:
                            dziesiaty_kms = 0

                        else:
                            dziesiaty_kms = (dziewiaty_kms-wspolczynnik)+60
                            dziesiaty_kmm -=1


                        if (pierwszy_kmm + m_result) < 60:
                            pierwszy_kmm += m_result
                        elif (pierwszy_kmm + m_result) == 60:
                            pierwszy_kmm = 0
                            pierwszy_kmh += 1
                        else:
                            pierwszy_kmm = (pierwszy_kmm + m_result) - 60
                            pierwszy_kmh += 1

                        if (pierwszy_kmm + drugi_kmm) < 60:
                            drugi_kmm += (pierwszy_kmm)
                        elif (pierwszy_kmm + drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh += 1
                        else:
                            drugi_kmm = (pierwszy_kmm + drugi_kmm) - 60
                            drugi_kmh += 1

                        if (drugi_kmm + trzeci_kmm) < 60:
                            trzeci_kmm += (drugi_kmm)
                        elif (drugi_kmm + trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh += 1
                        else:
                            trzeci_kmm = (drugi_kmm + trzeci_kmm) - 60
                            trzeci_kmh += 1

                        if (trzeci_kmm + czwarty_kmm) < 60:
                            czwarty_kmm += (trzeci_kmm)
                        elif (trzeci_kmm + czwarty_kmm) == 60:
                            czwarty_kmm = 0
                            czwarty_kmh += 1
                        else:
                            czwarty_kmm = (trzeci_kmm + czwarty_kmm) - 60
                            czwarty_kmh += 1

                        if (czwarty_kmm + piaty_kmm) < 60:
                            piaty_kmm += (czwarty_kmm)
                        elif (czwarty_kmm + piaty_kmm) == 60:
                            piaty_kmm = 0
                            piaty_kmh += 1
                        else:
                            piaty_kmm = (czwarty_kmm + piaty_kmm) - 60
                            piaty_kmh += 1

                        if (piaty_kmm + szosty_kmm)<60:
                            szosty_kmm += piaty_kmm
                        elif (piaty_kmm + szosty_kmm)==60:
                            szosty_kmm = 0
                            szosty_kmh += 1
                        else:
                            szosty_kmm = (piaty_kmm + szosty_kmm)-60
                            szosty_kmh +=1

                        if (szosty_kmm + siodmy_kmm)<60:
                            siodmy_kmm+= szosty_kmm
                        elif (szosty_kmm + siodmy_kmm)==60:
                            siodmy_kmm = 0
                            siodmy_kmh +=1
                        else:
                            siodmy_kmm = (szosty_kmm + siodmy_kmm)-60
                            siodmy_kmh +=1

                        if (siodmy_kmm+osmy_kmm)<60:
                            osmy_kmm += siodmy_kmm
                        elif (siodmy_kmm+osmy_kmm)==60:
                            osmy_kmm = 0
                            osmy_kmh +=1
                        else:
                            osmy_kmm = (siodmy_kmm+osmy_kmm)-60
                            osmy_kmh+=1

                        if (osmy_kmm+dziewiaty_kmm)<60:
                            dziewiaty_kmm += osmy_kmm
                        elif (osmy_kmm+dziewiaty_kmm)==60:
                            dziewiaty_kmm = 0
                            dziewiaty_kmh+=1
                        else:
                            dziewiaty_kmm = (osmy_kmm+dziewiaty_kmm)-60
                            dziewiaty_kmh +=1

                        if (dziewiaty_kmm+dziesiaty_kmm)<60:
                            dziesiaty_kmm += dziewiaty_kmm
                        elif (dziewiaty_kmm+dziesiaty_kmm)==60:
                            dziesiaty_kmm = 0
                            dziesiaty_kmh +=1
                        else:
                            dziesiaty_kmm = (dziewiaty_kmm +dziesiaty_kmm)-60
                            dziesiaty_kmh +=1

                        drugi_kmh += pierwszy_kmh + h_result
                        trzeci_kmh += drugi_kmh + h_result
                        czwarty_kmh += trzeci_kmh + h_result
                        piaty_kmh += czwarty_kmh + h_result
                        szosty_kmh += piaty_kmh + h_result
                        siodmy_kmh += szosty_kmh + h_result
                        osmy_kmh += siodmy_kmh + h_result
                        dziewiaty_kmh += osmy_kmh + h_result
                        dziesiaty_kmh += dziewiaty_kmh + h_result


                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result = str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        czwarty_kms = str(czwarty_kms)
                        piaty_kms = str(piaty_kms)
                        szosty_kms = str(szosty_kms)
                        siodmy_kms = str(siodmy_kms)
                        osmy_kms = str(osmy_kms)
                        dziewiaty_kms = str(dziewiaty_kms)
                        dziesiaty_kms = str(dziesiaty_kms)
                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        czwarty_kmm = str(czwarty_kmm)
                        piaty_kmm = str(piaty_kmm)
                        szosty_kmm = str(szosty_kmm)
                        siodmy_kmm = str(siodmy_kmm)
                        osmy_kmm = str(osmy_kmm)
                        dziewiaty_kmm = str(dziewiaty_kmm)
                        dziesiaty_kmm = str(dziesiaty_kmm)
                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)
                        czwarty_kmh = str(czwarty_kmh)
                        piaty_kmh = str(piaty_kmh)
                        szosty_kmh = str(szosty_kmh)
                        siodmy_kmh = str(siodmy_kmh)
                        osmy_kmh = str(osmy_kmh)
                        dziewiaty_kmh = str(dziewiaty_kmh)
                        dziesiaty_kmh = str(dziesiaty_kmh)

                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \n"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \n"
                        miedzyczas_czwarty = "4 km: " + czwarty_kmh + "h : " + czwarty_kmm + "m : " + czwarty_kms + "s \n"
                        miedzyczas_piaty = "5 km: " + piaty_kmh + "h : " + piaty_kmm + "m : " + piaty_kms + "s \n"
                        miedzyczas_szosty = "6 km: " + szosty_kmh + "h : " + szosty_kmm + "m : " + szosty_kms + "s \n"
                        miedzyczas_siodmy = "7 km: " + siodmy_kmh + "h : " + siodmy_kmm + "m : " + siodmy_kms + "s \n"
                        miedzyczas_osmy = "8 km: " + osmy_kmh + "h : " + osmy_kmm + "m : " + osmy_kms + "s \n"
                        miedzyczas_dziewiaty = "9 km: " + dziewiaty_kmh + "h : " + dziewiaty_kmm + "m : " + dziewiaty_kms + "s \n"
                        miedzyczas_dziesiaty = "10 km: " + dziesiaty_kmh + "h : " + dziesiaty_kmm + "m : " + dziesiaty_kms + "s \n"


                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty + miedzyczas_szosty + miedzyczas_siodmy + miedzyczas_osmy + miedzyczas_dziewiaty + miedzyczas_dziesiaty

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")
            elif self.HkmButton.isChecked():
                MainWindow.resize(480, 580)
                self.pushButton.setGeometry(QtCore.QRect(180, 490, 111, 31))
                self.pushButton_2.setGeometry(QtCore.QRect(180, 530, 111, 31))
                self.result.setGeometry(QtCore.QRect(220, 170, 300, 305))

                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h)/21.097
                        h_result = math.floor(x)
                        h_pomoc = (float(h)%21.097)*60
                        m_pomoc = float(m)+h_pomoc
                        m_result = math.floor(m_pomoc/21.097)
                        m_ppomoc = (m_pomoc%21.097)*60
                        s_pomoc = m_ppomoc+float(s)
                        s_result = math.floor(s_pomoc/21.097)

                        wspolczynnik = 2

                        pierwszy_kms = 0
                        pierwszy_kmm = 0
                        pierwszy_kmh = 0
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
                        f_kms = 0
                        f_kmm = 0
                        f_kmh = 0

                        if (s_result + (9+(11/21)) * wspolczynnik) < 60:
                            pierwszy_kms = math.floor(s_result + (9+(11/21)) * wspolczynnik)
                        elif (s_result + (9+(11/21)) * wspolczynnik) == 60:
                            pierwszy_kms = 0
                            pierwszy_kmm += 1
                        else:
                            pierwszy_kms = math.floor(s_result + (9+(11/21)) * wspolczynnik) - 60
                            pierwszy_kmm += 1

                        if (pierwszy_kms - wspolczynnik) > 0:
                            drugi_kms = (pierwszy_kms - wspolczynnik)
                        elif (pierwszy_kms - wspolczynnik) == 0:
                            drugi_kms = 0

                        else:
                            drugi_kms = (pierwszy_kms - wspolczynnik) + 60
                            drugi_kmm -= 1

                        if (drugi_kms - wspolczynnik) > 0:
                            trzeci_kms = drugi_kms - wspolczynnik
                        elif (drugi_kms - wspolczynnik == 0):
                            trzeci_kms = 0

                        else:
                            trzeci_kms = (drugi_kms - wspolczynnik) + 60
                            trzeci_kmm -= 1

                        if (trzeci_kms - wspolczynnik) > 0:
                            czwarty_kms = (trzeci_kms - wspolczynnik)
                        elif (trzeci_kms - wspolczynnik) == 0:
                            czwarty_kms = 0

                        else:
                            czwarty_kms = (trzeci_kms - wspolczynnik) + 60
                            czwarty_kmm -= 1

                        if (czwarty_kms - wspolczynnik) > 0:
                            piaty_kms = (czwarty_kms - wspolczynnik)
                        elif (czwarty_kms - wspolczynnik) == 0:
                            piaty_kms = 0

                        else:
                            piaty_kms = (czwarty_kms - wspolczynnik) + 60
                            piaty_kmm -= 1

                        if(piaty_kms - wspolczynnik) >0:
                            szosty_kms = (piaty_kms - wspolczynnik)
                        elif (piaty_kms - wspolczynnik)==0:
                            szosty_kms = 0

                        else:
                            szosty_kms = (piaty_kms -wspolczynnik)+60
                            szosty_kmm -=1

                        if(szosty_kms -wspolczynnik)>0:
                            siodmy_kms = (szosty_kms - wspolczynnik)
                        elif (szosty_kms -wspolczynnik)==0:
                            siodmy_kms = 0

                        else:
                            siodmy_kms = (szosty_kms +wspolczynnik)+60
                            siodmy_kmm -=1

                        if(siodmy_kms - wspolczynnik)>0:
                            osmy_kms = (siodmy_kms - wspolczynnik)
                        elif(siodmy_kms -wspolczynnik)==0:
                            osmy_kms = 0

                        else:
                            osmy_kms = (siodmy_kms - wspolczynnik)+60
                            osmy_kmm-=1

                        if(osmy_kms-wspolczynnik)>0:
                            dziewiaty_kms = (osmy_kms- wspolczynnik)
                        elif(osmy_kms- wspolczynnik)==0:
                            dziewiaty_kms = 0

                        else:
                            dziewiaty_kms = (osmy_kms-wspolczynnik)+60
                            dziewiaty_kmm -=1

                        if(dziewiaty_kms-wspolczynnik)>0:
                            dziesiaty_kms = (dziewiaty_kms-wspolczynnik)
                        elif((dziewiaty_kms- wspolczynnik))==0:
                            dziesiaty_kms = 0

                        else:
                            dziesiaty_kms = (dziewiaty_kms-wspolczynnik)+60
                            dziesiaty_kmm -=1

                        if (dziesiaty_kms - wspolczynnik) > 0:
                            jedenasty_kms = (dziesiaty_kms - wspolczynnik)
                        elif (dziesiaty_kms + -wspolczynnik) ==0:
                            jedenasty_kms = 0

                        else:
                            jedenasty_kms = (dziesiaty_kms - wspolczynnik) + 60
                            jedenasty_kmm -= 1

                        if (jedenasty_kms - wspolczynnik) > 0:
                            dwunasty_kms = (jedenasty_kms - wspolczynnik)
                        elif (jedenasty_kms - wspolczynnik) == 0:
                            dwunasty_kms = 0

                        else:
                            dwunasty_kms = (jedenasty_kms - wspolczynnik) + 60
                            dwunasty_kmm -=1
                        if (dwunasty_kms - wspolczynnik) > 0:
                            trzynasty_kms = (dwunasty_kms - wspolczynnik)
                        elif (dwunasty_kms - wspolczynnik) == 0:
                            trzynasty_kms = 0

                        else:
                            trzynasty_kms = (dwunasty_kms - wspolczynnik) + 60
                            trzynasty_kmm -= 1

                        if (trzynasty_kms - wspolczynnik) > 0:
                            czternasty_kms = (trzynasty_kms - wspolczynnik)
                        elif (trzynasty_kms - wspolczynnik) == 0:
                            czternasty_kms = 0

                        else:
                            czternasty_kms = (trzynasty_kms - wspolczynnik) + 60
                            czternasty_kmm -= 1
                        if (czternasty_kms - wspolczynnik) > 0:
                            pietnasty_kms = (czternasty_kms - wspolczynnik)
                        elif (czternasty_kms -wspolczynnik) == 0:
                            pietnasty_kms = 0

                        else:
                            pietnasty_kms = (czternasty_kms - wspolczynnik) + 60
                            pietnasty_kmm -= 1

                        if (pietnasty_kms - wspolczynnik) > 0:
                            szesnasty_kms = (pietnasty_kms - wspolczynnik)
                        elif (pietnasty_kms - wspolczynnik) == 0:
                            szesnasty_kms = 0

                        else:
                            szesnasty_kms = (pietnasty_kms - wspolczynnik) + 60
                            szesnasty_kmm -= 1

                        if (szesnasty_kms - wspolczynnik) > 0:
                            siedemnasty_kms = (szesnasty_kms - wspolczynnik)
                        elif (szesnasty_kms - wspolczynnik) == 0:
                            siedemnasty_kms = 0

                        else:
                            siedemnasty_kms = (szesnasty_kms - wspolczynnik) + 60
                            siedemnasty_kmm -= 1

                        if (siedemnasty_kms - wspolczynnik) > 0:
                            osiemnasty_kms = (siedemnasty_kms - wspolczynnik)
                        elif (siedemnasty_kms + - wspolczynnik) == 0:
                            osiemnasty_kms = 0

                        else:
                            osiemnasty_kms = (siedemnasty_kms - wspolczynnik) + 60
                            osiemnasty_kmm -= 1

                        if (osiemnasty_kms - wspolczynnik) > 0:
                            dziewietnasty_kms = (osiemnasty_kms - wspolczynnik)
                        elif (osiemnasty_kms - wspolczynnik) == 0:
                            dziewietnasty_kms = 0

                        else:
                            dziewietnasty_kms = (osiemnasty_kms - wspolczynnik) + 60
                            dziewietnasty_kmm -= 1

                        if (dziewietnasty_kms - wspolczynnik) > 0:
                            dwudziesty_kms = (dziewietnasty_kms - wspolczynnik)
                        elif (dziewietnasty_kms - wspolczynnik) == 0:
                            dwudziesty_kms = 0

                        else:
                            dwudziesty_kms = (dziewietnasty_kms - wspolczynnik) + 60
                            dwudziesty_kmm -= 1

                        if (dwudziesty_kms - wspolczynnik) > 0:
                            djeden_kms = (dwudziesty_kms - wspolczynnik)
                        elif (dwudziesty_kms - wspolczynnik) == 0:
                            djeden_kms = 0

                        else:
                            djeden_kms = (dwudziesty_kms - wspolczynnik) + 60
                            djeden_kmm -= 1



                        if (pierwszy_kmm + m_result) < 60:
                            pierwszy_kmm += m_result
                        elif (pierwszy_kmm + m_result) == 60:
                            pierwszy_kmm = 0
                            pierwszy_kmh += 1
                        else:
                            pierwszy_kmm = (pierwszy_kmm + m_result) - 60
                            pierwszy_kmh += 1

                        if (pierwszy_kmm + drugi_kmm) < 60:
                            drugi_kmm += (pierwszy_kmm)
                        elif (pierwszy_kmm + drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh += 1
                        else:
                            drugi_kmm = (pierwszy_kmm + drugi_kmm) - 60
                            drugi_kmh += 1

                        if (drugi_kmm + trzeci_kmm) < 60:
                            trzeci_kmm += (drugi_kmm)
                        elif (drugi_kmm + trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh += 1
                        else:
                            trzeci_kmm = (drugi_kmm + trzeci_kmm) - 60
                            trzeci_kmh += 1

                        if (trzeci_kmm + czwarty_kmm) < 60:
                            czwarty_kmm += (trzeci_kmm)
                        elif (trzeci_kmm + czwarty_kmm) == 60:
                            czwarty_kmm = 0
                            czwarty_kmh += 1
                        else:
                            czwarty_kmm = (trzeci_kmm + czwarty_kmm) - 60
                            czwarty_kmh += 1

                        if (czwarty_kmm + piaty_kmm) < 60:
                            piaty_kmm += (czwarty_kmm)
                        elif (czwarty_kmm + piaty_kmm) == 60:
                            piaty_kmm = 0
                            piaty_kmh += 1
                        else:
                            piaty_kmm = (czwarty_kmm + piaty_kmm) - 60
                            piaty_kmh += 1

                        if (piaty_kmm + szosty_kmm)<60:
                            szosty_kmm += piaty_kmm
                        elif (piaty_kmm + szosty_kmm)==60:
                            szosty_kmm = 0
                            szosty_kmh += 1
                        else:
                            szosty_kmm = (piaty_kmm + szosty_kmm)-60
                            szosty_kmh +=1

                        if (szosty_kmm + siodmy_kmm)<60:
                            siodmy_kmm+= szosty_kmm
                        elif (szosty_kmm + siodmy_kmm)==60:
                            siodmy_kmm = 0
                            siodmy_kmh +=1
                        else:
                            siodmy_kmm = (szosty_kmm + siodmy_kmm)-60
                            siodmy_kmh +=1

                        if (siodmy_kmm+osmy_kmm)<60:
                            osmy_kmm += siodmy_kmm
                        elif (siodmy_kmm+osmy_kmm)==60:
                            osmy_kmm = 0
                            osmy_kmh +=1
                        else:
                            osmy_kmm = (siodmy_kmm+osmy_kmm)-60
                            osmy_kmh+=1

                        if (osmy_kmm+dziewiaty_kmm)<60:
                            dziewiaty_kmm += osmy_kmm
                        elif (osmy_kmm+dziewiaty_kmm)==60:
                            dziewiaty_kmm = 0
                            dziewiaty_kmh+=1
                        else:
                            dziewiaty_kmm = (osmy_kmm+dziewiaty_kmm)-60
                            dziewiaty_kmh +=1

                        if (dziewiaty_kmm+dziesiaty_kmm)<60:
                            dziesiaty_kmm += dziewiaty_kmm
                        elif (dziewiaty_kmm+dziesiaty_kmm)==60:
                            dziesiaty_kmm = 0
                            dziesiaty_kmh +=1
                        else:
                            dziesiaty_kmm = (dziewiaty_kmm +dziesiaty_kmm)-60
                            dziesiaty_kmh +=1

                        if (dziesiaty_kmm  + jedenasty_kmm) < 60:
                            jedenasty_kmm += dziesiaty_kmm
                        elif (dziesiaty_kmm + jedenasty_kmm) == 60:
                            jedenasty_kmm = 0
                            jedenasty_kmh += 1
                        else:
                            jedenasty_kmm = (dziesiaty_kmm + jedenasty_kmm) - 60
                            jedenasty_kmh += 1
                        if (jedenasty_kmm + dwunasty_kmm) < 60:
                            dwunasty_kmm += jedenasty_kmm
                        elif (jedenasty_kmm+ dwunasty_kmm) == 60:
                            dwunasty_kmm = 0
                            dwunasty_kmh += 1
                        else:
                            dwunasty_kmm = (jedenasty_kmm + dwunasty_kmm) - 60
                            dwunasty_kmh += 1
                        if (dwunasty_kmm + trzynasty_kmm) < 60:
                            trzynasty_kmm += dwunasty_kmm
                        elif (dwunasty_kmm + trzynasty_kmm) == 60:
                            trzynasty_kmm = 0
                            trzynasty_kmh += 1
                        else:
                            trzynasty_kmm = (dwunasty_kmm + trzynasty_kmm) - 60
                            trzynasty_kmh += 1

                        if (trzynasty_kmm  + czternasty_kmm) < 60:
                            czternasty_kmm += trzynasty_kmm
                        elif (trzynasty_kmm + czternasty_kmm) == 60:
                            czternasty_kmm = 0
                            czternasty_kmh += 1
                        else:
                            czternasty_kmm = (trzynasty_kmm + czternasty_kmm) - 60
                            czternasty_kmh += 1
                        if (czternasty_kmm  + pietnasty_kmm) < 60:
                            pietnasty_kmm += czternasty_kmm
                        elif (czternasty_kmm  + pietnasty_kmm) == 60:
                            pietnasty_kmm = 0
                            pietnasty_kmh += 1
                        else:
                            pietnasty_kmm = (czternasty_kmm + pietnasty_kmm) - 60
                            pietnasty_kmh += 1

                        if (pietnasty_kmm + szesnasty_kmm) < 60:
                            szesnasty_kmm += pietnasty_kmm
                        elif (pietnasty_kmm + szesnasty_kmm) == 60:
                            szesnasty_kmm = 0
                            szesnasty_kmh += 1
                        else:
                            szesnasty_kmm = (pietnasty_kmm + szesnasty_kmm) - 60
                            szesnasty_kmh += 1
                        if (szesnasty_kmm  + siedemnasty_kmm) < 60:
                            siedemnasty_kmm += szesnasty_kmm
                        elif (szesnasty_kmm  + siedemnasty_kmm) == 60:
                            siedemnasty_kmm = 0
                            siedemnasty_kmh += 1
                        else:
                            siedemnasty_kmm = (szesnasty_kmm + siedemnasty_kmm) - 60
                            siedemnasty_kmh += 1

                        if (siedemnasty_kmm  + osiemnasty_kmm) < 60:
                            osiemnasty_kmm += siedemnasty_kmm
                        elif (siedemnasty_kmm  + osiemnasty_kmm) == 60:
                            osiemnasty_kmm = 0
                            osiemnasty_kmh += 1
                        else:
                            osiemnasty_kmm = (siedemnasty_kmm  + osiemnasty_kmm) - 60
                            osiemnasty_kmh += 1

                        if (osiemnasty_kmm  + dziewietnasty_kmm) < 60:
                            dziewietnasty_kmm += osiemnasty_kmm
                        elif (osiemnasty_kmm + dziewietnasty_kmm) == 60:
                            dziewietnasty_kmm = 0
                            dziewietnasty_kmh += 1
                        else:
                            dziewietnasty_kmm = (osiemnasty_kmm + dziewietnasty_kmm) - 60
                            dziewietnasty_kmh += 1

                        if (dziewietnasty_kmm + dwudziesty_kmm) < 60:
                            dwudziesty_kmm += dziewietnasty_kmm
                        elif (dziewietnasty_kmm + dwudziesty_kmm) == 60:
                            dwudziesty_kmm = 0
                            dwudziesty_kmh += 1
                        else:
                            dwudziesty_kmm = (dziewietnasty_kmm + dwudziesty_kmm) - 60
                            dwudziesty_kmh += 1

                        if (dwudziesty_kmm + djeden_kmm) < 60:
                            djeden_kmm += dwudziesty_kmm
                        elif (dwudziesty_kmm + djeden_kmm) == 60:
                            djeden_kmm = 0
                            djeden_kmh += 1
                        else:
                            djeden_kmm = (dwudziesty_kmm  + djeden_kmm) - 60
                            djeden_kmh += 1




                        drugi_kmh += pierwszy_kmh + h_result
                        trzeci_kmh += drugi_kmh + h_result
                        czwarty_kmh += trzeci_kmh + h_result
                        piaty_kmh += czwarty_kmh + h_result
                        szosty_kmh += piaty_kmh + h_result
                        siodmy_kmh += szosty_kmh + h_result
                        osmy_kmh += siodmy_kmh + h_result
                        dziewiaty_kmh += osmy_kmh + h_result
                        dziesiaty_kmh += dziewiaty_kmh + h_result
                        jedenasty_kmh += dziesiaty_kmh + h_result
                        dwunasty_kmh += jedenasty_kmh + h_result
                        trzynasty_kmh += dwunasty_kmh + h_result
                        czternasty_kmh += trzynasty_kmh + h_result
                        pietnasty_kmh += czternasty_kmh + h_result
                        szesnasty_kmh += pietnasty_kmh + h_result
                        siedemnasty_kmh += szesnasty_kmh + h_result
                        osiemnasty_kmh += siedemnasty_kmh + h_result
                        dziewietnasty_kmh += osiemnasty_kmh + h_result
                        dwudziesty_kmh += dziewietnasty_kmh + h_result
                        djeden_kmh += dwudziesty_kmh + h_result


                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result = str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        czwarty_kms = str(czwarty_kms)
                        piaty_kms = str(piaty_kms)
                        szosty_kms = str(szosty_kms)
                        siodmy_kms = str(siodmy_kms)
                        osmy_kms = str(osmy_kms)
                        dziewiaty_kms = str(dziewiaty_kms)
                        dziesiaty_kms = str(dziesiaty_kms)
                        jedenasty_kms = str(jedenasty_kms)
                        dwunasty_kms = str(dwunasty_kms)
                        trzynasty_kms = str(trzynasty_kms)
                        czternasty_kms = str(czternasty_kms)
                        pietnasty_kms = str(pietnasty_kms)
                        szesnasty_kms = str(szesnasty_kms)
                        siedemnasty_kms = str(siedemnasty_kms)
                        osiemnasty_kms = str(osiemnasty_kms)
                        dziewietnasty_kms = str(dziewietnasty_kms)
                        dwudziesty_kms = str(dwudziesty_kms)
                        djeden_kms = str(djeden_kms)

                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        czwarty_kmm = str(czwarty_kmm)
                        piaty_kmm = str(piaty_kmm)
                        szosty_kmm = str(szosty_kmm)
                        siodmy_kmm = str(siodmy_kmm)
                        osmy_kmm = str(osmy_kmm)
                        dziewiaty_kmm = str(dziewiaty_kmm)
                        dziesiaty_kmm = str(dziesiaty_kmm)
                        jedenasty_kmm = str(jedenasty_kmm)
                        dwunasty_kmm = str(dwunasty_kmm)
                        trzynasty_kmm = str(trzynasty_kmm)
                        czternasty_kmm = str(czternasty_kmm)
                        pietnasty_kmm = str(pietnasty_kmm)
                        szesnasty_kmm = str(szesnasty_kmm)
                        siedemnasty_kmm = str(siedemnasty_kmm)
                        osiemnasty_kmm = str(osiemnasty_kmm)
                        dziewietnasty_kmm = str(dziewietnasty_kmm)
                        dwudziesty_kmm = str(dwudziesty_kmm)
                        djeden_kmm = str(djeden_kmm)

                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)
                        czwarty_kmh = str(czwarty_kmh)
                        piaty_kmh = str(piaty_kmh)
                        szosty_kmh = str(szosty_kmh)
                        siodmy_kmh = str(siodmy_kmh)
                        osmy_kmh = str(osmy_kmh)
                        dziewiaty_kmh = str(dziewiaty_kmh)
                        dziesiaty_kmh = str(dziesiaty_kmh)
                        jedenasty_kmh = str(jedenasty_kmh)
                        dwunasty_kmh = str(dwunasty_kmh)
                        trzynasty_kmh = str(trzynasty_kmh)
                        czternasty_kmh = str(czternasty_kmh)
                        pietnasty_kmh = str(pietnasty_kmh)
                        szesnasty_kmh = str(szesnasty_kmh)
                        siedemnasty_kmh = str(siedemnasty_kmh)
                        osiemnasty_kmh = str(osiemnasty_kmh)
                        dziewietnasty_kmh = str(dziewietnasty_kmh)
                        dwudziesty_kmh = str(dwudziesty_kmh)
                        djeden_kmh = str(djeden_kmh)


                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \n"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \n"
                        miedzyczas_czwarty = "4 km: " + czwarty_kmh + "h : " + czwarty_kmm + "m : " + czwarty_kms + "s \n"
                        miedzyczas_piaty = "5 km: " + piaty_kmh + "h : " + piaty_kmm + "m : " + piaty_kms + "s \n"
                        miedzyczas_szosty = "6 km: " + szosty_kmh + "h : " + szosty_kmm + "m : " + szosty_kms + "s \n"
                        miedzyczas_siodmy = "7 km: " + siodmy_kmh + "h : " + siodmy_kmm + "m : " + siodmy_kms + "s \n"
                        miedzyczas_osmy = "8 km: " + osmy_kmh + "h : " + osmy_kmm + "m : " + osmy_kms + "s \n"
                        miedzyczas_dziewiaty = "9 km: " + dziewiaty_kmh + "h : " + dziewiaty_kmm + "m : " + dziewiaty_kms + "s \n"
                        miedzyczas_dziesiaty = "10 km: " + dziesiaty_kmh + "h : " + dziesiaty_kmm + "m : " + dziesiaty_kms + "s \n"
                        miedzyczas_jedenasty = "11 km: " + jedenasty_kmh + "h : " + jedenasty_kmm + "m : " + jedenasty_kms + "s \n"
                        miedzyczas_dwunasty = "12 km: " + dwunasty_kmh + "h : " + dwunasty_kmm + "m : " + dwunasty_kms + "s \n"
                        miedzyczas_trzynasty = "13 km: " + trzynasty_kmh + "h : " + trzynasty_kmm + "m : " + trzynasty_kms + "s \n"
                        miedzyczas_czternasty = "14 km: " + czternasty_kmh + "h : " + czternasty_kmm + "m : " + czternasty_kms + "s \n"
                        miedzyczas_pietnasty = "15 km: " + pietnasty_kmh + "h : " + pietnasty_kmm + "m : " + pietnasty_kms + "s \n"
                        miedzyczas_szesnasty = "16 km: " + szesnasty_kmh + "h : " + szesnasty_kmm + "m : " + szesnasty_kms + "s \n"
                        miedzyczas_siedemnasty = "17 km: " + siedemnasty_kmh + "h : " + siedemnasty_kmm + "m : " + siedemnasty_kms + "s \n"
                        miedzyczas_osiemnasty = "18 km: " + osiemnasty_kmh + "h : " + osiemnasty_kmm + "m : " + osiemnasty_kms + "s \n"
                        miedzyczas_dziewietnasty = "19 km: " + dziewietnasty_kmh + "h : " + dziewietnasty_kmm + "m : " + dziewietnasty_kms + "s \n"
                        miedzyczas_dwudziesty = "20 km: " + dwudziesty_kmh + "h : " + dwudziesty_kmm + "m : " + dwudziesty_kms + "s \n"
                        miedzyczas_djeden = "21 km: " + djeden_kmh + "h : " + djeden_kmm + "m : " + djeden_kms + "s \n"

                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty + miedzyczas_szosty + miedzyczas_siodmy + miedzyczas_osmy + miedzyczas_dziewiaty + miedzyczas_dziesiaty + miedzyczas_jedenasty + miedzyczas_dwunasty + miedzyczas_trzynasty + miedzyczas_czternasty + miedzyczas_pietnasty + miedzyczas_szesnasty + miedzyczas_siedemnasty + miedzyczas_osiemnasty + miedzyczas_dziewietnasty + miedzyczas_dwudziesty + miedzyczas_djeden

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")


            elif self.MkmButton.isChecked():
                MainWindow.resize(580, 580)
                self.pushButton.setGeometry(QtCore.QRect(180, 490, 111, 31))
                self.pushButton_2.setGeometry(QtCore.QRect(180, 530, 111, 31))
                self.result.setGeometry(QtCore.QRect(220, 170, 400, 305))
                h = self.godziny.text()
                m = self.minuty.text()
                s = self.sekundy.text()
                try:
                    int(h)#tylko sprawdza,czy się da,nie zamienia, bo później musi być wspisane jako text
                    int(m)
                    int(s)
                    if ((float(h) >= 0) and (float(m) in range(0, 60)) and (float(s) in range(0, 60))):
                        x = float(h)/42.195
                        h_result = math.floor(x)
                        h_pomoc = (float(h)%42.195)*60
                        m_pomoc = float(m)+h_pomoc
                        m_result = math.floor(m_pomoc/42.195)
                        m_ppomoc = (m_pomoc%42.195)*60
                        s_pomoc = m_ppomoc+float(s)
                        s_result = math.floor(s_pomoc/42.195)

                        wspolczynnik = 1
                        pierwszy_kms = 0
                        pierwszy_kmm = 0
                        pierwszy_kmh = 0
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
                        f_kms = 0
                        f_kmm = 0
                        f_kmh = 0

                        if (s_result + (20.5) * wspolczynnik) < 60:
                            pierwszy_kms = math.floor(s_result + (20.5) * wspolczynnik)
                        elif (s_result + (20.5) * wspolczynnik) == 60:
                            pierwszy_kms = 0
                            pierwszy_kmm += 1
                        else:
                            pierwszy_kms = math.floor(s_result + (20.5) * wspolczynnik) - 60
                            pierwszy_kmm += 1

                        if (pierwszy_kms - wspolczynnik) > 0:
                            drugi_kms = (pierwszy_kms - wspolczynnik)
                        elif (pierwszy_kms - wspolczynnik) == 0:
                            drugi_kms = 0

                        else:
                            drugi_kms = (pierwszy_kms - wspolczynnik) + 60
                            drugi_kmm -= 1

                        if (drugi_kms - wspolczynnik) > 0:
                            trzeci_kms = drugi_kms - wspolczynnik
                        elif (drugi_kms - wspolczynnik == 0):
                            trzeci_kms = 0

                        else:
                            trzeci_kms = (drugi_kms - wspolczynnik) + 60
                            trzeci_kmm -= 1

                        if (trzeci_kms - wspolczynnik) > 0:
                            czwarty_kms = (trzeci_kms - wspolczynnik)
                        elif (trzeci_kms - wspolczynnik) == 0:
                            czwarty_kms = 0

                        else:
                            czwarty_kms = (trzeci_kms - wspolczynnik) + 60
                            czwarty_kmm -= 1

                        if (czwarty_kms - wspolczynnik) > 0:
                            piaty_kms = (czwarty_kms - wspolczynnik)
                        elif (czwarty_kms - wspolczynnik) == 0:
                            piaty_kms = 0

                        else:
                            piaty_kms = (czwarty_kms - wspolczynnik) + 60
                            piaty_kmm -= 1

                        if(piaty_kms - wspolczynnik) >0:
                            szosty_kms = (piaty_kms - wspolczynnik)
                        elif (piaty_kms - wspolczynnik)==0:
                            szosty_kms = 0

                        else:
                            szosty_kms = (piaty_kms -wspolczynnik)+60
                            szosty_kmm -=1

                        if(szosty_kms -wspolczynnik)>0:
                            siodmy_kms = (szosty_kms - wspolczynnik)
                        elif (szosty_kms -wspolczynnik)==0:
                            siodmy_kms = 0

                        else:
                            siodmy_kms = (szosty_kms +wspolczynnik)+60
                            siodmy_kmm -=1

                        if(siodmy_kms - wspolczynnik)>0:
                            osmy_kms = (siodmy_kms - wspolczynnik)
                        elif(siodmy_kms -wspolczynnik)==0:
                            osmy_kms = 0

                        else:
                            osmy_kms = (siodmy_kms - wspolczynnik)+60
                            osmy_kmm-=1

                        if(osmy_kms-wspolczynnik)>0:
                            dziewiaty_kms = (osmy_kms- wspolczynnik)
                        elif(osmy_kms- wspolczynnik)==0:
                            dziewiaty_kms = 0

                        else:
                            dziewiaty_kms = (osmy_kms-wspolczynnik)+60
                            dziewiaty_kmm -=1

                        if(dziewiaty_kms-wspolczynnik)>0:
                            dziesiaty_kms = (dziewiaty_kms-wspolczynnik)
                        elif((dziewiaty_kms- wspolczynnik))==0:
                            dziesiaty_kms = 0

                        else:
                            dziesiaty_kms = (dziewiaty_kms-wspolczynnik)+60
                            dziesiaty_kmm -=1

                        if (dziesiaty_kms - wspolczynnik) > 0:
                            jedenasty_kms = (dziesiaty_kms - wspolczynnik)
                        elif (dziesiaty_kms + -wspolczynnik) ==0:
                            jedenasty_kms = 0

                        else:
                            jedenasty_kms = (dziesiaty_kms - wspolczynnik) + 60
                            jedenasty_kmm -= 1

                        if (jedenasty_kms - wspolczynnik) > 0:
                            dwunasty_kms = (jedenasty_kms - wspolczynnik)
                        elif (jedenasty_kms - wspolczynnik) == 0:
                            dwunasty_kms = 0

                        else:
                            dwunasty_kms = (jedenasty_kms - wspolczynnik) + 60
                            dwunasty_kmm -=1
                        if (dwunasty_kms - wspolczynnik) > 0:
                            trzynasty_kms = (dwunasty_kms - wspolczynnik)
                        elif (dwunasty_kms - wspolczynnik) == 0:
                            trzynasty_kms = 0

                        else:
                            trzynasty_kms = (dwunasty_kms - wspolczynnik) + 60
                            trzynasty_kmm -= 1

                        if (trzynasty_kms - wspolczynnik) > 0:
                            czternasty_kms = (trzynasty_kms - wspolczynnik)
                        elif (trzynasty_kms - wspolczynnik) == 0:
                            czternasty_kms = 0

                        else:
                            czternasty_kms = (trzynasty_kms - wspolczynnik) + 60
                            czternasty_kmm -= 1
                        if (czternasty_kms - wspolczynnik) > 0:
                            pietnasty_kms = (czternasty_kms - wspolczynnik)
                        elif (czternasty_kms -wspolczynnik) == 0:
                            pietnasty_kms = 0

                        else:
                            pietnasty_kms = (czternasty_kms - wspolczynnik) + 60
                            pietnasty_kmm -= 1

                        if (pietnasty_kms - wspolczynnik) > 0:
                            szesnasty_kms = (pietnasty_kms - wspolczynnik)
                        elif (pietnasty_kms - wspolczynnik) == 0:
                            szesnasty_kms = 0

                        else:
                            szesnasty_kms = (pietnasty_kms - wspolczynnik) + 60
                            szesnasty_kmm -= 1

                        if (szesnasty_kms - wspolczynnik) > 0:
                            siedemnasty_kms = (szesnasty_kms - wspolczynnik)
                        elif (szesnasty_kms - wspolczynnik) == 0:
                            siedemnasty_kms = 0

                        else:
                            siedemnasty_kms = (szesnasty_kms - wspolczynnik) + 60
                            siedemnasty_kmm -= 1

                        if (siedemnasty_kms - wspolczynnik) > 0:
                            osiemnasty_kms = (siedemnasty_kms - wspolczynnik)
                        elif (siedemnasty_kms + - wspolczynnik) == 0:
                            osiemnasty_kms = 0

                        else:
                            osiemnasty_kms = (siedemnasty_kms - wspolczynnik) + 60
                            osiemnasty_kmm -= 1

                        if (osiemnasty_kms - wspolczynnik) > 0:
                            dziewietnasty_kms = (osiemnasty_kms - wspolczynnik)
                        elif (osiemnasty_kms - wspolczynnik) == 0:
                            dziewietnasty_kms = 0

                        else:
                            dziewietnasty_kms = (osiemnasty_kms - wspolczynnik) + 60
                            dziewietnasty_kmm -= 1

                        if (dziewietnasty_kms - wspolczynnik) > 0:
                            dwudziesty_kms = (dziewietnasty_kms - wspolczynnik)
                        elif (dziewietnasty_kms - wspolczynnik) == 0:
                            dwudziesty_kms = 0

                        else:
                            dwudziesty_kms = (dziewietnasty_kms - wspolczynnik) + 60
                            dwudziesty_kmm -= 1

                        if (dwudziesty_kms - wspolczynnik) > 0:
                            djeden_kms = (dwudziesty_kms - wspolczynnik)
                        elif (dwudziesty_kms - wspolczynnik) == 0:
                            djeden_kms = 0

                        else:
                            djeden_kms = (dwudziesty_kms - wspolczynnik) + 60
                            djeden_kmm -= 1

                        if(djeden_kms + - wspolczynnik)>0:
                            ddwa_kms = (djeden_kms - wspolczynnik)
                        elif (djeden_kms - wspolczynnik)==0:
                            ddwa_kms = 0

                        else:
                            ddwa_kms = (djeden_kms - wspolczynnik)+60
                            ddwa_kmm -=1

                        if(ddwa_kms - wspolczynnik)>0:
                            dtrzy_kms = (ddwa_kms - wspolczynnik)
                        elif (ddwa_kms- wspolczynnik)==0:
                            dtrzy_kms = 0

                        else:
                            dtrzy_kms = (ddwa_kms - wspolczynnik)+60
                            dtrzy_kmm -=1

                        if(dtrzy_kms - wspolczynnik)>0:
                            dcztery_kms = (dtrzy_kms- wspolczynnik)
                        elif (dtrzy_kms- wspolczynnik)==0:
                            dcztery_kms = 0

                        else:
                            dcztery_kms = (dtrzy_kms- wspolczynnik)+60
                            dcztery_kmm -=1

                        if(dcztery_kms - wspolczynnik)>0:
                            dpiec_kms = (dcztery_kms - wspolczynnik)
                        elif (dcztery_kms  - wspolczynnik) == 0:
                            dpiec_kms = 0

                        else:
                            dpiec_kms = (dcztery_kms - wspolczynnik)+60
                            dpiec_kmm -=1

                        if(dpiec_kms  - wspolczynnik)>0:
                            dszesc_kms = (dpiec_kms  - wspolczynnik)
                        elif (dpiec_kms - wspolczynnik)==0:
                            dszesc_kms = 0

                        else:
                            dszesc_kms = (dpiec_kms - wspolczynnik)+60
                            dszesc_kmm -=1

                        if (dszesc_kms - wspolczynnik)>0:
                            dsiedem_kms = (dszesc_kms - wspolczynnik)
                        elif (dszesc_kms - wspolczynnik)==0:
                            dsiedem_kms = 0

                        else:
                            dsiedem_kms = (dszesc_kms - wspolczynnik)+60
                            dsiedem_kmm -=1

                        if(dsiedem_kms - wspolczynnik)>0:
                            dosiem_kms = (dsiedem_kms - wspolczynnik)
                        elif (dsiedem_kms - wspolczynnik)==0:
                            dosiem_kms = 0

                        else:
                            dosiem_kms = (dsiedem_kms - wspolczynnik)+60
                            dosiem_kmm -=1

                        if(dosiem_kms  - wspolczynnik)>0:
                            ddziewiec_kms = (dosiem_kms - wspolczynnik)
                        elif (dosiem_kms - wspolczynnik)==0:
                            ddziewiec_kms = 0

                        else:
                            ddziewiec_kms = (dosiem_kms - wspolczynnik)+60
                            ddziewiec_kmm -=1

                        if(ddziewiec_kms - wspolczynnik)>0:
                            trzydziesci_kms = (ddziewiec_kms - wspolczynnik)
                        elif (ddziewiec_kms - wspolczynnik)==0:
                            trzydziesci_kms = 0

                        else:
                            trzydziesci_kms = (ddziewiec_kms - wspolczynnik)+60
                            trzydziesci_kmm -=1

                        if(trzydziesci_kms - wspolczynnik)>0:
                            tjeden_kms = (trzydziesci_kms - wspolczynnik)
                        elif (trzydziesci_kms - wspolczynnik)==0:
                            tjeden_kms = 0

                        else:
                            tjeden_kms = (trzydziesci_kms - wspolczynnik)+60
                            tjeden_kmm -=1

                        if(tjeden_kms - wspolczynnik)>0:
                            tdwa_kms = (tjeden_kms - wspolczynnik)
                        elif (tjeden_kms - wspolczynnik)==0:
                            tdwa_kms = 0

                        else:
                            tdwa_kms = (tjeden_kms - wspolczynnik)+60
                            tdwa_kmm -=1

                        if(tdwa_kms - wspolczynnik)>0:
                            ttrzy_kms = (tdwa_kms - wspolczynnik)
                        elif (tdwa_kms - wspolczynnik)==0:
                            ttrzy_kms = 0

                        else:
                            ttrzy_kms = (tdwa_kms - wspolczynnik)+60
                            ttrzy_kmm -=1

                        if(ttrzy_kms - wspolczynnik)>0:
                            tcztery_kms = (ttrzy_kms - wspolczynnik)
                        elif (ttrzy_kms -wspolczynnik)==0:
                            tcztery_kms = 0

                        else:
                            tcztery_kms = (ttrzy_kms - wspolczynnik)+60
                            tcztery_kmm -=1

                        if(tcztery_kms - wspolczynnik)>0:
                            tpiec_kms = (tcztery_kms - wspolczynnik)
                        elif (tcztery_kms - wspolczynnik)==0:
                            tpiec_kms = 0

                        else:
                            tpiec_kms = (tcztery_kms - wspolczynnik)+60
                            tpiec_kmm -=1

                        if(tpiec_kms - wspolczynnik)>0:
                            tszesc_kms = (tpiec_kms - wspolczynnik)
                        elif (tpiec_kms - wspolczynnik)==0:
                            tszesc_kms = 0

                        else:
                            tszesc_kms = (tpiec_kms - wspolczynnik)+60
                            tszesc_kmm -=1

                        if(tszesc_kms - wspolczynnik)>0:
                            tsiedem_kms = (tszesc_kms - wspolczynnik)
                        elif (tszesc_kms - wspolczynnik)==0:
                            tsiedem_kms = 0

                        else:
                            tsiedem_kms = (tszesc_kms - wspolczynnik)+60
                            tsiedem_kmm -=1

                        if(tsiedem_kms - wspolczynnik)>0:
                            tosiem_kms = (tsiedem_kms - wspolczynnik)
                        elif (tsiedem_kms - wspolczynnik)==0:
                            tosiem_kms = 0

                        else:
                            tosiem_kms = tsiedem_kms - wspolczynnik +60
                            tosiem_kmm -=1

                        if(tosiem_kms - wspolczynnik)>0:
                            tdziewiec_kms = (tosiem_kms - wspolczynnik)
                        elif (tosiem_kms - wspolczynnik)==0:
                            tdziewiec_kms = 0

                        else:
                            tdziewiec_kms = (tosiem_kms - wspolczynnik)+60
                            tdziewiec_kmm -=1

                        if (tdziewiec_kms + wspolczynnik)>0:
                            czterdziesci_kms = (tdziewiec_kms - wspolczynnik)
                        elif (tdziewiec_kms - wspolczynnik)==0:
                            czterdziesci_kms = 0

                        else:
                            czterdziesci_kms = (tdziewiec_kms - wspolczynnik)+60
                            czterdziesci_kmm -=1

                        if(czterdziesci_kms + - wspolczynnik)>0:
                            cjeden_kms = (czterdziesci_kms - wspolczynnik)
                        elif (czterdziesci_kms - wspolczynnik) == 0:
                            cjeden_kms = 0

                        else:
                            cjeden_kms = czterdziesci_kms - wspolczynnik +60
                            cjeden_kmm -=1

                        if(cjeden_kms - wspolczynnik)>0:
                            cdwa_kms = (cjeden_kms - wspolczynnik)
                        elif (cjeden_kms - wspolczynnik)==0:
                            cdwa_kms = 0

                        else:
                            cdwa_kms = (cjeden_kms - wspolczynnik) +60
                            cdwa_kmm -=1


                        if (pierwszy_kmm + m_result) < 60:
                            pierwszy_kmm += m_result
                        elif (pierwszy_kmm + m_result) == 60:
                            pierwszy_kmm = 0
                            pierwszy_kmh += 1
                        else:
                            pierwszy_kmm = (pierwszy_kmm + m_result) - 60
                            pierwszy_kmh += 1

                        if (pierwszy_kmm + drugi_kmm) < 60:
                            drugi_kmm += (pierwszy_kmm)
                        elif (pierwszy_kmm + drugi_kmm) == 60:
                            drugi_kmm = 0
                            drugi_kmh += 1
                        else:
                            drugi_kmm = (pierwszy_kmm + drugi_kmm) - 60
                            drugi_kmh += 1

                        if (drugi_kmm + trzeci_kmm) < 60:
                            trzeci_kmm += (drugi_kmm)
                        elif (drugi_kmm + trzeci_kmm) == 60:
                            trzeci_kmm = 0
                            trzeci_kmh += 1
                        else:
                            trzeci_kmm = (drugi_kmm + trzeci_kmm) - 60
                            trzeci_kmh += 1

                        if (trzeci_kmm + czwarty_kmm) < 60:
                            czwarty_kmm += (trzeci_kmm)
                        elif (trzeci_kmm + czwarty_kmm) == 60:
                            czwarty_kmm = 0
                            czwarty_kmh += 1
                        else:
                            czwarty_kmm = (trzeci_kmm + czwarty_kmm) - 60
                            czwarty_kmh += 1

                        if (czwarty_kmm + piaty_kmm) < 60:
                            piaty_kmm += (czwarty_kmm)
                        elif (czwarty_kmm + piaty_kmm) == 60:
                            piaty_kmm = 0
                            piaty_kmh += 1
                        else:
                            piaty_kmm = (czwarty_kmm + piaty_kmm) - 60
                            piaty_kmh += 1

                        if (piaty_kmm + szosty_kmm)<60:
                            szosty_kmm += piaty_kmm
                        elif (piaty_kmm + szosty_kmm)==60:
                            szosty_kmm = 0
                            szosty_kmh += 1
                        else:
                            szosty_kmm = (piaty_kmm + szosty_kmm)-60
                            szosty_kmh +=1

                        if (szosty_kmm + siodmy_kmm)<60:
                            siodmy_kmm+= szosty_kmm
                        elif (szosty_kmm + siodmy_kmm)==60:
                            siodmy_kmm = 0
                            siodmy_kmh +=1
                        else:
                            siodmy_kmm = (szosty_kmm + siodmy_kmm)-60
                            siodmy_kmh +=1

                        if (siodmy_kmm+osmy_kmm)<60:
                            osmy_kmm += siodmy_kmm
                        elif (siodmy_kmm+osmy_kmm)==60:
                            osmy_kmm = 0
                            osmy_kmh +=1
                        else:
                            osmy_kmm = (siodmy_kmm+osmy_kmm)-60
                            osmy_kmh+=1

                        if (osmy_kmm+dziewiaty_kmm)<60:
                            dziewiaty_kmm += osmy_kmm
                        elif (osmy_kmm+dziewiaty_kmm)==60:
                            dziewiaty_kmm = 0
                            dziewiaty_kmh+=1
                        else:
                            dziewiaty_kmm = (osmy_kmm+dziewiaty_kmm)-60
                            dziewiaty_kmh +=1

                        if (dziewiaty_kmm+dziesiaty_kmm)<60:
                            dziesiaty_kmm += dziewiaty_kmm
                        elif (dziewiaty_kmm+dziesiaty_kmm)==60:
                            dziesiaty_kmm = 0
                            dziesiaty_kmh +=1
                        else:
                            dziesiaty_kmm = (dziewiaty_kmm +dziesiaty_kmm)-60
                            dziesiaty_kmh +=1

                        if (dziesiaty_kmm  + jedenasty_kmm) < 60:
                            jedenasty_kmm += dziesiaty_kmm
                        elif (dziesiaty_kmm + jedenasty_kmm) == 60:
                            jedenasty_kmm = 0
                            jedenasty_kmh += 1
                        else:
                            jedenasty_kmm = (dziesiaty_kmm + jedenasty_kmm) - 60
                            jedenasty_kmh += 1
                        if (jedenasty_kmm + dwunasty_kmm) < 60:
                            dwunasty_kmm += jedenasty_kmm
                        elif (jedenasty_kmm+ dwunasty_kmm) == 60:
                            dwunasty_kmm = 0
                            dwunasty_kmh += 1
                        else:
                            dwunasty_kmm = (jedenasty_kmm + dwunasty_kmm) - 60
                            dwunasty_kmh += 1
                        if (dwunasty_kmm + trzynasty_kmm) < 60:
                            trzynasty_kmm += dwunasty_kmm
                        elif (dwunasty_kmm + trzynasty_kmm) == 60:
                            trzynasty_kmm = 0
                            trzynasty_kmh += 1
                        else:
                            trzynasty_kmm = (dwunasty_kmm + trzynasty_kmm) - 60
                            trzynasty_kmh += 1

                        if (trzynasty_kmm  + czternasty_kmm) < 60:
                            czternasty_kmm += trzynasty_kmm
                        elif (trzynasty_kmm + czternasty_kmm) == 60:
                            czternasty_kmm = 0
                            czternasty_kmh += 1
                        else:
                            czternasty_kmm = (trzynasty_kmm + czternasty_kmm) - 60
                            czternasty_kmh += 1
                        if (czternasty_kmm  + pietnasty_kmm) < 60:
                            pietnasty_kmm += czternasty_kmm
                        elif (czternasty_kmm  + pietnasty_kmm) == 60:
                            pietnasty_kmm = 0
                            pietnasty_kmh += 1
                        else:
                            pietnasty_kmm = (czternasty_kmm + pietnasty_kmm) - 60
                            pietnasty_kmh += 1

                        if (pietnasty_kmm + szesnasty_kmm) < 60:
                            szesnasty_kmm += pietnasty_kmm
                        elif (pietnasty_kmm + szesnasty_kmm) == 60:
                            szesnasty_kmm = 0
                            szesnasty_kmh += 1
                        else:
                            szesnasty_kmm = (pietnasty_kmm + szesnasty_kmm) - 60
                            szesnasty_kmh += 1
                        if (szesnasty_kmm  + siedemnasty_kmm) < 60:
                            siedemnasty_kmm += szesnasty_kmm
                        elif (szesnasty_kmm  + siedemnasty_kmm) == 60:
                            siedemnasty_kmm = 0
                            siedemnasty_kmh += 1
                        else:
                            siedemnasty_kmm = (szesnasty_kmm + siedemnasty_kmm) - 60
                            siedemnasty_kmh += 1

                        if (siedemnasty_kmm  + osiemnasty_kmm) < 60:
                            osiemnasty_kmm += siedemnasty_kmm
                        elif (siedemnasty_kmm  + osiemnasty_kmm) == 60:
                            osiemnasty_kmm = 0
                            osiemnasty_kmh += 1
                        else:
                            osiemnasty_kmm = (siedemnasty_kmm  + osiemnasty_kmm) - 60
                            osiemnasty_kmh += 1

                        if (osiemnasty_kmm  + dziewietnasty_kmm) < 60:
                            dziewietnasty_kmm += osiemnasty_kmm
                        elif (osiemnasty_kmm + dziewietnasty_kmm) == 60:
                            dziewietnasty_kmm = 0
                            dziewietnasty_kmh += 1
                        else:
                            dziewietnasty_kmm = (osiemnasty_kmm + dziewietnasty_kmm) - 60
                            dziewietnasty_kmh += 1

                        if (dziewietnasty_kmm + dwudziesty_kmm) < 60:
                            dwudziesty_kmm += dziewietnasty_kmm
                        elif (dziewietnasty_kmm + dwudziesty_kmm) == 60:
                            dwudziesty_kmm = 0
                            dwudziesty_kmh += 1
                        else:
                            dwudziesty_kmm = (dziewietnasty_kmm + dwudziesty_kmm) - 60
                            dwudziesty_kmh += 1

                        if (dwudziesty_kmm + djeden_kmm) < 60:
                            djeden_kmm += dwudziesty_kmm
                        elif (dwudziesty_kmm + djeden_kmm) == 60:
                            djeden_kmm = 0
                            djeden_kmh += 1
                        else:
                            djeden_kmm = (dwudziesty_kmm  + djeden_kmm) - 60
                            djeden_kmh += 1

                        if(djeden_kmm  + ddwa_kmm) <60:
                            ddwa_kmm += djeden_kmm
                        elif (djeden_kmm + ddwa_kmm)==60:
                            ddwa_kmm = 0
                            ddwa_kmh +=1
                        else:
                            ddwa_kmm = (djeden_kmm + ddwa_kmm)-60
                            ddwa_kmh +=1

                        if(ddwa_kmm  + dtrzy_kmm)<60:
                            dtrzy_kmm += ddwa_kmm
                        elif (ddwa_kmm  + dtrzy_kmm)==60:
                            dtrzy_kmm= 0
                            dtrzy_kmh +=1
                        else:
                            dtrzy_kmm = (ddwa_kmm + dtrzy_kmm)-60
                            dtrzy_kmh +=1

                        if(dtrzy_kmm  + dcztery_kmm)<60:
                            dcztery_kmm += dtrzy_kmm
                        elif (dtrzy_kmm  + dcztery_kmm) ==60:
                            dcztery_kmm = 0
                            dcztery_kmh +=1
                        else:
                            dcztery_kmm = (dtrzy_kmm + dcztery_kmm)-60
                            dcztery_kmh +=1

                        if(dcztery_kmm  + dpiec_kmm)<60:
                            dpiec_kmm += dcztery_kmm
                        elif (dcztery_kmm  + dpiec_kmm) ==60:
                            dpiec_kmm = 0
                            dpiec_kmh +=1
                        else:
                            dpiec_kmm = (dcztery_kmm  + dpiec_kmm)-60
                            dpiec_kmh +=1

                        if (dpiec_kmm  + dszesc_kmm)<60:
                            dszesc_kmm += dpiec_kmm
                        elif (dpiec_kmm  + dszesc_kmm)==60:
                            dszesc_kmm = 0
                            dszesc_kmh +=1
                        else:
                            dszesc_kmm = (dpiec_kmm + dszesc_kmm)-60
                            dszesc_kmh +=1

                        if (dszesc_kmm + dsiedem_kmm)<60:
                            dsiedem_kmm += dszesc_kmm
                        elif (dszesc_kmm  + dsiedem_kmm)==60:
                            dsiedem_kmm = 0
                            dsiedem_kmh +=1
                        else:
                            dsiedem_kmm = (dszesc_kmm  + dsiedem_kmm)-60
                            dsiedem_kmh +=1

                        if(dsiedem_kmm  + dosiem_kmm)<60:
                            dosiem_kmm += dsiedem_kmm
                        elif (dsiedem_kmm + dosiem_kmm)==60:
                            dosiem_kmm = 0
                            dosiem_kmh +=1
                        else:
                            dosiem_kmm = (dsiedem_kmm  + dosiem_kmm)-60
                            dosiem_kmh +=1

                        if(dosiem_kmm  + ddziewiec_kmm)<60:
                            ddziewiec_kmm += dosiem_kmm
                        elif (dosiem_kmm  + ddziewiec_kmm)==60:
                            ddziewiec_kmm = 0
                            ddziewiec_kmh +=1
                        else:
                            ddziewiec_kmm = (dosiem_kmm + ddziewiec_kmm)-60
                            ddziewiec_kmh +=1

                        if(ddziewiec_kmm+ trzydziesci_kmm) <60:
                            trzydziesci_kmm += ddziewiec_kmm
                        elif (ddziewiec_kmm  + trzydziesci_kmm)==60:
                            trzydziesci_kmm = 0
                            trzydziesci_kmh +=1
                        else:
                            trzydziesci_kmm = (ddziewiec_kmm  + trzydziesci_kmm)-60
                            trzydziesci_kmh +=1

                        if(trzydziesci_kmm + tjeden_kmm)<60:
                            tjeden_kmm += trzydziesci_kmm
                        elif (trzydziesci_kmm + tjeden_kmm)==60:
                            tjeden_kmm = 0
                            tjeden_kmh+=1
                        else:
                            tjeden_kmm =  (trzydziesci_kmm + + tjeden_kmm)-60
                            tjeden_kmh +=1

                        if(tjeden_kmm  + tdwa_kmm)<60:
                            tdwa_kmm += tjeden_kmm
                        elif (tjeden_kmm  + tdwa_kmm)==60:
                            tdwa_kmm = 0
                            tdwa_kmh +=1
                        else:
                            tdwa_kmm=(tjeden_kmm + tdwa_kmm)-60
                            tdwa_kmh +=1

                        if(tdwa_kmm  + ttrzy_kmm) <60:
                            ttrzy_kmm += tdwa_kmm
                        elif (tdwa_kmm  + ttrzy_kmm) == 60:
                            ttrzy_kmm = 0
                            ttrzy_kmh+=1
                        else:
                            ttrzy_kmm = (tdwa_kmm + ttrzy_kmm)-60
                            ttrzy_kmh +=1

                        if(ttrzy_kmm + tcztery_kmm) <60:
                            tcztery_kmm += ttrzy_kmm
                        elif (ttrzy_kmm  + tcztery_kmm) == 60:
                            tcztery_kmm = 0
                            tcztery_kmh +=1
                        else:
                            tcztery_kmm = (ttrzy_kmm  + tcztery_kmm)-60
                            tcztery_kmh +=1

                        if(tcztery_kmm + tpiec_kmm)<60:
                            tpiec_kmm += tcztery_kmm
                        elif (tcztery_kmm + tpiec_kmm) == 60:
                            tpiec_kmm = 0
                            tpiec_kmh +=1
                        else:
                            tpiec_kmm = (tcztery_kmm + tpiec_kmm) -60
                            tpiec_kmh +=1

                        if (tpiec_kmm + tszesc_kmm) < 60:
                            tszesc_kmm += tpiec_kmm
                        elif (tpiec_kmm  + tszesc_kmm)==60:
                            tszesc_kmm = 0
                            tszesc_kmh +=1
                        else:
                            tszesc_kmm = (tpiec_kmm  + tszesc_kmm)-60
                            tszesc_kmh +=1

                        if (tszesc_kmm + tsiedem_kmm)<60:
                            tsiedem_kmm += tszesc_kmm
                        elif (tszesc_kmm + tsiedem_kmm)==60:
                            tsiedem_kmm = 0
                            tsiedem_kmh +=1
                        else:
                            tsiedem_kmm = (tszesc_kmm  + tsiedem_kmm)-60
                            tsiedem_kmh +=1

                        if (tsiedem_kmm + tosiem_kmm) <60:
                            tosiem_kmm += tsiedem_kmm
                        elif (tsiedem_kmm + tosiem_kmm)==60:
                            tosiem_kmm = 0
                            tosiem_kmh +=1
                        else:
                            tosiem_kmm = (tsiedem_kmm + tosiem_kmm) -60
                            tosiem_kmh +=1

                        if (tosiem_kmm + tdziewiec_kmm)<60:
                            tdziewiec_kmm += tosiem_kmm
                        elif (tosiem_kmm + tdziewiec_kmm)==60:
                            tdziewiec_kmm = 0
                            tdziewiec_kmh +=1
                        else:
                            tdziewiec_kmm = (tosiem_kmm + tdziewiec_kmm)-60
                            tdziewiec_kmh +=1

                        if(tdziewiec_kmm+ czterdziesci_kmm)<60:
                            czterdziesci_kmm += tdziewiec_kmm
                        elif (tdziewiec_kmm + czterdziesci_kmm)==60:
                            czterdziesci_kmm = 0
                            czterdziesci_kmh +=1
                        else:
                            czterdziesci_kmm = (tdziewiec_kmm + czterdziesci_kmm)-60
                            czterdziesci_kmh +=1

                        if(czterdziesci_kmm + cjeden_kmm)<60:
                            cjeden_kmm += czterdziesci_kmm
                        elif (czterdziesci_kmm + cjeden_kmm)==60:
                            cjeden_kmm = 0
                            cjeden_kmh += 1
                        else:
                            cjeden_kmm = (czterdziesci_kmm + cjeden_kmm)-60
                            cjeden_kmh +=1

                        if(cjeden_kmm + cdwa_kmm)<60:
                            cdwa_kmm += cjeden_kmm
                        elif (cjeden_kmm + cdwa_kmm)==60:
                            cdwa_kmm = 0
                            cdwa_kmh +=1
                        else:
                            cdwa_kmm = (cjeden_kmm + cdwa_kmm)-60
                            cdwa_kmh +=1



                        drugi_kmh += pierwszy_kmh + h_result
                        trzeci_kmh += drugi_kmh + h_result
                        czwarty_kmh += trzeci_kmh + h_result
                        piaty_kmh += czwarty_kmh + h_result
                        szosty_kmh += piaty_kmh + h_result
                        siodmy_kmh += szosty_kmh + h_result
                        osmy_kmh += siodmy_kmh + h_result
                        dziewiaty_kmh += osmy_kmh + h_result
                        dziesiaty_kmh += dziewiaty_kmh + h_result
                        jedenasty_kmh += dziesiaty_kmh + h_result
                        dwunasty_kmh += jedenasty_kmh + h_result
                        trzynasty_kmh += dwunasty_kmh + h_result
                        czternasty_kmh += trzynasty_kmh + h_result
                        pietnasty_kmh += czternasty_kmh + h_result
                        szesnasty_kmh += pietnasty_kmh + h_result
                        siedemnasty_kmh += szesnasty_kmh + h_result
                        osiemnasty_kmh += siedemnasty_kmh + h_result
                        dziewietnasty_kmh += osiemnasty_kmh + h_result
                        dwudziesty_kmh += dziewietnasty_kmh + h_result
                        djeden_kmh += dwudziesty_kmh + h_result
                        ddwa_kmh += djeden_kmh + h_result
                        dtrzy_kmh += ddwa_kmh +  h_result
                        dcztery_kmh += dtrzy_kmh + h_result
                        dpiec_kmh += dcztery_kmh + h_result
                        dszesc_kmh += dpiec_kmh + h_result
                        dsiedem_kmh += dszesc_kmh + h_result
                        dosiem_kmh += dsiedem_kmh + h_result
                        ddziewiec_kmh += dosiem_kmh + h_result
                        trzydziesci_kmh += ddziewiec_kmh + h_result
                        tjeden_kmh += trzydziesci_kmh + h_result
                        tdwa_kmh += tjeden_kmh + h_result
                        ttrzy_kmh += tdwa_kmh + h_result
                        tcztery_kmh += ttrzy_kmh + h_result
                        tpiec_kmh += tcztery_kmh + h_result
                        tszesc_kmh += tpiec_kmh + h_result
                        tsiedem_kmh+= tszesc_kmh + h_result
                        tosiem_kmh += tsiedem_kmh + h_result
                        tdziewiec_kmh += tosiem_kmh + h_result
                        czterdziesci_kmh += tdziewiec_kmh + h_result
                        cjeden_kmh += czterdziesci_kmh + h_result
                        cdwa_kmh += cjeden_kmh + h_result

                        h_result = str(h_result)
                        m_result = str(m_result)
                        s_result = str(s_result)

                        pierwszy_kms = str(pierwszy_kms)
                        drugi_kms = str(drugi_kms)
                        trzeci_kms = str(trzeci_kms)
                        czwarty_kms = str(czwarty_kms)
                        piaty_kms = str(piaty_kms)
                        szosty_kms = str(szosty_kms)
                        siodmy_kms = str(siodmy_kms)
                        osmy_kms = str(osmy_kms)
                        dziewiaty_kms = str(dziewiaty_kms)
                        dziesiaty_kms = str(dziesiaty_kms)
                        jedenasty_kms = str(jedenasty_kms)
                        dwunasty_kms = str(dwunasty_kms)
                        trzynasty_kms = str(trzynasty_kms)
                        czternasty_kms = str(czternasty_kms)
                        pietnasty_kms = str(pietnasty_kms)
                        szesnasty_kms = str(szesnasty_kms)
                        siedemnasty_kms = str(siedemnasty_kms)
                        osiemnasty_kms = str(osiemnasty_kms)
                        dziewietnasty_kms = str(dziewietnasty_kms)
                        dwudziesty_kms = str(dwudziesty_kms)
                        djeden_kms = str(djeden_kms)
                        ddwa_kms = str(ddwa_kms)
                        dtrzy_kms = str(dtrzy_kms)
                        dcztery_kms = str(dcztery_kms)
                        dpiec_kms = str(dpiec_kms)
                        dszesc_kms = str(dszesc_kms)
                        dsiedem_kms = str(dsiedem_kms)
                        dosiem_kms = str (dosiem_kms)
                        ddziewiec_kms = str(ddziewiec_kms)
                        trzydziesci_kms = str(trzydziesci_kms)
                        tjeden_kms = str(tjeden_kms)
                        tdwa_kms = str(tdwa_kms)
                        ttrzy_kms = str(ttrzy_kms)
                        tcztery_kms = str(tcztery_kms)
                        tpiec_kms = str(tpiec_kms)
                        tszesc_kms = str(tszesc_kms)
                        tsiedem_kms = str(tsiedem_kms)
                        tosiem_kms = str(tosiem_kms)
                        tdziewiec_kms = str(tdziewiec_kms)
                        czterdziesci_kms = str(czterdziesci_kms)
                        cjeden_kms = str(cjeden_kms)
                        cdwa_kms = str(cdwa_kms)

                        pierwszy_kmm = str(pierwszy_kmm)
                        drugi_kmm = str(drugi_kmm)
                        trzeci_kmm = str(trzeci_kmm)
                        czwarty_kmm = str(czwarty_kmm)
                        piaty_kmm = str(piaty_kmm)
                        szosty_kmm = str(szosty_kmm)
                        siodmy_kmm = str(siodmy_kmm)
                        osmy_kmm = str(osmy_kmm)
                        dziewiaty_kmm = str(dziewiaty_kmm)
                        dziesiaty_kmm = str(dziesiaty_kmm)
                        jedenasty_kmm = str(jedenasty_kmm)
                        dwunasty_kmm = str(dwunasty_kmm)
                        trzynasty_kmm = str(trzynasty_kmm)
                        czternasty_kmm = str(czternasty_kmm)
                        pietnasty_kmm = str(pietnasty_kmm)
                        szesnasty_kmm = str(szesnasty_kmm)
                        siedemnasty_kmm = str(siedemnasty_kmm)
                        osiemnasty_kmm = str(osiemnasty_kmm)
                        dziewietnasty_kmm = str(dziewietnasty_kmm)
                        dwudziesty_kmm = str(dwudziesty_kmm)
                        djeden_kmm = str(djeden_kmm)
                        ddwa_kmm = str(ddwa_kmm)
                        dtrzy_kmm = str(dtrzy_kmm)
                        dcztery_kmm = str(dcztery_kmm)
                        dpiec_kmm = str(dpiec_kmm)
                        dszesc_kmm = str(dszesc_kmm)
                        dsiedem_kmm = str(dsiedem_kmm)
                        dosiem_kmm = str(dosiem_kmm)
                        ddziewiec_kmm = str(ddziewiec_kmm)
                        trzydziesci_kmm = str(trzydziesci_kmm)
                        tjeden_kmm = str(tjeden_kmm)
                        tdwa_kmm = str(tdwa_kmm)
                        ttrzy_kmm = str(ttrzy_kmm)
                        tcztery_kmm = str(tcztery_kmm)
                        tpiec_kmm = str(tpiec_kmm)
                        tszesc_kmm = str(tszesc_kmm)
                        tsiedem_kmm = str(tsiedem_kmm)
                        tosiem_kmm = str(tosiem_kmm)
                        tdziewiec_kmm = str(tdziewiec_kmm)
                        czterdziesci_kmm = str(czterdziesci_kmm)
                        cjeden_kmm = str(cjeden_kmm)
                        cdwa_kmm = str(cdwa_kmm)

                        pierwszy_kmh = str(pierwszy_kmh)
                        drugi_kmh = str(drugi_kmh)
                        trzeci_kmh = str(trzeci_kmh)
                        czwarty_kmh = str(czwarty_kmh)
                        piaty_kmh = str(piaty_kmh)
                        szosty_kmh = str(szosty_kmh)
                        siodmy_kmh = str(siodmy_kmh)
                        osmy_kmh = str(osmy_kmh)
                        dziewiaty_kmh = str(dziewiaty_kmh)
                        dziesiaty_kmh = str(dziesiaty_kmh)
                        jedenasty_kmh = str(jedenasty_kmh)
                        dwunasty_kmh = str(dwunasty_kmh)
                        trzynasty_kmh = str(trzynasty_kmh)
                        czternasty_kmh = str(czternasty_kmh)
                        pietnasty_kmh = str(pietnasty_kmh)
                        szesnasty_kmh = str(szesnasty_kmh)
                        siedemnasty_kmh = str(siedemnasty_kmh)
                        osiemnasty_kmh = str(osiemnasty_kmh)
                        dziewietnasty_kmh = str(dziewietnasty_kmh)
                        dwudziesty_kmh = str(dwudziesty_kmh)
                        djeden_kmh = str(djeden_kmh)
                        ddwa_kmh = str(ddwa_kmh)
                        dtrzy_kmh = str(dtrzy_kmh)
                        dcztery_kmh = str(dcztery_kmh)
                        dpiec_kmh = str(dpiec_kmh)
                        dszesc_kmh = str(dszesc_kmh)
                        dsiedem_kmh = str(dsiedem_kmh)
                        dosiem_kmh = str(dosiem_kmh)
                        ddziewiec_kmh = str(ddziewiec_kmh)
                        trzydziesci_kmh = str(trzydziesci_kmh)
                        tjeden_kmh = str(tjeden_kmh)
                        tdwa_kmh = str(tdwa_kmh)
                        ttrzy_kmh = str(ttrzy_kmh)
                        tcztery_kmh = str(tcztery_kmh)
                        tpiec_kmh = str(tpiec_kmh)
                        tszesc_kmh = str(tszesc_kmh)
                        tsiedem_kmh = str(tsiedem_kmh)
                        tosiem_kmh = str(tosiem_kmh)
                        tdziewiec_kmh = str(tdziewiec_kmh)
                        czterdziesci_kmh = str(czterdziesci_kmh)
                        cjeden_kmh = str(cjeden_kmh)
                        cdwa_kmh = str(cdwa_kmh)

                        czas = "Średni czas na 1 km: " + h_result + "h : " + m_result + "m : " + s_result + "s \n"
                        miedzyczas_pierwszy = "1 km: " + pierwszy_kmh + "h : " + pierwszy_kmm + "m : " + pierwszy_kms + "s \t"
                        miedzyczas_drugi = "2 km: " + drugi_kmh + "h : " + drugi_kmm + "m : " + drugi_kms + "s \n"
                        miedzyczas_trzeci = "3 km: " + trzeci_kmh + "h : " + trzeci_kmm + "m : " + trzeci_kms + "s \t"
                        miedzyczas_czwarty = "4 km: " + czwarty_kmh + "h : " + czwarty_kmm + "m : " + czwarty_kms + "s \n"
                        miedzyczas_piaty = "5 km: " + piaty_kmh + "h : " + piaty_kmm + "m : " + piaty_kms + "s \t"
                        miedzyczas_szosty = "6 km: " + szosty_kmh + "h : " + szosty_kmm + "m : " + szosty_kms + "s \n"
                        miedzyczas_siodmy = "7 km: " + siodmy_kmh + "h : " + siodmy_kmm + "m : " + siodmy_kms + "s \t"
                        miedzyczas_osmy = "8 km: " + osmy_kmh + "h : " + osmy_kmm + "m : " + osmy_kms + "s \n"
                        miedzyczas_dziewiaty = "9 km: " + dziewiaty_kmh + "h : " + dziewiaty_kmm + "m : " + dziewiaty_kms + "s \t"
                        miedzyczas_dziesiaty = "10 km: " + dziesiaty_kmh + "h : " + dziesiaty_kmm + "m : " + dziesiaty_kms + "s \n"
                        miedzyczas_jedenasty = "11 km: " + jedenasty_kmh + "h : " + jedenasty_kmm + "m : " + jedenasty_kms + "s \t"
                        miedzyczas_dwunasty = "12 km: " + dwunasty_kmh + "h : " + dwunasty_kmm + "m : " + dwunasty_kms + "s \n"
                        miedzyczas_trzynasty = "13 km: " + trzynasty_kmh + "h : " + trzynasty_kmm + "m : " + trzynasty_kms + "s \t"
                        miedzyczas_czternasty = "14 km: " + czternasty_kmh + "h : " + czternasty_kmm + "m : " + czternasty_kms + "s \n"
                        miedzyczas_pietnasty = "15 km: " + pietnasty_kmh + "h : " + pietnasty_kmm + "m : " + pietnasty_kms + "s \t"
                        miedzyczas_szesnasty = "16 km: " + szesnasty_kmh + "h : " + szesnasty_kmm + "m : " + szesnasty_kms + "s \n"
                        miedzyczas_siedemnasty = "17 km: " + siedemnasty_kmh + "h : " + siedemnasty_kmm + "m : " + siedemnasty_kms + "s \t"
                        miedzyczas_osiemnasty = "18 km: " + osiemnasty_kmh + "h : " + osiemnasty_kmm + "m : " + osiemnasty_kms + "s \n"
                        miedzyczas_dziewietnasty = "19 km: " + dziewietnasty_kmh + "h : " + dziewietnasty_kmm + "m : " + dziewietnasty_kms + "s \t"
                        miedzyczas_dwudziesty = "20 km: " + dwudziesty_kmh + "h : " + dwudziesty_kmm + "m : " + dwudziesty_kms + "s \n"
                        miedzyczas_djeden = "21 km: " + djeden_kmh + "h : " + djeden_kmm + "m : " + djeden_kms + "s \t"
                        miedzyczas_ddwa = "22 km: " + ddwa_kmh + "h : " + ddwa_kmm + "m : " + ddwa_kms + "s \n"
                        miedzyczas_dtrzy = "23 km: " + dtrzy_kmh + "h : " + dtrzy_kmm + "m : " + dtrzy_kms + "s \t"
                        miedzyczas_dcztery = "24 km: " + dcztery_kmh + "h : " + dcztery_kmm + "m : " + dcztery_kms + "s \n"
                        miedzyczas_dpiec = "25 km: " + dpiec_kmh + "h : " + dpiec_kmm + "m : " + dpiec_kms + "s \t"
                        miedzyczas_dszesc = "26 km: " + dszesc_kmh + "h : " + dszesc_kmm + "m : " + dszesc_kms + "s \n"
                        miedzyczas_dsiedem = "27 km: " + dsiedem_kmh + "h : " + dsiedem_kmm + "m : " + dsiedem_kms + "s \t"
                        miedzyczas_dosiem = "28 km: " + dosiem_kmh + "h : " + dosiem_kmm + "m : " + dosiem_kms + "s \n"
                        miedzyczas_ddziewiec = "29 km: " + ddziewiec_kmh + "h : " + ddziewiec_kmm + "m : " + ddziewiec_kms + "s \t"
                        miedzyczas_trzydziesci = "30 km: " + trzydziesci_kmh + "h : " + trzydziesci_kmm + "m : " + trzydziesci_kms + "s \n"
                        miedzyczas_tjeden = "31 km: " + tjeden_kmh + "h : " + tjeden_kmm + "m : " + tjeden_kms + "s \t"
                        miedzyczas_tdwa = "32 km: " + tdwa_kmh + "h : " + tdwa_kmm + "m : " + tdwa_kms + "s \n"
                        miedzyczas_ttrzy = "33 km: " + ttrzy_kmh + "h : " + ttrzy_kmm + "m : " + ttrzy_kms + "s \t"
                        miedzyczas_tcztery = "34 km: " + tcztery_kmh + "h : " + tcztery_kmm + "m : " + tcztery_kms + "s \n"
                        miedzyczas_tpiec = "35 km: " + tpiec_kmh + "h : " + tpiec_kmm + "m : " + tpiec_kms + "s \t"
                        miedzyczas_tszesc = "36 km: " + tszesc_kmh + "h : " + tszesc_kmm + "m : " + tszesc_kms + "s \n"
                        miedzyczas_tsiedem = "37 km: " + tsiedem_kmh + "h : " + tsiedem_kmm + "m : " + tsiedem_kms + "s \t"
                        miedzyczas_tosiem = "38 km: " + tosiem_kmh + "h : " + tosiem_kmm + "m : " + tosiem_kms + "s \n"
                        miedzyczas_tdziewiec = "39 km: " + tdziewiec_kmh + "h : " + tdziewiec_kmm + "m : " + tdziewiec_kms + "s \t"
                        miedzyczas_czterdziesci = "40 km: " + czterdziesci_kmh + "h : " + czterdziesci_kmm + "m : " + czterdziesci_kms + "s \n"
                        miedzyczas_cjeden = "41 km: " + cjeden_kmh + "h : " + cjeden_kmm + "m : " + cjeden_kms + "s \t"
                        miedzyczas_cdwa = "42 km: " + cdwa_kmh + "h : " + cdwa_kmm + "m : " + cdwa_kms + "s \n"

                        rezultat = czas + miedzyczas_pierwszy + miedzyczas_drugi + miedzyczas_trzeci + miedzyczas_czwarty + miedzyczas_piaty + miedzyczas_szosty + miedzyczas_siodmy + miedzyczas_osmy + miedzyczas_dziewiaty + miedzyczas_dziesiaty + miedzyczas_jedenasty + miedzyczas_dwunasty + miedzyczas_trzynasty + miedzyczas_czternasty + miedzyczas_pietnasty + miedzyczas_szesnasty + miedzyczas_siedemnasty + miedzyczas_osiemnasty + miedzyczas_dziewietnasty + miedzyczas_dwudziesty + miedzyczas_djeden
                        rezultat += miedzyczas_ddwa + miedzyczas_dtrzy + miedzyczas_dcztery + miedzyczas_dpiec + miedzyczas_dszesc + miedzyczas_dsiedem + miedzyczas_dosiem + miedzyczas_ddziewiec + miedzyczas_trzydziesci
                        rezultat += miedzyczas_tjeden + miedzyczas_tdwa + miedzyczas_ttrzy + miedzyczas_tcztery + miedzyczas_tpiec + miedzyczas_tszesc + miedzyczas_tsiedem + miedzyczas_tosiem + miedzyczas_tdziewiec + miedzyczas_czterdziesci + miedzyczas_cjeden + miedzyczas_cdwa

                        self.result.setText(rezultat)
                    else:
                        self.result.setText("Sprawdź,czy dobrze podałeś wartości.")
                except:
                    self.result.setText("Podane warości nie są liczbami całkowitymi")



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.distance = QtWidgets.QListWidget(self.centralwidget)
        self.distance.setGeometry(QtCore.QRect(90, 80, 121, 192))
        self.distance.setObjectName("distance")
        self.TkmButton = QtWidgets.QRadioButton(self.centralwidget)
        self.TkmButton.setGeometry(QtCore.QRect(110, 120, 82, 17))
        self.TkmButton.setObjectName("TkmButton")
        self.PkmButton = QtWidgets.QRadioButton(self.centralwidget)
        self.PkmButton.setGeometry(QtCore.QRect(110, 150, 82, 17))
        self.PkmButton.setObjectName("PkmButton")
        self.DkmButton = QtWidgets.QRadioButton(self.centralwidget)
        self.DkmButton.setGeometry(QtCore.QRect(110, 180, 82, 17))
        self.DkmButton.setObjectName("DkmButton")
        self.HkmButton = QtWidgets.QRadioButton(self.centralwidget)
        self.HkmButton.setGeometry(QtCore.QRect(110, 210, 82, 17))
        self.HkmButton.setObjectName("HkmButton")
        self.MkmButton = QtWidgets.QRadioButton(self.centralwidget)
        self.MkmButton.setGeometry(QtCore.QRect(110, 240, 82, 17))
        self.MkmButton.setObjectName("MkmButton")
        self.JkmButton = QtWidgets.QRadioButton(self.centralwidget)
        self.JkmButton.setGeometry(QtCore.QRect(110, 90, 82, 17))
        self.JkmButton.setChecked(True)
        self.JkmButton.setObjectName("JkmButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 101, 31))
        self.label.setObjectName("label")
        self.godziny = QtWidgets.QLineEdit(self.centralwidget)
        self.godziny.setGeometry(QtCore.QRect(270, 80, 113, 20))
        self.godziny.setObjectName("godziny")
        #########
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 330, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 370, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        ###Evenet to przelicz button###
        self.pushButton.clicked.connect(self.timeCheck)
        self.pushButton_2.clicked.connect(self.timeProgres)
        ######
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 101, 31))
        self.label_2.setObjectName("label_2")
        ###
        self.minuty = QtWidgets.QLineEdit(self.centralwidget)
        self.minuty.setGeometry(QtCore.QRect(270, 110, 113, 20))
        self.minuty.setObjectName("minuty")
        self.sekundy = QtWidgets.QLineEdit(self.centralwidget)
        self.sekundy.setGeometry(QtCore.QRect(270, 140, 113, 20))
        self.sekundy.setObjectName("sekundy")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 70, 50, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 100, 50, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 130, 50, 31))
        self.label_5.setObjectName("label_5")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(220, 170, 300, 205))
        self.result.setText("")
        self.result.setObjectName("result")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Death Run"))
        self.TkmButton.setText(_translate("MainWindow", "3 km"))
        self.PkmButton.setText(_translate("MainWindow", "5 km"))
        self.DkmButton.setText(_translate("MainWindow", "10 km"))
        self.HkmButton.setText(_translate("MainWindow", "21,097 km"))
        self.MkmButton.setText(_translate("MainWindow", "42,195 km"))
        self.JkmButton.setText(_translate("MainWindow", "1 km"))
        self.label.setText(_translate("MainWindow", "Czas:"))
        self.pushButton.setText(_translate("MainWindow", "Tempo stałe"))
        self.pushButton_2.setText(_translate("MainWindow", "Tempo progresywne"))
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

