# Grafo Dirigido Ponderado con Python

Este repositorio contiene un ejemplo de cómo crear y visualizar un grafo dirigido ponderado utilizando las librerías NetworkX y matplotlib en Python.

## Descripción

El código incluido en este repositorio permite representar un grafo dirigido ponderado, donde los nodos están conectados por aristas que tienen un peso asociado. Este tipo de grafo es útil para modelar problemas como redes de transporte, circuitos eléctricos, o relaciones jerárquicas.

En este ejemplo:

Se utiliza NetworkX para manejar la estructura del grafo y sus propiedades.

matplotlib se utiliza para visualizar el grafo, mostrando las conexiones entre nodos y los pesos de cada arista.

El código crea un grafo dirigido con cinco nodos y varias aristas con pesos positivos y negativos, y luego muestra una visualización del grafo.

## Requisitos

Para ejecutar el código necesitarás instalar las siguientes librerías:

NetworkX

matplotlib

Puedes instalarlas usando pip:

pip install networkx matplotlib

Uso

El archivo grafo_dirigido.py contiene el siguiente código para crear y visualizar el grafo:

import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo dirigido
grafo = nx.DiGraph()

# Lista de aristas con pesos según la imagen
edges = [
    (0, 2, -3),
    (1, 0, 8),
    (2, 1, 7),
    (3, 1, 1),
    (4, 0, 2), (4, 1, 4), (4, 3, 2),
]

# Agregar nodos y aristas al grafo
for u, v, w in edges:
    grafo.add_edge(u, v, weight=w)

# Posición de los nodos para una mejor visualización
pos = nx.spring_layout(grafo)

# Dibujar los nodos y las aristas del grafo
nx.draw(grafo, pos, with_labels=True, node_size=700, node_color='lightblue', font_weight='bold', arrows=True)

# Dibujar los pesos de las aristas
edge_labels = {(u, v): w for u, v, w in edges}
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)

# Mostrar el grafo
plt.title("Grafo dirigido ponderado")
plt.show()

Ejemplo de Salida

La imagen generada muestra un grafo dirigido con nodos numerados del 0 al 4, conectados por aristas etiquetadas con sus respectivos pesos.

Contribuir

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request. También puedes abrir issues para reportar errores o sugerir mejoras.

Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
