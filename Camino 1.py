import sys

from Jupyter import diccionario
class Cola:
    def __init__(self):
        self.datos=list()
    def encolar(self,dato):
        self.datos.append(dato)
    def desencolar(self):
        return self.datos.pop(0)
    def es_vacia(self):
        if len(self.datos)==0:
            return True
        else:
            return False
class Recorrido:
    def __init__(self,visitados,length):
        self.visitados=[]
        self.visitados+=visitados
        self.length=length
def caminoCorto(diccionario, origen, destino):
    if origen not in diccionario or destino not in diccionario:
        print('Lo sentimos, los puntos seleccionados no son válidos, por favor vuelva a ingresarlos')
        return
    cola1=Cola()
    camino=Recorrido([origen],0)
    cola1.encolar(camino)
    minimo=Recorrido([],sys.maxsize)
    while not cola1.es_vacia():
        actual=cola1.desencolar()
        if actual.visitados[-1]==destino and actual.length<minimo.length:
            minimo=actual
            continue
        if actual.length>minimo.length:
            continue
        for i in diccionario[actual.visitados[-1]]:
            if i[0] not in actual.visitados:
                arrayVisitados=[]
                arrayVisitados.extend(actual.visitados)
                arrayVisitados.append(i[0])
                nuevoLength=actual.length+i[1]
                nuevoCamino=Recorrido(arrayVisitados,nuevoLength)
                cola1.encolar(nuevoCamino)
    return minimo
origen=input('Ingrese el origen\n')
destino=input('Ingrese el destino\n')
camino=caminoCorto(diccionario,origen,destino)
if camino.length!=sys.maxsize:
    print('Camino a seguir')
    for i in camino.visitados:
        print(i)
    print(f'Costo que tomará {round(camino.length,2)}')
else:
    print('No hay un camino especificado para llegar a la ruta especificada')
