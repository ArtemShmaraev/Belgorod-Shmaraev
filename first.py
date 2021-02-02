# -*- coding: utf8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QWidget, QTableWidgetItem, \
    QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import datetime as dt


from math import fabs
from PyQt5 import QtCore, QtGui, QtWidgets


class Cinema:
    def __init__(self, name):
        self.name = name
        self.zals = []
        self.films = []
        self.tickets = []
        self.balance = 0
        self.n_tick = 0

    # добавление зала в кинотеатр
    def append_zal(self, zal):
        self.zals.append(zal)

    # доавление фильма в кинотеатр
    def append_film(self, film):
        self.films.append(film)

    def __str__(self):
        s = ""
        for i in range(len(self.films)):
            s += str(self.films[i]) + "\n"
        s += "\n"
        for i in range(len(self.zals)):
            for j in range(len(self.zals[i].seanses)):
                s += str(self.zals[i].seanses[j].n) + "\n"
                s += str(self.zals[i].seanses[j])

        return s


class Zal:
    def __init__(self, n, x, y):
        self.x = x
        self.y = y
        self.n = n
        self.seanses = []

    # добавление сеанса в зал
    def append_seans(self, seans):
        self.seanses.append(seans)

    def sortirovka(self):
        self.seanses.sort(key=lambda i: i.time)

    def __str__(self):
        s = ""
        s += str(self.n) + " " + str(self.x) + " " + str(self.y)
        return s


class Film:
    def __init__(self, name, janr):
        self.name = name
        self.janr = janr
        self.dohod = 0
        self.n_tick = 0

    def __str__(self):
        s = ""
        s += self.name + " " + self.janr + " "
        return s


class Seans:
    def __init__(self, film, zal, date, time, price, matrix):
        self.x = zal.x
        self.y = zal.y
        self.film = film
        self.time = time
        self.date = date
        self.zal = matrix
        self.n = zal.n
        self.price = price
        rec = (lambda x: sum(map(rec, x)) if isinstance(x, list) else x)
        res = rec(self.zal)
        cinema.balance += self.price * res
        self.film.dohod += self.price * res
        cinema.n_tick += 1 * res
        self.film.n_tick += 1 * res

    # продажа билета на сеанс
    def get_ticket(self, x, y):
        if self.zal[y][x] != 1:
            self.zal[y][x] = 1
            cinema.balance += self.price
            self.film.dohod += self.price
            cinema.n_tick += 1
            self.film.n_tick += 1

    def __str__(self):
        s = ""
        s += str(self.film.name) + " " + str(self.time) + " " + str(self.price) + '\n\n'
        for i in range(len(self.zal)):
            for j in range(len(self.zal[i])):
                s += str(self.zal[i][j])
            s += "\n"
        return s


cinema = Cinema("Русич")


class Ticket:
    def __init__(self, seans, x, y):
        self.seans = seans
        self.x = x
        self.y = y
        cinema.tickets.append(self)


