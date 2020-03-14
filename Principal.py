import os
from Jugador import *
from random import  randint
from Juego import *
from Estadisticas import *


#********Variables Globales
_ListJuegos = [] #Se crea una varible que estará presente en todo el archivo principal
_numeroJugadores = 0
_numeroJugadoresVirtuales = 0
_numeroJugadoresHumanos = 0
_JugadoresList = []

#********Definiciones

def Limpiar():
  # _ListJuegos = [] #Se crea una varible que estará presente en todo el archivo principal
   _numeroJugadores = 0
   _numeroJugadoresVirtuales = 0
   _numeroJugadoresHumanos = 0
   _varJuego = None
   _JugadoresList.clear()
   _JugadoresList.clear()
   

def ValidacionMenu(op):
    if(op != '1' and op != '2' and op != '3'):
      print('Debe de seleccionar una opcion que se muestra en pantalla')
      InicioJuego()

def ValidacionNumeroJugadores(numJ): #Valida tanto letras como numeros fuera del rango 
     numJ = numJ  
     _letter = None
     if(numJ.isdigit() == False):
       MostrarTitulo()
       print('El valor ingresado no es un numero')
       numJ = ValidacionNumeroJugadores(input("Por favor ingrese el numero de jugadores: "))
     numJ = int(numJ)
     if(numJ == 1 or numJ > 5):   
       MostrarTitulo()
       print('El numero de jugadores virtuales tienen que ser menores a ' + str(_numeroJugadores))   
       numJ = ValidacionNumeroJugadores(input("Por favor ingrese el numero de jugadores: "))   
     print('\n')    
     return numJ

def ValidacionNumeroJugadoresVirtuales(numJ, numJT): 
     numJ = numJ  
     _letter = None
     if(numJ.isdigit() == False):
       MostrarTitulo()
       print('El valor ingresado no es un numero')
       numJ = ValidacionNumeroJugadoresVirtuales(input("Por favor ingrese el numero de jugadores: "), numJT)
     numJ = int(numJ)
        
     if(numJ >= numJT):   
       MostrarTitulo()
       print('El numero de jugadores virtuales no pueden ser mayor al numero de jugadores totales')   
       numJ = ValidacionNumeroJugadoresVirtuales(input("Por favor ingrese el numero de jugadores virtuales: "), numJT)   
     print('\n')    
     return numJ    

def Validacion_S_N(st):
    if(st == 'S'):
        st == 's'
    if(st == 'N'):
         st == 'n'
     #if(st != 'n' or st != 's'):


def CrearJuego(_JugadoresList): #Este método inicia el juego creando los dados por jugador
       for e in _JugadoresList:    #Recorre todos los jugadores
           _MisDados = []

           i = 1
           while i <= 5:
               _MisDados.append(randint(1,6)) #Genera numeros del 1 al 6 de forma aleatoria
               i+=1
           e.MisDados = _MisDados                  

def Jugar(_JugadoresList): #Recibe un list de todos los jugadores
    MostrarTitulo() #Se creó un método para mostrar el titulo
    _ListJuegos.clear()
   
    for e in _JugadoresList: #Se recorre todo los jugadores con sus respectivos dados ya generados.
     a = 0
     print('Los dados de ' + e.Nombre + ' son: ') #Muestra el nombre jugador.
     for u in e.MisDados:
      a+=1
      print('Dado [' + str(a) + '] es: ' + str(u)) #Muestra los dados de cada jugador.
     _varJuego = Juego(e,None).TipoJuego() #Devuelve el tipo de juego que tiene cada jugador
     _ListJuegos.append(_varJuego) #Llena la variable de tipo array
     print(_varJuego.Descripcion) #Muestra el juego que ha obtenido cada jugador
     print('\n')  
   

def RelanzarDados(_JugadoresList): #Definicion para relanzar los dados
    
    print('\n')
   
    if(input('Para reelanzar algun dado por favor ingrese (s / n): ') == 's'): #Input para preguntar sí quiere lanzar algún dado de demás.
        for i in _JugadoresList: #Recorre una list de jugadores
          if(i.Tipo == 1):
            a = 0
            os.system('cls')
            if(input('Desea ' + i.Nombre + ' reemplazar algun dado? (s / n): ') == 's'): #Pregunta por nombre de cada jugador sí le interesa lanzar algun dado
             print('Los dados de ' + i.Nombre + ' son:') #Muestra los dados de cada jugador
             for e in i.MisDados:
                 a+=1
                 print('Dado [' + str(a) + '] es: ' + str(e))
             
             print('\n')
             _varDadoCambiar = input('Cual dado desea cambiar? ') #Regenera un dado que seleccionó el jugador a cambiar
             i.MisDados[int(_varDadoCambiar) - 1] = randint(1,6)
            else:
                continue
          else:
              _indexDado = Juego(i, None).AnalisisJugadoresVirtual() #Para los jugadores de tipo virtual crea un analisis para mover un dado
              i.MisDados[_indexDado] = randint(1,6)
    else:
        return False


