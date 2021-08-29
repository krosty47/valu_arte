import hashlib


class MD5():

    def encrypt(self, password):
        password_hash = hashlib.md5(password.encode())
        md5_hash = password_hash.hexdigest()
        return md5_hash