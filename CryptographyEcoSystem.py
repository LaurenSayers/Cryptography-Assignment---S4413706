import serial
import time
import os

from AESctrEncrypt import encrypt_aes_ctr, decrypt_aes_ctr
from CustomHashForCryptography import custom_hash_function
from ecdhSharedKey import derive_shared_key

SERIAL_PORT = "COM3" #linking to esp32
BAUD_RATE = 115200
TIMEOUT = 1

AES_KEY = derive_shared_key() #although ecc key gen, shared key is aes

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout = TIMEOUT)
print("taking in server room sensor readings ")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print("collected sensor data: ", line)

            #calling on custom hash function
            digest = custom_hash_function(line.encode('utf-8'))
            print("digest: ", digest.hex())

            #calling on encryption
            nonce, ciphertext = encrypt_aes_ctr(AES_KEY, digest)
            print("encrypted: ", ciphertext.hex())

            # calling on decryption
            decrypted = decrypt_aes_ctr(AES_KEY, nonce, ciphertext)
            print("decrypted: ", decrypted.hex())

            #verify
            if decrypted == digest:
                print("decrypted ok")
            else:
                print("not decrypted ")

            time.sleep(1)
except KeyboardInterrupt:
    print("closing connection")
    ser.close()


