from collections import deque

# 1. BASE DE CONOCIMIENTO (HECHOS)
# Definimos los hechos lógicos como conexiones directas comprobables.
# Premisa implicita: Si A está conectado a B, entonces B está conectado a A (Bidireccional).

conexiones_hechos = [
    ("Portal Norte", "Calle 100"),
    ("Calle 100", "Héroes"),
    ("Héroes", "Ricaurte"),
    ("Ricaurte", "Banderas"),
    ("Banderas", "Portal Américas"),
    ("Héroes", "Marly"),
    ("Marly", "Universidades"),
    ("Ricaurte", "Universidades"),
]

# Construcción de la base de conocimiento en forma de diccionario (grafo espacial)

base_conocimiento = {}
for origen, destino in conexiones_hechos:
    base_conocimiento.setdefault(origen, []).append(destino)
    base_conocimiento.setdefault(destino, []).append(origen)


# 2. MOTOR DE INFERENCIA (Reglas y Búsquedas)

def buscar_mejor_ruta(origen, destino, kb):
    """
    Evalúa la base de conocimiento aplicando un algoritmo de búsqueda para encontrar
    la mejor ruta (menor cantidad de paradas)
    """

    # Regla de identidad: Si el origen es igual al destino, no hay que moverse.
    if origen == destino:
        return [origen]

    # Memoria de trabajo del sistema experto
    visitados = set()  # Para evitar ciclos
    cola = deque([[origen]])  # Cada elemento es un camino posible.

    while cola:
        camino_actual = cola.popleft()
        estacion_actual = camino_actual[-1]

        # Regla de infferencia recursiva: Si la estación no ha sido evaluada,
        # explorar sus hechos conocidos (conexiones).

        if estacion_actual not in visitados:
            for vecino in kb.get(estacion_actual, []):
                nuevo_camino = list(camino_actual)
                nuevo_camino.append(vecino)

                # Regla de éxito: Hemos deducido una ruta hasta el destino
                if vecino == destino:
                    return nuevo_camino

                cola.append(nuevo_camino)
            visitados.add(estacion_actual)

        # Regla de fallo: Agotados los hechos, se infiere que no existe ruta posible.
    return None  # No se encontró ruta


# 3. EJECUCIÓN Y CONSULTA

punto_a = "Portal Norte"
punto_b = "Universidades"
ruta_optima = buscar_mejor_ruta(punto_a, punto_b, base_conocimiento)

if ruta_optima:
    print(f"Ruta optima encontrada ({len(ruta_optima) - 1} saltos):")
    print(" -> ".join(ruta_optima))
else:
    print("No se encontró una ruta entre los puntos especificados.")