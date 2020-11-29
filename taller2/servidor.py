from socket import *

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    solicitud = str( conexionSocket.recv(1024), "utf-8" )
    with open('saldo.txt','r+') as archivo:
        saldo = int(archivo.read())
        if solicitud == '1':
            print('El cliente consulta su saldo actual')
            respuesta = str(saldo)
        elif solicitud[0] == '2':
            cantidad = int(solicitud[1:])
            print('El cliente desea debitar',cantidad)
            if saldo > cantidad:
                respuesta = 'OK'
                archivo.seek(0)
                archivo.write(str(saldo-cantidad))
            else:
                respuesta = 'Saldo insuficiente'
        elif solicitud[0] == '3':
            cantidad = int(solicitud[1:])
            print('El cliente desea acreditar',cantidad)
            respuesta = 'Nuevo saldo: ' + str(saldo+cantidad)
            archivo.seek(0)
            archivo.write(str(saldo+cantidad))
        else: respuesta = 'Opción no válida.'
    respuesta = respuesta+'\n'
    print(respuesta)
    conexionSocket.send(bytes(respuesta, "utf-8"))
    conexionSocket.close()