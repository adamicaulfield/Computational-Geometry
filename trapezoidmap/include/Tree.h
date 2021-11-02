// By Adam Caulfield (ac7717)
// October 25 2021

#ifndef TREE_H
#define TREE_H

#include <iostream>
#include <fstream>

#include "Node.h"

class Node; // handle cyclic dependency betewen Node and Tree

class Tree {
public:
	Tree();
    Node * getRoot();
    int getTreeSize();
    void insertNode(Node *);
    void balanceTree(Node *);
    void printTree(Node *, int = 0);
private:
    Node * root;
    int size; //total nodes
};

#endif /*TREE_H*/