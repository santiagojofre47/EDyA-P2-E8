import random
import numpy as np
from claseEspecialidad import Especialidad
from clasePaciente import Paciente
from claseColaEncadenada import Cola

if __name__ == '__main__':
    lista_nombres = ['Ginecologia','Clinica Medica', 'Oftalmologia', 'Pediatria']
    manejadorEspecialidades = np.empty(4,dtype = Especialidad)
    for i in range(4):#Se inicializan las 4 especialidades antes de comenzar la simulacion
        manejadorEspecialidades[i] = Especialidad(lista_nombres[i])
    
    #Se inicializa la cola de turnos y las demas variables
    cola_turnos = Cola()
    F_Pacientes = 1
    contador_tAtencion = 0
    atencion_medicos = 0
    cant_pacientes_cola = 0
    cant_pacientes_atendidos = 0
    tiempos_espera_pacientes = 0 #Contador de los tiempo de espera de todos los pacientes en la cola
    tiempos_espera_especialidad = 0 #Contador de los tiempos de espera de los pacientes en la cola de cada especialidad
    i = 0
    while i<=4*60:
        if 1/F_Pacientes > 1/(random.randint(1, 3)):
            print('Minuto {}: Ha llegado un paciente!'.format(i))
            nombre = input('Ingrese el nombre del paciente: ')
            dni = input('Ingrese el dni del paciente: ')
            paciente = Paciente(nombre, dni,i)
            cola_turnos.insertar(paciente)
            cant_pacientes_cola+=1
        
        if i <= 60:
            contador_tAtencion+=1
            if contador_tAtencion == 2:
                if not cola_turnos.vacio():
                    paciente_atender = cola_turnos.suprimir()
                    print('Hola {} elija la especialidad a la que desea obtener el turno: '.format(paciente_atender.getNombre()))
                    print('1- Ginecologia\n2-Clinica Medica\n3-Oftamologia\n4-Pediatria')
                    numero = int(input('Ingrese una opcion: '))
                    while  numero < 1 or numero > 4:
                        print('ERROR: Entrada invalida, no se guardara el turno!')
                        numero = int(input('Ingrese una opcion: '))
                    if not manejadorEspecialidades[numero-1].especialidad_llena():
                        manejadorEspecialidades[numero-1].agregarPaciente(paciente_atender,i)
                        contador_tAtencion = 0
                        cant_pacientes_atendidos+=1
                        tiempos_espera_pacientes+=paciente_atender.calcular_tiempo_espera_cola(i)
                    else:
                        contador_tAtencion = 0
                else:
                    contador_tAtencion = 0
        else:
            #Se comienzan a atender los turnos despues de las 8
            atencion_medicos +=1
            if atencion_medicos == 20:
                atencion_medicos = 0
                for j in range(4):
                    if not manejadorEspecialidades[j].especialidad_vacia():
                        print('Minuto {}: Se atedio a un paciente en la especialidad {}'.format(i,manejadorEspecialidades[j].getNombre()))
                        paciente_atendido = manejadorEspecialidades[j].atenderPaciente(i)
                        print('Nombre del paciente: {}'.format(paciente_atendido.getNombre()))
        i+=1
    #---------------------------------##
    print('--- \tSimulacion finalizada \t---')
    if cant_pacientes_atendidos != 0:
        print('Tiempo de espera promedio de los pacientes en la cola de turno: {0: .2f} minutos'.format(tiempos_espera_pacientes/cant_pacientes_atendidos))
    else:
        print('No hubieron pacientes atedidos!')

    print('--- \tTiempos promedio de espera en la cola de cada especialidad \t---')
    for k in range(4):
        print('Promedio en la especialidad {}: {} minutos'.format(manejadorEspecialidades[k].getNombre(),manejadorEspecialidades[k].calcular_tiempo_Promedio()))
    print('Cantidad de pacientes que no pudieron obtener turno: {}'.format(cant_pacientes_cola-cant_pacientes_atendidos))
