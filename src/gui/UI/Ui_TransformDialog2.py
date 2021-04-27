# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransformDialog2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import QRect, QMetaObject, QCoreApplication
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget


class Ui_TransformDialog2(object):
    def setupUi(self, TransformDialog2):
        if not TransformDialog2.objectName():
            TransformDialog2.setObjectName(u"TransformDialog2")
        TransformDialog2.resize(414, 250)
        self.verticalLayoutWidget = QWidget(TransformDialog2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 351, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rowBeginText = QLabel(self.verticalLayoutWidget)
        self.rowBeginText.setObjectName(u"rowBeginText")

        self.horizontalLayout_2.addWidget(self.rowBeginText)

        self.rowBegin = QLineEdit(self.verticalLayoutWidget)
        self.rowBegin.setObjectName(u"rowBegin")

        self.horizontalLayout_2.addWidget(self.rowBegin)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rowEndText = QLabel(self.verticalLayoutWidget)
        self.rowEndText.setObjectName(u"rowEndText")

        self.horizontalLayout.addWidget(self.rowEndText)

        self.rowEnd = QLineEdit(self.verticalLayoutWidget)
        self.rowEnd.setObjectName(u"rowEnd")

        self.horizontalLayout.addWidget(self.rowEnd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.okButton = QPushButton(self.verticalLayoutWidget)
        self.okButton.setObjectName(u"okButton")

        self.verticalLayout.addWidget(self.okButton)


        self.retranslateUi(TransformDialog2)

        QMetaObject.connectSlotsByName(TransformDialog2)
    # setupUi

    def retranslateUi(self, TransformDialog2):
        TransformDialog2.setWindowTitle(QCoreApplication.translate("TransformDialog2", u"\u8f6c\u6362\u4e0a\u8868\u5934", None))
        self.rowBeginText.setText(QCoreApplication.translate("TransformDialog2", u"\u8868\u5934\u8d77\u59cb\u884c\u53f7\uff1a", None))
        self.rowEndText.setText(QCoreApplication.translate("TransformDialog2", u"\u8868\u5934\u7ed3\u675f\u884c\u53f7\uff1a", None))
        self.okButton.setText(QCoreApplication.translate("TransformDialog2", u"\u786e\u8ba4", None))
    # retranslateUi

