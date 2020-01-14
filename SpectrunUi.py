# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(881, 641)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = GraphicsLayoutWidget(Form)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.OpenFileButton = QtWidgets.QPushButton(Form)
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.gridLayout_3.addWidget(self.OpenFileButton, 0, 1, 1, 1)
        self.ConfigFrame = QtWidgets.QFrame(Form)
        self.ConfigFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ConfigFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ConfigFrame.setObjectName("ConfigFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ConfigFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.AnalyzeButton = QtWidgets.QPushButton(self.ConfigFrame)
        self.AnalyzeButton.setObjectName("AnalyzeButton")
        self.gridLayout.addWidget(self.AnalyzeButton, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.ConfigFrame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.save = QtWidgets.QPushButton(self.ConfigFrame)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 6, 2, 1, 1)
        self.ClearFig = QtWidgets.QPushButton(self.ConfigFrame)
        self.ClearFig.setObjectName("ClearFig")
        self.gridLayout.addWidget(self.ClearFig, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.ConfigFrame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.FFTPoint = QtWidgets.QLineEdit(self.ConfigFrame)
        self.FFTPoint.setObjectName("FFTPoint")
        self.gridLayout.addWidget(self.FFTPoint, 0, 2, 1, 1)
        self.Ychidu = QtWidgets.QComboBox(self.ConfigFrame)
        self.Ychidu.setObjectName("Ychidu")
        self.Ychidu.addItem("")
        self.Ychidu.addItem("")
        self.gridLayout.addWidget(self.Ychidu, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.ConfigFrame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.fs = QtWidgets.QLineEdit(self.ConfigFrame)
        self.fs.setObjectName("fs")
        self.gridLayout.addWidget(self.fs, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.ConfigFrame, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.OpenFileButton.setText(_translate("Form", "打开文件"))
        self.AnalyzeButton.setText(_translate("Form", "Analyze"))
        self.label_2.setText(_translate("Form", "Log/Linear"))
        self.save.setText(_translate("Form", "save"))
        self.ClearFig.setText(_translate("Form", "clear"))
        self.label_3.setText(_translate("Form", "采样频率 Hz"))
        self.Ychidu.setItemText(0, _translate("Form", "linear"))
        self.Ychidu.setItemText(1, _translate("Form", "log"))
        self.label.setText(_translate("Form", "FFT point"))
from pyqtgraph import GraphicsLayoutWidget
