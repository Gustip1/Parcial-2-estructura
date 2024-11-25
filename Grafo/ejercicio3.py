class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
        self.__primer_adyacente = None  # El primer nodo adyacente
        self.__ultimo_adyacente = None  # El último nodo adyacente
        self.__adyacente=[]

    def getDato(self):
        return self.__dato

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

   
    def getPrimerAdyacente(self):
        return self.__primer_adyacente

    def getUltimoAdyacente(self):
        return self.__ultimo_adyacente

    def setPrimerAdyacente(self, nodo_adyacente):
        self.__primer_adyacente = nodo_adyacente

    def setUltimoAdyacente(self, nodo_adyacente):
        self.__ultimo_adyacente = nodo_adyacente

    def getAdyacentes(self):
        return self.__adyacente
    def agregarAdyacente(self, nodo,peso):
        self.__adyacente.append((nodo,peso))


class Grafo:
    def __init__(self):
        self.__nodos = []

    def agregarNodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.__nodos:
            self.__nodos[-1].setSiguiente(nuevo_nodo)
        self.__nodos.append(nuevo_nodo)
        return nuevo_nodo

    def agregarArista(self, nodo1, nodo2,peso=1):
        nodo1.agregarAdyacente(nodo2,peso)

    def busqueda_rapida(self,nodo_inicial):
        distancias= {nodo:float('inf') for nodo in self.__nodos}
        distancias[nodo_inicial]=0
        visitados=set()
        actual=nodo_inicial
        while actual is not None:
            visitados.add(actual)
            for adyacente,peso in actual.getAdyacentes():
                if adyacente not in visitados:
                    nueva_distancia=distancias[actual]+peso
                    if nueva_distancia<distancias[adyacente]:
                        distancias[adyacente]=nueva_distancia
            actual = None
            menor_distancia = float('inf')
            for nodo in self.__nodos:
                if nodo not in visitados and distancias[nodo] < menor_distancia:
                    actual = nodo
                    menor_distancia = distancias[nodo]
        return distancias


def main():
    # Crear el grafo
    grafo = Grafo()

    # Agregar nodos al grafo
    nodo_A = grafo.agregarNodo('A')
    nodo_B = grafo.agregarNodo('B')
    nodo_C = grafo.agregarNodo('C')
    nodo_D = grafo.agregarNodo('D')
    nodo_E = grafo.agregarNodo('E')
    nodo_F = grafo.agregarNodo('F')

    # Crear aristas con los pesos
    grafo.agregarArista(nodo_A, nodo_B, 3)  
    grafo.agregarArista(nodo_F, nodo_A, 5)  
    grafo.agregarArista(nodo_B, nodo_C, 1)  
    grafo.agregarArista(nodo_A, nodo_D, 6)  
    grafo.agregarArista(nodo_C, nodo_D, 2)  
    grafo.agregarArista(nodo_D, nodo_B, 3)  
    grafo.agregarArista(nodo_E, nodo_F, 2)  
    grafo.agregarArista(nodo_F, nodo_D, 1)  
    grafo.agregarArista(nodo_F, nodo_A, 5)  
    grafo.agregarArista(nodo_B,nodo_F, 1)
    grafo.agregarArista(nodo_B,nodo_E, 2)

    
    distancias = grafo.busqueda_rapida(nodo_A)

    print("Costo mínimo de enviar un SMS desde A:")
    for nodo, costo in distancias.items():
        print(f"A -> {nodo.getDato()}: {costo} centavos")


if __name__ == "__main__":
    main()

   