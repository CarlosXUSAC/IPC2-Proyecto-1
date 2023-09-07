class ReducirFreq():
    def __init__(self, nodo):
        self.nodo = nodo

    def __call__(self, x):
        return x / self.nodo
    
    def existe(nodo, busqueda):            
    n = 19
    cont = 0
    #nodo = nodo.siguiente
    while nodo != None:
        if nodo.dato != busqueda:            
            cont = cont + pow(10, n)            
            n = n-1        
        else:            
            n = n-1
        nodo = nodo.siguiente                  
    return cont
