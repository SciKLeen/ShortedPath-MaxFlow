import networkx as nx
import matplotlib.pyplot as plt
import Data.Readfiletxt as rf
from Data.Point import Point
from Data.Edges import Edges
from Algorithm.Dijkstra.Dijkstra import dijkstra, shortest_path


# Check path
def check_path(graph, _from, _to):
    def check_path_recursive(graph, stack_reverse, ps, _str, _to):
        for item in graph[_str]:
            stack_reverse.append(item)
            if item == _to:
                return True
        if len(stack_reverse) > 0:
            _str = stack_reverse.pop()
            ps[_str] = 1
            return check_path_recursive(graph, stack_reverse, ps, _str, _to)

        return False


    ps = {}
    for item in graph:
        ps[item] = 0
    stack_reverse = []

    return check_path_recursive(graph, stack_reverse, ps, _from, _to)


# Create new point
# id, name, longitude, latitude, address
def CreatePoints():
    return rf.Read_PointData()


# Create new edge
# id, street_name, from, to, weight, traffic_flow, max_flow
def CreateEdges():
    return rf.Read_EdgeData()


# Create Graph
def CreateGraph(p, e):
    filled_dict = {}

    # Create null dictionary
    for item in p:
        filled_dict.update({item.getName(): {}})

    # Add edges
    for item in e:
        filled_dict[item.getFrom()].update({item.getTo() : item.getWeight()})

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
def display_Graph(graph, paths, maxflow_edge):
    #title
    plt.title("Graph")
    # Create Graph
    G = nx.DiGraph()

    #Get point and edge
    po_arr = []
    eds_arr = []
    eds_arr_lbl = {}
    for point in graph:
        po_arr.append(point)
        for edge in graph[point]:
            eds_arr.append((point, edge))
            eds_arr_lbl[(point, edge)] = graph[point][edge]

    G.add_nodes_from(po_arr)                            # Add vertices to the graph
    G.add_edges_from(eds_arr)  # Add edges to the graph

    pos = nx.circular_layout(G)
    #pos = nx.spring_layout(G)                           # create Pos

    ed0 = create_shorted_case(paths[0])
    ed1 = create_shorted_case(paths[1])

    # Draw edges
    if len(maxflow_edge) > 0:
        draw_edges(maxflow_edge, 'red', G, pos)
    max_len = max(len(ed0), len(ed1))
    for i in range(0, max_len, 1):
        if len(ed0) > i:
            if len(maxflow_edge) > 0:
                if ed0[i][0] not in maxflow_edge:
                    draw_edges(ed0[i], 'blue', G, pos)
            else:
                draw_edges(ed0[i], 'blue', G, pos)

        if len(ed1) > i:
            if ed1[i][0] not in maxflow_edge:
                if len(ed0) > i:
                    if ed0[i] != ed1[i]:
                        draw_edges(ed1[i], 'gray', G, pos)
                else:
                    draw_edges(ed1[i], 'gray', G, pos)
    # draw_edges(ed0, 'blue', G, pos)
    # draw_edges(ed1, 'yellow', G, pos)
    # draw_edges(maxflow_edge, 'red', G, pos)

    nx.draw(G, pos, with_labels=True, node_size=500, alpha=0.8)  # set properties
    nx.draw_networkx_edge_labels(G, pos, edge_labels=eds_arr_lbl)

    #show
    plt.draw()
    plt.show()


def ifmaxflownotnull(_maxflow, graph, _from, _to):
    path = []
    temp = []


    if len(_maxflow) > 0:
        for item in _maxflow:
            temp.append(graph[item[0]][item[1]])
            del graph[item[0]][item[1]]

        # check path From -> To
        _bool = check_path(graph, _from, _to)
        if _bool == True:
            path, v = shortest_path(graph, _from, _to)


        # resert edge for graph
        for i in range(0, len(_maxflow), 1):
            graph[_maxflow[i][0]][_maxflow[i][1]] = temp[i]

        if _bool == False:
            temp = ''
            edge = ''
            StP, v = shortest_path(graph, _from, _to)

            edges = create_shorted_case(StP)
            for item in edges:
                if (item[0]) in _maxflow:
                    edge = [item[0][0], item[0][1]]
                    temp = graph[item[0][0]][item[0][1]]
                    del graph[item[0][0]][item[0][1]]
                    _bool = check_path(graph, _from, _to)
                    if _bool:
                        path, v = shortest_path(graph, _from, _to)
                        break
            graph[edge[0]][edge[1]] = temp
        # if path == []:
        #     temp = ''
        #     edge = ''
        #     StP, v = shortest_path(graph, _from, _to)
        #     for i in range (0, len(StP) - 1, 1):
        #         if (StP[i], StP[i+1]) in _maxflow:
        #             edge = [(StP[i], StP[i+1])]
        #             temp = (graph[StP[i][0]][StP[i][1]])
        #             del graph[StP[i]][StP[i+1]]
        #             path, v = shortest_path(graph, _from, _to)
        #             break
        #
        #     graph[edge[0]][edge[1]] = temp
    return path, _maxflow


# ---------------------------------------------- "Main Function" ----------------------------------------------
def main(_from, _to):
    _from = _from.upper()
    _to = _to.upper()

    # Pull point, edge, Maxflow data
    P = CreatePoints()
    E, _maxflow = CreateEdges()


    # Create graph
    graph = CreateGraph(P, E)

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
        def CreateNewGraph(graph):
            return graph

        graph0 = CreateNewGraph(graph)
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
        display_Graph(graph, paths, _maxflow)
        return "Find the object"
    else:
        return "Not Found"

