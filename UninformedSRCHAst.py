class Nodo:

    valor=0
    nodos = []
    costo=0
    suma=0

    def __init__(self, numero, costo):
        self.valor = numero
        self.nodos=[]
        self.costo = costo

    def NuevoNodo(self, nod):
        self.nodos.append(nod)
     
    def NuevoNodoBusqueda(self, grafoBase, nodoNuevo, nodoBase):
        nodoEncontrado= self.BuscarNodoDFS(grafoBase, nodoBase)
        if nodoEncontrado!=0:
            nodoEncontrado.nodos.append(nodoNuevo)
        else:
            print('nodo no encontrado')
        

    # BUSQUEDA POR PROFUNDIDAD
    def BuscarNodoDFS(self, nodo, busqueda):
        print(nodo.valor)
        if nodo.valor==busqueda:
            return nodo
        else:
            for n in nodo.nodos:
                x =  n.BuscarNodoDFS(n, busqueda)
                if x!=0:
                    return x
        return 0

    # BUSQUEDA POR AMPLITUD
    def BuscarNodoBFS(self, nodo, busqueda, cola):
        print(nodo.valor)
        if nodo.valor==busqueda:
            return nodo
        else:
            for n in nodo.nodos:               
                cola.put(n)
            y = self.BuscarNodoBFS(cola.get(), busqueda, cola) 
            if y!=0:
                return y  
            else:
                cola.pop()
        
        return 0


    # Busqueda sin informacion
    def UninformedSearch(self, nodo, busqueda, lista):
        # print("*")
        # for n in nodo.nodos:
        #     print(n.valor)
        # print("*")
        # nodo.nodos.sort(key=lambda l: l.costo)  
        # for n in nodo.nodos:
        #     print(n.valor)
        if len(lista)>0:
            lista.remove(lista[0])
        print("Nodo:"+str(nodo.valor)+" Costo:"+str(nodo.costo))
        if nodo.valor==busqueda:
            return nodo
        else:     
            for n in nodo.nodos:
                n.costo+=nodo.costo
                lista.append(n) 
            lista.sort(key=lambda l: l.costo)  
            return self.UninformedSearch(lista[0], busqueda, lista)
        return 0


grafo = Nodo(1, 0)
grafo.NuevoNodo(Nodo(8, 10))
grafo.NuevoNodo(Nodo(2, 1))
grafo.NuevoNodo(Nodo(3, 5))
grafo.NuevoNodoBusqueda(grafo, Nodo(4, 3), 8)
grafo.NuevoNodoBusqueda(grafo, Nodo(6, 1), 2)
grafo.NuevoNodoBusqueda(grafo, Nodo(8, 9), 6)
grafo.NuevoNodoBusqueda(grafo, Nodo(7, 5), 6)
grafo.NuevoNodoBusqueda(grafo, Nodo(8, 3), 3)
print("x")
# print(grafo.UninformedSearch(grafo, 8, 0))
lista=[]
grafo.UninformedSearch(grafo, 8, lista)

