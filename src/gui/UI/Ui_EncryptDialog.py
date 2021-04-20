# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EncryptDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QRect, QCoreApplication, QMetaObject
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QLabel, QLineEdit, QPushButton


class Ui_EncryptDialog(object):
    def setupUi(self, EncryptDialog):
        if not EncryptDialog.objectName():
            EncryptDialog.setObjectName(u"EncryptDialog")
        EncryptDialog.resize(400, 253)
        self.title = QLabel(EncryptDialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 401, 111))
        self.title.setTextFormat(Qt.MarkdownText)
        self.title.setAlignment(Qt.AlignCenter)
        self.PasswordEdit = QLineEdit(EncryptDialog)
        self.PasswordEdit.setObjectName(u"PasswordEdit")
        self.PasswordEdit.setGeometry(QRect(182, 120, 151, 21))
        self.PasswordText = QLabel(EncryptDialog)
        self.PasswordText.setObjectName(u"PasswordText")
        self.PasswordText.setGeometry(QRect(70, 120, 111, 21))
        self.PasswordText.setAlignment(Qt.AlignCenter)
        self.EncryptButton = QPushButton(EncryptDialog)
        self.EncryptButton.setObjectName(u"EncryptButton")
        self.EncryptButton.setGeometry(QRect(80, 200, 93, 28))
        self.DecryptButton = QPushButton(EncryptDialog)
        self.DecryptButton.setObjectName(u"DecryptButton")
        self.DecryptButton.setGeometry(QRect(230, 200, 93, 28))

        self.retranslateUi(EncryptDialog)

        QMetaObject.connectSlotsByName(EncryptDialog)
    # setupUi

    def retranslateUi(self, EncryptDialog):
        EncryptDialog.setWindowTitle(QCoreApplication.translate("EncryptDialog", u"\u6587\u4ef6\u52a0\u5bc6\u89e3\u5bc6\u5de5\u5177", None))
        self.title.setText(QCoreApplication.translate("EncryptDialog", u"**\u5bf9\u6587\u4ef6\u8fdb\u884c\u52a0\u5bc6\u6216\u89e3\u5bc6**", None))
        self.PasswordText.setText(QCoreApplication.translate("EncryptDialog", u"\u8f93\u5165\u5bc6\u94a5\uff1a", None))
        self.EncryptButton.setText(QCoreApplication.translate("EncryptDialog", u"\u52a0\u5bc6", None))
        self.DecryptButton.setText(QCoreApplication.translate("EncryptDialog", u"\u89e3\u5bc6", None))
    # retranslateUi

