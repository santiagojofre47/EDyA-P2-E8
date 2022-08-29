class Nodo:
    __elemento = None
    __siguiente = None
    
    def __init__(self, elemento):
        self.__elemento = elemento
        self.__siguiente = None
    
    def setSiguiente(self, sig):
        self.__siguiente = sig
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__elemento
