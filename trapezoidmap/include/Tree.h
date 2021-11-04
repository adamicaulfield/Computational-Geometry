// By Adam Caulfield (ac7717)
// October 25 2021

#ifndef TREE_H
#define TREE_H

#include <iostream>
#include <fstream>

#include "Node.h"
#include "Segment.h"

// handle cyclic dependencies
class Node; 
class Segment;

class Tree {
public:
	Tree();
    Node * getRoot();
    int getTreeSize();
    void insert(Segment *);
    void printTree(Node *, int = 0);
    void addLeafNodes(Node *);
    void deleteLeafNodes(Node *);
private:
    Node * root;
    int size; //total nodes
    int totalTrapezoids;
    int totalSegments;
};

#endif /*TREE_H*/