from ClaseFederado import Federado

import csv

class ManejadorFederados:
    __federados = []
    
    def __init__(self):
        __federados = []
        
    def carga(self, file):
        archivo = open(file, "r")
        reader = csv.reader(archivo, delimiter=";")
        
        for line in reader:
            apellido = line[0]
            nombre = line[1]
            DNI = line[2]
            edad = line[3]
            club = line[4]
            federado = Federado(apellido, nombre, DNI, edad, club)
            self.__federados.append(federado)
            
    def getFederado(self, dni):
        i = 0
        federado = None
        while i < len(self.__federados) and federado == None:
            if dni == self.__federados[i].getDNI():
                federado = self.__federados[i]
            i += 1
        
        return federado
            
    def mostrarFederadosporEdadyEstilo(self, edad, estilo, puntajes):
        dnis = []

        
        for puntaje in puntajes.getPuntajes():
            if estilo == puntaje.getEstilo():
                dnis.append(puntaje.getDNI())
                
        i = 0
        j = 0
        for i in range(len(self.__federados)):
            for j in range(len(dnis)):
                if dnis[j] == self.__federados[i].getDNI():
                    if edad == self.__federados[i].getEdad():
                        print(f"{self.__federados[i].getNombre()}, {self.__federados[i].getApellido()}, {self.__federados[i].getDNI()}")
    
        
            
    
        
    
    