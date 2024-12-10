Dijkstra's Algorithm Implementation
This project implements Dijkstra's Algorithm to find the shortest path between two nodes in a weighted graph. The graph is represented by an adjacency matrix, where the weight of the edge between two nodes is given, and 0 indicates that a node is unreachable.

Graph Representation
The graph is represented as an adjacency matrix, where graph[row][column] represents the weight of the edge between node row and node column.

Graphs used:
Graph 1: From page 105 in the textbook
Graph 2: From page 109 in the textbook
Graph 3: From a practice question solution on TES
Graph 4: From a different practice question source
Lol: Custom graph with 9 nodes and random weights
examTest: Custom graph used as a default for the implementation
Class Structure
Graph Class
Purpose: Manages the graph and stores the nodes and adjacency matrix.
Methods:
add_node(label): Adds a node to the graph.
get_nodes(): Prints the list of nodes.
get_adjacent_nodes(wantedNode): Returns the list of adjacent nodes for a given node.
Nodes Class
Purpose: Represents a node in the graph and performs operations related to Dijkstra's algorithm.
Methods:
show(): Displays the current working and final values for the node.
fill_working_val(): Updates the working value for adjacent nodes.
compare_working_val(): Finds the node with the smallest working value.
working_back(): Traces back the path from the destination node to the start node.
How to Use
Input: The user is prompted to enter the start and end nodes.
Process: The algorithm calculates the shortest path from the start node to the end node using the Dijkstra's algorithm.
Output: The shortest path and its corresponding nodes are displayed.
Example Usage
python
Copy code
Enter Start Node: A
Enter End Node: G
The shortest path from A to G is:
 ['A', 'B', 'F', 'G']
Notes
The graph uses the adjacency matrix representation, and 0 indicates unreachable nodes.
The algorithm works for graphs with any number of nodes and weighted edges.
