class Nodo:

    valor=0
    nodos = []

    def __init__(self, numero):
        self.valor = numero
        self.nodos=[]

    def NuevoNodo(self, nod):
        self.nodos.append(nod)

    def Multiplicacion(self, a, b):
        return a*b
     
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


grafo = Nodo(1)
grafo.NuevoNodo(Nodo(2))
grafo.NuevoNodo(Nodo(3))
grafo.NuevoNodoBusqueda(grafo, Nodo(4), 3)
grafo.NuevoNodoBusqueda(grafo, Nodo(8), 3)
grafo.NuevoNodoBusqueda(grafo, Nodo(5), 4)
grafo.NuevoNodoBusqueda(grafo, Nodo(6), 4)
grafo.NuevoNodoBusqueda(grafo, Nodo(7), 1)
grafo.NuevoNodoBusqueda(grafo, Nodo(8), 7)

print('---')

grafo.NuevoNodoBusqueda(grafo, Nodo(8), 11)
print('---')

print(grafo.BuscarNodoDFS(grafo,8).valor)

import queue

x=queue.Queue()

print('BFS')

print(grafo.BuscarNodoBFS(grafo,6, x).valor)

