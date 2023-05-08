
class Puntaje:
    __DNI = ""
    __estilo = ""
    __puntaje1 = 0.0
    __puntaje2 = 0.0
    __puntaje3 = 0.0
    
    def __init__(self, dni, estilo, p1, p2, p3):
        self.__DNI = dni
        self.__estilo = estilo
        self.__puntaje1 = p1
        self.__puntaje2 = p2
        self.__puntaje3 = p3
        
    def getDNI(self):
        return self.__DNI
    
    def getEstilo(self):
        return self.__estilo
    
    def getPuntaje1(self):
        return self.__puntaje1
    
    def getPuntaje2(self):
        return self.__puntaje2
    
    def getPuntaje3(self):
        return self.__puntaje3
    
    def __gt__(self, otro):
        promedio1 = (self.__puntaje1 + self.__puntaje2 + self.__puntaje3)/3
        promedio2 = (otro.__puntaje1 + otro.__puntaje2 + otro.__puntaje3)/3
        
        return promedio1 > promedio2
        