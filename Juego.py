from Jugador import *

class Juego:
    """Clasificar el tipo de juego segun los dados"""

    def __init__(self, Jugador, descripcion): #Constructor de la clase Juego.
        self.Jugador = Jugador
        self.Descripcion = descripcion

    def ListaJuegos(): #Este método devuelve un array de la lista de juegos
        _ListaJuegos = [    # Se crea una variable que contiene los valores del juego     
         'Poker real'    
        ,'Poker cuadruple'
        ,'Full'
        ,'Escalera mayor'
        ,'Escalera menor'
        ,'Tres iguales'
        ,'Pares dobles'
        ,'Pares'] 
       
        return _ListaJuegos; #Returna el array


    def TipoJuego(self): #Método o definición para seleccionar el tipo de juego, según los dados del jugador.

        if(self.Jugador.MisDados.count(self.Jugador.MisDados[0]) == 5): #Condición para el juego Poker Real.
            #return self.Jugador.Nombre + ' tiene un 5 iguales (Poker Real)'
            self.Descripcion = 'Poker real'
            return self

        for i in self.Jugador.MisDados: #Condición para el juego Poker cuádruple.
            if(self.Jugador.MisDados.count(i) == 4):
                 #return self.Jugador.Nombre + ' tiene un 4 iguales (Poker cuádruple)'
                 self.Descripcion = 'Poker cuadruple';
                 return self;

        a = 0
        b = 0
        for i in self.Jugador.MisDados:#Condición para el juego Poker Full.
            if(self.Jugador.MisDados.count(i) == 3):
                a += 1
            if(self.Jugador.MisDados.count(i) == 2):
                b += 1
        if(a == 3 and b == 2):
            #return self.Jugador.Nombre + ' tiene un Full (tres iguales y un par)'
            self.Descripcion = 'Full'
            return self;

        a = 2
        for i in self.Jugador.MisDados:  #Condición para el juego escalera mayor.       
                if(a == i):
                    a+=1
        if(a == 6):
             #return self.Jugador.Nombre + ' tiene una escalera mayor'
             self.Descripcion = 'Escalera mayor'
             return self;

        a = 1
        for i in self.Jugador.MisDados: #Condición para el juego escalera menor.
                
                if(a == i):
                    a+=1
        if(a == 5):
             #return self.Jugador.Nombre + ' tiene una escalera menor'
             self.Descripcion = 'Escalera menor'
             return self;

        a = 0
        for i in self.Jugador.MisDados: #Condición para el juego Triples
             if(self.Jugador.MisDados.count(i) == 3):     
              #return self.Jugador.Nombre + ' tiene 3 iguales (Triples)'
              self.Descripcion = 'Tres iguales'
              return self;

        a =0;
        b =0;
        for i in self.Jugador.MisDados:#Condición para el juego dobles.
              if(self.Jugador.MisDados.count(i) == 2 and i != a):
                 b +=1;
                 a = i;
                 if(b == 2):
                   #return self.Jugador.Nombre + ' Pares dobles (dos pares)'
                   self.Descripcion = 'Pares dobles'
                   return self;

        for i in self.Jugador.MisDados:#Condición para el juego par.
             if(self.Jugador.MisDados.count(i) == 2):
                #return self.Jugador.Nombre + ' tiene un par'
                self.Descripcion = 'Pares'
                return self;

        if(self.Descripcion == None):
            self.Descripcion = 'No tiene puntuacion'
            return self;

        


    def AnalisisJugadoresVirtual(self): #Método para que el jugador virtual pueda analizar
    
        for i in self.Jugador.MisDados:
         if(self.Jugador.MisDados.count(i) == 4):
          for u in self.Jugador.MisDados:   
            if(u != i):          
             return self.Jugador.MisDados.index(u);

    #***********************************************************Analizar tipo de juego Poker Real

          for i in self.Jugador.MisDados:
           if(self.Jugador.MisDados.count(i) == 3):
            for u in self.Jugador.MisDados:   
             if(u != i):          
              return self.Jugador.MisDados.index(u);

    #***********************************************************Analizar tipo de juego Poker Cúadruple    
         a = 0;
         b = 0;
         for i in self.Jugador.MisDados:
           if(self.Jugador.MisDados.count(i) == 2):
               a = i;
           if(self.Jugador.MisDados.count(i) == 2 and a != i):
               b = i
           if(i != a and i != b and self.Jugador.MisDados.count(i) == 1):
               return self.Jugador.MisDados.index(i); 
      
    #***********************************************************Analizar tipo de juego Full
        _escaleraMayor = [2,3,4,5,6]
        b=0;
        c=0;
        d=0;
        for a in self.Jugador.MisDados:
         if(_escaleraMayor[b] == a):
             c = c + 1
         else:
             d = self.Jugador.MisDados.index(a)
         b = b + 1
        if(c == 4):
            return d;
         
        _escaleraMenor = [1,2,3,4,5]
        b=0;
        c=0;
        d=0;
        for a in self.Jugador.MisDados:
         if(_escaleraMayor[b] == a):
             c = c + 1
         else:
             d = self.Jugador.MisDados.index(a)
         b = b + 1
        if(c == 4):
            return d;
          
       
    #***********************************************************Analizar tipo de juego Escaleras menor y mayor  
       
        a = 0
        b = 0
        for i in self.Jugador.MisDados:
         if(self.Jugador.MisDados.count(i) == 2):
          a = i;
         if(self.Jugador.MisDados.count(i) == 1 and i != a):
          return self.Jugador.MisDados.index(i)     
 
    #***********************************************************Analizar tipo de juego tres iguales


         a = 0;
         b = 0;
         for i in self.Jugador.MisDados:
           if(self.Jugador.MisDados.count(i) == 2):
               a = i;
           if(self.Jugador.MisDados.count(i) == 3 and a != i):
               b = i
           if(self.Jugador.MisDados.count(i) == 1):
               return self.Jugador.MisDados.index(i); 
   #***********************************************************Analizar tipo de juego dos pares
        a = 0;
        b = 0;
        for i in self.Jugador.MisDados:
         if(self.Jugador.MisDados.count(i) == 1):
             a = i;
         if(self.Jugador.MisDados.count(i) == 1 and i != a):
             return self.Jugador.MisDados.index(i); 
   #***********************************************************Analizar tipo de juego dos pares     
   
    def DefinirGanador(_listJuegos): #Método que define un jugador
        _nombre = "";
        _ListJ = Juego.ListaJuegos(); #Llena la variable _ListJ con todos los juegos
        _listt = [] #Se variable para retorno de los juegos empates


        _listt = list(filter(lambda x: x.Descripcion == 'No tiene puntuacion',_listJuegos))

        if(len(_listt) == len(_listJuegos)):
         return None;
        
        _listt = [] 
        for a in _ListJ: #Se recorre la lista de juegos
         _listt = list(filter(lambda x: x.Descripcion == a,_listJuegos)) #Se carga en una variable
         if(len(_listt) == 1): #Crea una condicion segun el tamaño del arreglo
          return _listt[0]#Retorna el primer elemento del arreglo de la lista.
         elif(len(_listt) > 1):#Condicion en caso de empate
          for b in _listt:#Se recorre la lista de juegos empates
            _nombre += b.Jugador.Nombre+' ' #Se concatenan el nombre de los jugadores
        _listt[0].Jugador.Nombre = _nombre.strip()#Se quitan los espacios del nombre, para retornar un solo valor
        return _listt[0]; #Retorna el objecto empate

          
     
                


        


    
