from pyvis.network import Network
import networkx as nx

G = Network(height=800, width=800, notebook=False)
G.toggle_hide_edges_on_drag(True)
G.barnes_hut()
G.from_nx(nx.davis_southern_women_graph())
G.show("ex.html")