# интерфес добовления кинозала
class Ui_Append_Zal(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(381, 324)
        Form.setStyleSheet("\n"
                           "background-color: rgb(38, 160, 239)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 341, 302))
        self.gridLayoutWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "\n"
                                            "border-radius: 8px;\n"
                                            "\n"
                                            "\n"
                                            "")
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                      "border: 2px solid rgb(255, 255, 255);\n"
                                      "border-radius: 8px;\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:  rgb(220, 20, 60);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 2px solid rgb(255, 255, 255);\n"
                                        "border-radius: 8px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                     "border: 2px solid rgb(255, 255, 255);\n"
                                     "border-radius: 8px;\n"
                                     "color: rgb(255, 255, 255);")
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color:rgb(85, 0, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                     "border: 2px solid rgb(255, 255, 255);\n"
                                     "border-radius: 8px;\n"
                                     "color: rgb(255, 255, 255);")
        self.spinBox_2.setMaximum(45)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 4, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                   "border: 2px solid rgb(255, 255, 255);\n"
                                   "border-radius: 8px;\n"
                                   "color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление зала"))
        self.label_3.setText(_translate("Form", "Количество мест в ряду:"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.pushButton_2.setText(_translate("Form", "Выход"))
        self.label_2.setText(_translate("Form", "Количество рядов:"))
        self.label.setText(_translate("Form", "             Добавление зала"))
        self.label_4.setText(_translate("Form", "№ зала:"))


# Добавление кинозала
class Wzal(QWidget, Ui_Append_Zal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.appendzal)
        self.pushButton_2.clicked.connect(self.exit)

    # выход из окна и сброс данных
    def exit(self):
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.label_5.setText("")
        self.close()

    # добавление зала
    def appendzal(self):
        n = self.spinBox.value()
        x = self.spinBox_2.value()
        y = self.spinBox_3.value()
        f = False
        for i in range(len(cinema.zals)):
            if cinema.zals[i].n == n:
                f = True
                break
        if f:
            self.label_5.setText("Номер занят!")
        else:
            if x < 1 or y < 1 or n < 1:
                self.label_5.setText("Неверные значения")
            else:
                zal = Zal(n, x, y)
                cinema.append_zal(zal)
                self.label_5.setText("Зал добавлен (" + str(n) + ")")


# интерфейс добавления фильма
class Ui_Append_Film(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(395, 296)
        Form.setStyleSheet("\n"
                           "background-color: rgb(38, 160, 239)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 361, 281))
        self.gridLayoutWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "\n"
                                            "border-radius: 8px;\n"
                                            "\n"
                                            "\n"
                                            "")
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color:rgb(85, 0, 255)")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                      "border: 2px solid rgb(255, 255, 255);\n"
                                      "border-radius: 8px;\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                    "border: 2px solid rgb(255, 255, 255);\n"
                                    "border-radius: 8px;\n"
                                    "color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                    "border: 2px solid rgb(255, 255, 255);\n"
                                    "border-radius: 8px;\n"
                                    "color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:  rgb(220, 20, 60);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 2px solid rgb(255, 255, 255);\n"
                                        "border-radius: 8px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление фильма"))
        self.label_3.setText(_translate("Form", "Жанр:"))
        self.label.setText(_translate("Form", "             Добавление фильма"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.label_4.setText(_translate("Form", "Название:"))
        self.comboBox.setItemText(0, _translate("Form", "Комедия"))
        self.comboBox.setItemText(1, _translate("Form", "Ужас"))
        self.comboBox.setItemText(2, _translate("Form", "Драмма"))
        self.comboBox.setItemText(3, _translate("Form", "Мелодрамма"))
        self.comboBox.setItemText(4, _translate("Form", "Боевик"))
        self.comboBox.setItemText(5, _translate("Form", "Фантастика"))
        self.comboBox.setItemText(6, _translate("Form", "Мульт"))
        self.comboBox.setItemText(7, _translate("Form", "Детектив"))
        self.pushButton_2.setText(_translate("Form", "Выход"))


# Добавление фильма
class Wfilm(QWidget, Ui_Append_Film):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.appendfilm)
        self.pushButton_2.clicked.connect(self.exit)

    # выход из окна и сброс данных
    def exit(self):
        self.lineEdit.setText("")
        self.label_5.setText("")
        self.close()

    # добавление фильма
    def appendfilm(self):
        name = self.lineEdit.text()
        janr = self.comboBox.currentText()
        f = False
        for i in range(len(cinema.films)):
            if cinema.films[i].name == name:
                f = True
                break
        if f:
            self.label_5.setText("Название занято")
        else:
            if len(name) < 2 or len(janr) < 2:
                self.label_5.setText("Неверные значения")
            else:
                film = Film(name, janr)
                cinema.append_film(film)
                self.label_5.setText("Фильм добавлен (" + name + ")")


# интерфейс добавление сенса
class Ui_Append_Seans(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(971, 453)
        Form.setStyleSheet("\n"
                           "background-color: rgb(38, 160, 239)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 911, 427))
        self.gridLayoutWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "\n"
                                            "border-radius: 8px;\n"
                                            "\n"
                                            "\n"
                                            "")
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.timeEdit = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                    "border: 3px solid rgb(255, 255, 255);\n"
                                    "border-radius: 12px;\n"
                                    "color: rgb(255, 255, 255);")
        self.timeEdit.setTime(QtCore.QTime(12, 0, 0))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                   "border: 3px solid rgb(255, 255, 255);\n"
                                   "border-radius: 12px;\n"
                                   "color: rgb(255, 255, 255);")
        self.spinBox.setMinimum(100)
        self.spinBox.setMaximum(990)
        self.spinBox.setSingleStep(20)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 5, 3, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("color:  rgb(85, 85, 255);\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 8px;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 10, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 2, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:  rgb(220, 20, 60);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 8px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 2, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                    "border: 3px solid rgb(255, 255, 255);\n"
                                    "border-radius: 12px;\n"
                                    "color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color:rgb(85, 0, 255)")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                     "border: 3px solid rgb(255, 255, 255);\n"
                                     "border-radius: 12px;\n"
                                     "color: rgb(255, 255, 255);")
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 3, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                      "border: 3px solid rgb(255, 255, 255);\n"
                                      "border-radius: 12px;\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 2, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление сеанса"))
        self.label_2.setText(_translate("Form", "Время:"))
        self.pushButton_2.setText(_translate("Form", "Выход"))
        self.label.setText(_translate("Form", "                             Добавление сеанса"))
        self.label_6.setText(_translate("Form", "Цена билета:"))
        self.label_3.setText(_translate("Form", "№ зала:"))
        self.label_4.setText(_translate("Form", "Название фильма:"))
        self.pushButton.setText(_translate("Form", "Добавить"))


