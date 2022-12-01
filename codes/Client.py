import threading 
import sys
import socket
import pickle
import os

class Client():
    
    def __init__(self, host = input("Inserte la IP del Servidor "), port = int(input("Inserte el Puerto del Servidor")),nickname = input ("Inserte su nickname ")):
        self.s = socket.socket()
        self.s.connect((host, int (port)))
        self.enviar('$' + nickname)
        print('\n\tProceso con PID = ', os.getpid(), '\n\tHilo Principal con ID = ', threading.currentThread().getname(),'\n\tHilo en modo Daemon =', threading.currentThread().isDaemon(),'\n\tTotal Hilos Activos en este punto del programa = ', threading.active_count())
        threading.Thread(target = self.recibir, daemon = True).start()
        
        While True:
            msg = input('\nEscribe texto? ** Enviar ** salir = 1 \n')
            if msg != '1':self.enviar(msg)
            else:
                print(" Me piro van piro; cierro el socket y mato al cliente con PID = ", os.getpaid())
                self.s.close()
                sys.exit()
                
    def recibir(self):
        print('\nHilo recibir con ID =',threading.currentThread().getname(), '\n\tPertenece al proceso con PID', os.getpaid(), "\n\tHilos activos Totales", threading.active_count())
        while True:
            try:
                
                data = self.s.recv(32)
                if data: print(pickle.loads(data))
            except:pass
        
    def enviar(self, msg):
        self.s.send(pickle.dumps(msg))
        
arrancar = Cliente()