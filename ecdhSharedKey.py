from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

def derive_shared_key(): #generate ECC key pairs
    private_key_a = ec.generate_private_key(ec.SECP256R1())
    public_key_a = private_key_a.public_key()

    private_key_b = ec.generate_private_key(ec.SECP256R1())
    public_key_b = private_key_b.public_key()

    shared_secret_a = private_key_a.exchange(ec.ECDH(), public_key_b) #derived shared secret
    shared_secret_b = private_key_b.exchange(ec.ECDH(), public_key_a)

    derived_key_a = HKDF( #key derived from HKD function with symmetric AES 128 key
        algorithm=hashes.SHA256(),
        length=16,
        salt=None,
        info=b'handshake data'
    ).derive(shared_secret_a)

    return derived_key_a
