# Adam Caulfield (ac7717)
# CSCI716 - Assignment 2
# visualizer.py - implements a visualizing function, which is called every time the sweep line is incremented
# October 14, 2021

import matplotlib.pyplot as plt

# Function to visualize the line-sweep over a continuous for loop
def visualize(segs, queue, intersections, sweepLine, time):
	plt.plot([],[],"black", label="Segments")
	plt.plot([],[],'ro', label="Initial Events")
	plt.plot([],[],'go', label="Intersection")

	for i in range(0, len(segs)):
		plt.plot([segs[i][0],segs[i][2]], [segs[i][1],segs[i][3]], color="black",)

	for i in range(0, len(queue)):
		plt.plot(queue[i][0], queue[i][1], 'ro')

	for i in range(0, len(intersections)):
		plt.plot(intersections[i][0], intersections[i][1], 'go')

	plt.plot(sweepLine[0], sweepLine[1], 'b:', label="Sweep Line")
	plt.title("Sweep Line at x="+str(sweepLine[0][0]))
	plt.legend()
	plt.show()
	plt.pause(time)
	plt.clf()
