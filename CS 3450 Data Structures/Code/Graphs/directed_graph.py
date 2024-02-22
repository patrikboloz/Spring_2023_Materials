from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges", "is_directed"])




def adjacency_dict(graph):
	"""Returns the adjacency list representation of the graph.

	Assumes that graph.nodes is qeuivalent to range(len(graph.nodes))."""

	adj = {node : [] for node in graph.nodes}
	for edge in graph.edges:
		node1, node2 = edge[0], edge[1]
		adj[node1].append(node2)
		if not graph.is_directed:
			adj[node2].append(node1)
	return adj

def adjacency_matrix(graph):
	"""Returns the adjancency matrix of the graph."""

	adj = [[0 for node in graph.nodes] for node in graph.nodes]
	for edge in graph.edges:
		node1, node2 = edge[0], edge[1]
		adj[node1][node2] += 1
		if not graph.is_directed:
			adj[node2][node1] += 1
	return adj


G = Graph(nodes=range(3), edges=[(1,0),(1,2),(0,2)], is_directed=False)

print(adjacency_dict(G))
print(adjacency_matrix(G))

G2 = Graph(nodes=range(3), edges=[(1,0),(1,2),(0,2)], is_directed=True)
print(adjacency_dict(G2))
print(adjacency_matrix(G2))