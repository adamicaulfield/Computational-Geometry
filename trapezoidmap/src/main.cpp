#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>     /* atoi */
#include "Tree.h"
#include "Node.h"
#include "Segment.h"
#include <string>
#include <sstream>

int main(int argc, char **argv) {
	printf("-------------------- START MAIN -------------------- \n");
	
	Tree * tree = new Tree();

	printf("----- PHASE 1: Read from file, insert into Tree/DAG -----\n");
	tree->readSegmentsFile("data/ac7717.txt");
	
	printf("----- Print Tree/DAG after read file and insert segments -----\n");
	tree->printTree(tree->getRoot());

	// Segment * s0 = new Segment(2,5,5,7);
	// Segment * s1 = new Segment(4,3,8,4);
	
	// tree->insert(s0);
	// tree->insert(s1);

	printf("----- PHASE 2: Write to Adjacency Matrix -----\n");
	tree->setupLists(tree->getRoot());
	tree->initAdjacencyMatrix();
	tree->writeAdjacencyMatrix(tree->getRoot());
	tree->wrireSumsAdjacencyMatrix();
	// tree->printAdjacencyMatrix();
	tree->writeAdjacencyMatrixToFile("data/adjMatrix.csv");

	printf("---- PHASE 3: Enter a Point in the form \"x y\" to discover which trapezoid it is located in: \n");
	std::string pointStr;
	std::cout << "POINT: ";
	std::getline(std::cin,pointStr);
	std::cout << std::endl;
	std::cout << pointStr;
	
	std::stringstream ss;

	int x,y;

	ss << pointStr;
	ss >> x >> y;
	printf("FINDING POINT: (%d,%d)\n", x,y);
	tree->findPoint(x,y, tree->getRoot());

	return 0;
}
