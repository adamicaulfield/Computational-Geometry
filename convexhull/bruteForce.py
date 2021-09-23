'''
Adam Caulfield (ac7717)
CSCI716 - Computational Geometry - Coding Assignment 1

bruteForce.py
Convex Hull via Brute Force function

This program finds the convex hull via a brute force approach
'''

import matplotlib.pyplot as plt
from fileProcessor import processPointsFile
from orient import orient
import time

# Process points file
total, points, x, y = processPointsFile('examplePoints.txt')

# Brute Force approach - iterate through all pairs (p,q), and determine if all
# remaining points r are on one side of the line segment connecting (p,q)
start = time.perf_counter()
hull = []
for i in range(0, total-1):
	#if p = points[i] is already in hull, continue to next
	if not(points[i] in hull):
		for j in range(i+1, total):
			# q = points[j] is in hull, continue to next point
			if not(points[j] in hull):
				# count number of points to the left and right of segment
				countLeft = 0
				countRight = 0
				for k in range(0, total):
					if k != i and k != j:
						# Check left or right using orientation func
						stack = [points[i], points[j], points[k]]
						orientPQR = orient(stack)
						if orientPQR > 0:
							countLeft = countLeft+1
						if orientPQR < 0:
							countRight = countRight+1

				# All points are on one side if one counter = 0 stil
				if countLeft == 0 or countRight == 0:
					hull.append(points[j]) # add q
					if not(points[i] in hull): # add p if not already in hull
						hull.append(points[i])

# Sort hull by x
hull = sorted(hull)

#Construct upper and lower
upper = []
lower = [] 
for r in range(0,len(hull)):
	if hull[r][1] >= 0:
		upper.append(hull[r])
	else:
		lower.append(hull[r])
lower.reverse()
hull = upper + lower
hull.append(upper[0]) # add first element to end for closed loop
stop = time.perf_counter()
print("%f" % float(1000*(stop-start)))

# Plotting
# xHull = []
# yhull= []
# for r in range(0,len(hull)):
# 	xHull.append(hull[r][0])
# 	yhull.append(hull[r][1])

# plt.title("Convex Hull using Brute Force Approach")
# plt.scatter(x, y, c='b')
# plt.plot(xHull, yhull, c='k')
# plt.show()

