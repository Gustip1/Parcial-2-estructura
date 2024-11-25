import numpy as np

class GrafoSecuencial:
    def __init__(self, num_nodos):
        self.__numNodos = num_nodos
        self.__matrizAdyacencia = np.zeros((self.__numNodos, self.__numNodos), dtype=int)  # Matriz de adyacencia con NumPy

    def agregarArista(self, u, v):
        """Agrega una arista del nodo u al nodo v."""
        self.__matrizAdyacencia[u][v] = 1  # Solo una dirección para grafo dirigido

    def adyacentes(self, u):
        """Determina los nodos adyacentes a u."""
        lista_adyacentes = []
        for v in range(self.__numNodos):
            if self.__matrizAdyacencia[u][v] == 1:
                lista_adyacentes.append(v)
        return lista_adyacentes

    def grado_entrada(self, nodo):
        """Calcula el grado de entrada de un nodo en un grafo dirigido."""
        grado = 0
        for i in range(self.__numNodos):
            if self.__matrizAdyacencia[i][nodo] == 1:
                grado += 1
        return grado

    def grado_salida(self, nodo):
        """Calcula el grado de salida de un nodo en un grafo dirigido."""
        grado = sum(self.__matrizAdyacencia[nodo])
        return grado

    def es_nodo_fuente(self, nodo):
        """Verifica si un nodo es fuente (sin entradas y con al menos una salida)."""
        return self.grado_entrada(nodo) == 0 and self.grado_salida(nodo) > 0

    def es_nodo_sumidero(self, nodo):
        """Verifica si un nodo es sumidero (con entradas pero sin salidas)."""
        return self.grado_salida(nodo) == 0 and self.grado_entrada(nodo) > 0

    def camino(self, u, v):
        """Determina el camino de u a v, si existe."""
        visitado = np.zeros(self.__numNodos, dtype=bool) #Arreglo lleno de False
        predecesor = np.full(self.__numNodos, None) #Arreglo lleno de None
        cola = []

        cola.append(u)
        visitado[u] = True

        while cola:
            actual = cola.pop(0)
            if actual == v:
                break
            for vecino in range(self.__numNodos):
                if self.__matrizAdyacencia[actual][vecino] == 1 and not visitado[vecino]:
                    visitado[vecino] = True
                    predecesor[vecino] = actual
                    cola.append(vecino)

        # Reconstruir el camino desde u hasta v
        camino = []
        nodo = v
        while nodo is not None:
            camino.insert(0, nodo)
            nodo = predecesor[nodo]
        if camino and camino[0] == u:
            return camino
        else:
            return "Error: No hay camino"  # No hay camino

    def conexo(self):
        """Verifica si el grafo es conexo e imprime si es conexo simple."""
        visitado = np.zeros(self.__numNodos, dtype=bool)
        cola = [0]
        visitado[0] = True

        while cola:
            actual = cola.pop(0)
            for vecino in range(self.__numNodos):
                if self.__matrizAdyacencia[actual][vecino] == 1 and not visitado[vecino]:
                    visitado[vecino] = True
                    cola.append(vecino)

        total_visitados = np.sum(visitado)
        if total_visitados == self.__numNodos:
            print("El grafo es conexo simple. Todos los nodos han sido visitados.")
        else:
            print(f"El grafo no es conexo. Solo se han visitado {total_visitados} de {self.__numNodos} nodos.")

    def aciclico(self):
        """Verifica si el grafo es acíclico utilizando DFS sin funciones auxiliares."""
        visitado = np.zeros(self.__numNodos, dtype=bool)  # Arreglo para marcar nodos visitados
        pila = []  # Pila para el recorrido DFS

        for i in range(self.__numNodos):
            if not visitado[i]:  # Si el nodo no ha sido visitado
                pila.append((i, -1))  # Añadimos el nodo y el padre (-1 indica que no tiene padre)

                while pila:  # Mientras haya nodos en la pila
                    actual, padre = pila.pop()  # Sacamos un nodo de la pila
                    if visitado[actual]:
                        continue  # Si ya fue visitado, saltamos

                    visitado[actual] = True  # Marcamos como visitado
                    for vecino in range(self.__numNodos):
                        if self.__matrizAdyacencia[actual][vecino] == 1:  # Si hay una arista
                            if not visitado[vecino]:
                                pila.append((vecino, actual))  # Añadimos vecino a la pila
                            elif vecino != padre:  # Si es adyacente y no es el padre
                                print("El grafo contiene ciclos.")
                                return

        print("El grafo es acíclico.")

    def REA(self):
        """Recorrido en amplitud (anchura) de todos los nodos del grafo."""
        visitado = np.zeros(self.__numNodos, dtype=bool)
        cola = []
        resultado = []

        for nodo_inicial in range(self.__numNodos):
            if not visitado[nodo_inicial]:
                cola.append(nodo_inicial)
                visitado[nodo_inicial] = True

                while cola:
                    actual = cola.pop(0)
                    resultado.append(actual)
                    
                    for vecino in range(self.__numNodos):
                        if self.__matrizAdyacencia[actual][vecino] == 1 and not visitado[vecino]:
                            visitado[vecino] = True
                            cola.append(vecino)

        return resultado

    def REP(self):
        """Recorrido en profundidad (DFS) de todos los nodos del grafo sin funciones auxiliares."""
        visitado = np.zeros(self.__numNodos, dtype=bool)
        pila = []
        resultado = []

        # Recorrer todos los nodos para asegurarnos de procesar todos los componentes del grafo
        for nodo_inicial in range(self.__numNodos):
            if not visitado[nodo_inicial]:
                pila.append(nodo_inicial)

                while pila:
                    actual = pila.pop()  # Sacamos el último nodo de la pila (LIFO)
                    
                    if not visitado[actual]:
                        visitado[actual] = True
                        resultado.append(actual)

                        # Agregar vecinos no visitados a la pila en orden inverso
                        for vecino in range(self.__numNodos - 1, -1, -1):
                            if self.__matrizAdyacencia[actual][vecino] == 1 and not visitado[vecino]:
                                pila.append(vecino)

        return resultado
    def GradEnt(self, u):
        """Determina la cantidad de aristas que llegan a u."""
        grado = 0
        for i in range(self.__numNodos):
            if self.__matrizAdyacencia[i][u] == 1:
                grado += 1
        return grado

    # Método GradSal: Calcula el grado de salida de un nodo
    def GradSal(self, u):
        """Determina la cantidad de aristas que salen de u."""
        grado = sum(self.__matrizAdyacencia[u])
        return grado

    # Método NodoF: Verifica si un nodo es fuente
    def NodoF(self, u):
        """Evalúa si u es nodo fuente de G."""
        return self.GradEnt(u) == 0 and self.GradSal(u) > 0

    # Método NodoS: Verifica si un nodo es sumidero
    def NodoS(self, u):
        """Evalúa si u es nodo sumidero de G."""
        return self.GradSal(u) == 0 and self.GradEnt(u) > 0

# Ejemplo de uso
if __name__ == "__main__":
    grafo = GrafoSecuencial(5)

    # Agregar algunas aristas al grafo
    grafo.agregarArista(0, 1)
    grafo.agregarArista(2, 3)
    grafo.agregarArista(3, 4)
    
    # Ejemplos de grado de entrada y salida
    for nodo in range(5):
        print(f"Nodo {nodo} - Grado de entrada: {grafo.grado_entrada(nodo)}, Grado de salida: {grafo.grado_salida(nodo)}")
        print(f"Nodo {nodo} es fuente: {grafo.es_nodo_fuente(nodo)}, es sumidero: {grafo.es_nodo_sumidero(nodo)}")

    # Otros métodos
    print("Adyacentes al nodo 0:", grafo.adyacentes(0))
    print("Camino de 0 a 4:", grafo.camino(0, 4))
    grafo.conexo()
    grafo.aciclico()
    print("Recorrido en anchura (REA):", grafo.REA())
    print("Recorrido en profundidad (REP):", grafo.REP())
