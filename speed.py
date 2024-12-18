import DGraphHW as DG


"""
Given the following

a graph G, 
starting node start_node,
minimum weight min_weight

determine if there is path 
in G starting at the start_node that 
can be indefinitely followed with 
every edge having weight at least 
min_weight

If such a path exists, return a 
list of node labels, like 
['a','c','f','c']
with the last node label 
being equal to one of the earlier 
ones in the same list.

If no such path exists, return None

Note: it is fine if this method changes the graph G.
"""
def find_indefinite_path(G, start_node, min_weight):
    setlis = G.getEdgeSet()
    for i in setlis:
        lis = list(i)
        if G.getEdgeWeight(lis[0], lis[1]) < min_weight:
            G.removeEdge(lis[0], lis[1])
    stend= G.detect_cycle(start_node)
    if stend == None:
        return None
    stend = list(stend)
    setlis = G.getEdgeSet()
    path = ()
    for i in setlis:
        if i[0] == stend[1]:
            pass
    return stend

def findInital(start_node, end1, end2):
    visited = [start_node]
    for node in G.getEdgeSet():
        print(node)
    pass

f = open('roads.txt', 'r')

G = DG.DGraph()
G.loadJSON(f.read())

print("Indefinite path is ")
print(str(find_indefinite_path(G, 'a', 50)))
print(str(findInital('e','o','f')))
