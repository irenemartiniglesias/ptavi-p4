#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP simple
"""

import socket
import sys

#Información del servidor
SERVER = sys.argv[1]
PORT = int(sys.argv[2])

#Lo que vamos a enviar
LISTA = sys.argv[3:]
LINE = ' '.join(LISTA)

if LINE.split()[0] == 'REGISTER':
	if '@' in LINE.split ()[1]:
		Line_sip = " sip:" + LINE.split()[1] + 'SIP/2.0\r\n\r\n'


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket: 

    my_socket.connect((SERVER, PORT))
   
    
    print("Enviando:" + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")


