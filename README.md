# Buscador de rutas de TransMilenio

Este programa encuentra una ruta entre estaciones usando las conexiones definidas en el código. Considera que las conexiones funcionan en ambos sentidos y busca un camino con la menor cantidad de saltos.

## Requisitos

- Python 3
- No necesita instalar paquetes adicionales; solo usa la biblioteca estándar de Python.

## Cómo ejecutarlo

Abre una terminal en esta carpeta y ejecuta:

```powershell
python main.py
```

La salida actual es:

```text
Ruta optima encontrada (4 saltos):
Portal Norte -> Calle 100 -> Héroes -> Ricaurte -> Universidades
```

## Archivos

- `main.py`: programa que construye las conexiones y busca la ruta.
- `README.md`: esta guía.

## Cambiar las estaciones consultadas

En `main.py`, cambia los valores de `punto_a` y `punto_b` por los nombres de las estaciones que quieras conectar. El nombre debe coincidir con el que aparece en `conexiones_hechos`.

Para agregar una conexión, añade un par de estaciones a `conexiones_hechos`, por ejemplo:

```python
("Estacion A", "Estacion B"),
```
