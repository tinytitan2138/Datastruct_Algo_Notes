'''Another interesting datastructure is that of the graph. Its structure consists of relational data
represented with vertices, weights, and direction. Each vertex may represent something, it can be locations,
related peoples or values, or just anything that is relational in nature. A common usage of graphs is in
representations of cities and paths. The weights themselves can like the distance between cities for example.
Graphs can be directional in nature too, where you may go to one node but not the other on a certain path. '''
#from Tools.scripts.mailerdaemon import x

'''There are 4 main data structures used for graphing algorithms. The edge list which is an unordered set 
of all the edges, an adjacency list which is thr set of all edges incident to some vertex. The adjacency map which 
is a mapping from some vertex to some edge. And finally the adjacency matrix which is an nxn matrix which 
describes adjacency from edges and vertices but as a matrix. '''

'''Graphs then require graph search algorithms, one such algorithm is depth first search. This algorithms basically 
works by visiting each vertex incident to another chosen vertex, the search then leaves a trail behind basically represneting 
where you have been. Were this vertex to be visited it would be painted which represents that its been visited already. 
Once u reach a dead end, the graph has been completely traversed. Another alternative in breadth first search which 
 subdivideds the vetices into what is called levels. It works like this: you choose some abritirary vertex which is you starting 
 level 0, you then reach out to all adjacent vertices one step away, this defines your level 1, you then repeat the process.
 The program is then terminated once you have reached all the vertices within the levels, they are as well painted as 
 being visited. '''

'''There are also problems relating to shortest possible path algorithms. One such algorithm is the floyd-warshall 
algorithm. Directed graphs can have applications in directional relational data, an example of lets say a non circular 
directed graph would be OOP inheritance and pre reqs. '''
#679

'''I will note that certain path algorithms are necessary for variables edge values. One algorithm is Dijkstra's algorithm 
which employs BDF in order to get the shortest path from some source node to each subsequent node by level. Each shortest 
path from each level is added to a path list. This is repeated until there are no more nodes to add. Thus you are left 
with the shortest possible path between each node to the source node. '''

'''There are problems in which you may need to find the shortest possible spanning tree of a graph. That is, 
you may have a problem in which you may need to find the shortest amount of cable to connect a bunch of nodes 
together, or basically anything like that. One algorithm is the Prim-Jarnik algorithm. It works very similar to dijkars 
algorithm, it starts at some vertex then goes to its neigbors and picks the edge with the shortest path. This is done until 
there is nothing to add left, this results in the minimum spanning tree of the graph. '''

'''Another important concept is memory management and allocation. Within lower level languages like c, memory 
is managed by the programmer. The way it works is like this: all declared or sorted variables have a memory location 
within the RAM, you can usually access the location by using a pointer to refereance the memory location 
or by using some built in python function. Within c, you may declare some variable once then never use it again, 
or even worse, you may constantly duplicate it within some algorithm, the way to fix this is with a memory 
allocation tool called the pointer. A pointer is essentially a variable that stores the memory location of some 
stored variable. This allows for memory location to be referanced in order to prevent duplicates or to deferance 
memory locations in order to free up memory. High level languages like python use what is called a garbage collector 
in order to deferance useless variables. For example, if the referance count of a variable is 0 after a certain point, it 
may be dereferences. There are many algorithms that are implemented within garbage collection, like mark sweep 
algorithm. Mark sweep algorithm works like this: you define live variables which are actively referanced, 
you then search through all the variables in DFS fashion, you then either define some variable as live or not, 
as opposed to marking them as been to. Stacks are used to represent the calling process of functions. 
So if you define some function those would be at the top of the stack with the main function being at the bottom. 
This is called the call stack. This can be filled to the brim when given some infinitely recursive function, interestingy
enough, this error is called stack overflow '''


'''def stackOverFlow(num):
    z = num^2
    print(z)
    stackOverFlow(z)

stackOverFlow(10)'''

'''Arithmatic operations are also done through the stack, a simple expression like 5+5 has the variables pushed 
to the operand stack and then they are evaluated with binary operations. CPU memory also has a hierarchy, it is as follows:
 registers which are the fastest to access but are quite small, following this pattern it is then 
 caches, internal memory, external memory, and network storage. Some architects say that 90% of a programs time 
 is spent in 10% of its code. You can bring data into the primary memory location which is called caching. You are 
 essentially hoping that it will be referenced again and are placing it in a location where it can be 
 pulled out of quickly. Given these memory caches you may find application within web caches. You also need 
 to allocate it accordingly, so naturally, you may implement FIFO, LFU, and randomness in order to pick the 
 data to omit. In order to store memory you need to implement trees containing many keys per node, and thus a
 generalization of (2, 4) trees are needed. These self-balancing trees are B-trees. A B-tree of order m (amount 
 of keys + 1) can have at most m child nodes. a non leaf node with k children contains k-1 keys. The root has at least
 2 children. Every non leaf node has at least (m/2)(ceiling)  children. There may be cases in which the inputed data
 is too much to allocate and so a sort algorithm like multi way merge sort is used to store the data block. '''

