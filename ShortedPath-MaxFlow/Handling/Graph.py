import math
import networkx as nx
import matplotlib.pyplot as plt
from Data.Point import Point
from Algorithm.Dijkstra.Dijkstra import dijkstra, shortest_path

# Create some point
def Points():

    obj = []

    obj.append(Point('A', 11, 12, {'B': 1,
                                   'D': 5}, 0, 0))
    obj.append(Point('B', 11, 12, {'C': 1}, 0, 0))
    obj.append(Point('C', 11, 12, {'D': 1,
                                   'F': 1}, 0, 0))
    obj.append(Point('D', 11, 12, {'E': 2,
                                   'F': 1}, 0, 0))
    obj.append(Point('E', 11, 12, {'A': 1}, 0, 0))
    obj.append(Point('F', 11, 12, {'D': 1,
                                   'E': 1}, 0, 0))

    return obj


# Create Graph
def CreateGraph(P):

    filled_dict = {}
    for i in range(0, len(P), 1):
        filled_dict.update({P[i].name: P[i].directions_result})

    return filled_dict


# Color the graph
def draw_edges(x, col, G, pos):
    nx.draw_networkx_edges(G, pos, edgelist=x, width=8, alpha=0.5, edge_color=col);


#Create edge to Draw
def create_shorted_case(path):
    ed = []
    for i in range(1, len(path), 1):
        ed.append([(path[i - 1], path[i])])
    return ed


#Display Graph
def display_Graph(p, paths, maxflow_edge):
    #title
    plt.title("Graph")
    # Create Graph
    G = nx.DiGraph()

    #Get point and edge
    po_arr = []
    eds_arr = []
    for point in p:
        po_arr.append(point.name)
        for edge in point.directions_result:
            eds_arr.append((point.name, edge))

    G.add_nodes_from(po_arr)                            # Add vertices to the graph
    G.add_edges_from(eds_arr)                           # Add edges to the graph

    pos = nx.spring_layout(G)                           # create Pos

    ed0 = create_shorted_case(paths[0])
    ed1 = create_shorted_case(paths[1])
    maxflow_edge = create_shorted_case(maxflow_edge)

    # Draw edges
    if len(maxflow_edge) > 0:
        draw_edges(maxflow_edge[0], 'red', G, pos)
    max_len = max(len(ed0), len(ed1))
    for i in range(0, max_len, 1):
        if len(ed0) > i:
            if len(maxflow_edge) > 0:
                if maxflow_edge[0] != ed0[i]:
                #     draw_edges(maxflow_edge[0], 'red', G, pos)
                # else:
                    draw_edges(ed0[i], 'blue', G, pos)
            else:
                draw_edges(ed0[i], 'blue', G, pos)
        if len(ed1) > i:
            if len(ed0) > i:
                if ed0[i] != ed1[i]:
                    draw_edges(ed1[i], 'gray', G, pos)
            else:
                draw_edges(ed1[i], 'gray', G, pos)
    # draw_edges(ed0, 'blue', G, pos)
    # draw_edges(ed1, 'yellow', G, pos)
    # draw_edges(maxflow_edge, 'red', G, pos)

    nx.draw(G, pos, with_labels=True, node_size=500, alpha=0.8)  # set properties

    #show
    plt.draw()
    plt.show()


def ifmaxflownotnull(_maxflow, graph, _from, _to):
    maxflow_edge = []
    path = []
    if _maxflow != '':
        maxflow_edge = _maxflow.split('-')

        temp = graph[maxflow_edge[0]][maxflow_edge[1]]

        del graph[maxflow_edge[0]][maxflow_edge[1]]

        path, v = shortest_path(graph, _from, _to)

        graph[maxflow_edge[0]][maxflow_edge[1]] = temp

    return path, maxflow_edge


# ---------------------------------------------- "Main Function" ----------------------------------------------
def main(_from, _to, _maxflow):
    _from = _from.upper()
    _to = _to.upper()
    _maxflow = _maxflow.upper()

    P = Points()

    # Create graph
    graph = CreateGraph(P)

    # Check the element in the array
    chk_Fr = 0
    chk_To = 0

    # check valid values
    for item in P:
        if item.name == _from:
            chk_Fr = 1
        if item.name == _to:
            chk_To = 1

    if chk_Fr & chk_To:

        paths = []
        graph0 = graph
        path0, v = shortest_path(graph0, _from, _to)

        path1, maxflow_edge = ifmaxflownotnull(_maxflow, graph0, _from, _to)

        paths.append(path0)
        paths.append(path1)

        '''
        # dist is a dict mapping each node to its shortest distance from the specified starting node:
        # assert dist == {'a': 0, 'c': 3, 'b': 1, 'd': 4}

        # pred is a dict mapping each node to its predecessor node on the shortest path from the specified starting node:
        # assert pred == {'b': 'a', 'c': 'b', 'd': 'c'}
        '''

        # display Graph
        display_Graph(P, paths, maxflow_edge)
        return "Find the object"
    else:
        return "Not Found"

