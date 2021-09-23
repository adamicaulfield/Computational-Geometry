'''
Adam Caulfield (ac7717)
CSCI716 - Computational Geometry - Coding Assignment 1

graham.py
Convex Hull via Graham scan

This program finds the convex hull via Graham Scan
'''

import numpy as np
import matplotlib.pyplot as plt
import time
from mergeSort import mergeSort, merge
from orient import orient
from fileProcessor import processPointsFile

###################################################3

# Process points file
total, points, x, y = processPointsFile('examplePoints.txt')

#Graham Scan
start = time.perf_counter()

#Sort by X coordinate smallest to largest using merge sort
sortedPoints = mergeSort(points)

upperhull = []

# Upper hull starts with first two points
upperhull.append(sortedPoints[total-1])
upperhull.append(sortedPoints[total-2])

# Track last index checked
verifiedInd = 0

i = total-3
while i >= 0:
	# Add next point to hull
	upperhull.append(sortedPoints[i])

	#Stack is most recently added 3 points
	stack = upperhull[verifiedInd:verifiedInd+3]

	if(orient(stack) > 0): # If orientation > 0, keep in hull and incr index
		verifiedInd = verifiedInd+1
	else:
		upperhull.pop(verifiedInd+1) # Point is not in hull, pop to remove
	i = i-1

#Repeat for lower hull
lowerhull = []
lowerhull.append(sortedPoints[0])
lowerhull.append(sortedPoints[1])
verifiedInd = 0
i = 2
while i < total:
	lowerhull.append(sortedPoints[i])
	
	stack = lowerhull[verifiedInd:verifiedInd+3]
	
	if(orient(stack) > 0):
		verifiedInd = verifiedInd+1
	else:	
		lowerhull.pop(verifiedInd+1)
	i = i+1

stop = time.perf_counter()
print("%f" % float(1000*(stop-start)))

# Plotting
# xHull = []
# yhull= []
# for r in range(0,len(upperhull)):
# 	xHull.append(upperhull[r][0])
# 	yhull.append(upperhull[r][1])
# for r in range(0,len(lowerhull)):
# 	xHull.append(lowerhull[r][0])
# 	yhull.append(lowerhull[r][1])

# plt.title("Final")
# plt.scatter(x, y)
# plt.plot(xHull, yhull, '-o')
# plt.show()




	