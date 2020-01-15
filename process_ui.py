# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readdata.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(918, 500)
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.openCsvButton = QtWidgets.QPushButton(self.widget)
        self.openCsvButton.setObjectName("openCsvButton")
        self.horizontalLayout_3.addWidget(self.openCsvButton)
        self.savenpzButton = QtWidgets.QPushButton(self.widget)
        self.savenpzButton.setObjectName("savenpzButton")
        self.horizontalLayout_3.addWidget(self.savenpzButton)
        self.savematButton = QtWidgets.QPushButton(self.widget)
        self.savematButton.setObjectName("savematButton")
        self.horizontalLayout_3.addWidget(self.savematButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.graphicsView = GraphicsLayoutWidget(Widget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 3, 1)
        self.widget_2 = QtWidgets.QWidget(Widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.batProcessingButton = QtWidgets.QPushButton(self.widget_2)
        self.batProcessingButton.setObjectName("batProcessingButton")
        self.horizontalLayout_2.addWidget(self.batProcessingButton)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.saveDirLineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.saveDirLineEdit.setObjectName("saveDirLineEdit")
        self.horizontalLayout_2.addWidget(self.saveDirLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.isSavematRaido = QtWidgets.QRadioButton(self.widget_2)
        self.isSavematRaido.setObjectName("isSavematRaido")
        self.verticalLayout.addWidget(self.isSavematRaido)
        self.isSavenpz = QtWidgets.QRadioButton(self.widget_2)
        self.isSavenpz.setObjectName("isSavenpz")
        self.verticalLayout.addWidget(self.isSavenpz)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Widget)
        self.widget_3.setObjectName("widget_3")
        self.formLayout = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.fslineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.fslineEdit.setObjectName("fslineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fslineEdit)
        self.PlotSpectrumButton = QtWidgets.QPushButton(self.widget_3)
        self.PlotSpectrumButton.setObjectName("PlotSpectrumButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.PlotSpectrumButton)
        self.gridLayout.addWidget(self.widget_3, 2, 0, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.openCsvButton.setText(_translate("Widget", "OpenCsv"))
        self.savenpzButton.setText(_translate("Widget", "saveNPz"))
        self.savematButton.setText(_translate("Widget", "saveMat"))
        self.batProcessingButton.setText(_translate("Widget", "BatProcessing"))
        self.label_2.setText(_translate("Widget", "savedir"))
        self.isSavematRaido.setText(_translate("Widget", "savemat"))
        self.isSavenpz.setText(_translate("Widget", "savenpz"))
        self.label.setText(_translate("Widget", "fs"))
        self.PlotSpectrumButton.setText(_translate("Widget", "PlotSpectrum"))

from pyqtgraph import GraphicsLayoutWidget
