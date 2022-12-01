import socket
import threading
import sys 
import pickle
import os 


class Server():
    
    def __init__(self, host = socket.gethostname(), port = int(input("Introduzca el Puerto que quiere usar "))):
        self.clientes = []
        self.nickname = []
        print('\nSu IP actual es: ', socket.gethostbyname(host))
        print('\n\tProceso con PID = ', os.getpid(), '\n\tHilo principal con ID =', threading.current_thread().getname(), '\n\tHilo en modo Daemon= ', threading.current_thread().isDaemon(), '\n\tTotal Hilos activos en este punto del programa =', threading.active_count())
        self.s = socket.socket()
        self.s.bind((str(host), int (port)))
        self.s.listen(30)
        self.s.setblocking(False)
        
        threading.Thread(target = self.aceptarC, daemon = True).start()
        threading.Thread(target = self.procesarC, daemon = True).start()
        
        while True:
            msg = input ('\n <<Salir = 1>> \n')
            if msg == '1':
                print("*** me piro van piro ; cierro socket y mato Server con PID =", os.getpid())
                self.s.close()
                sys.exit()
            else:
                pass
            
    def aceptarC (self):
        print('\nHilo aceptar con ID=', threading.currentThread().getname(), '\n\tHilo en modo Daemon=', threading.currentThread().isDaemon(), '\n\tPertenece al proceso con PID', os.getpid(), "\n\tHilos activos Totales", threading.active_count())
        
        while True:
            try:
                conn, adr = self.s.accept()
                print(f"\nConexion aceptada via {addr}\n")
                conn.setblocking(False)
                self.clientes.append(conn)
            except:
                pass
            
    def procesarC(self):
        print('\nHilo procesar con ID =', threading.current_Thread().getname(), '\n\tHilo modo Daemon =',threading.current_Thread().isDaemon(), '\n\tPertenece al proceso con PID', os.getpid(),"\n\tHilos activos Totales", threading.active_count())
        while True:
            if len(self.clientes)> 0:
                for c in self.clientes:
                    try:
                        data = c.recv(32)
                        mensaje = pickle.loads(data)
                        if mensaje.startswith(mensaje):
                            self.nicknames.append(mensaje)
                        if data: self.broadcast(data, c)
                    except:
                        pass
                    
    def broadcast (self, msg,cliente):
        for c in self.clientes:
            print("Clientes connectados ahora = ", len(self.clientes))
            print(*self.nicknames, sep = "\n")
            try:
                if len(self.nicknames) > 0:
                    for x in self.clientes:
                        if x == cliente:
                            numero = self.clientes.index(x)
                    mensajeconnick = self.nicknames[numero] + ": " + pickle.loads(msg)
                    print(mensajeconnick)
                    c.send(pickle.dumps(mensajeconnick))
                    with open ('22140379.txt', 'a') as f:
                        f.write('\n' + mensajeconnick)
            except:
                self.clientes.remove(c)
                
arrancar = Server()