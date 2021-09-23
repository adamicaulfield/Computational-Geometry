'''
Adam Caulfield (ac7717)
CSCI716 - Computational Geometry - Coding Assignment 1

fileProcessor.py
Processes text file into needed data structures

This program processes the text file provided into the required outputs:
	- the total number of points
	- 2D list of points, where each point p is a list [px,py]
	- 1D list of all x coordinates
	- 1D list of all y coordinates
'''

import csv

def processPointsFile(filename):
	#Open the file and read the file as a CSV with spaces into list
	with open(filename, newline='\n') as csvfile:
		points = list(csv.reader(csvfile, delimiter=' '))

	x = []
	y = []
	#extract the x and y into their own lists, and convert the data into int
	for r in range(0,len(points)):
		for c in range(0,len(points[r])):
			points[r][c] = int(points[r][c])
			
		if(r != 0):
			x.append(points[r][0])
			y.append(points[r][1])

	# First line of the file is the total number of points.
	# Save a separate variable and remove from master list
	total = points[0][0]
	points.pop(0)

	return total, points, x, y