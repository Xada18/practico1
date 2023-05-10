from ClaseFederado import Federado

import csv

class ManejadorFederados:
    __federados: list
    
    def __init__(self):
        self.__federados = []
        
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
    
    def getFederados(self):
        return self.__federados

    def getFederado(self, dni):
        i = 0
        federado = None
        while i < len(self.__federados) and federado == None:
            if dni == self.__federados[i].getDNI():
                federado = self.__federados[i]
            i += 1
        
        return federado
    
    