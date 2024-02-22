from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges"])

nodes = ["A", "B", "C", "D"]
edges = [("A","B"), ("A", "B"),
         ("A","C"), ("A", "C"),
         ("A","D"), ("B", "D"), ("C", "D")]

G = Graph(nodes, edges) #first data structure to represent Graphs
print(G)
print()

def adjacency_dict(graph): #second data structure to represent Graphs
	"""Return the adjency list representation of the graph."""

	adj = {node : [] for node in graph.nodes}
	for edge in graph.edges:
		node1, node2 = edge[0], edge[1]
		adj[node1].append(node2)
		adj[node2].append(node1)

	return adj

print(adjacency_dict(G))


def adjacency_matrix(graph): #third data structure to represent Graphs
	"""Return the adjacency matrix of the graph."""

	adj = [[0 for node in graph.nodes] for node in graph.nodes]
	for edge in graph.edges:
		node1, node2 = edge[0], edge[1]
		adj[node1][node2] += 1
		adj[node2][node1] += 1

	return adj

nodes = range(4)
edges = [(0,1),(0,1),
         (0,2),(0,2),
         (0,3),(1,3),(2,3)]
G = Graph(nodes, edges)

print(adjacency_matrix(G))