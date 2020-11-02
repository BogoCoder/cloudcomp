# PUNTO 8
# This is Samuel
from socket import *
from time import sleep

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

servidorNombre = "127.0.0.1"
servidorPuerto = 12000

clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((servidorNombre,servidorPuerto))

# We are going to use AES for the message encryption
message = b"I love Cloud Computing course :)"
key = os.urandom(32)
iv = b'hey bro, miss ya'

cipher = Cipher(algorithms.AES(key), modes.CBC(iv),backend=default_backend())
encryptor = cipher.encryptor()
encrypted_message = encryptor.update(message) + encryptor.finalize() # We encrypt the message

# We open the private and public key from Samuel (sender), and the public key from Nicolas (receiver)
with open("sam_private_key.pem", "rb") as key_file:
     my_private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
     )

with open("sam_public_key.pem", "rb") as key_file:
     my_public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
     )

with open("nico_public_key.pem", "rb") as key_file:
     public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
     )

# We encrypt our message key with our public key
encrypted_key = public_key.encrypt(
    key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# We sign our message with hash SHA256
signature = my_private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# We send a package with the encrypted key, the encrypted message, and the signature
print("-----PGP-----" + "\n")
package = encrypted_key + b"\t\n" +  encrypted_message + b"\t\n" + signature
clienteSocket.send(package)
print("-----PGP package sent-----" + "\n")
respuesta = clienteSocket.recv(1024)
print(str(respuesta, "utf-8"))
clienteSocket.close()

