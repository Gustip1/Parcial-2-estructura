import random

class TablaHash:
    def __init__(self, m):
        self.m = m
        self.tabla = [None] * m
        self.colisiones = 0  # Contador de colisiones

    def funcion_hash(self, clave):
        """Función hash utilizando el método de la división."""
        return clave % self.m

    def insertar(self, clave):
        """Inserta una clave en la tabla hash utilizando prueba lineal.
        Cuenta las colisiones durante el proceso.
        """
        posicion_inicial = self.funcion_hash(clave)
        posicion = posicion_inicial

        while self.tabla[posicion] is not None:
            if self.tabla[posicion] == clave:
                # La clave ya está en la tabla
                return  # No hacemos nada si la clave ya está presente
            # Incrementamos el contador de colisiones
            self.colisiones += 1
            posicion = (posicion + 1) % self.m
            if posicion == posicion_inicial:
                # La tabla está llena
                raise Exception("Tabla hash llena, no se pudo insertar la clave.")
        self.tabla[posicion] = clave

    def buscar(self, clave):
        """Busca una clave en la tabla hash y devuelve la posición donde se encuentra y los pasos realizados."""
        posicion_inicial = self.funcion_hash(clave)
        posicion = posicion_inicial
        pasos = 1  # Contamos el primer intento

        while self.tabla[posicion] is not None:
            if self.tabla[posicion] == clave:
                return posicion, pasos  # Retornamos la posición y los pasos realizados
            posicion = (posicion + 1) % self.m
            pasos += 1
            if posicion == posicion_inicial:
                # Se ha recorrido toda la tabla y la clave no está
                return -1, pasos  # Clave no encontrada
        # Clave no encontrada
        return -1, pasos


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
        try:
            tabla_no_primo.insertar(clave)
        except Exception as e:
            print(e)
            break

    # Calculamos el promedio de pasos al buscar las claves
    promedio_pasos_no_primo = calcular_promedio_pasos(tabla_no_primo, claves)
    print(f"Promedio de pasos al buscar en tabla no prima (m={m_no_primo}): {promedio_pasos_no_primo:.2f}")
    print(f"Colisiones ocurridas en tabla no prima: {tabla_no_primo.colisiones}")

    # Caso 2: Tamaño de la tabla primo
    m_primo = 1009  # 1009 es primo
    tabla_primo = TablaHash(m_primo)

    # Insertamos las claves en la tabla de tamaño primo
    for clave in claves:
        try:
            tabla_primo.insertar(clave)
        except Exception as e:
            print(e)
            break

    # Calculamos el promedio de pasos al buscar las claves
    promedio_pasos_primo = calcular_promedio_pasos(tabla_primo, claves)
    print(f"Promedio de pasos al buscar en tabla prima (m={m_primo}): {promedio_pasos_primo:.2f}")
    print(f"Colisiones ocurridas en tabla primo: {tabla_primo.colisiones}")

if __name__ == "__main__":
    main()