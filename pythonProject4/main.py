
def Graph():
    def run():
        run=run()
        graph = Graph()


    graph.add_node("SportsComplex")
    graph.add_node("Siwaka")
    graph.add_node("Ph.1A")
    graph.add_node("Ph.1B")
    graph.add_node("STC")
    graph.add_node("Phase2")
    graph.add_node("Phase3")
    graph.add_node("ParkingLot")
    graph.add_node("J1")
    graph.add_node("Mada")


    graph.add_edge("SportsComplex", "Siwaka", weight="450")
    graph.add_edge("Siwaka", "Ph.1A", weight="10")
    graph.add_edge("Siwaka", "Ph.1B", weight="230")
    graph.add_edge("Ph.1A", "Ph.1B", weight="100")
    graph.add_edge("Ph.1B", "STC", weight="50")
    graph.add_edge("Ph.1B", "Phase2", weight="keriRd112")
    graph.add_edge("STC", "Phase2", weight="50")
    graph.add_edge("Phase2", "Phase3", weight="500")
    graph.add_edge("Phase2", "J1", weight="600")
    graph.add_edge("J1", "Mada", weight="200")
    graph.add_edge("STC", "ParkingLot", weight="250")
    graph.add_edge("ParkingLot", "Mada", weight="700")
    graph.add_edge("Phase3", "ParkingLot", weight="350")
    graph.add_edge("Ph.1A", "Mada", weight="850")
    alt =Greddy(graph,"SportsComplex","Ph1.A")
    path, path_length =alg.search()
    print("->".join(path))
    print(f"Lengthof the path: {path_length}")
    if __name__=='__main__':
        run()

        alt = UCS(graph, "SportsComplex", "Ph1.A")
        path, path_length = alg.search()
        print("->".join(path))
        print(f"Lengthof the path: {path_length}")
        if __name__ == '__main__':
            run()





        node_pos = nx.get_node_attributes(G, 'pos')
        # call BFS to return set of all possible routes to the goal
        route_bfs = BfsTraverser()
        routes = route_bfs.BFS(G, "SportsComplex", "ParkingLot")
        print(route_bfs.visited)
        route_list = route_bfs.visited
        # color the nodes in the route_bfs
        node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
        peru_colored_edges = list(zip(route_list, route_list[1:]))
        # color the edges as well
        # print(peru_colored_edges)
        edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
        arc_weight = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
        nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col)
        # nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

