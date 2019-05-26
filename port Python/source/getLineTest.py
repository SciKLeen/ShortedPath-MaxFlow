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

        #print(_Flow0, "--------------")
        # check path From -> To
        _bool = check_path(graph, _from, _to)
        if _bool == True:
            path, dist = shortest_path(graph, _from, _to)
            
        # else:
        #     temp = ''
        #     edge = ''
        #     StP, v = shortest_path(graph, _from, _to)
            
        #     print("LOL")
        #     edges = create_shorted_case(StP)
        #     #print(edges)
            
        #     for item in edges:
        #         if (item[0]) in _maxflow:
        #             edge = [item[0][0], item[0][1]]
        #             temp = graph[item[0][0]][item[0][1]]
        #             del graph[item[0][0]][item[0][1]]
        #             _bool = check_path(graph, _from, _to)
        #             if _bool:
        #                 path, v = shortest_path(graph, _from, _to)
        #                 break
        #     graph[edge[0]][edge[1]] = temp

        # resert edge for graph
        for items in _maxflow:
            for i in range(1, len(items), 1):
                graph[items[i -1]][items[i]] = temp[i - 1]
    print(dist)
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
def checkFlow(path, maxflow_line):#, status):
    _flow = []
    # if(status == 0):
    for items in maxflow_line:
        temp = 0
        index = -1
        for i in range (0, len(items), 1):
            if(items[i] not in path):
                temp = 1
                break
            else:
                index1 = path.index(items[i])
                if(i > 0):
                    print(index1, index)
                    if(index1 - index != 1):
                        temp = 1
                        break
                index = index1
        if(temp == 0):
            _flow.append(items)
    # else:
    #     for items in maxflow_line:
    #         temp = 0
    #         for item in items:
    #             if(item not in path):
    #                 temp = 1
    #                 break
    #         if(temp == 0 and len(items) > 2):
    #             _flow.append(items)
    return _flow

#processing input
def preprocessing(_str):

    lst = []
    lstRaw = (_str.lower()).split(',')
    print(lstRaw)
    for i in range (0, len(lstRaw), 1):
        lstRaw[i] = lstRaw[i].strip()
    print(lstRaw)
    if(lstRaw[0][0].isdigit()):
        street = lstRaw[0].split(' ')
        lst.append(street[0])

        temp = ''
        for i in range (1, len(street), 1):
            if(street[i] != ''):
                temp = temp + " " + street[i]
        temp = temp.strip()
        lst.append(temp)
    
        for i in range (1, len(lstRaw), 1):
            street = lstRaw[i].split(' ')
            temp = ''
            for i in range (0, len(street), 1):
                    if(street[i] != ''):
                        temp = temp + " " + street[i]
            temp = temp.strip()
            lst.append(temp)
    else:
        lst = lstRaw
    return lst


def checkValidPath(input, points):
    _chk = False
    point = ''
    #processing input
    lst = preprocessing(input)

    #for item in points:
        # if points[item]['Name'] == _from:
        #     chk_Fr = True
        #     _from = item
        # if points[item]['Name'] == _to:
        #     chk_To = True
        #     _to = item

    i = 0
    print("---------------", lst)
    if (lst[0].isdigit()):
        # duyet theo ten dương co so duong
        temp = 10000
        for item in points:
            address = points[item]['address'].lower()
            if( address.find(lst[1]) >= 0):
                dataSnum = int(points[item]['streetnumber'])
                inputSnum = int(lst[0])
                #print(dataSnum, inputSnum, '-----------------------')
                if( abs(dataSnum - inputSnum) < temp):
                    temp = abs(dataSnum - inputSnum)
                    point = item
                    _chk = True
                    #print(temp)
    else:
        # duyet theo ten dương khi hong co so duong
        temp = 10000
        for item in points:
            address = points[item]['address'].lower()
            if( address.find(lst[1]) >= 0):
                dataSnum = int(points[item]['streetnumber'])
                inputSnum = 0
                if( abs(dataSnum - inputSnum) < temp):
                    temp = abs(dataSnum - inputSnum)
                    point = item
                    _chk = True
        

    return _chk, point


def shortestpath(_from, _to, _maxflow):
    points, edges = getData()
    graph = CreateGraph(points, edges)

    # check valid values
    #check input
    chk_Fr, _from = checkValidPath(_from, points)
    chk_To, _to = checkValidPath(_to, points)

    #print(chk_Fr, _from, "------------------------------")
    #print(chk_To, _to, "------------------------------")
    if chk_Fr & chk_To:
        path0 = []
        path1 = []
        path2 = []

        dist0 = 0
        dist1 = 0
        dist2 = 0


        # create new grap variable
        def CreateNewGraph(graph):
            return graph

        graph0 = CreateNewGraph(graph)

        # Get line Path 0
        path0, dist0 = shortest_path(graph0, _from, _to)

        #print(_maxflow, "------------------")
        _Flow1 = []
        _Flow0 = []
        # Check Flow of Path 0
        _Flow0 = checkFlow(path0, _maxflow)
        print(_Flow0)
        if (len(_Flow0) > 0):
            path1, dist1 = ifmaxflownotnull(_Flow0, graph0, _from, _to)
            
            # Check flow of Path 1
            _Flow1 = checkFlow(path1, _maxflow)
            if(len(_Flow1) > 0):
                path2, dist2 = ifmaxflownotnull(_maxflow, graph0, _from, _to)
        
        #return _maxflow
        ls0 = getlstCoordinates(points, path0)
        ls1 = getlstCoordinates(points, path1)
        ls2 = getlstCoordinates(points, path2)

        lsFlow = []
        #print(_Flow0, " ", _Flow1)
        _Flow = _Flow0 + _Flow1
        for item in _Flow:
            lsFlow.append(getlstCoordinates(points, item))

        return [ls0, ls1, ls2, lsFlow, dist0, dist1, dist2]
    return

#shortestpath('Cổng 1 Đại Học Công Nghiệp', 'Công ty TNHH Đất Mũi', 'Bún măm Thu', 'Công Ty Tnhh Thương Mại Phát Triển Xây Dựng Minh Hùng')
