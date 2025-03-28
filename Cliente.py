import socket
import sys

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket al puerto donde el servidor estará escuchando
server_address = ('localhost', 5000)
print('conectando a {} en el puerto {}'.format(*server_address))
sock.connect(server_address)

try:

    while True:
            
            # Solicita mensaje a enviar
            message = bytes(input("Escribe el mensaje a enviar al SERVIDOR:"), 'utf-8')
            print('Enviando {!r}'.format(message))
            sock.sendall(message)

            # buscando respuesta
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                dataRec = sock.recv(16)
                amount_received += len(dataRec)
                print('respuesta recibida {!r}'.format(dataRec))
            
            if dataRec:
                
                if message.decode(encoding="utf-8") == 'DESCONEXION':
                    print("salir")
                    # Cerrando la conexión
                    sock.close()
                    exit()
            else:
                print('En espera de recepción ', client_address)
                break


finally:
    print('Cerrando conexión')
    sock.close()