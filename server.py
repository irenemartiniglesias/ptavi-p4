#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json
from time import time, gmtime, strftime


def register (line_decod, dicc_usuarios, dicc, client_infor):
    """
    Registro de usuarios
    """
    sip = line_decod.split()[1]
    direccion = sip.split('sip:')[0]
    expiracion = int(line_decod.split()[4])
    expira = int(time()) + expiracion
    dicc_usuarios['address'] = client_infor[0]
    
    #coje el dia al que estamos y la hora y lo almacena en tiempo_ahora
    tiempo_ahora = int(time())
    strf_ahora = strftime('%Y-%m-%d %H:%M:%S', gmtime(tiempo_ahora))
    tiempo_expira = expiracion + tiempo_ahora
    strf_expira = strftime('%Y-%m-%d %H:%M:%S', gmtime(tiempo_expira))
    
 
    dicc_usuarios["expira"] = strf_expira + ' + ' + str(expiracion)

    if expiracion == 0:
        if direccion in dicc:
            del dicc[direccion]
    elif '@' in direccion:
        dicc[direccion] = dicc_usuarios
    
    for usuario in dicc:
        if int(time())> expira:
            deldicc[direccion]

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
                    self.register2json()
            print("El cliente nos manda " + line_decod)
            
            if not line:
                break
                
    def register2json(self):
        """
        Registro de los usuarios en un json
        """
        fichero_json= json.dumps(self.dicc)
        with open ('registro.json', 'w') as fichero_json:
            json.dump(self.dicc, fichero_json, sort_keys = True, indent = 4)


    def json2register(self):
        """
        Comprobacion de si existe el fichero json
        """
        fichero_json = 'registro.json'
        try:
            sself.dicc = json.loads(open(fichero_json).read())
        except:
            self.dicc = {}


if __name__ == "__main__":
    serv = socketserver.UDPServer(("", int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
