from ClaseManejadorFederados import ManejadorFederados
from ClaseManejadorPuntajes import ManejadorPuntajes

if __name__ == '__main__':
    
    archivo1 = "federados.csv"
    ListaFederados = ManejadorFederados()
    ListaFederados.carga(archivo1)
    
    archivo2 = "evaluacion.csv"
    ListaPuntajes = ManejadorPuntajes()
    ListaPuntajes.carga(archivo2)
    
    ban = True
    while ban:
        print("Menu")
        print("1 - Federados por estilo y edad")
        print("2 - ")
        print("0 - Salir")
        
        op = input("Ingrese una opcion: ")
        
        
        
        if op == "0":
            ban = False
        elif op == "1":
            estilo = input("Ingrese un estilo: ")
            edad = input("Ingrese una edad: ")
            ListaFederados.mostrarFederadosporEdadyEstilo(edad, estilo, ListaPuntajes)
            
        elif op == "2":
            mayor = ListaPuntajes.mayorPuntaje()
            unFederado = ListaFederados.getFederado(mayor.getDNI())
            print(f"{unFederado.getNombre()}, {unFederado.getApellido()}, {mayor.getEstilo()}, {unFederado.getClub()}")
            

        else:
            print("Opcion no valida")