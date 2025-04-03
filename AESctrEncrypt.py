from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_aes_ctr(key, plaintext):
    nonce = os.urandom(16)  # 128bit number used once at 16 byte
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return nonce, ciphertext

def decrypt_aes_ctr(key, nonce, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()