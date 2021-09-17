import logging
import os

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog
from PySide2.QtGui import QIcon

from src.gui.UI_file.Ui_EncryptDialog import Ui_EncryptDialog
from src.utils.encryptor import Encryptor


class EncryptDialog(QDialog):
    """
    加密解密文件功能窗口
    """
    def __init__(self, father_window, success_window):
        super().__init__()
        self.father_window = father_window
        self.success_window = success_window
        self.setWindowIcon(QIcon("./gui/ZZM.ico"))

        # 应用UI
        self.ui = Ui_EncryptDialog()
        self.ui.setupUi(self)

    # 自动connect
    @Slot()
    def on_EncryptButton_clicked(self):
        filename = self.father_window.widget.file_path.text()
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                logging.info("读取文件{}成功".format(filename))
                message = file.read()
                password = self.ui.PasswordEdit.text()
                logging.info("获取密码成功")
                message_encrypt = Encryptor.encrypt(message, password)
                logging.info("加密成功")
                filename_encrypt = filename.replace(filename.split('.')[-1], 'encrypt')
                file_encrypt = open(filename_encrypt, 'wb')
                file_encrypt.write(message_encrypt)
                file_encrypt.close()
                logging.info("写入加密文件成功")
                self.success_window.show()
                self.close()
            self.father_window.widget.show_text(filename + "加密成功\n")
            self.father_window.widget.show_text("写入文件{}\n".format(filename_encrypt))
        else:
            logging.warning("未读取文件")

    @Slot()
    def on_DecryptButton_clicked(self):
        filename = self.father_window.widget.file_path.text()
        if os.path.exists(filename):
            with open(self.father_window.widget.file_path.text(), 'rb') as file:
                logging.info("读取文件{}成功".format(filename))
                message_encrypt = file.read()
                password = self.ui.PasswordEdit.text()
                logging.info("读取密码成功")
                message_decrypt = Encryptor.decrypt(message_encrypt, password)
                logging.info("解密成功")
                filename_decrypt = filename.replace('.encrypt', '_decrypt.xlsx')
                file_decrypt = open(filename_decrypt, 'wb')
                file_decrypt.write(message_decrypt)
                file_decrypt.close()
                logging.info("写入解密文件成功")
                self.success_window.show()
                self.close()
            self.father_window.widget.show_text(filename + "解密成功\n")
            self.father_window.widget.show_text("写入文件{}\n".format(filename_decrypt))
        else:
            logging.warning("未读取文件")
