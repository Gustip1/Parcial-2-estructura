class Nodo:
    def __init__(self,clave):
        self.__clave=clave
        self.__siguiente=None
    
    def getSiguiente(self):
        return self.__siguiente
    
    def SetSiguiente(self,siguiente):
        self.__siguiente=siguiente
    
    def GetClave(self):
        return self.__clave
    
class hash_encadenado:

    def __init__(self,tamaño):
        self.__tabla=[None] * tamaño
        self.__colisiones=0
        self.__tamaño=tamaño
    
    def funcion_hash(self,clave):
        return clave % self.__tamaño

    def insertar(self,clave):
        indice=self.funcion_hash(clave)
        nodo_actual=self.__tabla[indice]
        if nodo_actual is not None:
            self.__tabla[indice]= Nodo(clave)
        else:
            self.__colisiones +=1
            while nodo_actual:
               if nodo_actual.getSiguiente() is None:
                   nodo_actual.setSiguiente(Nodo(clave))
            nodo_actual=nodo_actual.getSiguiente()
               
    def buscar(self,clave):
        indice=self.funcion_hash(clave)
        nodo_actual=self.__tabla[indice]
        pasos= 1
        while nodo_actual is not None:
            if nodo_actual.getClave() ==clave:
                return True,pasos
            pasos+=1
            nodo_actual=nodo_actual.getSiguiente()
        return -1
    
    

