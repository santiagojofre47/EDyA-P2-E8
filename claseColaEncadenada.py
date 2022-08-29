from ast import Import
from claseNodo import Nodo

class Cola:
    __pr = None
    __ul = None
    __cantidad = None
    
    def __init__(self):
        self.__cantidad = 0
        self.__ul = None
        self.__pr = None
    
    def vacio(self):
        resultado = None
        if self.__cantidad == 0:
            resultado = True
        else:
            resultado = False
        return resultado
    
    def insertar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        
        if self.__ul == None:
            self.__pr = nuevo_nodo
        else:
            self.__ul.setSiguiente(nuevo_nodo)
        
        self.__ul = nuevo_nodo
        self.__cantidad+=1
        
        val = nuevo_nodo.getDato()
        return val
    
    def suprimir(self):
        val = None
        if not self.vacio():
            val = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cantidad-=1
            if self.__pr == None:
                self.__ul = None
        else:
            print('ERROR: pila vacia!')
        return val
            
                   
            