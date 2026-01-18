import hashlib

class User:
    def __init__(self, login, password):
        self.login = login
        self.password_hash = self._hash_password(password)

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(input_password: str, stored_hash: str) -> bool:
        return User._hash_password(input_password) == stored_hash

    