def MostrarTitulo():#Metodo para mostrar un menu
   os.system('cls')
   print('ICO-TEC, CURSO TALLER I GRP2')
   print('Bienvenido al poker de dados Python')       
   print('\n')

 
   
#***********Inicio del programa
def InicioJuego():
    MostrarTitulo()     
    
    
    print('------------------')
    print('Menu principal')
    print('------------------')
          
          
    print('\n')
          
    print('1 Iniciar el juego')
          
    print('\n')
          
          
    print('2 Mostrar estadisticas')
          
    print('\n')
          
    print('3 Salir')
          
    print('\n')
    OpcionesJuego()

def OpcionesJuego():
    opcion = input('Por favor, digite una opcion: ') #Menú a mostrar
    ValidacionMenu(opcion)
    
    if(opcion == '1'):   #Opciones del menú
        
         MostrarTitulo() #Mostrar un titulo
        
    
       
         _numeroJugadores = ValidacionNumeroJugadores(input('Por favor ingresar el numero de jugadores: '))
         _numeroJugadoresVirtuales = ValidacionNumeroJugadoresVirtuales(input("De estos jugadores, cuantos son virtuales: "),_numeroJugadores)

        # _numeroJugadoresVirtuales = int(input("De estos jugadores, cuantos son virtuales: ")) #Jugadores virtuales
         _numeroJugadoresHumanos = _numeroJugadores - _numeroJugadoresVirtuales #Cálculo para los jugadores humanos.
    
         MostrarTitulo()
         print('Definir el nombre para los jugadores')
    
         _JugadoresList = [] #Arrays para crear la lista de jugadores
    
         i = 1
    
         while i <= _numeroJugadoresHumanos: #Muestra el nombre de los jugadores humanos, se construye un objecto solo con
                                             #el nombre.
              _JugadoresList.append(Jugador(input('Nombre del jugador ' + str(i) + ': '), 'Prueba', 1))         
              i += 1
    

         i = 1
         while i <= _numeroJugadoresVirtuales:#Muestra el nombre de los jugadores virtuales, se construye un objecto solo con
                                              #el nombre.
              _JugadoresList.append(Jugador('Virtual_' + str(i), 'Prueba', 0))        
              i += 1   
    
         os.system('cls') #Comando para limpiar en consola
         CrearJuego(_JugadoresList) #Se ejecuta el metodo CrearJuego y que por parametro lleva la lista de
                                    #jugadores
        
         Jugar(_JugadoresList)
         if(RelanzarDados(_JugadoresList) != False): #Se ejecuta sí los jugadores lanzan de nuevo algún dado
            Jugar(_JugadoresList)#Se juega ya con los dados lanzados
         _Ganador = Juego.DefinirGanador(_ListJuegos) #Metodo para definir un ganador del juego, utilizando la clase de tipo Juego

         if(_Ganador != None):
          if(len(_Ganador.Jugador.Nombre.split(' ')) == 1):
            print('Ganador : ' + _Ganador.Jugador.Nombre + ' con ' + _Ganador.Descripcion) #Muestra el ganador del juego   
          elif(len(_Ganador.Jugador.Nombre.split(' ')) > 1):
            print('Juego empate : ' + _Ganador.Jugador.Nombre + ' con ' + _Ganador.Descripcion) #Muestra el ganador del juego
          Estadisticas(_Ganador, None, None).CrearArchivo() #Llama la clase Estadisticas, al método Crear Archivo donde mete a lista de                                                      #jugadores
         else:
           print('No hay ganadores')
         RetornoMenu()#Regresa al juego.
         
           
    if(opcion == '2'): #Opcion para mostrar en estadisticas
         MostrarTitulo() #Muestra el titulo
         print(Estadisticas.MostrarEstadisticas()) #Inprime en consola las estadisticas de los estudiantes
         RetornoMenu()#Regresa al menu
    
     
    if(opcion == '3'): #Opcion para salir del programa
         os.system('exit()') #Comando para salir del programa
        
def RetornoMenu(): #Se creaa un metodo para retornar al juego
    print('\n')
    if(input('Desea regresar al menu (s / n): ') == 's'):
        Limpiar()
        InicioJuego()
    else:
        os.system('exit()')

InicioJuego()

    
           