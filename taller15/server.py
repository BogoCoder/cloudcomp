# PUNTO 8
# This is Nicolas

from socket import *

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Connected to ", clienteDireccion)
    package = conexionSocket.recv(1024)
    print("Package received from", clienteDireccion)
    #print(message)

    # We split our package to extract the different elements
    splitted = package.split(b"\t\n")

    # The elements of the package
    encrypted_key = splitted[0]
    encrypted_message = splitted[1]
    signature = splitted[2]

    # We open the Nicolas private key (we assume he is the only one that has access to it)
    with open("nico_private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # We decrypt the key with the Nicolas the private key
    key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # We decrypt the message with the decrypted key
    iv = b'hey bro, miss ya'
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv),backend=default_backend())
    decryptor = cipher.decryptor()
    message = decryptor.update(encrypted_message) + decryptor.finalize()

    # We open the public key from Samuel
    with open("sam_public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    # We verify the sender and integrity of the message
    verification = public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Verified sender: Samuel")
    print("Message decrypted: " + str(message, "utf-8"))
    
    respuesta = "-----PGP package received-----" + "\n"
    respuesta = respuesta+'\n'
    conexionSocket.send(bytes(respuesta, "utf-8"))
    conexionSocket.close()