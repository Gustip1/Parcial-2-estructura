class Nodo:
    __dato: int
    __izquierdo: object
    __derecho: object

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


class abb:
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

    def eliminar(self, dato):
        self.__raiz = self.__eliminar_nodo(self.__raiz, dato)

    def __eliminar_nodo(self, nodo_actual, dato):
        if nodo_actual is None:
            return None
        if dato < nodo_actual.getDato():
            nodo_actual.setIzquierdo(self.__eliminar_nodo(nodo_actual.getIzquierdo(), dato))
        elif dato > nodo_actual.getDato():
            nodo_actual.setDerecho(self.__eliminar_nodo(nodo_actual.getDerecho(), dato))
        else:
            if nodo_actual.getIzquierdo() is None and nodo_actual.getDerecho() is None:
                nodo_actual = None
            elif nodo_actual.getIzquierdo() is None:
                nodo_actual = nodo_actual.getDerecho()
            elif nodo_actual.getDerecho() is None:
                nodo_actual = nodo_actual.getIzquierdo()
            else:
                aux = nodo_actual.getIzquierdo()
                while aux.getDerecho() is not None:
                    aux = aux.getDerecho()
                nodo_actual.setDato(aux.getDato())
                nodo_actual.setIzquierdo(self.__eliminar_nodo(nodo_actual.getIzquierdo(), aux.getDato()))
        return nodo_actual

    def inorden(self, nodo_actual):
        if nodo_actual is not None:
            self.inorden(nodo_actual.getIzquierdo())
            print(nodo_actual.getDato())
            self.inorden(nodo_actual.getDerecho())

    def preorden(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.getDato())
            self.preorden(nodo_actual.getIzquierdo())
            self.preorden(nodo_actual.getDerecho())

    def postorden(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden(nodo_actual.getIzquierdo())
            self.postorden(nodo_actual.getDerecho())
            print(nodo_actual.getDato())

    def nivel(self, dato):
        return self.__nivel_recursivo(dato, self.__raiz, 1)

    def __nivel_recursivo(self, dato, nodo_actual, nivel):
        if nodo_actual is None:
            return -1
        if dato == nodo_actual.getDato():
            return nivel
        elif dato < nodo_actual.getDato():
            return self.__nivel_recursivo(dato, nodo_actual.getIzquierdo(), nivel + 1)
        else:
            return self.__nivel_recursivo(dato, nodo_actual.getDerecho(), nivel + 1)

    def hoja(self, dato):
        nodo = self.__buscar_nodo(self.__raiz, dato)
        if nodo is not None:
            return nodo.getIzquierdo() is None and nodo.getDerecho() is None
        return False

    def hijo(self, x, z):
        nodo_z = self.__buscar_nodo(self.__raiz, z)
        if nodo_z is not None:
            es_izquierdo = nodo_z.getIzquierdo() is not None and nodo_z.getIzquierdo().getDato() == x
            es_derecho = nodo_z.getDerecho() is not None and nodo_z.getDerecho().getDato() == x
            return es_izquierdo or es_derecho
        return False

    def __buscar_nodo(self, nodo_actual, dato):
        if nodo_actual is None or nodo_actual.getDato() == dato:
            return nodo_actual
        if dato < nodo_actual.getDato():
            return self.__buscar_nodo(nodo_actual.getIzquierdo(), dato)
        else:
            return self.__buscar_nodo(nodo_actual.getDerecho(), dato)

    def altura(self):
        return self.__altura_recursiva(self.__raiz)

    def __altura_recursiva(self, nodo_actual):
        if nodo_actual is None:
            return 0
        altura_izquierda = self.__altura_recursiva(nodo_actual.getIzquierdo())
        altura_derecha = self.__altura_recursiva(nodo_actual.getDerecho())
        return max(altura_izquierda, altura_derecha) + 1

    def camino(self, origen, destino):
        subarbol_origen = self.__buscar_nodo(self.__raiz, origen)
        if subarbol_origen is None:
            return f"Error: nodo origen {origen} no encontrado"
        camino = []
        nodo_actual = subarbol_origen
        while nodo_actual is not None and nodo_actual.getDato() != destino:
            camino.append(nodo_actual.getDato())
            if destino < nodo_actual.getDato():
                nodo_actual = nodo_actual.getIzquierdo()
            else:
                nodo_actual = nodo_actual.getDerecho()
        if nodo_actual is None:
            return f"Error: el nodo destino {destino} no es descendiente de {origen}"
        camino.append(destino)
        return " -> ".join(map(str, camino))
#practicar ejercicios de si una raiz tiene hijos o si no tiene y esasa cosas
# Ejemplo de uso
arbol = abb()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Recorrido inorden antes de eliminar:")
arbol.inorden(arbol.getRaiz())

# Buscar un elemento
print("\nBuscar 40:", arbol.buscar(40))

# Eliminar un elemento
arbol.eliminar(50)
print("\nRecorrido inorden después de eliminar 50:")
arbol.inorden(arbol.getRaiz())

# Ejemplo de otras funciones
print("\nAltura del árbol:", arbol.altura())
print("Nivel del nodo 30:", arbol.nivel(30))
print("Es hoja el nodo 20:", arbol.hoja(20))
print("Es 40 hijo de 30:", arbol.hijo(40, 30))
print("Camino de 70 a 60:", arbol.camino(70, 60))
