// By Adam Caulfield (ac7717)
// October 25 2021

#include "Tree.h"
#include "Node.h"
#include <cmath>

Tree::Tree(){
	size = 0;
	root = NULL;
	totalTrapezoids = 0;
}

// Get node at the top of the tree
Node * Tree::getRoot(){
	return root;
}

int Tree::getTreeSize(){
	return size;
}

void Tree::insert(Segment * s){
	printf("beginning insert()....\n");

	printf("getting left and right endpoints from segment\n");
	std::vector<int> leftEndPoint = s->getLeftEndpoint();
	std::vector<int> rightEndPoint = s->getRightEndpoint();

	int xl = leftEndPoint[0];
	int yl = leftEndPoint[1];
	int xr = rightEndPoint[0];
	int yr = rightEndPoint[1];


	Node * r = new Node(this, s, NodeType::x);
	Node * l = new Node(this, s, NodeType::x);
	l->setValue(xl);		
	r->setValue(xr);

	Node * seg = new Node(this, s, NodeType::y);
	seg->setValue(totalSegments);

	if(size == 0){
		printf("Adding seg to tree, tree has size = 0\n");
		// Add point nodes

		root = l;
		l->setRight(r);

		// Add segment node
		r->setLeft(seg);
		addLeafNodes(root);
	} else{

		// Locate trapezoid leaf node which holds the left endpoint
		Node * searchNode = root;
		Node * prevNode;
		NodeType searchNodeType = searchNode->getNodeType();
		bool dir = true;
		printf("Starting LEFT while loop...\n");
		while(searchNodeType != NodeType::leaf){
			prevNode = searchNode;
			switch(searchNodeType){	
				case NodeType::x:
					if(xl < searchNode->getValue()){
						searchNode = searchNode->getLeft();
						dir = true;
					} else{
						searchNode = searchNode->getRight();
						dir = false;
					}
					break;
				
				case NodeType::y:
					if(yl < searchNode->getSegment()->getYonSeg(xl)){
						searchNode = searchNode->getLeft();
						dir = true;
					} else{
						searchNode = searchNode->getRight();
						dir = false;
					}
					break;
			}
			searchNodeType = searchNode->getNodeType();
		}
		printf("Finished LEFT while loop...\n");
		// searchNode now holds leaf node, prevNode now holds its parent

		// replace leaf node with the new x-node
		if(dir){ //left
			prevNode->setLeft(l);
			delete(searchNode);

		} else{
			prevNode->setRight(l);
			delete(searchNode);
		}
		l->setRight(seg);
		addLeafNodes(l);

		//Locate trapezoid leaf node which holds the right endpoint
		searchNode = root;
		searchNodeType = searchNode->getNodeType();
		dir = true;
		printf("Starting RIGHT while loop...\n");
		while(searchNodeType != NodeType::leaf){
			prevNode = searchNode;
			switch(searchNodeType){	
				case NodeType::x:
					if(xr < searchNode->getValue()){
						searchNode = searchNode->getLeft();
						dir = true;
					} else{
						searchNode = searchNode->getRight();
						dir = false;
					}
					break;
				
				case NodeType::y:
					if(yr < searchNode->getSegment()->getYonSeg(xr)){
						searchNode = searchNode->getLeft();
						dir = true;
					} else{
						searchNode = searchNode->getRight();
						dir = false;
					}
					break;
			}
			searchNodeType = searchNode->getNodeType();
		}
		printf("Finished RIGHT while loop...\n");

		if(dir){ //left
			prevNode->setLeft(r);
			delete(searchNode);
		} else{
			prevNode->setRight(r);
			delete(searchNode);
		}
		r->setLeft(seg);
		addLeafNodes(r);
		// searchNode now holds leaf node, prevNode now holds its parent

	}
	// printf("beginning addLeafNodes()....\n");
	// addLeafNodes(root);
	// printf("finished addLeafNodes()....\n");
	// printf("finished insert()....\n");
	totalSegments++;
	size++;
}

void Tree::addLeafNodes(Node * node){
	if(node != nullptr){
		if(node->getLeft() == nullptr){
			Node * leaf = new Node(this, nullptr, NodeType::leaf);
			leaf->setValue(totalTrapezoids);
			totalTrapezoids++;
			node->setLeft(leaf);
		} else{
			if(node->getLeft()->getNodeType() != NodeType::leaf){
				addLeafNodes(node->getLeft());	
			}
		}

		if(node->getRight() == nullptr){
			Node * leaf = new Node(this, nullptr, NodeType::leaf);
			leaf->setValue(totalTrapezoids);
			totalTrapezoids++;
			node->setRight(leaf);
		} else{
			if(node->getRight()->getNodeType() != NodeType::leaf){
				addLeafNodes(node->getRight());
			}
		}
	} else{
		return;
	}
}

void Tree::deleteLeafNodes(Node * node){
	if(node != nullptr){
		if(node->getLeft() != nullptr){
			if(node->getLeft()->getNodeType() == NodeType::leaf){
				Node * leaf = node->getLeft();
				node->setLeft(nullptr);
				delete(leaf);
			} else {
				deleteLeafNodes(node->getLeft());
				totalTrapezoids--;
			}
		} else{
			return;
		}

		if(node->getRight() != nullptr){
			if(node->getRight()->getNodeType() == NodeType::leaf){
				Node * leaf = node->getRight();
				node->setRight(nullptr);
				delete(leaf);
			} else {
				deleteLeafNodes(node->getRight());
				totalTrapezoids--;
			}
		} else{
			return;
		}
	}
}

void Tree::printTree(Node * startNode, int depth){
	depth++;
	switch(startNode->getNodeType()){
		case NodeType::x:
			printf("Node(type:x, val:%d)\n", startNode->getValue());
			break;
		case NodeType::y:
			printf("Node(type:y, segID:%d)\n", startNode->getValue());
			break;
		case NodeType::leaf:
			printf("Node(type:leaf, tpzdID=%d)\n", startNode->getValue());
			break;
	}
	
	if(startNode->getRight()!=nullptr){
		for(int i=0; i<depth; i++){
			printf("\t");
		}
		printf("R: ");
		printTree(startNode->getRight(), depth+1);
	}

	if(startNode->getLeft()!=nullptr){
		for(int i=0; i<depth; i++){
			printf("\t");
		}
		printf("L: ");
		printTree(startNode->getLeft(), depth+1);
	}
}