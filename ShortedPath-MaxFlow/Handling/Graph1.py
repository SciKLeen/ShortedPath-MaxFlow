def ifmaxflownotnull(_maxflow, graph, _from, _to):
    path = []
    temp = []


    if len(_maxflow) > 0:
        for item in _maxflow:
            temp.append(graph[item[0]][item[1]])
            del graph[item[0]][item[1]]

        _bool = check_path(graph, _from, _to)

        for i in range(0, len(_maxflow), 1):
            graph[_maxflow[i][0]][_maxflow[i][1]] = temp

        print(graph)
        if _bool:
            path, v = shortest_path(graph, _from, _to)
        else:
            if path == []:
                temp = ''
                edge = ''
                StP, v = shortest_path(graph, _from, _to)
                for i in range (0, len(StP) - 1, 1):
                    if (StP[i], StP[i+1]) in _maxflow:
                        edge = [(StP[i], StP[i+1])]
                        temp = (graph[StP[i][0]][StP[i][1]])
                        del graph[StP[i]][StP[i+1]]
                        path, v = shortest_path(graph, _from, _to)
                        break

                graph[edge[0]][edge[1]] = temp
    return path, _maxflow