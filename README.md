# Technical Interview Cheat Sheet

### Table of Contents

- [Behavioral Questions](#behavioral-questions)
- [Algorithms and Data Structures](#algorithms-and-data-structures)
- [Operating Systems](#operating-systems)
- [Scalability and Design](#scalability-and-design)
- [Object-Oriented Programming](#object-oriented-programming)
- [Resources](#resources)


## Interview Preparation Grid

![Interview Preparation Grid](./assets/interview-preparation-grid.jpg)

**Evaluated skills**:
- Analytical skills
- Coding skills
- Technical knowledge / Computer Science fundamentals
- Experience
- Culture fit / Communication skills


## Behavioral Questions

- Be specific, not arrogant
- Limit Details
- Focus on yourself, not your team
- Give structured answers: **Nugget first**, situation, action, result

#### Tell Me About Yourself

- Current Role (Headline Only)
- College
- Post College & Onwards
- Current Role (Details)
- Outside of Work
- Wrap Up


## Algorithms and Data Structures

### Big-O

- Big O - upper bound
- Big Omega - lower bound
- Big Theta - upper and lower bound - that's what's usually used but called Big O.

#### Amortized time

An ArrayList is implemented with an array. When the array hits capacity, the ArrayList class will 
create a new array with double the capacity and copy all the elements over to the new array.

For most inserts it takes O(1) time. For those inserts where the array is doubling it takes X time. 
`X + X/2 + X/4 + Y/8 + ... + 1` is roughly 2X. 

Therefore X insertions take O(X) time. The amortized time for each insertion is O(1).

### Divide and Conquer
 
Usually recursive  - ex. **Merge Sort**.

**Master Method** (allows to estimate time complexity of a recursive the algorithm):

`T(n) <= a*T(n/b) + O(n^d)`

![Master Method](./assets/master-method.png)

**QuickSort** - uses partitioning around pivot, works in-place, n*log(n) running time on average.

**Randomized Selection** - allows finding n-th order statistic of an array - uses quick sort algorithm but iterates 
only to 1 subarray, and thus O(n) time (master method case 2).

**Guiding principles for algorithms analysis**:

- Worst case analysis (other are average case, best case)
- Drop constant factors, lower-order terms
- Asymptotic analysis (focus on running time for large input)

### Graphs and Trees

**Minimum cut** - Karger's basic algorithm iteratively contracts randomly chosen edges until only two nodes remain; 
those nodes represent a cut in the original graph. By iterating this basic algorithm a sufficient number of times, 
a minimum cut can be found with high probability.

**BFS (Breadth-first search)** - uses queue. Can be used to find shortest path, connected components.

**DFS (Depth-first search)** - uses stack or recursion. Can be used for topological ordering of DAGs. 
Strongly connected components of directed graphs - 2 passes - first on reverted graph, second on straight graph.

[graph_dfs_bfs.py](code/graph_dfs_bfs.py)

[graph_topological_sort.py](code/graph_topological_sort.py)

**Dijkstra's algorithm** - choose edge with lowest score (sum of current vertex length of shortest path and edge length),
 and add it to the set of explored vertexes. 
- runs in O(m*log(n)) time if heap data structure is used.

[graph_dijkstra.py](code/graph_dijkstra.py)

**Heap data structure** - a tree where values in all nodes are larger (smaller for min-heap) that all values in 
respective subnodes.
Time complexity is log(n) for inserting an element, and for extracting min/max element.

**Binary search tree** - all operations are log(n), better than sorted array for inserting/deleting, but worse for 
getting i-th order statistic, min/max, rank, successor/predecessor.
- Find min or max - take `n*log(n)` time. For min, follow left child until there is none. 
- Find successor or predecessor - take `n*log(n)` time. For predecessor, if there is left node, find max of it;
if there is no left node, follow the parent until node is right node of the parent. 
- Insertion and deletion - takes `n*log(n)` time. For insertion just follow search algorithm until you find NULL and 
insert new element there. For deletion, in case a node has only left or right subtree, put it in place of deleted node;
in case both left and right are present, find the predecessor of deleted node, put it in place of deleted node, then 
follow deletion algorithm for predecessor.
- Select and rank (find n-th order statistic) - takes `n*log(n)` time, requires keeping size of subtree i.e. how
many nodes are contained in the tree.


**Red-black tree** - makes binary search tree relatively balances. 
- Invariants: root is always black, no consecutive red nodes, root-to-NULL paths all have same number of block nodes. 
- Invariants are maintained by recoloring nodes and rotations, 
when nodes are inserted or deleted.

**AVL trees** - makes binary search tree relatively balances. Stores in each node the height of the subtrees rooted 
at this node. 
- Invariant: the height of the left subtree and the height of the right subtree differ by no more than one.
- Invariants are maintained via rotations: if left subtree is heavier: LEFT RIGHT SHAPE -> LEFT LEFT SHAPE -> BALANCED.

Binary tree traversals:
- **In-Order** Traversal means to "visit" (often, print) the left branch, then the current node, and finally, the right
branch.
- **Pre-order** traversal visits the current node before its child nodes (hence the name "pre-order").
- **Post-order** traversal visits the current node after its child nodes (hence the name "post-order").

### Greedy Algorithms

**Minimum Spanning Tree** - a tree with minimum sum of edge costs that spans all vertices.

There are 2 greedy algorithms for finding a minimum spanning tree: 
 
- **Prim's algorithms** - pick random vertex, choose edge with smallest weight that comes from tree to outside. 
Add vertex to tree. Repeat.
- **Kruskal's algorithm** - pick edge with smallest weight, add it to MST if it doesn't create the cycle. Repeat. 
Uses Union-find data structure to check if edge adds a cycle.


**Union-Find** - array where values are references to parent. find() returns the root of tree, union() merges 2 roots.
It provides near-constant-time operations (bounded by the inverse Ackermann function) for both operations.

[union_find.py](code/union_find.py)

**Optimal Caching** - when cache is full, replace furthest-in-the-future element, i.e. the one that will be requested 
latest in the future. 
Replacing least recently used (LRU) is a good approximation to the most optimal algorithms.

**Scheduling Jobs** - pick the job with highest ratio of w/l, where w is job's weight, l is job's length.


#### NP-Completeness

- P is the class of decision problems which can be solved in polynomial time by a deterministic Turing machine.
- NP is the class of decision problems which can be solved in polynomial time by a non-deterministic Turing machine. 
Equivalently, it is the class of problems which can be verified in polynomial time by a deterministic Turing machine.
- NP-hard is the class of decision problems to which all problems in NP can be reduced to in polynomial time by a 
deterministic Turing machine.
- NP-complete is the intersection of NP-hard and NP. Equivalently, NP-complete is the class of decision problems in 
NP to which all problems in NP can be reduced to in polynomial time by a deterministic Turing machine.

A reduction from X to Y is simply an algorithm A which solves X by making use of some other algorithm B which solves 
problem Y. This reduction is called a "polynomial time reduction" if all parts of A other than B have a polynomial 
time complexity. As a trivial example, the problem of finding the smallest element in an array is constant-time 
reducible to the sorting problem, since you can sort the array and then return the first element of the sorted array.

Examples of NP-complete problems:

- Knapsack problem - fill the knapsack with items sum of weights of which don't exceed the limit, providing maximum 
sum of values of items. 
- Subset sum problem - given the integers or natural numbers w1, w2, ... wn, does any subset of them sum to precisely W.
- Travelling salesman problem - given a list of cities and the distances between each pair of cities, what is the 
shortest possible route that visits each city and returns to the origin city?
- Graph coloring problem - can be solved using backtracking.

Approaches for solving NP-complete problems:
- Approximation: Instead of searching for an optimal solution, search for a solution that is at most a factor from an 
optimal one.
- Randomization: Use randomness to get a faster average running time, and allow the algorithm to fail with some small 
probability. Note: The Monte Carlo method is not an example of an efficient algorithm in this specific sense, although 
evolutionary approaches like Genetic algorithms may be.
- Restriction: By restricting the structure of the input (e.g., to planar graphs), faster algorithms are usually 
possible.
- Parameterization: Often there are fast algorithms if certain parameters of the input are fixed.
- Heuristic: An algorithm that works "reasonably well" in many cases, but for which there is no proof that it is both 
always fast and always produces a good result. Metaheuristic approaches are often used.

#### Checklist for Solving Algorithm and Data Structures Problems

1. Have at least 2 examples.
1. State the brute force solution.
1. Estimate time and space complexities before writing code - worst case, average case.
1. For optimization 
    - try different data structures - graph, tree, hashmap, stack, queue.
    - try different algorithm approaches - divide and conquer, greedy, dynamic programming.
1. Check corner cases.
1. No *break* in nested loops - replace with functions.

## Operating Systems

http://pages.cs.wisc.edu/~remzi/OSTEP/


## Scalability and Design

- List all assumptions - needed to scope the project
- Draft high-level solution
- List limitations
- List Hard problems - what will take most effort


## Object-Oriented Programming

- Abstraction - represent real-world entities with their abstraction i.e. classes in code.
- Encapsulation - hide the implementation details and expose the interface.
- Inheritance - build class hierarchy to represent subset/superset relationships in real world.  
- Polymorphism - write your code with interfaces, the implementation will be chosen at runtime.


## Resources

- Cracking The Coding Interview https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850
- Operation Systems http://pages.cs.wisc.edu/~remzi/OSTEP/
- Algorithms Specialization on Coursera https://www.coursera.org/specializations/algorithms

