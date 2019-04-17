import json
from Algorithm.Dijkstra.Dijkstra import dijkstra, shortest_path

def getData():
    points = "data\points.json"
    edges = "data\edges.json"    
    with open(points, encoding='utf-8') as fh:
        points = json.load(fh)
        
    with open(edges, encoding='utf-8') as fh1:
        edges = json.load(fh1)
        
        
    return points, edges

def CreateGraph(points, edges):
    #create dictionary null
    _dict = {};
    max_flow = []
    
    for point in points:
        _dict.update({point: {}})
        
    # Add edges
    for edge in edges:
        distance = edges[edge]['distance']
        _dict[edges[edge]['from']].update({edges[edge]['to'] : int(distance)})
        #print(type(edges[edge]['trafficflow']))
        trafficflow = int(edges[edge]['trafficflow'])
        maxflow = int(edges[edge]['maxflow'])
        if ((trafficflow/maxflow)*100) >= 80:
            max_flow.append((edges[edge]['from'], edges[edge]['to']))
   
    return _dict, max_flow

#------------------------------------------------------------------------------
    
# Check path by DFS
def check_path(graph, _from, _to):
    def check_path_recursive(graph, stack_reverse, ps, _str, _to):
        for item in graph[_str]:
            if(ps[item] == 0):
                stack_reverse.append(item)
                if item == _to:
                    return True
        if len(stack_reverse) > 0:
            _str = stack_reverse.pop()
            ps[_str] = 1
            return check_path_recursive(graph, stack_reverse, ps, _str, _to)
#
        return False
#
#
    ps = {}
    for item in graph:
        ps[item] = 0
    stack_reverse = []
#
    return check_path_recursive(graph, stack_reverse, ps, _from, _to)
#------------------------------------------------------------------------------

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
            
            print("LOL")
            edges = create_shorted_case(StP)
            print(edges)
            
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
    return path, _maxflow
#------------------------------------------------------------------------------
def getlstCoordinates(points, _path):
    lst =[];
    
    for item in _path:
        _lat = float(points[item]['latitude'])
        _lng = float(points[item]['longtitude'])
        
        lst.append([_lat, _lng])
    
    return lst

def ProcessLine(ls0, ls1, ls2):
    for i in range(0, len(ls0), 1):
        if ls0[i] in ls1:
            ls1.remove(ls0[i])

    for i in range(0, len(ls2), 1):
        if ls2[i] in ls0:
            ls0.remove(ls2[i])
    return ls0, ls1, ls2
    


def shortestpath(_from, _to):
    points, edges = getData()
    graph, _maxflow = CreateGraph(points, edges)
    
    # check valid values
    for item in points:
        if item == _from:
            chk_Fr = 1
        if item == _to:
            chk_To = 1
    
    if chk_Fr & chk_To:
        paths = []
        
        def CreateNewGraph(graph):
            return graph

        graph0 = CreateNewGraph(graph)
        path0, v = shortest_path(graph0, _from, _to);
        path1, maxflow_edge = ifmaxflownotnull(_maxflow, graph0, _from, _to)
        
        
    ls0 = getlstCoordinates(points, path0)
    ls1 = getlstCoordinates(points, path1)
    ls2 = getlstCoordinates(points, [_maxflow[0][0], _maxflow[0][1]])

    #ls0, ls1, ls2 = ProcessLine(ls0, ls1, ls2)

    return [ls0, ls1, ls2]
    #print("line 1:", ls0)
    #print("line 2:", ls1)
    #print("Max Flow", ls2)
        


#main('06', '03')