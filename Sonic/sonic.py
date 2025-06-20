# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sonic.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Play.setGeometry(QtCore.QRect(330, 460, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_Play.setFont(font)
        self.pushButton_Play.setStyleSheet("QPushButton{\n"
"background-color: #4952ff; /* Cor de fundo */ \n"
"color: white; /* Cor do texto */ \n"
"font-size: 16px; /* Tamanho da fonte */ \n"
"border-radius: 8px; /* Bordas arredondadas */ \n"
"} \n"
"")
        self.pushButton_Play.setObjectName("pushButton_Play")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 60, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_Sonic = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sonic.setGeometry(QtCore.QRect(70, 140, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Sonic.setFont(font)
        self.pushButton_Sonic.setStyleSheet("background-color: #8122ce;\n"
"color: white;")
        self.pushButton_Sonic.setObjectName("pushButton_Sonic")
        self.pushButton_Tails = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tails.setGeometry(QtCore.QRect(70, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Tails.setFont(font)
        self.pushButton_Tails.setStyleSheet("background-color: #8122ce;\n"
"color: white;")
        self.pushButton_Tails.setObjectName("pushButton_Tails")
        self.pushButton_Knuckles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Knuckles.setGeometry(QtCore.QRect(70, 270, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Knuckles.setFont(font)
        self.pushButton_Knuckles.setStyleSheet("background-color: #8122ce;\n"
"color: white;")
        self.pushButton_Knuckles.setObjectName("pushButton_Knuckles")
        self.pushButton_Amy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Amy.setGeometry(QtCore.QRect(70, 340, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Amy.setFont(font)
        self.pushButton_Amy.setStyleSheet("background-color: #8122ce;\n"
"color: white;\n"
"")
        self.pushButton_Amy.setObjectName("pushButton_Amy")
        self.pushButton_Shadow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Shadow.setGeometry(QtCore.QRect(580, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Shadow.setFont(font)
        self.pushButton_Shadow.setStyleSheet("background-color: #8122ce;\n"
"color: white;")
        self.pushButton_Shadow.setObjectName("pushButton_Shadow")
        self.pushButton_Eggman = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Eggman.setGeometry(QtCore.QRect(580, 280, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Eggman.setFont(font)
        self.pushButton_Eggman.setStyleSheet("background-color: #8122ce;\n"
"color: white;")
        self.pushButton_Eggman.setObjectName("pushButton_Eggman")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Imagens/FundoSonic.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_PersonagemSelecionado = QtWidgets.QLabel(self.centralwidget)
        self.label_PersonagemSelecionado.setGeometry(QtCore.QRect(310, 170, 171, 271))
        self.label_PersonagemSelecionado.setObjectName("label_PersonagemSelecionado")
        self.label_2.raise_()
        self.pushButton_Play.raise_()
        self.label.raise_()
        self.pushButton_Sonic.raise_()
        self.pushButton_Tails.raise_()
        self.pushButton_Knuckles.raise_()
        self.pushButton_Amy.raise_()
        self.pushButton_Shadow.raise_()
        self.pushButton_Eggman.raise_()
        self.label_PersonagemSelecionado.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.pushButton_Play.setText(_translate("MainWindow", "Play"))
        self.label.setText(_translate("MainWindow", "Escolha seu Personagem"))
        self.pushButton_Sonic.setText(_translate("MainWindow", "Sonic"))
        self.pushButton_Tails.setText(_translate("MainWindow", "Tails"))
        self.pushButton_Knuckles.setText(_translate("MainWindow", "Knuckles"))
        self.pushButton_Amy.setText(_translate("MainWindow", "Amy"))
        self.pushButton_Shadow.setText(_translate("MainWindow", "Shadow"))
        self.pushButton_Eggman.setText(_translate("MainWindow", "Dr. Eggman"))
        self.label_PersonagemSelecionado.setText(_translate("MainWindow", "TextLabel"))
