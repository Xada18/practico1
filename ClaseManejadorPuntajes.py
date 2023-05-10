from ClasePuntaje import Puntaje
import csv
class ManejadorPuntajes: 
    __puntajes = []
    
    def __init__(self):
        self.__puntajes = []
        
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
    
    def mostrarFederadosporEdadyEstilo(self, edad, estilo, federados):
        for puntaje in self.__puntajes:
            if estilo == puntaje.getEstilo():
                dni = puntaje.getDNI()
                federado = federados.getFederado(dni)
                if federado.getEdad() == edad:
                    print(f"{federado.getApellido()} {federado.getNombre()}, {dni}")
    
    
    def mayorPuntaje(self):
        mayor = self.__puntajes[0]
        for i in range(len(self.__puntajes)):
            if self.__puntajes[i] > mayor:
                mayor = self.__puntajes[i]          
        return mayor
    
    def buscarRepetidos(self, dni, indice, federados):
        ban = False
        while indice < len(self.__puntajes) and not ban:
            if dni == self.__puntajes[indice].getDNI():
                print(federados.getFederado(dni))
                ban = True
            indice+=1
        

    def federadosEstilos(self, federados):
        for i in range(len(self.__puntajes)):
            dni = self.__puntajes[i].getDNI()
            self.buscarRepetidos(dni, i+1, federados)




    def buscarPuntaje(self, dni, i=0):
        pos = -1
        ban = False
        while i < len(self.__puntajes) and not ban :
            if dni == self.__puntajes[i].getDNI():
                pos = i
                ban = True
            else:
                i+=1
        
        return pos

    def mostrarPuntaje(self, dni, estilo, indice=0):

        indice = self.buscarPuntaje(dni, indice)
        
        if indice == -1:
            print("No se encontro ninguna evaluacion")
        else:
            if estilo == self.__puntajes[indice].getEstilo():
                print(f"{self.__puntajes[indice].getPuntaje1():^5}{self.__puntajes[indice].getPuntaje2():^5}{self.__puntajes[indice].getPuntaje3():^5}")
            else:
                indice = self.mostrarPuntaje(dni, estilo, indice+1)

