import unittest
import networkx as nx
from grafo_dirig_pond import G, edges

class TestGrafoDirigidoPonderado(unittest.TestCase):

    def setUp(self):
        self.grafo = G

    def test_numero_de_nodos(self):
        self.assertEqual(len(self.grafo.nodes), 5, "El número de nodos debería ser 5")

    def test_numero_de_aristas(self):
        self.assertEqual(len(self.grafo.edges), 7, "El número de aristas debería ser 7")

    def test_pesos_aristas(self):
        for (u, v, w) in edges:
            self.assertEqual(self.grafo[u][v]['weight'], w, f"El peso de la arista ({u}, {v}) debería ser {w}")

if __name__ == '__main__':
    unittest.main()
