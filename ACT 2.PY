class TransporteMasivo:
    def __init__(self):

        # Grafo para representar el sistema de transporte
        self.rutas = {}

    def agregar_ruta(self, estacion_origen, estacion_destino, tiempo):

        # Establece una conexión directa entre dos estaciones
        if estacion_origen not in self.rutas:
            self.rutas[estacion_origen] = []
        if estacion_destino not in self.rutas:
            self.rutas[estacion_destino] = []
        self.rutas[estacion_origen].append((estacion_destino, tiempo))
        self.rutas[estacion_destino].append((estacion_origen, tiempo)) 

def regla_transitiva(transporte, origen, destino):

    # Si hay una conexión directa entre origen y destino
    if destino in dict(transporte.rutas.get(origen, [])):
        return True

    # Si hay una conexión indirecta (a través de otra estación)
    for estacion_intermedia, _ in transporte.rutas.get(origen, []):
        if destino in dict(transporte.rutas.get(estacion_intermedia, [])):
            return True

    return False
import heapq

def dijkstra(transporte, inicio, objetivo):
    # Crear una cola de prioridad (min-heap)
    cola = [(0, inicio)]  # (tiempo_acumulado, estacion_actual)
    tiempos = {inicio: 0}  # tiempos mínimos para cada estación
    previos = {inicio: None}  # Para reconstruir la ruta

    while cola:
        tiempo_actual, estacion_actual = heapq.heappop(cola)

        # Si llegamos al objetivo, reconstruimos la ruta
        if estacion_actual == objetivo:
            ruta = []
            while estacion_actual:
                ruta.append(estacion_actual)
                estacion_actual = previos[estacion_actual]
            return ruta[::-1], tiempo_actual  # Ruta desde el inicio hasta el objetivo

        # Explorar las rutas desde la estación actual
        for estacion_vecina, tiempo in transporte.rutas.get(estacion_actual, []):
            nuevo_tiempo = tiempo_actual + tiempo
            if estacion_vecina not in tiempos or nuevo_tiempo < tiempos[estacion_vecina]:
                tiempos[estacion_vecina] = nuevo_tiempo
                previos[estacion_vecina] = estacion_actual
                heapq.heappush(cola, (nuevo_tiempo, estacion_vecina))

    return None, float('inf')  # Si no hay ruta

def encontrar_mejor_ruta(transporte, origen, destino):
    if regla_transitiva(transporte, origen, destino):
        ruta, tiempo_total = dijkstra(transporte, origen, destino)
        if ruta:
            print(f"Ruta óptima: {' -> '.join(ruta)}")
            print(f"Tiempo total de viaje: {tiempo_total} minutos")
        else:
            print("No se encontró una ruta disponible.")
    else:
        print(f"No existe una ruta indirecta válida entre {origen} y {destino}.")
        
# Ejemplo:
transporte = TransporteMasivo()
transporte.agregar_ruta("A", "B", 10)
transporte.agregar_ruta("B", "C", 15)
transporte.agregar_ruta("C", "D", 5)
transporte.agregar_ruta("A", "D", 30)

# Búsqueda de La mejor ruta
encontrar_mejor_ruta(transporte, "A", "B")  # Puede tomar una ruta directa o indirecta. A -> B -> C -> D

Creado por: Sebastián Villalba
