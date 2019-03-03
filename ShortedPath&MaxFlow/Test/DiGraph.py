import networkx as nx
import matplotlib.pyplot as plt


def _main():
    g = nx.DiGraph()

    g.add_edge(2, 3, key=0, weight=1)
    g.add_edge(2, 3, key=1, weight=3)
    g.add_edge(3, 4, weight=5)
    g.add_edge(5, 1, weight=10)
    g.add_edge(1, 3, weight=15)


    pos = nx.circular_layout(g)

    edge_labels = {(u, v): d['weight'] for u, v, d in g.edges(data=True)}

    nx.draw_networkx_nodes(g, pos, node_size=300)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

    plt.title("Graph Title")
    plt.axis('off')

    plt.show()


if __name__ == '__main__':
    _main()