# Добавление сеанса
class Wseans(QWidget, Ui_Append_Seans):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.append_sean)
        self.pushButton_2.clicked.connect(self.exit)

    # выход из окна и сброс данных
    def exit(self):
        self.lineEdit.setText("")
        self.timeEdit.setTime(dt.time(12, 00, 00))
        self.spinBox_3.setValue(0)
        self.spinBox.setValue(0)
        self.label_5.setText("")
        self.close()

    # добавление сеанса
    def append_sean(self):
        ni = 0
        nni = 0
        name = self.lineEdit.text()
        n = self.spinBox_3.value()
        time = self.timeEdit.text()
        time = time.split(":")
        price = self.spinBox.value()
        date = self.calendarWidget.selectedDate().toString('yyyy-MM-dd')
        date = date.split("-")
        # запись времени
        dateall = dt.date(int(date[0]), int(date[1]), int(date[2]))
        timeall = dt.time(int(time[0]), int(time[1]), 0)
        # Проверка на наличие фильма
        f = False
        for i in range(len(cinema.films)):
            if cinema.films[i].name == name:
                ni = i  # индекс названия фильма
                f = True
                break
        if f:
            # Проверка на наличие зала
            ff = False
            for i in range(len(cinema.zals)):
                if cinema.zals[i].n == n:
                    nni = i  # индекс зала
                    ff = True
                    break
            if ff:
                fff = True
                t1 = int((str((timeall))[:2]))
                for i in range(len(cinema.zals[nni].seanses)):
                    if cinema.zals[nni].seanses[i].date == dateall:
                        t = int(str(cinema.zals[nni].seanses[i].time)[:2])
                        if fabs(t1 - t) < 2:
                            fff = False
                            break
                if fff:
                    matrix = \
                        [[0 for a in range(cinema.zals[nni].x)] for b in range(cinema.zals[nni].y)]
                    seans = Seans(
                        cinema.films[ni], cinema.zals[nni], dateall, timeall, price, matrix)
                    cinema.zals[nni].append_seans(seans)
                    cinema.zals[nni].sortirovka()
                    ex.loadTable()
                    st = "  Сеанс добавлен " + str(dateall) + " " + str(timeall)[:5]
                    self.label_5.setText(st)
                else:
                    self.label_5.setText(" Зал занят в это время")
            else:
                self.label_5.setText(" Зал не найден!")
        else:
            self.label_5.setText(" Фильм не найден!")


# интерфейс выбора даты
class Ui_W_Date(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(374, 300)
        Form.setStyleSheet("\n"
                           "background-color: rgb(38, 160, 239)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 331, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                      "border: 3px solid rgb(255, 255, 255);\n"
                                      "border-radius: 12px;\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 8px;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 1, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:  rgb(220, 20, 60);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 8px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Выберите дату"))
        self.pushButton.setText(_translate("Form", "Ок"))
        self.pushButton_2.setText(_translate("Form", "Выход"))


# выбор даты для сеансов
class WDate(QWidget, Ui_W_Date):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.date)
        self.pushButton_2.clicked.connect(self.exit)

    # выход из окна
    def exit(self):
        self.close()

    # выбор даты
    def date(self):
        date = self.calendarWidget.selectedDate().toString('yyyy-MM-dd')
        date = date.split("-")
        # запись времени
        datea = dt.date(int(date[0]), int(date[1]), int(date[2]))
        ex.dateall = datea
        ex.loadTable()
        self.close()


# интерфейс статистики
class Ui_Stats(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(771, 445)
        Form.setStyleSheet("\n"
                           "background-color: rgb(38, 160, 239)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 731, 401))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                      "border: 3px solid rgb(255, 255, 255);\n"
                                      "border-radius: 12px;\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_9.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 3, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(85, 170, 255);\n"
                                       "border: 2px solid rgb(85, 0, 255);\n"
                                       "border-radius: 5px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 6, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color:rgb(85, 0, 255)")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 12px;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Статистика"))
        self.pushButton.setText(_translate("Form", "Билеты"))
        self.label_5.setText(_translate("Form", "Топ фильмов:"))
        self.label_4.setText(_translate("Form", "Выручка:"))
        self.label_3.setText(_translate("Form", "Количество проданных билетов:"))
        self.label_2.setText(_translate("Form", "Количество фильмов:"))
        self.label_7.setText(_translate("Form", "0"))
        self.label_8.setText(_translate("Form", "0"))
        self.label_9.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "Количество кинозалов:"))
        self.pushButton_2.setText(_translate("Form", "Выручка"))
        self.label_6.setText(_translate("Form", "0"))


# Отображение статистики
class Stats(QWidget, Ui_Stats):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ticket_stats)
        self.pushButton_2.clicked.connect(self.balance_stats)
        self.label_6.setText(str(len(cinema.films)))
        self.label_7.setText(str(len(cinema.zals)))
        self.label_8.setText(str(cinema.n_tick))
        self.label_9.setText(str(cinema.balance))

    # сортировка статистики по доходу
    def balance_stats(self):
        s = []
        for i in range(len(cinema.films)):
            s.append([cinema.films[i].name, cinema.films[i].n_tick, cinema.films[i].dohod])
        s.sort(key=lambda i: i[2], reverse=True)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(len(cinema.films) + 1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setItem(
            0, 0, QTableWidgetItem("Название фильма:"))
        self.tableWidget.setItem(
            0, 1, QTableWidgetItem("Продано билетов:"))
        self.tableWidget.setItem(
            0, 2, QTableWidgetItem("Выручка:"))

        for i in range(1, len(s) + 1):
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(s[i - 1][0]))
            self.tableWidget.setItem(
                i, 1, QTableWidgetItem(str(s[i - 1][1])))
            self.tableWidget.setItem(
                i, 2, QTableWidgetItem(str(s[i - 1][2])))
        self.tableWidget.resizeColumnsToContents()

    # сортировка статистики по количеству билетов
    def ticket_stats(self):
        s = []
        for i in range(len(cinema.films)):
            s.append([cinema.films[i].name, cinema.films[i].n_tick, cinema.films[i].dohod])
        s.sort(key=lambda i: i[1], reverse=True)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(len(cinema.films) + 1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setItem(
            0, 0, QTableWidgetItem("Название фильма:"))
        self.tableWidget.setItem(
            0, 1, QTableWidgetItem("Продано билетов:"))
        self.tableWidget.setItem(
            0, 2, QTableWidgetItem("Выручка:"))

        for i in range(1, len(s) + 1):
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(s[i - 1][0]))
            self.tableWidget.setItem(
                i, 1, QTableWidgetItem(str(s[i - 1][1])))
            self.tableWidget.setItem(
                i, 2, QTableWidgetItem(str(s[i - 1][2])))
        self.tableWidget.resizeColumnsToContents()


