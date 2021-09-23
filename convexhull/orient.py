'''
Adam Caulfield (ac7717)
CSCI716 - Computational Geometry - Coding Assignment 1

orient.py
Orientation calculator

This program finds the orientation of three points. In other words, 
this function constructs a 3x3 matrix with the three points given as input
and calculates the determinant. The determinant informs whether the points
form a left-hand turn.

This function is based upon the defintion provided by slide 26 of 
the slides titled '3-1-ConvexHulls'

This is used by both the Graham's Scan and the Brute Force approach
'''

import numpy as np

#Check Left Hand Turn using 3x3 matrix determinant
def orient(h):
	# extract 3 points from the input
	p = h[0] 
	q = h[1] 
	r = h[2]

	# Construct 3 x 3 matrix
	mat = np.array([[1, p[0], p[1]],
					[1, q[0], q[1]],
					[1, r[0], r[1]]])

	# Find determinant
	orientPQR = np.linalg.det(mat)
	
	return orientPQR