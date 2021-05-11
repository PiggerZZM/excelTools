# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DesensitizeDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_desensitizeDialog(object):
    def setupUi(self, desensitizeDialog):
        if not desensitizeDialog.objectName():
            desensitizeDialog.setObjectName(u"desensitizeDialog")
        desensitizeDialog.resize(400, 261)
        self.verticalLayoutWidget = QWidget(desensitizeDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(49, 9, 271, 194))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.choiceLabel = QLabel(self.verticalLayoutWidget)
        self.choiceLabel.setObjectName(u"choiceLabel")

        self.horizontalLayout.addWidget(self.choiceLabel)

        self.choiceBox = QComboBox(self.verticalLayoutWidget)
        self.choiceBox.addItem("")
        self.choiceBox.addItem("")
        self.choiceBox.setObjectName(u"choiceBox")

        self.horizontalLayout.addWidget(self.choiceBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.columnLabel = QLabel(self.verticalLayoutWidget)
        self.columnLabel.setObjectName(u"columnLabel")

        self.horizontalLayout_2.addWidget(self.columnLabel)

        self.columnEdit = QLineEdit(self.verticalLayoutWidget)
        self.columnEdit.setObjectName(u"columnEdit")

        self.horizontalLayout_2.addWidget(self.columnEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.OKButton = QPushButton(desensitizeDialog)
        self.OKButton.setObjectName(u"OKButton")
        self.OKButton.setGeometry(QRect(150, 210, 93, 28))

        self.retranslateUi(desensitizeDialog)

        QMetaObject.connectSlotsByName(desensitizeDialog)
    # setupUi

    def retranslateUi(self, desensitizeDialog):
        desensitizeDialog.setWindowTitle(QCoreApplication.translate("desensitizeDialog", u"\u6570\u636e\u8131\u654f", None))
        self.choiceLabel.setText(QCoreApplication.translate("desensitizeDialog", u"\u9009\u62e9\u8131\u654f\u7c7b\u578b", None))
        self.choiceBox.setItemText(0, QCoreApplication.translate("desensitizeDialog", u"\u6570\u503c", None))
        self.choiceBox.setItemText(1, QCoreApplication.translate("desensitizeDialog", u"\u65e5\u671f", None))

        self.columnLabel.setText(QCoreApplication.translate("desensitizeDialog", u"\u8f93\u5165\u9700\u8981\u8131\u654f\u7684\u5217\u53f7(\u82f1\u6587)\uff1a", None))
        self.OKButton.setText(QCoreApplication.translate("desensitizeDialog", u"\u786e\u8ba4", None))
    # retranslateUi

