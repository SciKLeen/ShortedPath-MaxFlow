import math
import networkx as nx
import matplotlib.pyplot as plt
from Data.Point import Point
from Algorithm.Dijkstra.Dijkstra import dijkstra, shortest_path

# Create some point
def Points():

    obj = []

    obj.append(Point('A', 11, 12, {'B': 2,
                                    'E': 3}, 0, 0))
    obj.append(Point('B', 11, 12, {'A': 2,
                                    'C': 4,
                                    'D': 6}, 0, 0))
    obj.append(Point('C', 11, 12, {'B': 4,
                                    'D': 3,
                                    'E': 5}, 0, 0))
    obj.append(Point('D', 11, 12, {'B': 6,
                                    'C': 3}, 0, 0))
    obj.append(Point('E', 11, 12, {'A': 3,
                                    'C': 5}, 0, 0))

    return obj


# Create Graph
def CreateGraph(P):

    filled_dict = {}
    for i in range(0, len(P), 1):
        filled_dict.update({P[i].name: P[i].directions_result})

    return filled_dict


# Color the graph
def draw_edges(x, col, G, pos):
    nx.draw_networkx_edges(G, pos, edgelist = x, width=8, alpha=0.5, edge_color=col);

#Display Graph
def display_Graph(P, Path):
    #title
    plt.title("Graph")
    # Create Graph
    G = nx.DiGraph()

    #Get point and edge
    po_arr = []
    eds_arr = []
    for point in P:
        po_arr.append(point.name)

        for edge in point.directions_result:
            eds_arr.append((point.name, edge))

    G.add_nodes_from(po_arr)                            # Add vertices to the graph
    G.add_edges_from(eds_arr)                           # Add edges to the graph

    pos = nx.spring_layout(G)                           # create Pos

    ed = []
    for i in range (1, len(Path), 1):
        ed.append((Path[i - 1], Path[i]))


    draw_edges(ed, 'blue', G, pos)

    nx.draw(G, pos, with_labels=True, node_size=500, alpha=0.8)  # set properties

    #show
    plt.draw()
    plt.show()


# ---------------------------------------------- "Main Function" ----------------------------------------------
def main(_from, _to):
    _from = _from.upper()
    _to = _to.upper()
    P = Points()

    # Create graph
    graph = CreateGraph(P)

    # find Shortest path
    dist, pred = dijkstra(graph, start='A')
    # print(dist)
    # print(pred)

    # Check the element in the array
    chk_Fr = 0
    chk_To = 0

    for item in P:
        if item.name == _from:
            chk_Fr = 1
        if item.name == _to:
            chk_To = 1

    if chk_Fr & chk_To:
        path = shortest_path(graph, _from, _to)

        '''
        # dist is a dict mapping each node to its shortest distance from the specified starting node:
        # assert dist == {'a': 0, 'c': 3, 'b': 1, 'd': 4}

        # pred is a dict mapping each node to its predecessor node on the shortest path from the specified starting node:
        # assert pred == {'b': 'a', 'c': 'b', 'd': 'c'}
        '''

        # display Graph
        display_Graph(P, path)
        return "Find the object"
    else:
        return "Not Found"

