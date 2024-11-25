class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None

    def getDato(self):
        return self.__dato

    def setDato(self, dato):
        self.__dato = dato

    def getIzquierdo(self):
        return self.__izquierdo

    def setIzquierdo(self, izquierdo):
        self.__izquierdo = izquierdo

    def getDerecho(self):
        return self.__derecho

    def setDerecho(self, derecho):
        self.__derecho = derecho

    def getGrado(self):
        if self.__derecho is None and self.__izquierdo is None:
            return 0
        elif self.__derecho is not None and self.__izquierdo is None:
            return 1
        elif self.__derecho is None and self.__izquierdo is not None:
            return 1
        else:
            return 2

class Arbol:
    def __init__(self):
        self.__raiz = None

    def getRaiz(self):
        return self.__raiz

    def insertar(self, dato):
        if self.__raiz is None:
            self.__raiz = Nodo(dato)
        else:
            self.__insertar_recursivo(dato, self.__raiz)

    def __insertar_recursivo(self, dato, nodo_actual):
        if dato < nodo_actual.getDato():
            if nodo_actual.getIzquierdo() is None:
                nodo_actual.setIzquierdo(Nodo(dato))
            else:
                self.__insertar_recursivo(dato, nodo_actual.getIzquierdo())
        elif dato > nodo_actual.getDato():
            if nodo_actual.getDerecho() is None:
                nodo_actual.setDerecho(Nodo(dato))
            else:
                self.__insertar_recursivo(dato, nodo_actual.getDerecho())

    def buscar(self, dato):
        return self.__buscar_recursivo(dato, self.__raiz)

    def __buscar_recursivo(self, dato, nodo_actual):
        if nodo_actual is None:
            return False
        if dato == nodo_actual.getDato():
            return True
        elif dato < nodo_actual.getDato():
            return self.__buscar_recursivo(dato, nodo_actual.getIzquierdo())
        else:
            return self.__buscar_recursivo(dato, nodo_actual.getDerecho())

    def inorden(self, nodo_actual):
        if nodo_actual is not None:
            self.inorden(nodo_actual.getIzquierdo())
            print(nodo_actual.getDato(), end=" ")
            self.inorden(nodo_actual.getDerecho())

    def postorden(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden(nodo_actual.getIzquierdo())
            self.postorden(nodo_actual.getDerecho())
            print(nodo_actual.getDato(), end=" ")

    def preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.getDato(), end=" ")
            self.preorden(nodo_actual.getIzquierdo())
            self.preorden(nodo_actual.getDerecho())

    def camino(self, nodo1, nodo2):
        camino = []
        nodo_actual = nodo1
        while nodo_actual is not None and nodo_actual.getDato() != nodo2.getDato():
            camino.append(nodo_actual.getDato())
            if nodo_actual.getDato() > nodo2.getDato():
                nodo_actual = nodo_actual.getIzquierdo()
            else:
                nodo_actual = nodo_actual.getDerecho()
        if nodo_actual is not None:
            camino.append(nodo2.getDato())
        return " -> ".join(map(str, camino))

    def frontera(self, nodo_actual):
        if nodo_actual is not None:
            self.frontera(nodo_actual.getIzquierdo())
            if nodo_actual.getGrado() == 0:
                print(nodo_actual.getDato(), end=" ")
            self.frontera(nodo_actual.getDerecho())

    def un_solo_hijo(self, nodo_actual):
        if nodo_actual is not None:
            self.un_solo_hijo(nodo_actual.getIzquierdo())
            if nodo_actual.getGrado() == 1:
                print(nodo_actual.getDato(), end=" ")
            self.un_solo_hijo(nodo_actual.getDerecho())

    def hnos(self, nodo_actual):
        if nodo_actual is not None:
            self.hnos(nodo_actual.getIzquierdo())
            if nodo_actual.getGrado() == 2 and nodo_actual != self.__raiz:
                print(nodo_actual.getIzquierdo().getDato(), nodo_actual.getDerecho().getDato())
            self.hnos(nodo_actual.getDerecho())

    def nodo_interior(self, nodo_actual):
        if nodo_actual is not None:
            self.nodo_interior(nodo_actual.getIzquierdo())
            if nodo_actual.getGrado() > 0 and nodo_actual != self.__raiz:
                print(nodo_actual.getDato(), end=" ")
            self.nodo_interior(nodo_actual.getDerecho())

def main():
    # Crear el árbol
    arbol = Arbol()

    # Insertar nodos en el árbol
    datos = [10, 5, 15, 3, 7, 12, 20, 6, 8]
    for dato in datos:
        arbol.insertar(dato)

    print("\n--- Recorrido Inorden ---")
    arbol.inorden(arbol.getRaiz())
    
    print("\n--- Recorrido Preorden ---")
    arbol.preorden(arbol.getRaiz())
    
    print("\n--- Recorrido Postorden ---")
    arbol.postorden(arbol.getRaiz())

    print("\n\n--- Nodos en la Frontera ---")
    arbol.frontera(arbol.getRaiz())

    print("\n\n--- Nodos con un Solo Hijo ---")
    arbol.un_solo_hijo(arbol.getRaiz())

    print("\n\n--- Nodos Hermanos ---")
    arbol.hnos(arbol.getRaiz())

    print("\n\n--- Nodos Interiores ---")
    arbol.nodo_interior(arbol.getRaiz())

if __name__ == "__main__":
    main()
