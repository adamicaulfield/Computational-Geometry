# Programming Assignment 1 - Convex Hulls
### Adam Caulfield (ac7717@rit.edu)

### Introduction
This contains all files for my Programming Assignment 1. I decided to implement the Brute Force approach and the Graham scan for finding the Convex Hull of a set of points. The code provided in this folder includes my implementaiton of both verisons, helper functions, and a bash script for timing. 

## Python dependencies
This project runs on Python3, and requires the following packages to be available

- time
- numpy
- matplotlib
- csv
- numpy

## Each Program

### bruteForce.py
This program executes the Brute-Force approach for finding the Convex Hull. This approach when given a set of points iterates through every pair of points (p,q) and checks if all remaining points r are all on the same side of the segment which connects (p,q) - assuming p,q,r are not equal.

### fileProcessor.py
This is a helper program with the purpose of processing the file `examplePoints.txt` and extracting the data as python data structures.

### graham.py
This program executes the Graham Scan, as described in the lecture slides. This program first sorts the points by their x coordinates using merge sort, then constructes the upper and lower hulls.

### mergesort.py
This program is a helper program for the Graham Scan, which requires the merge sort (or other O(n log n) sorting algorithm). This file contains two functions `mergesort()` and `merge()` which execute the merge sort algorithm together.

### orient.py
This function acts as a helper for both the Brute-Force and Graham Scan approaches. Given a set of three points, this function returns a value representing their orientation. This calculation is based upon slide 26 of '3-1-ConvexHulls'. Given three points, a 3x3 matrix can be constructed using their x and y coordinates to determine whether the three points make a left-hand turn.

### runAndTime.sh
This is a bash script to run multiple iterations of both bruteForce.py and graham.py, and this script will determine & display the average run time of both algorithms.

## How to run
Simply run the bash script with the command `./runAndTime.sh ITERS` replacing 'ITERS' with the number of iterations that you would like to run. For example, to run 25 iterations of both algorithms execute the command `./runAndTime.sh 25`

## Run Time Analysis
I used the script and python programs to run 100 iterations of both the Brute Force and Graham Scan approaches. Afterwards, the average run time for both approaches was the following: 
- Brute Force: 5.897 ms
- Graham Scan: 0.806 ms

This verifies the complexity difference between the two algorithms, with the Brute Force approach having a complexity of O(n^3) and the Graham Scan having a complexity of O(n log n)