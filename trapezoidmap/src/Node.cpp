// By Adam Caulfield (ac7717)
// October 25 2021

#include "Node.h"

Node::Node(Tree * t, int v){
	leftNode = nullptr;
	rightNode = nullptr;
	tree = t;
	value = v;
	leftCount = 0;
	rightCount = 0;
}

void Node::setValue(int v){
	value = v;
}

int Node::getValue(){
	return value;
}

// Get pointer to  left node
Node * Node::getLeft(){
	return leftNode;
}

// Get pointer to right node
Node * Node::getRight(){
	return rightNode;
}

// Get pointer to  left node
void Node::setLeft(Node * node){
	leftNode = node;
}

// Get pointer to right node
void Node::setRight(Node * node){
	rightNode = node;
}


// Get pointer to tree, which this node is in
Tree * Node::getTree(){
	return tree;
}

