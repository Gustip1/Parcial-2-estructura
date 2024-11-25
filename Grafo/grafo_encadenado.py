class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
        self.__primer_adyacente = None  # El primer nodo adyacente
        self.__ultimo_adyacente = None  # El último nodo adyacente

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

  
  
    def agregarAdyacente(self, nuevo_adyacente):
        if self.__primer_adyacente is None:
            self.setPrimerAdyacente(nuevo_adyacente)
            self.setUltimoAdyacente(nuevo_adyacente)
        else:
            self.__ultimo_adyacente.setSiguiente(nuevo_adyacente)
            self.setUltimoAdyacente(nuevo_adyacente)


class Grafo:
    def __init__(self):
        self.__nodos = []

    def agregarNodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.__nodos:
            self.__nodos[-1].setSiguiente(nuevo_nodo)
        self.__nodos.append(nuevo_nodo)
        return nuevo_nodo

    def agregarArista(self, nodo1, nodo2):
        nodo1.agregarAdyacente(nodo2)
        # grafo  no dirigido
        nodo2.agregarAdyacente(nodo1)

    def adyacentes(self, nodo):
        adyacentes = []
        actual = nodo.getPrimerAdyacente()
        while actual is not None:
            adyacentes.append(actual.getDato())
            actual = actual.getSiguiente()
        return adyacentes

    def camino(self, u, v):
        """Determina el camino de u a v, si existe, evitando bucles."""
        camino = []          # Lista para almacenar el camino
        visitados = []       # Lista para almacenar los nodos ya visitados
        actual = u

        # Recorrer el grafo desde el nodo 'u' buscando el nodo 'v'
        while actual is not None:
            # Añadir el nodo actual al camino y marcarlo como visitado
            camino.append(actual.getDato())
            visitados.append(actual)

            # Si hemos llegado al destino, devolver el camino
            if actual == v:
                return camino

            # Avanzar al primer nodo adyacente no visitado
            siguiente = actual.getPrimerAdyacente()
            while siguiente is not None and siguiente in visitados:
                siguiente = siguiente.getSiguiente()  # Saltar nodos ya visitados

            # Si encontramos un adyacente no visitado, avanzamos a él; si no, terminamos
            actual = siguiente
        
        # Si no encontramos el camino, devolver un mensaje claro
        return "No hay camino entre los nodos especificados"


    def es_conexo(self):
        if not self.__nodos:
            return True
        visitados = set()
        self.__dfs(self.__nodos[0], visitados)
        return len(visitados) == len(self.__nodos)

   
    def es_acyclic(self):
        visitados = set()
        for nodo in self.__nodos:
            if nodo not in visitados:
                if self.__dfs_ciclo(nodo, visitados, None):
                    return False
        return True


    def rea(self):
        if not self.__nodos:
            return []
        cola = [self.__nodos[0]]
        visitados = set([self.__nodos[0]])
        resultado = []
        while cola:
            actual = cola.pop(0)
            resultado.append(actual.getDato())
            adyacente = actual.getPrimerAdyacente()
            while adyacente is not None:
                if adyacente not in visitados:
                    visitados.add(adyacente)
                    cola.append(adyacente)
                adyacente = adyacente.getSiguiente()
        return resultado

    def rep(self):
        if not self.__nodos:
            return []
        visitados = set()
        resultado = []
        self.__dfs_rec(self.__nodos[0], visitados, resultado)
        return resultado

  
    def __dfs(self, nodo, visitados):
        visitados.add(nodo)
        adyacente = nodo.getPrimerAdyacente()
        while adyacente is not None:
            if adyacente not in visitados:
                self.__dfs(adyacente, visitados)
            adyacente = adyacente.getSiguiente()

    def __dfs_rec(self, nodo, visitados, resultado):
        visitados.add(nodo)
        resultado.append(nodo.getDato())
        adyacente = nodo.getPrimerAdyacente()
        while adyacente is not None:
            if adyacente not in visitados:
                self.__dfs_rec(adyacente, visitados, resultado)
            adyacente = adyacente.getSiguiente()

    def __dfs_ciclo(self, nodo, visitados, padre):
        visitados.add(nodo)
        adyacente = nodo.getPrimerAdyacente()
        while adyacente is not None:
            if adyacente not in visitados:
                if self.__dfs_ciclo(adyacente, visitados, nodo):
                    return True
            elif adyacente != padre:
                return True
            adyacente = adyacente.getSiguiente()
        return False
    #  metodos para el grafo dirigido 
    def grado_entrada(self, nodo):
        grado = 0
        for n in self.__nodos:
            adyacente = n.getPrimerAdyacente()
            while adyacente is not None:
                if adyacente == nodo:
                    grado += 1
                adyacente = adyacente.getSiguiente()
        return grado

    def grado_salida(self, nodo):
        adyacente = nodo.getPrimerAdyacente()
        grado = 0
        while adyacente is not None:
            grado += 1
            adyacente = adyacente.getSiguiente()
        return grado
    
    def es_nodo_fuente(self, nodo):
        return self.grado_entrada(nodo) == 0 and self.grado_salida(nodo) > 0

    def es_nodo_sumidero(self, nodo):
        return self.grado_salida(nodo) == 0 and self.grado_entrada(nodo) > 0
    

def main():
    grafo = Grafo()

    # Agregar nodos al grafo
    nodo_A = grafo.agregarNodo('A')
    nodo_B = grafo.agregarNodo('B')
    nodo_C = grafo.agregarNodo('C')
    nodo_D = grafo.agregarNodo('D')

    # Crear aristas (conexiones)
    grafo.agregarArista(nodo_A, nodo_B)  # A -> B
    grafo.agregarArista(nodo_A, nodo_C)  # A -> C
    grafo.agregarArista(nodo_B, nodo_D)  # B -> D
    grafo.agregarArista(nodo_C, nodo_D)  # C -> D

    # Imprimir los nodos adyacentes de A
    print(f"Adyacentes de A: {grafo.adyacentes(nodo_A)}")

    # Imprimir los nodos adyacentes de B
    print(f"Adyacentes de B: {grafo.adyacentes(nodo_B)}")

    # Verificar si existe un camino entre A y D
    camino_A_D = grafo.camino(nodo_A, nodo_D)
    if camino_A_D:
        print(f"Camino de A a D: {camino_A_D}")
    else:
        print("No hay camino de A a D")

    # Verificar si el grafo es conexo
    if grafo.es_conexo():
        print("El grafo es conexo")
    else:
        print("El grafo no es conexo")

    # Verificar si el grafo es acíclico
    if grafo.es_acyclic():
        print("El grafo es acíclico")
    else:
        print("El grafo tiene ciclos")

    # Imprimir el recorrido en anchura (REA)
    print(f"Recorrido en Anchura (REA): {grafo.rea()}")

    # Imprimir el recorrido en profundidad (REP)
    print(f"Recorrido en Profundidad (REP): {grafo.rep()}")

    # Verificar el grado de entrada y salida de los nodos
    print(f"Grado de Entrada de D: {grafo.grado_entrada(nodo_D)}")
    print(f"Grado de Salida de A: {grafo.grado_salida(nodo_A)}")

    # Verificar si un nodo es fuente
    if grafo.es_nodo_fuente(nodo_A):
        print("A es un nodo fuente")
    else:
        print("A no es un nodo fuente")

    # Verificar si un nodo es sumidero
    if grafo.es_nodo_sumidero(nodo_D):
        print("D es un nodo sumidero")
    else:
        print("D no es un nodo sumidero")


if __name__ == "__main__":
    main()

   