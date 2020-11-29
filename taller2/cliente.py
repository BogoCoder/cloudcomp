from socket import *
from time import sleep

servidorNombre = "54.242.109.109" 
servidorPuerto = 12000

def solicitar(tipoSolicitud, cantidad):
    clienteSocket = socket(AF_INET, SOCK_STREAM)
    clienteSocket.connect((servidorNombre,servidorPuerto))
    if tipoSolicitud == 2 or tipoSolicitud == 3:
        solicitud = str(tipoSolicitud)+str(cantidad)
    else:
        solicitud = str(tipoSolicitud)
    clienteSocket.send(bytes(solicitud, "utf-8"))
    respuesta = clienteSocket.recv(1024)
    print(str(respuesta, "utf-8"))
    clienteSocket.close()

print("Solicitar el saldo al servidor.")
solicitar(1,0)
sleep(1)

print("Debitar una cantidad superior al saldo.")
solicitar(2,6000)
sleep(1)

print("Debitar una cantidad inferior al saldo.")
solicitar(2,1000)
sleep(1)

print("Solicitar el nuevo saldo.")
solicitar(1,0)
sleep(1)

print("Acreditar el saldo para duplicarlo.")
solicitar(3,4000)
sleep(1)

print("Acreditar el nuevo saldo.")
solicitar(1,0)
