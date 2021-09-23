'''
Adam Caulfield (ac7717)
CSCI716 - Computational Geometry - Coding Assignment 1

mergeSort.py
Functions for Merge Sort

This program defines the functions needed for merge sort:
	- mergeSort
	- merge

The Graham Scan involves executing a O(n log n) sorting algorithm, and thus
a merge sort can be used.
'''

# Functions merge and mergeSort to execute  merge sort
def mergeSort(points):
	if(len(points)<=1):
		return points

	else:
		# Find Mid point
		mid = int(len(points)/2)
		
		# split list into two halves
		left = points[:mid]
		right = points[mid:]

		# Recursive merge sort on left and right
		left = mergeSort(left)
		right = mergeSort(right)

		# After splitting is complete, sort and merge through merge()
		return merge(left, right)

def merge(left, right):
	# Get sizes of left and right
	leftSize = int(len(left))
	rightSize = int(len(right))
	
	sortedPoints = []

	# Indices for left(l) and right(r) lists
	l = 0
	r = 0

	# Iterate until either the left or right has been completed
	while l < leftSize and r < rightSize:
		#Add whichever element is smaller to the list first
		if(left[l][0] < right[r][0]):
			sortedPoints.append(left[l])
			l = l+1
		else:
			sortedPoints.append(right[r])
			r = r+1

	# Either the left or right side has not addedd all points so either
	# Add remaining points from left or right
	while l < leftSize:
		sortedPoints.append(left[l])
		l = l+1

	while r < rightSize:
		sortedPoints.append(right[r])
		r = r+1

	return sortedPoints