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

g = {'A': {'B': 1, 'D': [5, 1]}, 'B': {'C': 1}, 'C': {'D': 1, 'F': [5, 1]}, 'D': {'F': 1, 'E': 2}, 'E': {}, 'F': {'E': 1, 'D': 1}}
