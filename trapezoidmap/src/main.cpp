#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>     /* atoi */
#include "Tree.h"
#include "Node.h"
#include "Segment.h"

int main(int argc, char **argv) {
	printf("------START MAIN----\n");
	Tree * tree = new Tree();

	Segment * s0 = new Segment(2,5,5,7);
	Segment * s1 = new Segment(4,3,8,4);
	// Segment * s0 = new Segment();
	// s0->setLeftEndpoint(2,5);
	// s1->setRightEndpoint(5,7);

	printf("------Tree after inserting S0------\n");
	tree->insert(s0);
	tree->printTree(tree->getRoot());

	// printf("------running deleteLeafNodes()------\n");
	// tree->deleteLeafNodes(tree->getRoot());
	// printf("------Tree after deleting leaf nodes:------\n");
	// tree->printTree(tree->getRoot());

	printf("------Tree after inserting S1------\n");
	tree->insert(s1);
	tree->printTree(tree->getRoot());


	return 0;
}
