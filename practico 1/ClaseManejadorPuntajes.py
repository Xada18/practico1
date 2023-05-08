from ClasePuntaje import Puntaje
import csv
class ManejadorPuntajes: 
    __puntajes = []
    
    def __init__(self):
        __puntajes = []
        
    def carga(self, file):
        archivo = open(file, "r")
        reader = csv.reader(archivo, delimiter=";")
        
        for line in reader:
            DNI = line[0]
            estilo = line[1]
            puntaje1 = float(line[2])
            puntaje2 = float(line[3])
            puntaje3 = float(line[4])
            puntaje = Puntaje(DNI, estilo, puntaje1, puntaje2, puntaje3)
            self.__puntajes.append(puntaje)
            
    def getPuntajes(self):
        return self.__puntajes
    
    def mayorPuntaje(self):
        i = 0
        mayor = self.__puntajes[0]
        for i in range(len(self.__puntajes)):
            if self.__puntajes[i] > mayor:
                mayor = self.__puntajes[i]          
        return mayor
    

            
            

        
            
    
                
                