# Показ билеов
class ShowTicket(QWidget):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.k = 0
        self.s = cinema.tickets[len(cinema.tickets) - self.n:]
        self.initUI()

    def initUI(self):
        xp = self.n % 4
        if xp > 0:
            xp = 1
        x = ((self.n // 4) + xp) * 370
        if self.n / 4 >= 1:
            y = 220 * 4
        else:
            y = 220 * (self.n % 4)
        self.resize(x, y)
        self.setWindowTitle("Билеты")
        self.setStyleSheet("QLabel {background-color:rgb(85, 0, 255);  color: rgb(255, "
                           "255, 255); font-size: 14pt}")

        xm = 10
        ym = 10
        for i in range(int(x / 370)):
            for j in range((int(y / 220))):
                if self.k == self.n:
                    break
                else:
                    self.k += 1
                    self.tick = QLabel(" ", self)
                    self.tick.resize(350, 200)
                    self.tick.move(xm, ym)
                    self.tick.setStyleSheet(
                        "background-color:rgb(85, 0, 255);  "
                        "color: rgb(255, 255, 255) "
                        "font-size: 14pt; "
                        "border: 3px solid rgb(38, 160, 239); "
                        "border-radius: 28px;")

                    self.name = QLabel("Билет в кино", self)
                    self.name.move(xm + 120, ym + 20)

                    self.film = QLabel("Фильм:", self)
                    self.film.move(xm + 20, ym + 50)

                    self.film1 = QLabel(str(self.s[self.k - 1].seans.film.name), self)
                    self.film1.move(xm + 90, ym + 50)

                    self.row = QLabel("Ряд", self)
                    self.row.move(xm + 220, ym + 75)

                    self.row1 = QLabel(str(self.s[self.k - 1].y + 1), self)
                    self.row1.move(xm + 220, ym + 95)

                    self.mesto = QLabel("Место", self)
                    self.mesto.move(xm + 280, ym + 75)

                    self.mesto1 = QLabel(str(self.s[self.k - 1].x + 1), self)
                    self.mesto1.move(xm + 280, ym + 95)

                    self.zal = QLabel("Зал:", self)
                    self.zal.move(xm + 20, ym + 90)

                    self.zal1 = QLabel(str(self.s[self.k - 1].seans.n), self)
                    self.zal1.move(xm + 75, ym + 90)

                    self.time = QLabel("Время:", self)
                    self.time.move(xm + 20, ym + 120)

                    self.time1 = QLabel(str(self.s[self.k - 1].seans.time)[:-3], self)
                    self.time1.move(xm + 85, ym + 120)

                    self.data = QLabel("Дата:", self)
                    self.data.move(xm + 150, ym + 120)

                    self.data1 = QLabel(str(self.s[self.k - 1].seans.date), self)
                    self.data1.move(xm + 205, ym + 120)

                    self.price = QLabel("Цена:", self)
                    self.price.move(xm + 20, ym + 150)

                    self.price1 = QLabel(str(self.s[self.k - 1].seans.price), self)
                    self.price1.move(xm + 75, ym + 150)
                ym += 220
            xm += 370
            ym = 10


# Показ схемы зала и продажа билетов
class ShowSeans(QWidget):
    def __init__(self, wseans):
        super().__init__()
        self.seans = wseans
        self.btn = {}
        self.vt = []
        self.lr = {}
        self.k = 0
        self.sell = QPushButton("Купить", self)
        self.exit = QPushButton("Выход", self)
        self.display = QLabel("Экран", self)
        self.nz = QLabel(str(self.seans.n) + " зал", self)
        self.initUI()

    # загрузка интерфейса
    def initUI(self):
        self.resize((self.seans.x * 40 + 130), (self.seans.y * 40 + 230))
        self.setWindowTitle(self.seans.film.name)
        self.setStyleSheet(
            "background-color: rgb(85, 170, 255)")

        self.display.resize((self.seans.x * 40 + 60), 40)
        self.display.move(60, (self.seans.y * 40 + 70))
        self.display.setStyleSheet(
            "background-color:rgb(49, 49, 49); color: rgb(255, 255, 255); font-size: 14pt")
        self.display.setAlignment(Qt.AlignCenter)

        self.nz.move(10, (self.seans.y * 40 + 90))
        self.nz.setStyleSheet("color: rgb(255, 255, 255); font-size: 12pt")
        self.nz.setAlignment(Qt.AlignCenter)

        # кнопка купить
        self.sell.move(40, (self.seans.y * 40 + 140))
        self.sell.resize((self.seans.x * 40 + 60), 35)
        self.sell.setStyleSheet(
            "color: rgb(255, 255, 255); background-color: rgb(85, 170, 27); "
            "border-radius: 12px; "
            "border: 2px solid rgb(85, 0, 255); font-size: 14pt;")
        self.sell.clicked.connect(self.buy_ticket)

        # кнопка выход
        self.exit.move(40, (self.seans.y * 40 + 180))
        self.exit.resize((self.seans.x * 40 + 60), 35)
        self.exit.setStyleSheet(
            "color: rgb(255, 255, 255); background-color: rgb(220, 20, 60); border-radius: "
            "12px; border: 2px solid rgb(85, 0, 255); font-size: 14pt;")
        self.exit.clicked.connect(self.exit_menu)

        # генератор номеров рядов
        yl = (self.seans.y * 40 + 130) - 130
        for i in range(self.seans.y):
            self.lr[i] = QLabel(str(i + 1) + " ряд", self)
            self.lr[i].setStyleSheet("font-size: 14pt; color: rgb(255, 255, 255)")
            self.lr[i].move(20, yl)
            yl -= 40

        # генератор кнопок(мест)
        xm = 90
        ym = (self.seans.y * 40 + 130) - 130
        for i in range(1, self.seans.y + 1):
            for j in range(1, self.seans.x + 1):
                self.btn[(j, i)] = QPushButton(str(j), self)
                self.btn[(j, i)].resize(35, 35)
                self.btn[(j, i)].move(xm, ym)
                if self.seans.zal[i - 1][j - 1] == 1:
                    self.btn[(j, i)].setStyleSheet(
                        "color: rgb(255, 255, 255); "
                        "background-color: rgb(0, 0, 127); "
                        "border-radius: 12px")
                    self.btn[(j, i)].setText("")
                    self.btn[(j, i)].setEnabled(False)
                    self.btn[(j, i)].resize(33, 33)
                else:
                    self.btn[(j, i)].setStyleSheet(
                        "color: rgb(255, 255, 255); background-color:rgb(85, 0, 255); "
                        "border-radius: 12px")
                    self.btn[(j, i)].setEnabled(True)
                self.btn[(j, i)].clicked.connect(self.select_tick)

                xm += 40
            ym -= 40
            xm = 90

    # выбор билетов на покупку
    def select_tick(self):
        xm = 0
        ym = 0

        for i in range(1, self.seans.y + 1):
            for j in range(1, self.seans.x + 1):
                if (j, i) in self.btn:
                    if self.sender() == self.btn[(j, i)]:
                        xm = j
                        ym = i
                        break
        if (xm - 1, ym - 1) in self.vt:
            self.k -= 1
            self.sender().setStyleSheet(
                "color: rgb(255, 255, 255); background-color:rgb(85, 0, 255); border-radius: 12px")
            self.sender().resize(36, 36)
            for i in range(len(self.vt)):
                if self.vt[i] == (xm - 1, ym - 1):
                    self.vt.pop(i)
                    break
        else:
            if self.k <= 19:
                self.k += 1
                self.vt.append((xm - 1, ym - 1))
                self.sender().setStyleSheet(
                    "color: rgb(255, 255, 255); "
                    "background-color: rgb(85, 170, 27); "
                    "border-radius: 12px")
                self.sender().resize(35, 35)
        if len(self.vt) > 0:
            st = f"{self.seans.price} х {self.k} = {self.seans.price * self.k} р."
        else:
            st = "Купить"
        self.sell.setText(st)

    # покупка билетов
    def buy_ticket(self):
        if self.k > 0:
            self.k = 0
            for i in range(len(self.vt)):
                x, y = self.vt[i]
                self.seans.get_ticket(x, y)
                Ticket(self.seans, x, y)
                self.btn[(x + 1, y + 1)].setEnabled(False)
                self.btn[(x + 1, y + 1)].setStyleSheet(
                    "color: rgb(255, 255, 255); background-color: rgb(0, 0, 130); "
                    "border-radius: 12px")
                self.btn[(x + 1, y + 1)].setText("")
                self.btn[(x + 1, y + 1)].resize(33, 33)
            self.showticket = ShowTicket(len(self.vt))
            self.showticket.show()
            self.vt = []
            self.sell.setText("Купить")

    # выход в главное меню
    def exit_menu(self):
        self.close()


# Удаление зала
class DZal(QWidget):
    def __init__(self):
        super().__init__()
        self.z = {}
        self.delz = QPushButton("Удалить", self)
        self.initUI()

    # загрузка интерфейса
    def initUI(self):
        self.resize(120, (len(cinema.zals) * 50) + 130)
        self.setWindowTitle("Удаление зала")
        self.setStyleSheet("background-color: rgb(38, 160, 239)")

        self.delz.move(10, ((len(cinema.zals) * 50) + 70))
        self.delz.resize(100, 40)
        self.delz.setStyleSheet("background-color:  rgb(220, 20, 60); "
                                "color: rgb(255, 255, 255); border: 2px "
                                "solid rgb(255, 255, 255); border-radius: 8px; font-size: 14pt;")
        self.delz.clicked.connect(self.delete)
        yl = 40
        for i in range(len(cinema.zals)):
            self.z[cinema.zals[i].n] = QPushButton(str(cinema.zals[i].n) + " зал", self)
            self.z[cinema.zals[i].n].setStyleSheet(
                "background-color: rgb(85, 85, 255); "
                "border: 2px solid rgb(255, 255, 255); border-radius: 8px; color: "
                "rgb(255, 255, 255);")
            self.z[cinema.zals[i].n].resize(60, 40)
            self.z[cinema.zals[i].n].move(30, yl)
            self.z[cinema.zals[i].n].clicked.connect(self.deletev)
            yl += 50

    # выбор залов на удаление
    def deletev(self):
        txt = self.sender().text()
        if txt[-1] == "!":
            self.sender().setText(txt[:-2])
            self.sender().setStyleSheet(
                "background-color: rgb(85, 85, 255); "
                "border: 2px solid rgb(255, 255, 255); border-radius: 8px; color: "
                "rgb(255, 255, 255);")
        else:
            self.sender().setText(txt + " !")
            self.sender().setStyleSheet(
                "background-color:  rgb(220, 20, 60); color: "
                "rgb(255, 255, 255); border: 2px "
                "solid rgb(255, 255, 255); border-radius: 8px; ")

    # удаление выбранных залов
    def delete(self):
        sdel = []
        sdel2 = []
        for key, value in self.z.items():
            txt = value.text()
            if txt[-1] == "!":
                sdel.append(int(txt.split()[0]))
        for i in range(len(sdel)):
            for j in range(len(cinema.zals)):
                if cinema.zals[j].n == sdel[i]:
                    self.z[cinema.zals[j].n].hide()
                    sdel2.append(j)
                    break
        sdel2.sort(reverse=True)
        for i in range(len(sdel2)):
            del cinema.zals[sdel2[i]]
        ex.loadTable()
        self.close()


# Удаление фильмов
class DFilm(QWidget):
    def __init__(self):
        super().__init__()
        self.f = {}
        self.delf = QPushButton("Удалить", self)
        self.initUI()

    # загрузка интерфейса
    def initUI(self):
        self.resize(300, (len(cinema.films) * 50) + 130)
        self.setWindowTitle("Удаление фильма")
        self.setStyleSheet(
            "background-color: rgb(38, 160, 239)")

        self.delf.move(100, ((len(cinema.films) * 50) + 70))
        self.delf.resize(100, 40)
        self.delf.setStyleSheet(
            "background-color:  rgb(220, 20, 60); color: "
            "rgb(255, 255, 255); border: 2px "
            "solid rgb(255, 255, 255); border-radius: 8px; font-size: 14pt;")
        self.delf.clicked.connect(self.delete)
        yl = 40
        for i in range(len(cinema.films)):
            self.f[cinema.films[i].name] = QPushButton(str(cinema.films[i].name), self)
            self.f[cinema.films[i].name].setStyleSheet(
                "background-color: rgb(85, 85, 255); "
                "border: 2px solid rgb(255, 255, 255); border-radius: 8px; color: "
                "rgb(255, 255, 255);")
            self.f[cinema.films[i].name].resize(120, 40)
            self.f[cinema.films[i].name].move(90, yl)
            self.f[cinema.films[i].name].clicked.connect(self.deletev)
            yl += 50

    # выбор фильмов на удаление
    def deletev(self):
        txt = self.sender().text()
        if txt[-1] == "*":
            self.sender().setText(txt[:-2])
            self.sender().setStyleSheet(
                "background-color: rgb(85, 85, 255); border: 2px solid rgb(255, 255, 255); "
                "border-radius: 8px; color: "
                "rgb(255, 255, 255);")
        else:
            self.sender().setText(txt + " *")
            self.sender().setStyleSheet(
                "background-color:  rgb(220, 20, 60); "
                "color: rgb(255, 255, 255); "
                "border: 2px solid rgb(255, 255, 255); "
                "border-radius: 8px; ")

    # удаление фильмов
    def delete(self):
        sdel = []
        sdel2 = []
        for key, value in self.f.items():
            txt = value.text()
            if txt[-1] == "*":
                sdel.append(txt[:-2])
        for i in range(len(sdel)):
            for j in range(len(cinema.films)):
                if cinema.films[j].name == sdel[i]:
                    self.f[cinema.films[i].name].hide()
                    sdel2.append(j)
                    break
        sdel2.sort(reverse=True)
        for i in range(len(cinema.zals)):
            j = 0
            while j != len(cinema.zals[i].seanses):
                if cinema.zals[i].seanses[j].film.name in sdel:
                    del cinema.zals[i].seanses[j]
                    j -= 1
                j += 1
        for i in range(len(sdel2)):
            del cinema.films[sdel2[i]]
        ex.loadTable()
        self.close()


# интерфейс экрана удаления сеансов
class Ui_Del_Seans(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(788, 370)
        Form.setStyleSheet("\n"
                           "background-color: rgb(38, 160, 239)")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 746, 341))
        self.gridLayoutWidget.setStyleSheet("")
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 12px;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:  rgb(220, 20, 60);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 3px solid rgb(255, 255, 255);\n"
                                      "border-radius: 8px;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("color:  rgb(85, 85, 255);\n"
                                          "background-color: rgb(255, 255, 255);\n"
                                          "border-radius: 8px;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color:rgb(85, 0, 255)")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.tableWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(85, 170, 255);\n"
                                       "border: 2px solid rgb(255, 255, 255);\n"
                                       "border-radius: 8px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Удаление сеанса"))
        self.pushButton_2.setText(_translate("Form", "Обновить"))
        self.label_2.setText(_translate("Form", "Выберите дату"))
        self.pushButton.setText(_translate("Form", "Удалить"))
        self.label.setText(_translate("Form", "Выберите сеанс:"))


