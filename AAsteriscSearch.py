class Nodo:

    valor=0
    nodos = []
    distanciaInicio=0
    distanciaObjetivo=0

    def __init__(self, numero, distanciaInicio, distanciaObjetivo):
        self.valor = numero
        self.nodos=[]
        self.distanciaInicio = distanciaInicio
        self.distanciaObjetivo = distanciaObjetivo

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
        if nodo.valor==busqueda:
            return nodo
        else:
            for n in nodo.nodos:
                x =  n.BuscarNodoDFS(n, busqueda)
                if x!=0:
                    return x
        return 0

    # Busqueda con informacion
    # SE DEBERIA HACER UN RECONOCIMIENTO INICIAL
    def AStartSearch(self, nodo, busqueda, lista):
        print(nodo.valor)
        if len(lista)>0:
            lista.remove(lista[0])
        if nodo.valor==busqueda:
            return nodo
        else:     
            for n in nodo.nodos:
                lista.append(n) 
            lista.sort(key=lambda l: (l.distanciaInicio+l.distanciaObjetivo))  
            return self.AStartSearch(lista[0], busqueda, lista)
        return 0


grafo = Nodo(1, 0, 40)
grafo.NuevoNodo(Nodo(4, 21, 70))
grafo.NuevoNodo(Nodo(2, 22, 32))
grafo.NuevoNodo(Nodo(3, 20, 20))
grafo.NuevoNodoBusqueda(grafo, Nodo(6, 47, 10), 2)
grafo.NuevoNodoBusqueda(grafo, Nodo(7, 115, 15), 3)
grafo.NuevoNodoBusqueda(grafo, Nodo(8, 178, 0), 6)
grafo.NuevoNodoBusqueda(grafo, Nodo(5, 55, 35), 6)
grafo.NuevoNodoBusqueda(grafo, Nodo(8, 296, 0), 6)
grafo.NuevoNodoBusqueda(grafo, Nodo(9, 85, 8), 6)
grafo.NuevoNodoBusqueda(grafo, Nodo(8, 90, 0), 9)
print("x")
# print(grafo.UninformedSearch(grafo, 8, 0))
lista=[]
grafo.AStartSearch(grafo, 8, lista)

