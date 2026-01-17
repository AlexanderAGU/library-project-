import hashlib

class User:

    def __init__(self, login, raw_password):
        self.login = login
        self.password_hash = self._hash_password(raw_password)
        # Uses the hashlib library with SHA-256 to create a unique hash of the password

    def _hash_password(self, raw_password):
        return hashlib.sha256(raw_password.encode()).hexdigest()
    
    def verify_password(self, input_password):
        return self.password_hash == hashlib.sha256(input_password.encode()).hexdigest()

    


