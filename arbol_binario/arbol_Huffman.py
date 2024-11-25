class Nodo:
    def __init__(self, caracter=None, frecuencia=0):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self, frecuencias):
        self.raiz = self.construir_arbol(frecuencias)
        self.codigos = {}
        self.generar_codigos(self.raiz, '')

    def construir_arbol(self, frecuencias):
        # Crear una lista de nodos hoja
        nodos = []
        for caracter in frecuencias:
            nodo = Nodo(caracter, frecuencias[caracter])
            nodos.append(nodo)
            print(f"Insertado nodo '{caracter}' con frecuencia {frecuencias[caracter]}.")

        print("\nConstruyendo el árbol de Huffman:")
        paso = 1
        while len(nodos) > 1:
            # Ordenar los nodos por frecuencia
            nodos.sort(key=lambda x: x.frecuencia)

            # Seleccionar los dos nodos con menor frecuencia
            nodo_izquierdo = nodos.pop(0)
            nodo_derecho = nodos.pop(0)

            print(f"Paso {paso}:")
            print(f"  Suprimiendo nodos '{nodo_izquierdo.caracter}' ({nodo_izquierdo.frecuencia}) y '{nodo_derecho.caracter}' ({nodo_derecho.frecuencia}).")

            # Crear un nuevo nodo combinando las frecuencias
            frecuencia_total = nodo_izquierdo.frecuencia + nodo_derecho.frecuencia
            nodo_padre = Nodo(None, frecuencia_total)
            nodo_padre.izquierda = nodo_izquierdo
            nodo_padre.derecha = nodo_derecho

            print(f"  Agrupando en un nuevo nodo con frecuencia total {frecuencia_total}.")

            # Agregar el nuevo nodo a la lista
            nodos.append(nodo_padre)
            print(f"  Insertado nuevo nodo en la lista.\n")
            paso += 1

        print("Árbol de Huffman construido exitosamente.\n")
        return nodos[0]  # Raíz del árbol

    def generar_codigos(self, nodo, codigo_actual):
        if nodo is None:
            return
        if nodo.caracter is not None:
            self.codigos[nodo.caracter] = codigo_actual
            print(f"  Carácter '{nodo.caracter}': Código '{codigo_actual}'")
            return
        self.generar_codigos(nodo.izquierda, codigo_actual + '0')
        self.generar_codigos(nodo.derecha, codigo_actual + '1')

    def codificar(self, texto):
        texto_codificado = ''
        print("Codificando el texto:")
        for caracter in texto:
            codigo = self.codigos[caracter]
            texto_codificado += codigo
            print(f"  Carácter '{caracter}' codificado como '{codigo}'")
        print()
        return texto_codificado

    def decodificar(self, texto_codificado):
        texto_decodificado = ''
        nodo_actual = self.raiz
        for bit in texto_codificado:
            if bit == '0':
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha

            if nodo_actual.caracter is not None:
                texto_decodificado += nodo_actual.caracter
                nodo_actual = self.raiz
        return texto_decodificado

def calcular_frecuencias(texto):
    frecuencias = {}
    for caracter in texto:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1
    return frecuencias

def main():
    # Leer el archivo de texto
    nombre_archivo = input("Ingrese el nombre del archivo a comprimir: ")
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()

    # Paso 1: Calcular las frecuencias
    frecuencias = calcular_frecuencias(texto)
    print("\nFrecuencias de los caracteres:")
    for caracter in frecuencias:
        print(f"'{caracter}': {frecuencias[caracter]}")

    # Paso 2: Construir el árbol de Huffman
    arbol = Arbol(frecuencias)

    # Paso 3: Codificar el texto
    texto_codificado = arbol.codificar(texto)
    print(f"Texto codificado: {texto_codificado}")

    # Guardar el texto codificado en un archivo
    nombre_archivo_codificado = 'archivo_codificado.txt'
    with open(nombre_archivo_codificado, 'w', encoding='utf-8') as archivo:
        archivo.write(texto_codificado)
    print(f"\nEl texto codificado se ha guardado en '{nombre_archivo_codificado}'.")

    # Paso 4: Decodificar el texto (para verificar)
    texto_decodificado = arbol.decodificar(texto_codificado)
    print(f"\nTexto decodificado: {texto_decodificado}")

    # Verificar que el texto original y el decodificado son iguales
    if texto == texto_decodificado:
        print("\nLa decodificación fue exitosa. El texto original y el decodificado son iguales.")
    else:
        print("\nLa decodificación falló. El texto original y el decodificado son diferentes.")

if __name__ == '__main__':
    main()
