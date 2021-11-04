// By Adam Caulfield (ac7717)
// November 3 2021

#ifndef SEGMENT_H
#define SEGMENT_H

#include <iostream>
#include <fstream>
#include <vector>

class Segment {
public:
    // Segment();
    Segment(int , int , int , int );

    std::vector<int> getLeftEndpoint();
    void setLeftEndpoint(int, int);

    std::vector<int> getRightEndpoint();
    void setRightEndpoint(int, int);

    void initDual();

    int getYonSeg(int);

private:
    std::vector<int> rightEndpoint;
    std::vector<int> leftEndpoint;
    int slope;
    int intercept;
};

#endif /*SEGMENT_H*/