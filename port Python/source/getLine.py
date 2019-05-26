import json
from Algorithm.Dijkstra.Dijkstra import dijkstra, shortest_path

def getData():
    points = "static/JSON/points.json"
    edges = "static/JSON/edges.json"    
    with open(points, encoding='utf-8') as fh:
        points = json.load(fh)
        
    with open(edges, encoding='utf-8') as fh1:
        edges = json.load(fh1)
        
        
    return points, edges

def CreateGraph(points, edges):
    #create dictionary null
    _dict = {}
    max_flow = []
    
    for point in points:
        _dict.update({point: {}})
        
    # Add edges
    for edge in edges:
        distance = edges[edge]['distance']
        _dict[edges[edge]['from']].update({edges[edge]['to'] : int(distance)})
        #print(type(edges[edge]['trafficflow']))
        #trafficflow = int(edges[edge]['trafficflow'])
        #maxflow = int(edges[edge]['maxflow'])
        #if ((trafficflow/maxflow)*100) >= 80:
        #    max_flow.append((edges[edge]['from'], edges[edge]['to']))
   
    return _dict#, max_flow

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
        # for item in _maxflow:
        #     temp.append(graph[item[0]][item[1]])
        #     del graph[item[0]][item[1]]
        for items in _maxflow:
            for i in range (1, len(items), 1):
                temp.append(graph[items[i - 1]][items[i]])
                del graph[items[i - 1]][items[i]]


        # check path From -> To
        _bool = check_path(graph, _from, _to)
        if _bool == True:
            path, dist = shortest_path(graph, _from, _to)


        # resert edge for graph
        for i in range(0, len(_maxflow), 1):
            graph[_maxflow[i][0]][_maxflow[i][1]] = temp[i]

        if _bool == False:
            temp = ''
            edge = ''
            StP, v = shortest_path(graph, _from, _to)
            
            print("LOL")
            edges = create_shorted_case(StP)
            #print(edges)
            
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
    return path, dist
#------------------------------------------------------------------------------
def getlstCoordinates(points, _path):
    lst =[]
    for item in _path:
        lst.append(points[item])
    return lst

def getlstCoordinatesFlow(points, _flow):
    ls = []
    for items in _flow:
        ls.append([points[items[0]], points[items[1]]])
    return ls

def ProcessLine(ls0, ls1, ls2):
    for i in range(0, len(ls0), 1):
        if ls0[i] in ls1:
            ls1.remove(ls0[i])

    for i in range(0, len(ls2), 1):
        if ls2[i] in ls0:
            ls0.remove(ls2[i])
    return ls0, ls1, ls2
    

def getTheContent(points, _dict):
    for item in _dict:
        for point in points:
            if(points[point]['latitude'] == str(item[0]) and points[point]['longtitude'] == str(item[1])):
                _dict.append(points[point])
                #print([point])
                return
    return _dict



# Check Flow
def checkFlow(path, maxflow_line):
    _flow = []
    for items in maxflow_line:
        temp = 0
        for item in items:
            if(item not in path):
                temp = 1
                break
        if(temp == 0):
            _flow.append(items)
    return _flow

def shortestpath(_from, _to, _maxflow):
    points, edges = getData()
    graph = CreateGraph(points, edges)

    # check valid values
    #check input
    chk_Fr = chk_To = False
    for item in points:
        if points[item]['Name'] == _from:
            chk_Fr = True
            _from = item
        if points[item]['Name'] == _to:
            chk_To = True
            _to = item


    if chk_Fr & chk_To:
        path0 = []
        path1 = []
        ls2 = []
        dist0 = 0
        dist1 = 0

        def CreateNewGraph(graph):
            return graph

        graph0 = CreateNewGraph(graph)

        # Get line Path 0
        path0, dist0 = shortest_path(graph0, _from, _to)

        # Check Flow of Path 0
        _Flow = checkFlow(path0, _maxflow)

        if (len(_Flow) > 0):
            path1, dist1 = ifmaxflownotnull(_Flow, graph0, _from, _to)
        
        #return _maxflow
        ls0 = getlstCoordinates(points, path0)
        ls1 = getlstCoordinates(points, path1)
        for item in _Flow:
            ls2.append(getlstCoordinates(points, item))
 
        return [ls0, ls1, ls2, dist0, dist1]
    return

#shortestpath('Cổng 1 Đại Học Công Nghiệp', 'Công ty TNHH Đất Mũi', 'Bún măm Thu', 'Công Ty Tnhh Thương Mại Phát Triển Xây Dựng Minh Hùng')
