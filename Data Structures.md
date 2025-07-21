
==Array

A collection of elements stored in contiguous memory locations which are accessible by indices.
Use Case : list of user roles, error codes etc.

==Linked List

A Collection of nodes where each node contains data and a pointer to the next node.

Use case: efficient insertions and deletions in the list. implementing queues and statcks.
==Stack

Collection of elements which are  inserted and removed according to the Last in first Out principle.

Methods are :  --> top - gives last inserted element
				 pop - deletes the last inserted elements and prints it

Use Case : Undo Operations, Function call management, expression evaluation

==Queues 

First in First Out

Collection of elements which are inserted and deleted according to the first in first out principle. Elements are inseted at the rear and removed from the front.

==singly LinkedList

Collection of nodes in which every node represents an element and a reference to the next element.

==Doubly Linked List

Collection of nodes in which every node represents an element and reference to an element which came before it and reference to an element which came after it.


==HashTable or HashMap

Stores key-value pairs with fast lookups using a hash function.

Use Case : caching, config storage, Json-like data structures.


==Tree

A tree is an abstract data type that stores elements hierarchically. With the exception of the top element, each element in a tree has a parent element and zero or more children.


==Binary Tree

A binary tree is an ordered tree with the following properties: 
1. Every node has at most two children.
2. Each child node is labeled as being either a left child or a right child.
3. A left child precedes a right child in the order of children of a node. 

The subtree rooted at a left or right child of an internal node v is called a left subtree or right subtree, respectively, of v. A binary tree is proper if each node has either zero or two children. Some people also refer to such trees as being full binary trees. Thus, in a proper binary tree, every internal node has exactly two children. A binary tree that is not proper is improper.

==Binary Search Tree

A binary tree with left < root < right property
A binary search tree (BST) is ==a tree-based data structure where each node has at most two children, and the values within the tree are organized in a specific order==. Specifically, for every node, all nodes in its left subtree have values less than the node's value, and all nodes in its right subtree have values greater than the node's value.
Use Case : Efficient Search , Insert, Delete Operations in sorted data

==Heap

A complete binary tree where each node satisfies the heap property. (parents <= or >= Children)

Use Case : Priority queues, scheduling algorithms, top-k problems

==Trie (Prefix Tree)

A Tree for storing strings where each node represents a character.

Use Case : Auto-Completion, prefix matching, dictionary implementation.

==Graph

A set of nodes (vertices) connected by edges. Can be directed/undirected, weighted/unweighted.

Use Case : Social Networks, dependency resolution, routing algorithms.


Viewed abstractly, a graph G is simply a set V of vertices and a collection E of pairs of vertices from V, called edges. Thus, a graph is a way of representing connections or relationships between pairs of objects from some set V. Incidentally, some books use different terminology for graphs and refer to what we call vertices as nodes and what we call edges as arcs. We use the terms “vertices” and “edges.” Edges in a graph are either directed or undirected. An edge (u,v) is said to be directed from u to v if the pair (u,v) is ordered, with u preceding v. An edge (u,v) is said to be undirected if the pair (u,v) is not ordered. Undirected edges are sometimes denoted with set notation, as {u,v}, but for simplicity we use the pair notation (u,v), noting that in the undirected case (u,v) is the same as (v,u). Graphs are typically visualized by drawing the vertices as ovals or rectangles and the edges as segments or curves connecting pairs of ovals and rectangles. The following are some examples of directed and undirected graphs.


==Set

Unordered collection of unique elements

Use Case: removing duplicates, membership testing, mathematical operations



==Deque (Double Ended Queue)

A linear data structure that allows insertion and deletion from both ends.

Use Case : Implementing Caches, sliding window problems.


==Priority Queue

Elements are served based on priority not just insertion order.

Use Case : Task Prioritization,  job scheduling, pathfinding