# Удаление сеанса
class DSeans(QWidget, Ui_Del_Seans):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newt_btn = {}
        self.newt = {}
        self.v = []
        self.pushButton.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.load)

    # загрузка сеансов
    def load(self):
        table = cinema.zals
        films = cinema.films
        self.newt = {}
        self.newt_btn = {}
        self.v = []
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        lentable = len(table)
        date = self.calendarWidget.selectedDate().toString('yyyy-MM-dd')
        date = date.split("-")
        # запись времени
        data = dt.date(int(date[0]), int(date[1]), int(date[2]))
        f = False
        for i in range(lentable):
            if len(table[i].seanses) > 0:
                f = True
                break
        if f:
            if data not in self.newt:
                self.newt[data] = {}
                self.newt_btn[data] = {}
            for i in range(len(films)):
                if films[i].name not in self.newt[data]:
                    self.newt[data][films[i].name] = []

            for i in range(lentable):
                for j in range(len(table[i].seanses)):
                    if table[i].seanses[j].date == data:
                        time = table[i].seanses[j].time.strftime("%H:%M")
                        if table[i].seanses[j] not in self.newt_btn[data]:
                            self.newt_btn[data][table[i].seanses[j]] = QPushButton(
                                "  " + str(table[i].seanses[j].n) + " - " + str(time) + "|" + str(
                                    table[i].seanses[j].price) + "  ")
                            self.newt[data][table[i].seanses[j].film.name].append(
                                self.newt_btn[data][table[i].seanses[j]])

            # создание таблицы
            self.tableWidget.setRowCount(len(self.newt[data]))
            rowlen = 0
            for key, value in self.newt[data].items():
                long = len(value)
                if long == 0:
                    long = 2
                else:
                    long += 1
                if long > rowlen:
                    rowlen = long
            self.tableWidget.setColumnCount(rowlen)

            i = -1
            for key, value in self.newt[data].items():
                i += 1
                for j in range(len(value) + 1):
                    if j == 0:
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem(key))
                        if not value:
                            self.tableWidget.setItem(
                                i, j + 1,
                                QTableWidgetItem("Нет сеансов"))
                    else:
                        self.tableWidget.setCellWidget(i, j, value[j - 1])

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.setColumnWidth(120, 120)
            for key, value in self.newt_btn.items():
                for k, v in self.newt_btn[key].items():
                    self.newt_btn[key][k].clicked.connect(self.vseans)

    # выбор сеансов на удаление
    def vseans(self):
        for data, value in self.newt_btn.items():
            for seans, v in self.newt_btn[data].items():
                if self.newt_btn[data][seans] == self.sender():
                    wseans = seans
        if wseans not in self.v:
            self.v.append(wseans)
            self.sender().setStyleSheet(
                "color: rgb(255, 255, 255); border-radius: 8px; background-color: rgb(220, 20, 60);")
        else:
            for i in range(len(self.v)):
                if self.v[i] == wseans:
                    self.sender().setStyleSheet("color: rgb(255, 255, 255); border-radius: 8px;")
                    self.v.pop(i)
                    break

    # удаление сеанса
    def delete(self):
        for i in range(len(cinema.zals)):
            j = 0
            while j != len(cinema.zals[i].seanses):
                if cinema.zals[i].seanses[j] in self.v:
                    del cinema.zals[i].seanses[j]
                    j -= 1
                j += 1
        ex.loadTable()
        self.close()


