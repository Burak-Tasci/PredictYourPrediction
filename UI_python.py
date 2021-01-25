# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ABRA/Desktop/Kodlama/MachineLearning/PredictYourPrediction/UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 324)
        MainWindow.setStyleSheet("background-color:rgb(99, 133, 109);\n"
"")
        self.Main = QtWidgets.QWidget(MainWindow)
        self.Main.setObjectName("Main")
        self.DataInput0Btn = QtWidgets.QPushButton(self.Main)
        self.DataInput0Btn.setGeometry(QtCore.QRect(650, 130, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataInput0Btn.sizePolicy().hasHeightForWidth())
        self.DataInput0Btn.setSizePolicy(sizePolicy)
        self.DataInput0Btn.setStyleSheet("#DataInput0Btn\n"
"{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: white;\n"
"background-color:rgb(66, 84, 51);\n"
"}\n"
"#DataInput0Btn:pressed\n"
"{\n"
"background:rgb(99, 133, 109);\n"
"}")
        self.DataInput0Btn.setObjectName("DataInput0Btn")
        self.Title = QtWidgets.QLabel(self.Main)
        self.Title.setGeometry(QtCore.QRect(10, 10, 611, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.DataInput1Btn = QtWidgets.QPushButton(self.Main)
        self.DataInput1Btn.setGeometry(QtCore.QRect(530, 130, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataInput1Btn.sizePolicy().hasHeightForWidth())
        self.DataInput1Btn.setSizePolicy(sizePolicy)
        self.DataInput1Btn.setStyleSheet("#DataInput1Btn\n"
"{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: white;\n"
"background-color:rgb(66, 84, 51);\n"
"}\n"
"#DataInput1Btn:pressed\n"
"{\n"
"background:rgb(99, 133, 109);\n"
"}")
        self.DataInput1Btn.setObjectName("DataInput1Btn")
        self.DataInput = QtWidgets.QTextEdit(self.Main)
        self.DataInput.setEnabled(False)
        self.DataInput.setGeometry(QtCore.QRect(20, 120, 475, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataInput.sizePolicy().hasHeightForWidth())
        self.DataInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.DataInput.setFont(font)
        self.DataInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DataInput.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-radius:25;")
        self.DataInput.setTabChangesFocus(False)
        self.DataInput.setObjectName("DataInput")
        self.help = QtWidgets.QPushButton(self.Main)
        self.help.setGeometry(QtCore.QRect(760, 10, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.help.setFont(font)
        self.help.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.help.setAutoFillBackground(False)
        self.help.setStyleSheet("#help\n"
"{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: white;\n"
"background-color:rgb(66, 84, 51);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"#help:pressed\n"
"{\n"
"background:rgb(99, 133, 109);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon)
        self.help.setCheckable(False)
        self.help.setDefault(False)
        self.help.setFlat(False)
        self.help.setObjectName("help")
        self.label = QtWidgets.QLabel(self.Main)
        self.label.setGeometry(QtCore.QRect(50, 100, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Predict = QtWidgets.QTextEdit(self.Main)
        self.Predict.setEnabled(False)
        self.Predict.setGeometry(QtCore.QRect(20, 210, 475, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Predict.sizePolicy().hasHeightForWidth())
        self.Predict.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.Predict.setFont(font)
        self.Predict.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-radius:25;")
        self.Predict.setObjectName("Predict")
        self.label_2 = QtWidgets.QLabel(self.Main)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Predict0Btn = QtWidgets.QPushButton(self.Main)
        self.Predict0Btn.setGeometry(QtCore.QRect(650, 220, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Predict0Btn.sizePolicy().hasHeightForWidth())
        self.Predict0Btn.setSizePolicy(sizePolicy)
        self.Predict0Btn.setStyleSheet("#Predict0Btn\n"
"{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: white;\n"
"background-color:rgb(66, 84, 51);\n"
"}\n"
"#Predict0Btn:pressed\n"
"{\n"
"background:rgb(99, 133, 109);\n"
"}")
        self.Predict0Btn.setObjectName("Predict0Btn")
        self.Predict1Btn = QtWidgets.QPushButton(self.Main)
        self.Predict1Btn.setGeometry(QtCore.QRect(530, 220, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Predict1Btn.sizePolicy().hasHeightForWidth())
        self.Predict1Btn.setSizePolicy(sizePolicy)
        self.Predict1Btn.setStyleSheet("#Predict1Btn\n"
"{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: white;\n"
"background-color:rgb(66, 84, 51);\n"
"}\n"
"#Predict1Btn:pressed\n"
"{\n"
"background:rgb(99, 133, 109);\n"
"}")
        self.Predict1Btn.setObjectName("Predict1Btn")
        MainWindow.setCentralWidget(self.Main)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.DataInput1Btn.clicked.connect(MainWindow.data_input_1btn)
        self.DataInput0Btn.clicked.connect(MainWindow.data_input_0btn)
        self.Predict1Btn.clicked.connect(MainWindow.predict_1btn)
        self.Predict0Btn.clicked.connect(MainWindow.predict_0btn)
        self.help.clicked.connect(MainWindow.help)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DataInput0Btn.setText(_translate("MainWindow", "0"))
        self.Title.setText(_translate("MainWindow", "PREDICT YOUR PREDICTION"))
        self.DataInput1Btn.setText(_translate("MainWindow", "1"))
        self.help.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/help.png\"/></p></body></html>"))
        self.help.setWhatsThis(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/help.png\" /></p></body></html>"))
        self.help.setText(_translate("MainWindow", "? "))
        self.label.setText(_translate("MainWindow", "Data Input"))
        self.label_2.setText(_translate("MainWindow", "Predict"))
        self.Predict0Btn.setText(_translate("MainWindow", "0"))
        self.Predict1Btn.setText(_translate("MainWindow", "1"))

