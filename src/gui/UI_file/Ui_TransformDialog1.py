# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI_file file 'TransformDialog1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI_file file!
################################################################################
from PySide2.QtCore import QRect, QMetaObject, QCoreApplication
from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


class Ui_TransformDialog1(object):
    def setupUi(self, TransformDialog1):
        if not TransformDialog1.objectName():
            TransformDialog1.setObjectName(u"TransformDialog1")
        TransformDialog1.resize(546, 248)
        self.verticalLayoutWidget = QWidget(TransformDialog1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 481, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dataRowBeginText = QLabel(self.verticalLayoutWidget)
        self.dataRowBeginText.setObjectName(u"dataRowBeginText")

        self.horizontalLayout_2.addWidget(self.dataRowBeginText)

        self.dataRowBegin = QLineEdit(self.verticalLayoutWidget)
        self.dataRowBegin.setObjectName(u"dataRowBegin")

        self.horizontalLayout_2.addWidget(self.dataRowBegin)

        self.dataRowEndText = QLabel(self.verticalLayoutWidget)
        self.dataRowEndText.setObjectName(u"dataRowEndText")

        self.horizontalLayout_2.addWidget(self.dataRowEndText)

        self.dataRowEnd = QLineEdit(self.verticalLayoutWidget)
        self.dataRowEnd.setObjectName(u"dataRowEnd")

        self.horizontalLayout_2.addWidget(self.dataRowEnd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dataColBeginText = QLabel(self.verticalLayoutWidget)
        self.dataColBeginText.setObjectName(u"dataColBeginText")

        self.horizontalLayout.addWidget(self.dataColBeginText)

        self.dataColBegin = QLineEdit(self.verticalLayoutWidget)
        self.dataColBegin.setObjectName(u"dataColBegin")

        self.horizontalLayout.addWidget(self.dataColBegin)

        self.dataColEndText = QLabel(self.verticalLayoutWidget)
        self.dataColEndText.setObjectName(u"dataColEndText")

        self.horizontalLayout.addWidget(self.dataColEndText)

        self.dataColEnd = QLineEdit(self.verticalLayoutWidget)
        self.dataColEnd.setObjectName(u"dataColEnd")

        self.horizontalLayout.addWidget(self.dataColEnd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.okButton = QPushButton(self.verticalLayoutWidget)
        self.okButton.setObjectName(u"okButton")

        self.verticalLayout.addWidget(self.okButton)


        self.retranslateUi(TransformDialog1)

        QMetaObject.connectSlotsByName(TransformDialog1)
    # setupUi

    def retranslateUi(self, TransformDialog1):
        TransformDialog1.setWindowTitle(QCoreApplication.translate("TransformDialog1", u"\u884c\u5217\u8f6c\u7f6e", None))
        self.dataRowBeginText.setText(QCoreApplication.translate("TransformDialog1", u"\u6570\u636e\u96c6\u8d77\u59cb\u884c\u6570\uff1a", None))
        self.dataRowEndText.setText(QCoreApplication.translate("TransformDialog1", u"\u6570\u636e\u96c6\u7ed3\u675f\u884c\u6570\uff1a", None))
        self.dataColBeginText.setText(QCoreApplication.translate("TransformDialog1", u"\u6570\u636e\u96c6\u8d77\u59cb\u5217\u6570\uff1a", None))
        self.dataColEndText.setText(QCoreApplication.translate("TransformDialog1", u"\u6570\u636e\u96c6\u7ed3\u675f\u5217\u6570\uff1a", None))
        self.okButton.setText(QCoreApplication.translate("TransformDialog1", u"\u786e\u8ba4", None))
    # retranslateUi

