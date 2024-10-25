# Grafo Dirigido Ponderado en Python

Este repositorio contiene un ejemplo sencillo de cómo crear y visualizar un grafo dirigido ponderado utilizando Python y las librerías NetworkX y Matplotlib.

## Descripción
El código proporciona una implementación básica para:

- Crear un grafo dirigido.
- Agregar nodos y aristas con pesos específicos.
- Visualizar el grafo con los pesos de las aristas.
  
## Requisitos
Antes de ejecutar el código, asegúrate de tener instaladas las siguientes librerías:
- NetworkX
- Matplotlib

Puedes instalarlas utilizando "pip install":

```bash
pip install networkx matplotlib
```

## Cómo Ejecutar el Código
Clona el repositorio o descarga el archivo grafo_dirigido_ponderado.py.

Ejecuta el script desde la línea de comandos o utilizando un entorno de desarrollo como Visual Studio Code, PyCharm, etc.

bash
Copiar código
python grafo_dirigido_ponderado.py
Visualiza el grafo: Se abrirá una ventana mostrando el grafo dirigido con los pesos de las aristas.

## Explicación del Código
Importación de librerías:

python
Copiar código
import matplotlib
from matplotlib import pyplot as plt
import networkx as nx
Creación del grafo dirigido:

python
Copiar código
grafo = nx.DiGraph()
Definición de las aristas y sus pesos:

python
Copiar código
aristas = [
    (0, 2, -3),
    (1, 0, 8),
    (2, 1, 7),
    (3, 1, 1),
    (4, 0, 2),
    (4, 1, 4),
    (4, 3, 2),
]
Agregar aristas al grafo:

python
Copiar código
for origen, destino, peso in aristas:
    grafo.add_edge(origen, destino, weight=peso)
Posicionamiento y dibujo del grafo:

python
Copiar código
posicion = nx.spring_layout(grafo)
nx.draw(grafo, posicion, with_labels=True, node_size=700, node_color='lightblue', font_weight='bold', arrows=True)
Agregar etiquetas de pesos a las aristas:

python
Copiar código
etiquetas_aristas = {(origen, destino): peso for origen, destino, peso in aristas}
nx.draw_networkx_edge_labels(grafo, posicion, edge_labels=etiquetas_aristas)
Mostrar el grafo:

python
Copiar código
plt.title("Grafo Dirigido Ponderado")
plt.show()
Personalización
Puedes modificar la lista aristas para agregar, eliminar o cambiar aristas y pesos según tus necesidades. Por ejemplo, para agregar una nueva arista:

python
Copiar código
aristas.append((2, 4, 5))
Recursos Adicionales
Documentación de NetworkX
Documentación de Matplotlib
Contacto
Si tienes preguntas o sugerencias, no dudes en contactarme a través de mi perfil de GitHub o tomar una consulta gratuita de 30 minutos a través de mi página web:  https://mauroquil-bit.github.io/

