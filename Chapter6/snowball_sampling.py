import networkx as nx

def get_json_name(graph, name):
    """
    Download the LiveJournal page of name, and adds the related links to the graph
    Note: this function modifies the graph!
    """
    try:
        import urllib.request as urllib2
    except ImportError:
        import urllib2

    response = urllib2.urlopen('http://www.livejournal.com/misc/fdata.bml?user=' + name)
    valid_lines = [line for line in response.read().splitlines() if (len(line) > 0 and not line.startswith(b'#'))]
    for line in valid_lines:
        chunks = line.decode('utf8').split(" ")
        if chunks[0] == ">":
            graph.add_edge(name, chunks[1])
        else:
            graph.add_edge(chunks[1], name)
    return


def snowball_sampling(graph, max_depth, central_name, sampling_rate=1.0):
    """
    Recursively add nodes, one depth at the time, till max_depth is reached
    Note: this function modifies the graph!
    """
    import random

    graph.add_node(central_name)

    for depth in range(max_depth):
        print ("Reching depth", depth)
        nodes_that_depth = [node for node in graph.nodes() if
                            nx.shortest_path_length(graph, source=central_name, target=node) == depth]
        print (" new nodes to investigate:", nodes_that_depth)

        for node in nodes_that_depth:

            if len(nodes_that_depth) == 1:
                get_json_name(graph, node)

            elif random.random() <= sampling_rate:
                get_json_name(graph, node)

            else:
                # Sampling stops here
                pass


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    G = nx.Graph()
    snowball_sampling(G, 2, 'alberto')
    nx.draw(G)
    plt.show()