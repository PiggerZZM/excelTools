# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StripDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import QRect, QMetaObject, QCoreApplication
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton


class Ui_StripDialog(object):
    def setupUi(self, StripDialog):
        if not StripDialog.objectName():
            StripDialog.setObjectName(u"StripDialog")
        StripDialog.resize(342, 139)
        self.verticalLayoutWidget = QWidget(StripDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 10, 266, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.StripChText = QLabel(self.verticalLayoutWidget)
        self.StripChText.setObjectName(u"StripChText")

        self.horizontalLayout.addWidget(self.StripChText)

        self.StripCh = QLineEdit(self.verticalLayoutWidget)
        self.StripCh.setObjectName(u"StripCh")

        self.horizontalLayout.addWidget(self.StripCh)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.OKButton = QPushButton(self.verticalLayoutWidget)
        self.OKButton.setObjectName(u"OKButton")

        self.verticalLayout.addWidget(self.OKButton)


        self.retranslateUi(StripDialog)

        QMetaObject.connectSlotsByName(StripDialog)
    # setupUi

    def retranslateUi(self, StripDialog):
        StripDialog.setWindowTitle(QCoreApplication.translate("StripDialog", u"\u53bb\u9664\u5b57\u7b26", None))
        self.StripChText.setText(QCoreApplication.translate("StripDialog", u"\u8981\u53bb\u9664\u7684\u5b57\u7b26\uff1a", None))
        self.OKButton.setText(QCoreApplication.translate("StripDialog", u"\u786e\u8ba4", None))
    # retranslateUi

