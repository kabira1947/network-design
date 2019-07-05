import  networkx as n
import matplotlib.pyplot as p


g=n.Graph()
g.add_node(1)
g.add_nodes_from([2,3,4,5])



g.add_edge(1,8)
g.add_edges_from([(1,2),(2,4),(5,3),(2,5)])
n.draw_networkx(g,node_color='green',node_size=700)
print(n.info(g))

p.show()
