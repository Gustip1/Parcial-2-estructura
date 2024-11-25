import numpy as np
import random

class tablaHashBuckets:
    __tamaño:int
    __columnas:int
    __tamañoOverflow:int
    __tabla:np.ndarray
    __colisiones:int
    __indiceOverflow:int
    
    def __init__(self,tamaño,columnas,tamañoOverflow):
        self.__tamaño=tamaño #Cantidad de buckets
        self.__columnas=columnas
        
        #El tamaño total es el tamaño de los buckets mas el tamaño de overflow
        self.__tamañoTotal=tamaño+tamañoOverflow
        
        #Inicializamos el arreglo bidimensional, con las mismas columnas para cada bucket
        self.__tabla= np.full((self.__tamañoTotal,columnas), -1, dtype=int)
        
        #Indice inicial del área de overflow (inicia despues del area primaria)
        self.__inicioOverflow=tamaño
        
        #Para gestionar el siguiente espacio libre en el área de overflow
        self.__indiceOverflow=0
        
        self.__colisiones=0
        
    def funcionHash(self,clave):
        return clave % self.__tamaño
    
    def insertar(self, clave):
        indiceBucket = self.funcionHash(clave)
        
        # Intenta insertar en el área primaria
        for i in range(self.__columnas):
            if self.__tabla[indiceBucket][i] == -1:
                self.__tabla[indiceBucket][i] = clave
                return
            # Evitar duplicados
            elif self.__tabla[indiceBucket][i] == clave:
                return
        
        # Si se llega aquí, el bucket está lleno, insertar en el área de overflow
        totalOverflowEspacios = (self.__tamañoTotal - self.__tamaño) * self.__columnas #Calcula la cantidad de claves que pueden almacenarse en el overflow
        if self.__indiceOverflow < totalOverflowEspacios:
            self.__colisiones += 1
            
            # Insertar clave en el siguiente lugar disponible (se debe llenar de izquierda a derecha, fila por fila)
            filaOv = self.__inicioOverflow + (self.__indiceOverflow // self.__columnas)
            columnaOv = self.__indiceOverflow % self.__columnas
            self.__tabla[filaOv][columnaOv] = clave
            
            # Incrementar el índice de overflow
            self.__indiceOverflow += 1
        else:
            print(f"Área de overflow llena, no se pudo insertar la clave {clave}.")

            
    def buscar(self, clave):
        indiceBucket = self.funcionHash(clave)
        
        # Buscar en el área primaria
        for i in range(self.__columnas):
            if self.__tabla[indiceBucket][i] == clave:
                return True, f"Área primaria, bucket {indiceBucket}, columna {i+1},fila: {}"
        
        # Calcular cuántas filas en el área de overflow han sido utilizadas
        filas_usadas = (self.__indiceOverflow + self.__columnas - 1) // self.__columnas

        # Buscar en el área de overflow
        for i in range(filas_usadas):  # Recorre las filas usadas en el área de overflow
            for j in range(self.__columnas):  # Recorre cada columna
                if self.__tabla[self.__inicioOverflow + i][j] == clave:
                    return True, f"Área de overflow, fila {i+1}, columna {j+1}"
        
        # En caso de no encontrar la clave en el área primaria ni en el overflow:
        return False, None

    
    def mostrarTabla(self):
        print("Área primaria (Buckets):")
        for i in range(self.__tamaño):
            print(f"Bucket {i}: {self.__tabla[i]}")
        
        print("Área de overflow:")
        # Calculamos cuántas filas se han utilizado en el área de overflow
        filas_usadas = (self.__indiceOverflow + self.__columnas - 1) // self.__columnas
        for i in range(filas_usadas):
            print(f"Fila {i+1}: {self.__tabla[self.__inicioOverflow + i]}")


    def mostrarColisiones(self):
        print(f"Total de colisiones: {self.__colisiones}")

# Ejemplo de uso
if __name__ == "__main__":
    tamaño = 10
    columnas = 3  # Máximo 3 elementos por bucket en el área primaria
    tamañoOverflow = 5  # Máximo 5 filas en el área de overflow

    tabla = tablaHashBuckets(tamaño, columnas, tamañoOverflow)

    # Insertar claves
    for _ in range(50):  # Inserta más claves que la capacidad de los buckets
        clave = random.randint(1, 100)
        tabla.insertar(clave)
    
    # Mostrar la tabla
    tabla.mostrarTabla()

    # Buscar una clave
    clave_buscada = 42
    encontrado, ubicacion = tabla.buscar(clave_buscada)
    if encontrado:
        print(f"Clave {clave_buscada} encontrada en {ubicacion}")
    else:
        print(f"Clave {clave_buscada} no encontrada.")

    # Mostrar cantidad de colisiones
    tabla.mostrarColisiones()
