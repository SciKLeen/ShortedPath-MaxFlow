import networkx as nx

# and the following code block is not needed
# but we want to see which module is used and
# if and why it fails
try:
    import pygraphviz
    from networkx.drawing.nx_agraph import write_dot
    print("using package pygraphviz")
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import write_dot
        print("using package pydot")
    except ImportError:
        print()
        print("Both pygraphviz and pydot were not found ")
        print("see  https://networkx.github.io/documentation/latest/reference/drawing.html")
        print()
        raise

G = nx.DiGraph()

G.add_node(1,pos="100,100")

G.add_node(2,pos="0,0")
G.add_node(3,pos="200,0")
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,1)

print(G.edges(data=True))
# [(1, 1, {}), (1, 2, {}), (1, 3, {})]

nx.write_dot(G,'graph.dot')