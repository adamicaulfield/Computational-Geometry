// By Adam Caulfield (ac7717)
// October 25 2021

#ifndef NODE_H
#define NODE_H

#include <iostream>
#include <fstream>

#include "Tree.h"

class Tree;

class Node {
public:
    Node(Tree *, int);
    Node * getLeft();
    Node * getRight();
    void setLeft(Node *);
    void setRight(Node *);
    Tree * getTree();
    int getValue();
    void setValue(int);
    int leftCount;
    int rightCount;
private:
    Node * leftNode;
    Node * rightNode;
    Tree * tree;
    int value;
};

#endif /*NODE_H*/