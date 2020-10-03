from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import requests
from bs4 import BeautifulSoup
import webbrowser , os
import time


ui,_ = loadUiType('main.ui')

class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_btn()

    def handel_btn(self):
        QApplication.processEvents()
        #self.pushButton.clicked.connect()
        self.pushButton_13.clicked.connect(self.open_website)
        self.pushButton_11.clicked.connect(self.chose)
        self.pushButton_12.clicked.connect(self.clear2)

###################################################################################
        self.pushButton.clicked.connect(self.Al_Ghamdi)
        self.pushButton_2.clicked.connect(self.Fares)
        self.pushButton_3.clicked.connect(self.Al_Minshawi)
        self.pushButton_5.clicked.connect(self.Mahmoud_ElBanna)
        self.pushButton_6.clicked.connect(self.Al_Hussary)
        self.pushButton_8.clicked.connect(self.Abdulbaset)
        self.pushButton_4.clicked.connect(self.clear)
        QApplication.processEvents()

    def chose(self):
        try:
            QApplication.processEvents()
            link = self.lineEdit.text()
            num = 0
            while num < 114:
                num = num + 1
                a = str(link) + str(num) + ".html"
                url = a
                QApplication.processEvents()
                QApplication.processEvents()
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
                rq = requests.session()
                rq.headers.update(headers)
                r = rq.get(url)
                soub = BeautifulSoup(r.content, 'lxml')
                for fv in soub.findAll('section', {'class', 'post-content-area single-post-area'}):
                    for f1 in fv.findAll('div', {'class': 'container'}):
                        for f3 in f1.findAll('div', {'class': 'row'}):
                            for f2 in f3.findAll('div', {'class': 'col-lg-8 posts-list'}):
                                for f4 in f2.findAll('div', {'class': 'single-post row'}):
                                    for f5 in f4.findAll('div', {'class': 'col-lg-12'}):
                                        for f6 in f5.findAll('div', {'class': 'feature-img'}):
                                            vv = f6.findAll({"a"})
                                            print(vv[2].text)
                                            for f7 in f6.findAll('p', {'style': 'text-align: center;'}):
                                                for f11 in f7.findAll({'a': 'href'}):
                                                    print(f11.get('href'))
                                                    dowlink = f11.get('href')
                                                    acv=link.split("/")
                                                    ff = open(str(acv[4])+".txt", 'a')
                                                    ff.write(dowlink + "\n")
                                                    ff.close()
                                                    self.textEdit_2.append(vv[2].text)
                                                    self.textEdit_2.append(dowlink)

                                                    # website = https://surahquran.com/qura.html#seen
                                                    QApplication.processEvents()


            self.statusBar().showMessage("                                              --> :)Have Fun Coding By Anas Nashat (: <--")
            QMessageBox.information(QMessageBox(), "Done", "Dowenlod Done")
        except:
            print('check your link')

    def open_website(self):
        webbrowser.open("https://surahquran.com/qura.html#seen")





    def Al_Minshawi(self):
        QApplication.processEvents()
        f = open('  محمد صديق المنشاوي.txt', 'w')
        f.write("")
        f.close()
        link = "https://surahquran.com/mp3/Al-Minshawi/"
        num = 0
        while num < 114:
            num = num + 1
            a = str(link) + str(num) + ".html"
            url = a
            QApplication.processEvents()
            self.textEdit_2.append(a)
            QApplication.processEvents()
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
            rq = requests.session()
            rq.headers.update(headers)
            r = rq.get(url)
            soub = BeautifulSoup(r.content, 'lxml')
            for fv in soub.findAll('section', {'class', 'post-content-area single-post-area'}):
                for f1 in fv.findAll('div', {'class': 'container'}):
                    for f3 in f1.findAll('div', {'class': 'row'}):
                        for f2 in f3.findAll('div', {'class': 'col-lg-8 posts-list'}):
                            for f4 in f2.findAll('div', {'class': 'single-post row'}):
                                for f5 in f4.findAll('div', {'class': 'col-lg-12'}):
                                    for f6 in f5.findAll('div', {'class': 'feature-img'}):
                                        vv = f6.findAll({"a"})
                                        print(vv[2].text)
                                        for f7 in f6.findAll('p', {'style': 'text-align: center;'}):
                                            for f11 in f7.findAll({'a': 'href'}):
                                                print(f11.get('href'))
                                                dowlink = f11.get('href')
                                                ff = open(' محمد صديق المنشاوي.txt', 'a')
                                                ff.write(dowlink + "\n")
                                                self.textEdit.append(vv[2].text)
                                                self.textEdit.append(dowlink)



                                                # website = https://surahquran.com/qura.html#seen
                                                QApplication.processEvents()
        self.statusBar().showMessage( "                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Dowenlod Done")



    def Fares(self):
        QApplication.processEvents()
        f = open('فارس عباد.txt', 'w')
        f.write("")
        f.close()
        link = "https://surahquran.com/mp3/Fares/"
        num = 0
        while num < 114:
            num = num + 1
            a = str(link) + str(num) + ".html"
            url = a
            QApplication.processEvents()
            QApplication.processEvents()
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
            rq = requests.session()
            rq.headers.update(headers)
            r = rq.get(url)
            soub = BeautifulSoup(r.content, 'lxml')
            for fv in soub.findAll('section', {'class', 'post-content-area single-post-area'}):
                for f1 in fv.findAll('div', {'class': 'container'}):
                    for f3 in f1.findAll('div', {'class': 'row'}):
                        for f2 in f3.findAll('div', {'class': 'col-lg-8 posts-list'}):
                            for f4 in f2.findAll('div', {'class': 'single-post row'}):
                                for f5 in f4.findAll('div', {'class': 'col-lg-12'}):
                                    for f6 in f5.findAll('div', {'class': 'feature-img'}):
                                        vv = f6.findAll({"a"})
                                        print(vv[2].text)
                                        for f7 in f6.findAll('p', {'style': 'text-align: center;'}):
                                            for f11 in f7.findAll({'a': 'href'}):
                                                print(f11.get('href'))
                                                dowlink = f11.get('href')
                                                ff = open(' فارس عباد.txt', 'a')
                                                ff.write(dowlink + "\n")
                                                self.textEdit.append(vv[2].text)
                                                self.textEdit.append(dowlink)


                                                # website = https://surahquran.com/qura.html#seen
                                                QApplication.processEvents()
        self.statusBar().showMessage( "                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Dowenlod Done")




    def Al_Ghamdi(self):
        QApplication.processEvents()
        f = open(' سعد الغامدي.txt', 'w')
        f.write("")
        f.close()
        link = "https://surahquran.com/mp3/Al-Ghamdi/"
        num = 0
        while num < 114:
            num = num + 1
            a = str(link) + str(num) + ".html"
            url = a
            QApplication.processEvents()
            QApplication.processEvents()
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
            rq = requests.session()
            rq.headers.update(headers)
            r = rq.get(url)
            soub = BeautifulSoup(r.content, 'lxml')
            for fv in soub.findAll('section', {'class', 'post-content-area single-post-area'}):
                for f1 in fv.findAll('div', {'class': 'container'}):
                    for f3 in f1.findAll('div', {'class': 'row'}):
                        for f2 in f3.findAll('div', {'class': 'col-lg-8 posts-list'}):
                            for f4 in f2.findAll('div', {'class': 'single-post row'}):
                                for f5 in f4.findAll('div', {'class': 'col-lg-12'}):
                                    for f6 in f5.findAll('div', {'class': 'feature-img'}):
                                        vv = f6.findAll({"a"})
                                        print(vv[2].text)
                                        for f7 in f6.findAll('p', {'style': 'text-align: center;'}):
                                            for f11 in f7.findAll({'a': 'href'}):
                                                print(f11.get('href'))
                                                dowlink = f11.get('href')
                                                ff = open(' سعد الغامدي.txt', 'a')
                                                ff.write(dowlink + "\n")
                                                QApplication.processEvents()

                                                self.textEdit.append(vv[2].text)
                                                QApplication.processEvents()
                                                self.textEdit.append(dowlink)
                                                QApplication.processEvents()
        self.statusBar().showMessage( "                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Dowenlod Done")

    def Abdulbaset(self):
        QApplication.processEvents()
        link = "https://surahquran.com/mp3/Abdulbaset/"
        num = 0
        while num < 114:
            num = num + 1
            a = str(link) + str(num) + ".html"
            url = a
            QApplication.processEvents()
            QApplication.processEvents()
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
            rq = requests.session()
            rq.headers.update(headers)
            r = rq.get(url)
            soub = BeautifulSoup(r.content, 'lxml')
            for fv in soub.findAll('section', {'class', 'post-content-area single-post-area'}):
                for f1 in fv.findAll('div', {'class': 'container'}):
                    for f3 in f1.findAll('div', {'class': 'row'}):
                        for f2 in f3.findAll('div', {'class': 'col-lg-8 posts-list'}):
                            for f4 in f2.findAll('div', {'class': 'single-post row'}):
                                for f5 in f4.findAll('div', {'class': 'col-lg-12'}):
                                    for f6 in f5.findAll('div', {'class': 'feature-img'}):
                                        vv = f6.findAll({"a"})
                                        print(vv[2].text)
                                        for f7 in f6.findAll('p', {'style': 'text-align: center;'}):
                                            for f11 in f7.findAll({'a': 'href'}):
                                                print(f11.get('href'))
                                                dowlink = f11.get('href')
                                                acv = link.split("/")
                                                ff = open(str(acv[4]) + ".txt", 'a')
                                                ff.write(dowlink + "\n")
                                                ff.close()
                                                self.textEdit_2.append(vv[2].text)
                                                self.textEdit_2.append(dowlink)

                                                # website = https://surahquran.com/qura.html#seen
                                                QApplication.processEvents()

        self.statusBar().showMessage(
            "                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Dowenlod Done")

    def Mohamed_Refaat(self):
        QApplication.processEvents()

        webbrowser.open("https://archive.org/compress/quran-by-mohammad-ref3at-high-quality--cairosound-quran-86part/formats=VBR%20MP3&file=/quran-by-mohammad-ref3at-high-quality--cairosound-quran-86part.zip")


        self.statusBar().showMessage(
            "                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Dowenlod Done")

    def Al_Hussary(self):
        QApplication.processEvents()
        link = "https://surahquran.com/mp3/Al-Hussary/"
        num = 0
        while num < 114:
            num = num + 1
            a = str(link) + str(num) + ".html"
            url = a
            QApplication.processEvents()
            QApplication.processEvents()
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
            rq = requests.session()
            rq.headers.update(headers)
            r = rq.get(url)
            soub = BeautifulSoup(r.content, 'lxml')
            for fv in soub.findAll('section', {'class', 'post-content-area single-post-area'}):
                for f1 in fv.findAll('div', {'class': 'container'}):
                    for f3 in f1.findAll('div', {'class': 'row'}):
                        for f2 in f3.findAll('div', {'class': 'col-lg-8 posts-list'}):
                            for f4 in f2.findAll('div', {'class': 'single-post row'}):
                                for f5 in f4.findAll('div', {'class': 'col-lg-12'}):
                                    for f6 in f5.findAll('div', {'class': 'feature-img'}):
                                        vv = f6.findAll({"a"})
                                        print(vv[2].text)
                                        for f7 in f6.findAll('p', {'style': 'text-align: center;'}):
                                            for f11 in f7.findAll({'a': 'href'}):
                                                print(f11.get('href'))
                                                dowlink = f11.get('href')
                                                acv = link.split("/")
                                                ff = open(str(acv[4]) + ".txt", 'a')
                                                ff.write(dowlink + "\n")
                                                ff.close()
                                                self.textEdit_2.append(vv[2].text)
                                                self.textEdit_2.append(dowlink)

                                                # website = https://surahquran.com/qura.html#seen
                                                QApplication.processEvents()

        self.statusBar().showMessage("                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Dowenlod Done")

    def Mahmoud_ElBanna(self):
        QApplication.processEvents()
        link = "https://surahquran.com/mp3/Mahmoud-El-Banna/"
        num = 0
        while num < 114:
            num = num + 1
            a = str(link) + str(num) + ".html"
            url = a
            QApplication.processEvents()
            QApplication.processEvents()
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
            rq = requests.session()
            rq.headers.update(headers)
            r = rq.get(url)
            soub = BeautifulSoup(r.content, 'lxml')
            for fv in soub.findAll('section', {'class', 'post-content-area single-post-area'}):
                for f1 in fv.findAll('div', {'class': 'container'}):
                    for f3 in f1.findAll('div', {'class': 'row'}):
                        for f2 in f3.findAll('div', {'class': 'col-lg-8 posts-list'}):
                            for f4 in f2.findAll('div', {'class': 'single-post row'}):
                                for f5 in f4.findAll('div', {'class': 'col-lg-12'}):
                                    for f6 in f5.findAll('div', {'class': 'feature-img'}):
                                        vv = f6.findAll({"a"})
                                        print(vv[2].text)
                                        for f7 in f6.findAll('p', {'style': 'text-align: center;'}):
                                            for f11 in f7.findAll({'a': 'href'}):
                                                print(f11.get('href'))
                                                dowlink = f11.get('href')
                                                acv = link.split("/")
                                                ff = open(str(acv[4]) + ".txt", 'a')
                                                ff.write(dowlink + "\n")
                                                ff.close()
                                                self.textEdit_2.append(vv[2].text)
                                                self.textEdit_2.append(dowlink)

                                                # website = https://surahquran.com/qura.html#seen
                                                QApplication.processEvents()

        self.statusBar().showMessage(
            "                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Dowenlod Done")

























                                                # website = https://surahquran.com/qura.html#seen
        QApplication.processEvents()
        self.statusBar().showMessage( "                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Dowenlod Done")


    def clear(self):
        self.textEdit.setText("")
        self.statusBar().showMessage( "                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Clear Done")


    def clear2(self):
        self.textEdit_2.setText("")
        self.statusBar().showMessage("                                              --> :)Have Fun Coding By Anas Nashat (: <--")
        QMessageBox.information(QMessageBox(), "Done", "Clear Done")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
