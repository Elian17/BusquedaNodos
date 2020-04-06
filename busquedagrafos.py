class Nodo:

    valor=0
    nodos = []
    ruta = "-"

    def __init__(self, numero):
        self.valor = numero
        self.nodos=[]
        self.ruta = "-"

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
        if nodo.valor==busqueda:
            return nodo
        else:
            for n in nodo.nodos:
                x =  n.BuscarNodoDFS(n, busqueda)
                if x!=0:
                    return x
        return 0

    # BUSQUEDA POR PROFUNDIDAD RETORNA CAMINO
    def BuscarNodoDFSR(self, nodo, busqueda):
        if nodo.valor==busqueda:
            return nodo.valor
        else:
            for n in nodo.nodos:
                x =  n.BuscarNodoDFSR(n, busqueda)
                if x!=0:
                    return str(x)+"-"+str(nodo.valor)
        return 0

    # BUSQUEDA POR AMPLITUD
    def BuscarNodoBFS(self, nodo, busqueda, cola):
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

    # BUSQUEDA POR AMPLITUD RETORNA CAMINO
    def BuscarNodoBFSR(self, nodo, busqueda, cola):
        if nodo.valor==busqueda:
            nodo.ruta+="-"+str(nodo.valor)
            return nodo
        else:
            for n in nodo.nodos: 
                n.ruta += str(nodo.ruta)+"-"+str(nodo.valor)+"-"
                cola.put(n)
            y = self.BuscarNodoBFSR(cola.get(), busqueda, cola) 
            if y!=0:
                return y 
            else:
                cola.pop()
        
        return 0


grafo = Nodo(1)
grafo.NuevoNodo(Nodo(8))
grafo.NuevoNodo(Nodo(2))
grafo.NuevoNodo(Nodo(3))
grafo.NuevoNodoBusqueda(grafo, Nodo(4), 8)
grafo.NuevoNodoBusqueda(grafo, Nodo(5), 8)
grafo.NuevoNodoBusqueda(grafo, Nodo(6), 2)
grafo.NuevoNodoBusqueda(grafo, Nodo(8), 6)
grafo.NuevoNodoBusqueda(grafo, Nodo(7), 6)
grafo.NuevoNodoBusqueda(grafo, Nodo(8), 3)

# print('---')

# grafo.NuevoNodoBusqueda(grafo, Nodo(8), 11)

print('DFS')
print(grafo.BuscarNodoDFSR(grafo,7)[::-1])
import queue
x=queue.Queue()
print('BFS')
print(grafo.BuscarNodoBFSR(grafo,7, x).ruta)

