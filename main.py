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
        print("1 - Patinadores federados por estilo y edad")
        print("2 - Patinador federado con mayor puntaje")
        print("3 - Patinadores federados que participaron en los 2 estilos")
        print("4 - Mostrar puntaje de un patinador en un esilo")
        print("0 - Salir")
        
        op = input("Ingrese una opcion: ")
        
        if op == "0":
            ban = False

        elif op == "1":
            estilo = input("Ingrese un estilo: ")
            edad = input("Ingrese una edad: ")
            ListaPuntajes.mostrarFederadosporEdadyEstilo(edad, estilo, ListaFederados)
            
        elif op == "2":
            mayor = ListaPuntajes.mayorPuntaje()
            unFederado = ListaFederados.getFederado(mayor.getDNI())
            print(f"{unFederado.getNombre()}, {unFederado.getApellido()}, {mayor.getEstilo()}, {unFederado.getClub()}")
        
        elif op == "3":
            ListaPuntajes.federadosEstilos(ListaFederados)

        elif op == "4":
            dni = input("Ingrese un DNI: ")
            estilo = input("Ingrese un estilo: ")
            ListaPuntajes.mostrarPuntaje(dni, estilo)
           
        else:
            print("Opcion no valida")
        
        print("")