# интерфейс меню
class Ui_Menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 750)
        MainWindow.setStyleSheet("\n"
                                 "background-color: rgb(38, 160, 239)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1031, 691))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 12px;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 45))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                      "border: 3px solid rgb(255, 255, 255);\n"
                                      "border-radius: 12px;\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color:rgb(85, 0, 255)")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setIndent(-5)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 12px;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 7, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                    "border: 3px solid rgb(255, 255, 255);\n"
                                    "border-radius: 12px;\n"
                                    "color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:rgb(85, 0, 255)\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 12px;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_3.setBaseSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 12px;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(85, 170, 255);\n"
                                       "border: 2px solid rgb(255, 255, 255);\n"
                                       "border-radius: 8px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.gridLayout.addWidget(self.tableWidget, 9, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(85, 0, 255)\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(85, 85, 255);\n"
                                        "border: 3px solid rgb(255, 255, 255);\n"
                                        "border-radius: 12px;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 7, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Кинотеатр"))
        self.pushButton_4.setText(_translate("MainWindow", "Сортировать"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate(
            "MainWindow", "                                                Кинотеатр"))
        self.pushButton_5.setText(_translate("MainWindow", "Выбрать дату"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Все"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Комедия"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Драмма"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Мелодрамма"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Боевик"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Фантастика"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Мульт"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Детектив"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Ужас"))
        self.label_2.setText(_translate("MainWindow", "                  Сортировка по жанру:"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_3.setText(_translate("MainWindow", "Статистика"))
        self.pushButton_7.setText(_translate("MainWindow", "Сохранить"))


# Главное окно меню
class MyWidget(QMainWindow, Ui_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.append)
        self.pushButton_5.clicked.connect(self.datevybor)
        self.pushButton_2.clicked.connect(self.delete)
        self.dateall = dt.datetime.now().date()
        self.pushButton_4.clicked.connect(self.loadTable)
        self.pushButton_3.clicked.connect(self.stat)
        self.update()
        self.wzal = Wzal()
        self.wfilm = Wfilm()
        self.wseans = Wseans()
        self.wdate = WDate()
        self.newt_btn = {}
        self.newt = {}
        self.loadTable()

    # статистика
    def stat(self):
        self.stats = Stats()
        self.stats.show()

    # показ схемы зала
    def zalshow(self):
        for data, value in self.newt_btn.items():
            for seans, v in self.newt_btn[data].items():
                if self.newt_btn[data][seans] == self.sender():
                    wseans = seans
                    self.showseans = ShowSeans(wseans)
                    self.showseans.show()

    # загрузка таблицы сеансов
    def loadTable(self):
        table = cinema.zals
        films = cinema.films
        janr = self.comboBox.currentText()
        self.newt = {}
        self.newt_btn = {}
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        lamentable = len(table)  # длина списка
        data = self.dateall
        self.label_3.setText("  Сеансы на " + str(data))
        f = False
        for i in range(lamentable):
            if len(table[i].seanses) > 0:
                f = True
                break
        if f:
            if data not in self.newt:
                self.newt[data] = {}
                self.newt_btn[data] = {}
            for i in range(len(films)):
                if films[i].janr == janr or janr == "Все":
                    if films[i].name not in self.newt[data]:
                        self.newt[data][films[i].name] = []

            for i in range(lamentable):
                for j in range(len(table[i].seanses)):
                    if table[i].seanses[j].date == data and\
                            (table[i].seanses[j].film.janr == janr or janr == "Все"):
                        time = table[i].seanses[j].time.strftime("%H:%M")
                        if table[i].seanses[j] not in self.newt_btn[data]:
                            self.newt_btn[data][table[i].seanses[j]] = QPushButton(
                                "  " + str(table[i].seanses[j].n) + " - " + str(time) + "|" + str(
                                    table[i].seanses[j].price) + "  ")
                            self.newt[data][table[i].seanses[j].film.name].append(
                                self.newt_btn[data][table[i].seanses[j]])

                # создание таблицы
            self.tableWidget.setRowCount(len(self.newt[data]))
            rowlen = 0
            for key, value in self.newt[data].items():
                long = len(value)
                if long == 0:
                    long = 2
                else:
                    long += 1
                if long > rowlen:
                    rowlen = long
            self.tableWidget.setColumnCount(rowlen)

            i = -1
            for key, value in self.newt[data].items():
                i += 1
                for j in range(len(value) + 1):
                    if j == 0:
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem(key))
                        if i % 2 == 0:
                            self.tableWidget.item(i, 0).setBackground(QColor(85, 0, 255))
                        if not value:
                            self.tableWidget.setItem(
                                i, j + 1,
                                QTableWidgetItem(" Нет сеансов "))
                            if i % 2 == 0:
                                self.tableWidget.item(i, 1).setBackground(QColor(85, 0, 255))
                    else:
                        self.tableWidget.setCellWidget(i, j, value[j - 1])
                        if i % 2 == 0:
                            value[j - 1].\
                                setStyleSheet("background-color: rgb(85, 0, 255); font-size: 12pt")
                        else:
                            value[j - 1].setStyleSheet("font-size: 12pt")

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.setColumnWidth(120, 120)
            for key, value in self.newt_btn.items():
                for k, v in self.newt_btn[key].items():
                    self.newt_btn[key][k].clicked.connect(self.zalshow)

    # показ окна
    def datevybor(self):
        self.wdate.show()

    # добавление элемнтов
    def append(self):  # Функционал кнопки добовления
        # Диалоговое окно
        vybor, ok_pressed = QInputDialog.getItem(
            self, "Добавление", "Что добавить?",
            ("Сеанс", "Фильм", "Кинозал"), 1, False)
        if ok_pressed:
            if vybor == "Кинозал":
                self.wzal.show()
            if vybor == "Фильм":
                self.wfilm.show()
            if vybor == "Сеанс":
                self.wseans.show()

    # удаление элементов
    def delete(self):
        # Диалоговое окно
        vybor, ok_pressed = QInputDialog.getItem(
            self, "Удалениее", "Что удалить?",
            ("Фильм", "Кинозал", "Сеанс", "Старые сеансы", "Всё"), 1, False)
        if ok_pressed:
            if vybor == "Кинозал":
                self.dzal = DZal()
                self.dzal.show()
            if vybor == "Фильм":
                self.dfilm = DFilm()
                self.dfilm.show()
            if vybor == "Сеанс":
                self.dseans = DSeans()
                self.dseans.show()
            if vybor == "Старые сеансы":
                for i in range(len(cinema.zals)):
                    j = 0
                    while j != len(cinema.zals[i].seanses):
                        if cinema.zals[i].seanses[j].date < dt.datetime.now().date():
                            del cinema.zals[i].seanses[j]
                            j -= 1
                        j += 1
                self.loadTable()
            if vybor == "Всё":
                valid = QMessageBox.question(
                    self, '', "Действительно удалить ВСЁ?",
                    QMessageBox.Yes, QMessageBox.No)
                if valid == QMessageBox.Yes:
                    cinema.zals = []
                    cinema.films = []
                    cinema.tickets = []
                    cinema.n_tick = 0
                    cinema.balance = 0
                    self.loadTable()
            self.statusBar().showMessage("Данные удадены")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
