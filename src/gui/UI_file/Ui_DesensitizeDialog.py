# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI_file file 'DesensitizeDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI_file file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_desensitizeDialog(object):
    def setupUi(self, desensitizeDialog):
        if not desensitizeDialog.objectName():
            desensitizeDialog.setObjectName(u"desensitizeDialog")
        desensitizeDialog.resize(515, 299)
        self.verticalLayoutWidget = QWidget(desensitizeDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(49, 9, 421, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.numColumnLabel = QLabel(self.verticalLayoutWidget)
        self.numColumnLabel.setObjectName(u"numColumnLabel")

        self.horizontalLayout.addWidget(self.numColumnLabel)

        self.numColumnEdit = QLineEdit(self.verticalLayoutWidget)
        self.numColumnEdit.setObjectName(u"numColumnEdit")

        self.horizontalLayout.addWidget(self.numColumnEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dateColumnLabel = QLabel(self.verticalLayoutWidget)
        self.dateColumnLabel.setObjectName(u"dateColumnLabel")

        self.horizontalLayout_2.addWidget(self.dateColumnLabel)

        self.dateColumnEdit = QLineEdit(self.verticalLayoutWidget)
        self.dateColumnEdit.setObjectName(u"dateColumnEdit")

        self.horizontalLayout_2.addWidget(self.dateColumnEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.OKButton = QPushButton(desensitizeDialog)
        self.OKButton.setObjectName(u"OKButton")
        self.OKButton.setGeometry(QRect(200, 260, 93, 28))

        self.retranslateUi(desensitizeDialog)

        QMetaObject.connectSlotsByName(desensitizeDialog)
    # setupUi

    def retranslateUi(self, desensitizeDialog):
        desensitizeDialog.setWindowTitle(QCoreApplication.translate("desensitizeDialog", u"\u6570\u636e\u8131\u654f", None))
        self.numColumnLabel.setText(QCoreApplication.translate("desensitizeDialog", u"\u6570\u503c\u7c7b\u578b\u5217\u53f7(\u591a\u4e2a\u5217\u7528\u7a7a\u683c\u9694\u5f00)\uff1a", None))
        self.dateColumnLabel.setText(QCoreApplication.translate("desensitizeDialog", u"\u65e5\u671f\u7c7b\u578b\u5217\u53f7(\u591a\u4e2a\u5217\u7528\u7a7a\u683c\u9694\u5f00)\uff1a", None))
        self.OKButton.setText(QCoreApplication.translate("desensitizeDialog", u"\u786e\u8ba4", None))
    # retranslateUi

