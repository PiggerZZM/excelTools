# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SuccessDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import QRect, QMetaObject, QCoreApplication
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QDialogButtonBox, QLabel


class Ui_successDialog(object):
    def setupUi(self, successDialog):
        if not successDialog.objectName():
            successDialog.setObjectName(u"successDialog")
        successDialog.resize(294, 108)
        self.successButton = QDialogButtonBox(successDialog)
        self.successButton.setObjectName(u"successButton")
        self.successButton.setGeometry(QRect(100, 60, 91, 31))
        self.successButton.setOrientation(Qt.Horizontal)
        self.successButton.setStandardButtons(QDialogButtonBox.Ok)
        self.successButton.setCenterButtons(True)
        self.successLabel = QLabel(successDialog)
        self.successLabel.setObjectName(u"successLabel")
        self.successLabel.setGeometry(QRect(50, 20, 201, 31))
        self.successLabel.setTextFormat(Qt.MarkdownText)
        self.successLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(successDialog)
        self.successButton.accepted.connect(successDialog.accept)
        self.successButton.rejected.connect(successDialog.reject)

        QMetaObject.connectSlotsByName(successDialog)
    # setupUi

    def retranslateUi(self, successDialog):
        successDialog.setWindowTitle(QCoreApplication.translate("successDialog", u"\u64cd\u4f5c\u6210\u529f", None))
        self.successLabel.setText(QCoreApplication.translate("successDialog", u"**\u64cd\u4f5c\u6210\u529f\uff01**", None))
    # retranslateUi

