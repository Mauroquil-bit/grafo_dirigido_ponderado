import matplotlib
from matplotlib import pyplot as plt
import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

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
    G.add_edge(u, v, weight=w)

# Posición de los nodos para una mejor visualización
pos = nx.spring_layout(G)

# Dibujar los nodos y las aristas del grafo
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_weight='bold', arrows=True)

# Dibujar los pesos de las aristas
edge_labels = {(u, v): w for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostrar el grafo
plt.title("Grafo dirigido ponderado")
plt.show()
