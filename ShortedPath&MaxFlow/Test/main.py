# Nhập khẩu module math để sử dụng.
import math
import networkx                 as nx
import matplotlib.pyplot        as plt
import pylab

# Function
def Insert_Edge(mat, n, Graph):
    for i in range(1, n, 1):
        for j in range(i + 1, n, 1):
            if (mat[i][j] > 0):
                Graph.add_edge(i, j);
            if (mat[j][i] > 0):
                Graph.add_edge(j, i);

    return Graph;

#To mau
def draw_edges(x, col, G, pos):
    nx.draw_networkx_edges(G, pos, edgelist = x, width=8, alpha=0.5, edge_color=col);

def weight_Way(x, mtx):
    sum = 0;
    for item in x:
        sum += mtx[item[0]][item[1]];
    return sum;

def main():
    # 1 - 2
    # 2 - 3
    # 3 - 4
    # 3 - 5
    # 4 - 2
    # 5 - 1

    n = 6
    # Create matrix
    mattrix = [[0, 0, 0, 0, 0, 0],
               [0, 0, 3, 0, 2, 0],
               [0, 3, 0, 1, 0, 0],
               [0, 0, 0, 0, 5, 2],
               [0, 0, 2, 5, 0, 0],
               [0, 1, 0, 0, 0, 0]];

    #title
    plt.title("Graph")
    # Create Graph
    G = nx.DiGraph();

    G.add_nodes_from([1, 2, 3, 4, 5]);
    pos = nx.spring_layout(G)

    draw_edges([(1, 4)], 'r', G, pos);
    draw_edges([(1, 2), (2, 3), (3, 4)], 'b', G, pos);

    G = Insert_Edge(mattrix, n, G);

    nx.draw(G, pos, with_labels=True, node_size=500, alpha=0.8);

    print(weight_Way([(1, 2), (2, 3)], mattrix));

    plt.draw();
    plt.show();

x = main()