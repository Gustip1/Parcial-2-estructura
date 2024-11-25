import random 

class Nodo: 
    __clave: object
    __siguiente: object

    def __init__(self, clave):
        self.__clave = clave
        self.__siguiente = None
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente  
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getClave(self):
        return self.__clave
    
class TablaHash:
    def __init__(self, tamaño):
        self.__tamaño = tamaño
        self.__tabla = [None] * tamaño
        self.__colisiones = 0  # Contador de colisiones

    def funcion_hash(self, clave):
        """Función hash utilizando el método de la división."""
        return clave % self.__tamaño
    
    def get_colisiones(self):
        """Devuelve el número total de colisiones ocurridas."""
        return self.__colisiones
    
    def insertar(self, clave):
        """Inserta una clave en la tabla hash, usando encadenamiento si hay colisión."""
        indice = self.funcion_hash(clave)
        nodo_actual = self.__tabla[indice]

        # Si no hay colisión, insertamos directamente
        if nodo_actual is None:
            self.__tabla[indice] = Nodo(clave)
            return
        else:
            # Si hay colisión, usamos encadenamiento
            self.__colisiones += 1
            while nodo_actual:
                # Si la clave ya existe, no hacemos nada
                if nodo_actual.getClave() == clave:
                    return
                # Si alcanzamos el final de la lista encadenada, agregamos el nodo
                if nodo_actual.getSiguiente() is None:
                    nodo_actual.setSiguiente(Nodo(clave))
                    return
                nodo_actual = nodo_actual.getSiguiente()
    
    def buscar(self, clave):
        """Busca una clave en la tabla hash y devuelve si la encontró y el número de pasos."""
        indice = self.funcion_hash(clave)
        nodo_actual = self.__tabla[indice]
        pasos = 0

        # Recorremos la lista encadenada en busca de la clave
        while nodo_actual:
            pasos += 1
            if nodo_actual.getClave() == clave:
                return True, pasos
            nodo_actual = nodo_actual.getSiguiente()
        return False, pasos

def generar_claves(num_claves, rango_maximo):
    """Genera una lista de claves numéricas aleatorias."""
    return [random.randint(0, rango_maximo) for _ in range(num_claves)]

def calcular_promedio_pasos(tabla_hash, claves):
    """Calcula el promedio de pasos al buscar todas las claves en la tabla."""
    pasos_totales = 0
    for clave in claves:
        _, pasos = tabla_hash.buscar(clave)
        pasos_totales += pasos
    promedio_pasos = pasos_totales / len(claves)
    return promedio_pasos

def main():
    num_claves = 1000
    rango_maximo = 100000

    # Generamos las 1000 claves aleatorias
    claves = generar_claves(num_claves, rango_maximo)

    # Caso 1: Tamaño de la tabla no primo
    m_no_primo = 1000  # 1000 no es primo
    tabla_no_primo = TablaHash(m_no_primo)

    # Insertamos las claves en la tabla de tamaño no primo
    for clave in claves:
        tabla_no_primo.insertar(clave)

    # Calculamos el promedio de pasos al buscar las claves
    promedio_pasos_no_primo = calcular_promedio_pasos(tabla_no_primo, claves)
    print(f"Promedio de pasos al buscar en tabla no prima (m={m_no_primo}): {promedio_pasos_no_primo:.2f}")
    print(f"Colisiones ocurridas en tabla no prima: {tabla_no_primo.get_colisiones()}")

    # Caso 2: Tamaño de la tabla primo
    m_primo = 1009  # 1009 es primo
    tabla_primo = TablaHash(m_primo)

    # Insertamos las claves en la tabla de tamaño primo
    for clave in claves:
        tabla_primo.insertar(clave)

    # Calculamos el promedio de pasos al buscar las claves
    promedio_pasos_primo = calcular_promedio_pasos(tabla_primo, claves)
    print(f"Promedio de pasos al buscar en tabla prima (m={m_primo}): {promedio_pasos_primo:.2f}")
    print(f"Colisiones ocurridas en tabla primo: {tabla_primo.get_colisiones()}")

if __name__ == "__main__":
    main()
