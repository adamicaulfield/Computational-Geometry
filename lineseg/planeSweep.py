# Adam Caulfield (ac7717)
# CSCI716 - Assignment 2
# planeSweep.py - the main function for the plane-sweep assignment
# October 14, 2021

from eventQueue import *
from sweepLineStatus import *
from visualizer import *
import csv
import matplotlib.pyplot as plt

# Utility function to find  an event based upon its X coordinate
def findEvent(queue, x):
	qSize = len(queue)
	# If is beyong the bounds, return false
	if(x < queue[0][0] or x > queue[qSize-1][0]):
		return [False, []]

	stop = qSize
	start = 0

	found = False
	inds = [] #implemented as list since could have multiple events with same x coordinate
	#Search
	for i in range(start, stop):
		
		if(queue[i][0] == x):
			# print("Found")
			found = True
			inds.append(queue[i][2])
		if(queue[i][0] > x):
			break # break once greater than x, since the queue is sorted by x

	return [found, inds]

# Open data file, read and begin
with open('datapoints.txt', newline='') as file:
    data = list(csv.reader(file, delimiter=' '))

totalSegs = int(data[0][0])
segs = data[1:]

# Boundaries of the segments for plotting
minX = int(segs[0][0])
maxX = int(segs[0][0])
minY = int(segs[0][1])
maxY = int(segs[0][1])
coords = 4

# Initialize interactive plot
plt.ion()

# Dual representation of the points
coeffs = []
for i in range(0, totalSegs):
	for j in range(0, coords):
		segs[i][j] = int(segs[i][j])
	segs[i].append(i) # 5th index is the segment id

	# Ensure the first coordinate is the left point and second coordinate is right point
	if(segs[i][0]>segs[i][2]):
		# Swap endpoint positions if in list backwards
		tmp = segs[i][0]
		segs[i][0] = segs[i][2]
		segs[i][2] = tmp

		tmp = segs[i][1]
		segs[i][1] = segs[i][3]
		segs[i][3] = tmp

	# Get slope and intercept, add to coeffs with first Y
	m = (segs[i][3]-segs[i][1])/(segs[i][2]-segs[i][0]) # slope
	b = segs[i][1]-m*segs[i][0] # intercept

	coeffs.append([m,b,segs[i][1],i]) # each entry contains slope, intercept, y coord, id

	# Update min and max X if needed
	if(segs[i][2] > maxX):
		maxX = segs[i][2]
	if(segs[i][0] < minX):
		minX = segs[i][0]
	if(segs[i][3] > maxY):
		maxY = segs[i][3]
	if(segs[i][1] < minY):
		minY = segs[i][1]
	
print("Min and Max")
print("\tmin: ("+str(minX)+","+str(minY))
print("\tmax: ("+str(maxX)+","+str(maxY))
print("---------------")

print("Segments: ("+str(totalSegs)+")")
for s in segs:
	print(s)
print("---------------")

print("Coeffs: ")
for c in coeffs:
	print(c)
print("---------------")

# 1) Initialize event queue - Insert all left endpoints of the line segments into the event queue
queue = []
for i in range(0, totalSegs):
	if(segs[i][0] < segs[i][2]):
		s = segs[i][:2]+[segs[i][4]]
		queue = eqInsert(s, queue)
	else:
		queue = eqInsert(segs[i][2:], queue)

print("Initial Event Queue: "+str(queue))
print("---------------")

print("Plane Sweep Execution log:")
x = minX
sls = [] #sweep line status 
nextEvent = eqExtract(queue)
sweepLine = [[x,x],[minY,maxY]]
intersections = []
while (x < maxX):
	visualize(segs, queue, intersections, sweepLine, .025)
	if(len(queue)>0):
		# Add any left coordinates
		[found, ind] = findEvent(queue,x)
		if(found):
			for idx in ind:
				print("x="+str(x)+":\tSLS UPDATE: Add item: "+str(coeffs[idx]))
				sls = slsInsert(coeffs[idx], sls)
				

		# Move forward the sweep line, If two events have passed each other in position, add event
		x+=1
		sweepLine[0][0] += 1
		sweepLine[0][1] += 1

		[sls, newEvents] = slsMove(sls,x)
		for event in newEvents:
			intersections.append(event)

		# Check if passed right endpoint
		i = 0
		sizeSLS = len(sls)
		while i < sizeSLS:
			curID = sls[i][3]
			# print("try (x="+str(x)+") >= (segs["+str(curID)+"][2]="+str(segs[curID][2])+")")
			if(x >= segs[curID][2]):
				print("x="+str(x)+":\tQUEUE UPDATE: Removing item: "+str(segs[curID]))
				# print("\tRemoving event Queue")

				for j in range(0, len(queue)):
					if(queue[j][2]==curID):
						queue = eqDelete(queue[j], queue)
						# print("\tQueue:"+str(queue))
						break 

				print("x="+str(x)+":\t"+"SLS UPDATE: Removing item: "+str(sls[i]))
				sls = slsDelete(sls[i], sls)
				sizeSLS -= 1
			i+=1
	else:
		x+=1

print("---------------")
print("Writing intersections to file...")
with open('intersections.txt', mode='w') as file:
	writer = csv.writer(file, delimiter=" ")
	writer.writerow([len(intersections)])
	for point in intersections:
		writer.writerow(point[:2]) # the third element is the ID, which is not needed for the output file
print("Done: \'intersections.txt\' ready")
print("---------------")
# print(sls)
print("Press 'X' button on Plot to end, or wait 30s")
visualize(segs, queue, intersections, sweepLine, 30)	
print("---------------")