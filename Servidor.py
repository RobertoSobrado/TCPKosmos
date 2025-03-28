import socket
import sys

# Creando socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vinculando el socket al puerto
server_address = ('localhost', 5000)
print('Levantando el puerto {} port {}'.format(*server_address))
sock.bind(server_address)

# Escuchando las conexiones entrantes
sock.listen(1)

while True:
    # Esperando conexión del cliente
    print('Esperando conexión del cliente')
    connection, client_address = sock.accept()
    try:
        print('Conexión desde', client_address)

        # Recibiendo la transmisión y regresando el mensaje
        while True:
            data = connection.recv(16)
            print('Recibido {!r}'.format(data))
            print(data.decode(encoding="utf-8"))
            if data:
                print('Regresando el mensaje al cliente')
                dataSend = data.decode(encoding="utf-8").upper()
                dataSend = bytes(dataSend, 'utf-8')
                print(dataSend)
                connection.sendall(dataSend)
                
                if data.decode(encoding="utf-8") == 'DESCONEXION':
                    print("salir")
                    # Cerrando la conexión
                    connection.close()
                    exit()
            else:
                print('En espera de recepción ', client_address)
                break

    finally:
        # Cerrando la conexión
        connection.close()