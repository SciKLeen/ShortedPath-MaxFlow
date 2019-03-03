from Algorithm.Dijkstra.Dijkstra import dijkstra, shortest_path
from Data.Point import Point


def points():

    obj = []

    obj.append(Point('A', 11, 12, {'B': 1,
                                   'D': 5}, 0, 0))
    obj.append(Point('B', 11, 12, {'C': 1}, 0, 0))
    obj.append(Point('C', 11, 12, {'F': 1}, 0, 0))
    obj.append(Point('D', 11, 12, {'E': 1,
                                   'F': 1}, 0, 0))
    obj.append(Point('E', 11, 12, {'A': 1}, 0, 0))
    obj.append(Point('F', 11, 12, {'D': 1,
                                   'E': 1}, 0, 0))

    return obj


def create_graph(p):

    filled_dict = {}
    for i in range(0, len(p), 1):
        filled_dict.update({p[i].name: p[i].directions_result})

    return filled_dict


def cv_list_to_string(ar):
    _str = ''
    for i in range(0, len(ar), 1):
        if i > 0:
            _str = _str + ','
        _str = _str + str(ar[i])
    return _str


def allpath(g, l, _from, _to):

    for item in g:
        if(_to in g[item]):
            path, value = shortest_path(graph, _from, _to)
            l[cv_list_to_string(path)] = value
            print(path)
            print(path[len(path) - 2])
            del g[path[len(path) - 2]][path[len(path) - 1]]
            return allpath(g, l, _from, _to)
    return



p = points()


graph = create_graph(p)
List_path = {}
allpath(graph, List_path, 'A', 'E')

print(List_path)

