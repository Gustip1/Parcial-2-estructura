class Nodo:
    def __init__(self,dato):
        self.__dato=dato
        self.__primer_adyacente=None
        self.__ultimo_adyacente=None
        self.__siguiente=None
        self.__adyacentes={}

    def getDato(self):
        return self.__dato
    
    def getPrimer_adyacente(self):
        return self.__primer_adyacente
    
    def getUltimo_adyacente(self):
        return self.__ultimo_adyacente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    
    def setPrimerAdyacente(self,nodo_adyacente):
        self.__primer_adyacente=nodo_adyacente
    
    def setUltimo_adyacente(self,nodo_adyacente):
        self.__ultimo_adyacente=nodo_adyacente

    def agregar_adyacente(self,nodo_adyacente,peso=1):
        self.__adyacentes[nodo_adyacente]=peso
    
class grafo:
    def __init__(self):
        self.__nodos=[]
    def agregar_nuevo_nodo(self,dato):
        nuevo_nodo=Nodo(dato)
        if self.__nodos:
            self.__nodos[-1].setSiguiente(nuevo_nodo)
        self.__nodos.append(nuevo_nodo)
    
    def agregar_arista(self,nodo1,nodo2):
        nodo1.agregar_Adyacente(nodo2)
    
    def camino(self,u,v):
        camino=[]
        visitado=[]
        actual=u
        while actual is not None:
            camino.append(actual.getDato())
            visitado.append(actual)
            if actual ==v:
                return camino
            siguiente=actual.getPrimerAdyacente()
            while siguiente is not None and siguiente not in visitado:
                siguiente=siguiente.getSiguiente()
            actual=siguiente

    def es_conexo (self):
        if not self.__nodos:
            return True
        visitados=set()
        self.dfs(self.__nodos,visitados)
        return len (visitados) == len (self.__nodos)
    
    def dfs(self,nodo_actual,visitados):
        visitados.add(nodo_actual)
        adyacente=nodo_actual.getPrimerAdycaente()
        while adyacente is not None:
            if adyacente not in visitados:
               self.dfs(nodo_actual,visitados)
            adyacente=adyacente.getSiguiente()
    
    def es_aciclico(self):
        visitados=set()
        for  nodo in self.__nodos:
            if nodo not in visitados:
                if self.dfs_ciclo(visitados,nodo,None):
                    return False
        return True
    
    def dfs_ciclo(self,padre,nodo,visitados):
        visitados.add(nodo)
        adyacente=nodo.getPrimerAdyacente()
        while adyacente is not None:
            if adyacente not in visitados:
                if self.dfs_ciclo(nodo,visitados,adyacente):
                    return True
            elif adyacente != padre:
                return True
        adyacente = adyacente.getSiguiente()
        return False
    
    def rea(self):
        if not self.__nodos:
            return []
        cola=[self.__nodos[0]]
        visitados=set(self.__nodos[0])
        resultado=[]
        while cola:
            actual=cola.pop(0)
            resultado.append(actual.getDato())
            adyacente=actual.getPrimerAdyacente()
            while adyacente is not None:
                if adyacente not in visitados:
                    visitados.add(adyacente)
                    cola.append(adyacente)
                adyacente=adyacente.getSiguiente()
        return resultado
    
    def rep (self):
        if not self.__nodos:
            return []
        visitados=set() 
        resultado=[]
        self.dfs_rec(self.__nodos[0],resultado,visitados)
        return resultado
    
    def dfs_rec(self,nodo,visitado,resultado):
        visitado.add(nodo)
        resultado.append(nodo.getDato())
        adyacente=nodo.getPrimerAdyacente()
        while adyacente is not None:
            if adyacente not in visitado:
                self.dfs_rec(adyacente,resultado,visitado)
            adyacente=adyacente.getSiguiente()
    
    

        
