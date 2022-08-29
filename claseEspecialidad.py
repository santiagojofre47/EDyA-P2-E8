from claseColaSecuencial import ColaSecuencial
from clasePaciente import Paciente

class Especialidad:
    __nombre = None
    __cola = None
    __cant_pacientes = None#Cantidad de pacientes en la cola
    __contador_tiempos_pacientes = None
    __cant_atendidos = None


    def __init__(self, nombre):
        self.__nombre = nombre
        self.__cola = ColaSecuencial(10)
        self.__cant_pacientes = 0        
        self.__contador_tiempos_pacientes = 0
        self.__cant_atendidos = 0
    
    def getCantidadPacientes(self):
        return self.__cant_pacientes
    
    def getNombre(self):
        return self.__nombre
    
    def especialidad_llena(self):
        resultado = None
        if self.__cant_pacientes == 10:
            resultado = True
        else:
            resultado = False
        return resultado
    
    def especialidad_vacia(self):
        resultado = None
        if self.__cant_pacientes == 0:
            resultado = True
        else:
            resultado = False
        return resultado
    
    def agregarPaciente(self, unPaciente,t_actual):
        assert isinstance(unPaciente, Paciente)
        if not self.especialidad_llena():
            unPaciente.set_tiempo_llegada_especialidad(t_actual)
            self.__cola.insertar(unPaciente)
            self.__cant_pacientes+=1
        else:
            print('ERROR: No se pudo agregar al paciente porque no hay mas turnos disponibles!')
  
    
    def atenderPaciente(self,tiempo_actual):
        paciente_atendido = self.__cola.suprimir()
        self.incrementar_contador(paciente_atendido.calcular_tiempo_espera_especialidad(tiempo_actual))
        self.__cant_pacientes-=1
        self.__cant_atendidos+=1
        return paciente_atendido
    
    def incrementar_contador(self,tiempo_espera):
        self.__contador_tiempos_pacientes+=tiempo_espera
    
    def calcular_tiempo_Promedio(self):
        promedio = 0
        if self.__cant_atendidos != 0:
            promedio = self.__contador_tiempos_pacientes/(self.__cant_atendidos)
        return promedio
            