# Pathfinding Starter Code
Random Pathing Algo:
    The random pathing algorithm randomly picks any node adjacent to the current node with one restriction, it cannot pick the node it was previously on. If there is only one node adjacent, the restriction is ignored to avoid being unable to navigate out of a dead end. The restriction helps with reducting the total number of moves and number of potetial loops occuring (No bouncing back and forth between the same nodes). Aditionally, the player must arrive at the target node before being allowed to exit
Scoreboard:
    The feature added to the scoreboard is the Unique number of nodes visited. This tells you how many of the nodes present on the graph were visited by the player. This does not include starting on the start node, only nodes that the player moves on to. Ie if a graph is node 1 -> node 2 -> node 3 and player takes path 1 -> 2 -> 3 only nodes 2 and 3 were visited

F_W
    added global_game_data.graph_paths.append(f_w.F_W.floyd_Warshall(global_game_data.target_node[global_game_data.current_graph_index])) to def set_current_graph_paths() in pathing.py
    added F_W player into config_data.py
    and commented out djikstra