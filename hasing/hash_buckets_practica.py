import numpy as np

class hash:
    def __init__(self,tamaño,tamaño_overflow,columnas):
        self.__tamaño=tamaño
        self.__colisiones=0
        self.__tamaño_total=tamaño+tamaño_overflow
        self.__columnas=columnas
        self.__tabla=np.full((self.__tamaño_total,columnas),-1 ,dtype=int)
        self.__indice_overflow=0
        self.__inicio_overflow=tamaño

    def funcion_hash(self,clave):
        return clave % self.__tamaño
    
    def insertar(self,clave):
        indice_bucket= self.funcion_hash(clave)
        for i in range(self.__columnas):
            if self.__tabla[indice_bucket][i] ==-1:
                self.__tabla[indice_bucket][i]=clave
            else:
               if self.__tabla[indice_bucket][i]==clave:
                return
            espacios_overflow= (self.__tamaño_total - self.__tamaño) * self.__columnas
            if self.__indice_overflow < espacios_overflow:
                self.__colisiones+=1
                fila_overflow=self.__inicio_overflow + (self.__inicio_overflow // self.__columnas)
                columnas_overflow= self.__inicio_overflow % self.__columnas
                self.__tabla[fila_overflow][columnas_overflow] = clave
                self.__indice_overflow +=1
    def buscar (self,clave):
        indice_bucket= self.funcion_hash(clave)
        for i in range (self.__columnas):
            if self.__tabla[indice_bucket][i] == clave:
                return ("La clave fue encontrada en el area del bucket")
        filas_usadas_en_overflow= (self.__indice_overflow + self.__columnas-1) // self.__columnas
        for i in range (filas_usadas_en_overflow):
            for j in range (self.__columnas):
                if self.__tabla[self.__inicio_overflow+i][j] ==clave:
                    return ("La clave fue encontrada en el area de Overflow")

