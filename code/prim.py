
import random
# random.seed(3)


# ---------------------------------------------------------------------------------------
def prim(graph):
    # root = random.choice(graph)
    root = graph[0]
    min_spanning_tree = [root]
    used_nodes = set(root[0][0])
    free_edges = list(graph)
    free_edges.remove(root)
    free_nodes = set(''.join(n[0] for n in free_edges))
    while len(free_nodes) > 0:
        # edges = [edge for edge in free_edges if edge[0][0] in used_nodes or edge[0][1] in used_nodes]
        edges = [edge for edge in free_edges if edge[0][0] in used_nodes]
        print edges
        min_edge = min(edges, key=lambda e: e[1])
        # free_nodes.discard(min_edge[0][0])
        free_nodes.discard(min_edge[0][1])
        free_edges.remove(min_edge)
        min_spanning_tree.append(min_edge)
        used_nodes.update(min_edge[0])
        # print 'edges: %s' % str(edges)
        # print 'min_edge: %s' % str(min_edge)
        print 'used_nodes: %s' % str(used_nodes)
        print 'free_edges: %s' % str(free_edges)
        # print 'min_spanning_tree(%i): %s' % (len(min_spanning_tree), str(min_spanning_tree))
    return min_spanning_tree

        
# ---------------------------------------------------------------------------------------
def read_graph(file_name='graph.txt'):
    inf = open(file_name, 'r')
    graph = []
    for line in inf:
        [n0, n1, c] = line.strip().upper().split(',')
        graph.append(('%s%s' % (n0, n1), int(c)))
    inf.close()
    return graph


# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    min_spanning_tree = prim(read_graph())
    print min_spanning_tree
