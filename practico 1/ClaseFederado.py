class Federado:
    __apellido = ""
    __nombre = ""
    __DNI = ""
    __edad = ""
    __club = ""
    
    def __init__(self, apellido, nombre, dni, edad, club):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__DNI = dni
        self.__edad = edad
        self.__club = club
        
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__DNI
    
    def getEdad(self):
        return self.__edad
    
    def getClub(self):
        return self.__club
    
        
    
        