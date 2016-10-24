#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


def register (line_decod, dicc_usuarios, dicc, client_infor):
    """
    Registro de usuarios
    """
    sip = line_decod.split()[1]
    direccion = sip.split('sip:')[0]
    expiracion = int(line_decod.split()[4])
    dicc_usuarios['address'] = client_infor[0]

    if direccion in dicc:
        dicc[direccion]
    elif '@' in direccion:
        dicc[direccion] = dicc_usuarios
    
    for usuario in dicc:
        dicc[direccion]

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    dicc = {}


    def handle(self):

        dicc_usuarios = {}
        client_infor = self.client_address
        while 1:
            #Lee linea a linea lo que nos manda el cliente
            line = self.rfile.read()
            line_decod = line.decode('utf-8')
            if len(line_decod) >= 2:
                if line_decod.split()[0].upper() == 'REGISTER':
                    register(line_decod, dicc_usuarios, self.dicc, client_infor)
                    self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")       
            print("El cliente nos manda " + line_decod)
            if not line:
                break


if __name__ == "__main__":
    serv = socketserver.UDPServer(("", int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
