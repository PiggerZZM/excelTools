from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Encryptor:

    # 加密函数
    @staticmethod
    def encrypt(message: bytes, password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'0',  # 添加固定的随机数，保证加密密钥不变
            iterations=100000,
        )
        key = urlsafe_b64encode(kdf.derive(password.encode('utf8')))
        fernet = Fernet(key)
        message_encrypt = fernet.encrypt(message)
        return message_encrypt

    # 解密函数
    @staticmethod
    def decrypt(message_encrypt: bytes, password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'0',  # 添加固定的随机数，保证加密密钥不变
            iterations=100000,
        )
        key = urlsafe_b64encode(kdf.derive(password.encode('utf8')))
        fernet = Fernet(key)
        message_decrypt = fernet.decrypt(message_encrypt)
        return message_decrypt

