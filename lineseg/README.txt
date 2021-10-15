Adam Caulfield (ac7717)
October 14, 2021
CSCI716: Plane-Sweep algorithm

----- Details ----
This file set for my assignment submission includes three python files
	- eventQueue.py:	implements functions for the event queue structure
	- sweepLineStatus.py:	implements functions for the sweep line status structure
	- visualizer.py:	my function to visiualize the live execution of the plane-sweep algorithm
	- planeSweep.py:	the main function, which executes the plane-sweep algorithm
	- datapoints.txt:	input points
	- intersections.txt:	output - points which are line-segment intersections found by the algorithm

----- Dependencies ----
This is built upon Python3. The following packages within python are required:
	- csv
	- matploylib

---- How to run -----
Simply execute the following command: 'python3 planeSweep.py'

In the console, some details are printed, such as the structure of the event queue and sweep-line-status, or when a addition/swap/remove is made, or other details.

While this goes on, a plot should pop up simultaneously, and continuously update adding more intersection points as the algorithm goes on.

Once it has swept through the entire plane, the program writes output to 'intersection.txt'.

After this, the program will automatically keep the plot on screen for 30s before terminating the execution. You can manually end the program by closing the plot with the 'X' button.


