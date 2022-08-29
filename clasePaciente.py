class Paciente:
    __nombre = None
    __dni = None
    __tEspera_cola = None
    __tEspera_especialidad = None
    __tLllegada_cola = None
    __tLlegada_especialidad = None
    def __init__(self, nombre, dni, llegada_cola):
        self.__nombre = nombre
        self.__dni = dni
        self.__tEspera_cola = 0
        self.__tEspera_especialidad = 0
        self.__tLllegada_cola = llegada_cola
    
    def set_tiempo_llegada_especialidad(self, tiempo):
        self.__tLlegada_especialidad = tiempo
    
    def calcular_tiempo_espera_cola(self, tiempo_actual):
        self.__tEspera_cola = tiempo_actual - self.__tLllegada_cola
        return self.__tEspera_cola
    
    def calcular_tiempo_espera_especialidad(self,tiempo_actual):
        self.__tEspera_especialidad = tiempo_actual - self.__tLlegada_especialidad
        return self.__tLlegada_especialidad
    
    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__dni
    
    