import networkx as nx
import matplotlib.pyplot as plt

graph = nx.DiGraph()
# Adding the nodes and dependencies
graph.add_nodes_from(["A", "FA", "FH", "H", "M"])
graph.add_edges_from([("M", "FH"), ("M", "H"), ("FH", "H"), ("H", "A"), ("FA", "A")])

pos = {"A": (0, 0), "FA": (1, 1), "FH": (0, 2), "H": (1, 0), "M": (2, 1)}


nx.draw(
    graph,
    pos,
    with_labels=True,
    node_size=1000,
    node_color="skyblue", 
    font_size=10,  
    font_color="black",
    edge_color="gray", 
    arrowsize=15,
    connectionstyle="arc3,rad=0.1", 
)

# plt.savefig("bonus.png")
plt.show()
