// By Adam Caulfield (ac7717)
// October 25 2021

#ifndef NODE_H
#define NODE_H

#include <iostream>
#include <fstream>

#include "Tree.h"

class Tree;
class Segment;

enum NodeType {x, y, leaf}; 

class Node {
public:
    Node(Tree *, Segment *, NodeType);
    
    Node * getLeft();
    Node * getRight();
    Segment * getSegment();

    void setLeft(Node *);
    void setRight(Node *);
    void setSegment(Segment *);

    Tree * getTree();
    
    int getValue();
    void setValue(int);
    
    NodeType getNodeType();
    void setNodeType(NodeType);

    int leftCount;
    int rightCount;
    // x-nodes contain the point p and its two children correspond to points lying to left & right of p
    // y-nodes contain pointer to  line segment of the subdivision, left and right are regions above or below the line segment
private:
    Node * left;
    Node * right;
    Segment * s;
    Tree * tree;
    int value;
    NodeType type;
};

#endif /*NODE_H*/