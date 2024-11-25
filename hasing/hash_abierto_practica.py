class hash_abierto:
    def __init__(self,tamaño):
        self.__tamaño=tamaño
        self.__tabla=[None] * tamaño
        self.__colisiones=0

    def funcion_hash(self,clave):
        return clave %self.__tamaño
    
    def insertar(self,clave):
        posicion= self.funcion_hash(clave)
        posicion_inicial=posicion
        while self.__tabla[posicion_inicial] is not None:
            if self.__tabla[posicion_inicial]==clave:
                return ("ya esta en la tabla se provoco una colision")
            self.__colisiones +=1
            posicion=(posicion+1) % self.__tamaño
            if posicion == posicion_inicial:
                raise Exception ("tabla hash llena")
        self.__tabla[posicion_inicial]= clave

    def buscar(self,clave):
        posicion_incial= self.funcion_hash(clave)
        posicion=posicion_incial
        pasos=1

        while self.__tabla[posicion] is not None:
            if self.__tabla[posicion]==clave:
                return posicion,pasos
            else:
                posicion = (posicion+1) % self.__tamaño
                pasos +=1
            if posicion==posicion_incial:
                return -1
        return -1
    
    