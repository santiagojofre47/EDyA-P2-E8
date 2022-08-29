import numpy as np
from clasePaciente import Paciente
class ColaSecuencial:
    __arreglo = None
    __pr = None
    __ul = None
    __max = None
    __cant = None

    def __init__(self, tamanio = 10):
        self.__arreglo = np.empty(tamanio,dtype=Paciente)
        self.__max = tamanio
        self.__pr = 0
        self.__ul = 0
        self.__cant = 0
    
    def vacia(self):
        resultado = None
        if self.__cant == 0:
            resultado = True
        else:
            resultado = False
        return resultado
    
    def insertar(self, x):
        valor = None
        if self.__cant < self.__max-1:
            self.__arreglo[self.__ul] = x
            self.__ul = (self.__ul+1)%self.__max
            self.__cant+=1
            valor = x
        else:
            print('ERROR: Cola llena!')
            valor = 0
        return valor
    
    def suprimir(self):
        valo = None
        if not self.vacia():
            valor = self.__arreglo[self.__pr]
            self.__pr = (self.__pr+1)%self.__max
            self.__cant-=1
        else:
            print('ERROR: Cola vacia!')
            valor = 0
        return valor
    
    def recorrer(self):
        if not self.vacia():
            i = self.__pr
            j = 0
            while j <= self.__cant-1:
                print('Elemento: {}' .format(self.__arreglo[i]))
                i = (i+1)%self.__max
                j+=1
        else:
            print('ERROR: Cola vacia!')


            

