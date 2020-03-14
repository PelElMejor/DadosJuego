import os 
import time
from Juego import *
from Jugador import *




class Estadisticas:
    

     def __init__(self, Juego, fecha, hora): #Constructor de la clase
         self.Nombre = Juego.Jugador.Nombre
         self.TipoJuego = Juego.Descripcion
         self.fecha = fecha
         self.hora = hora

     def CrearArchivo(self):#Método para crear el archivo
        _ListJuegos = Juego.ListaJuegos(); #Llama y llena la variable con la lista de juegos
        _EstadList = [] #Se crea una lista de tipo de list


        _root = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') #Se llena la variable para obtener la ruta del escritorio del usuario actual del sistema operativo
        _path = _root +'\\DadosPokerFolder'+ '\\DadosPokerFile.txt'# Construye una ruta para el archivo

        if(os.path.isfile(_path) == False):#Valida sí el archivo existe
            os.makedirs(_root + '\\DadosPokerFolder'); #Construye un folder
            _path = _root + '\\DadosPokerFolder'+ '\\DadosPokerFile.txt' #Construye una ruta completa
            file = open(_path,'w') #Construye un archivo con la ruta y la acción en este caso "W"
     

        file = open(_path,'r') #lee el archivo
        _cont = file.read() #Almacena el contenido del archivo en una variable
        _count = 0 #Variable que funcionara como contador
        
        self.fecha = time.strftime("%d/%m/%Y") #Variable para almacenar la fecha
        self.hora = time.strftime("%I:%M:%S") #Variable para almacenar la hora
        
        
        _EstadList.append(self) #Alamacena en una variable de tipo list todos los jugadores
        
        if(len(_cont) > 1): #Validacion para sacar solo las lineas que contengan información
         for a in _cont.split('\n'):
           b = a.split('\t')
           if(len(b) > 1):
            _EstadList.append(Estadisticas(Juego(Jugador(b[1],None,0),b[2]), b[3], b[4])) #Crea un objecto de tipo Estadistica para almacenarlos en un list con los datos del archivo
           else:
            break;
        
        if(len(_EstadList) == 11): #Valida que no existan mas de 10 jugadores, de lo contrario borrará el último
            del(_EstadList[10])

        file = open(_path,'w')# Escribe sobre el archivo
        for b in _ListJuegos: #Estos for recorren los jugadores y la lista de juegos para ordenarlos.
          for c in _EstadList:
              if(b == c.TipoJuego):    
               _count = _count +1;          
               file.write(str(_count)+ '.' + '\t' +c.Nombre + '\t' + c.TipoJuego + '\t' + c.fecha + '\t' + c.hora +"\n") #Estructura para guardar en el archivo
        file.close()#Cierra el archivo
    
     def MostrarEstadisticas(): #Método para mostrar en pantalla el archivo
       _path = _root = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\DadosPokerFolder'+ '\\DadosPokerFile.txt' #Ruta para cargar el archivo

       if(os.path.isfile(_path) == False):#Valida que exista el archivo
           return 'No existe el archivo'

       file = open(_path,'r')#Lectura del archivo
       _cont = file.read()#Lee el contenido del archivo

       return _cont #Devuelve lo cargado en el archivo

