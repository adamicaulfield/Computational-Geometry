# Adam Caulfield (ac7717)
# CSCI716 - Assignment 2
# eventQueue.py - implements the event queue object as a list, with additional information
# each entry in the queue contains [leftX, leftY, rightX, rightY, id]
# October 14, 2021

import random

# Inserts into the event queue while maintaining the order
# Conducts a binary search of the queue for the correct index
# Complexity: O(Log n)
def eqInsert(seg, queue):
	totalChecks = 1
	qSize = len(queue)
	# print("Size of queue: "+str(qSize))

	# If queue is empty, initialize queue
	if(qSize==0):
		queue.append(seg)
	
	else:	
		# New seg has smallest x of all segs in queue
		if(seg[0] <= queue[0][0]):
			# print("Adding to front of queue: "+str(seg))
			queue = [seg]+queue 

		else:
			# New seg has largest x of all segs in the queue
			if(seg[0] >= queue[qSize-1][0]):
				queue.append(seg)

			# Not an edge case
			else:
				mid = int(qSize/2)

				checkLeft = (seg[0] < queue[mid-1][0])
				checkRight = (seg[0] > queue[mid][0])
				rightEnd = qSize
				leftEnd = 0

				while(checkLeft or checkRight):

					totalChecks = totalChecks+1
					if(checkRight): #checkRight is true
						leftEnd=mid
						mid = int((rightEnd+mid)/2);
						
					else: # checkLeft is true
						rightEnd=mid
						mid = int((leftEnd+mid)/2)

					checkLeft = (seg[0] < queue[mid-1][0])
					checkRight = (seg[0] > queue[mid][0])

				queue = queue[:mid] + [seg] + queue[mid:]
	return queue

# In the ordered queue, the event with the smallest x-coordinate will
# always be in the first index
def eqExtract(queue):
	return queue[0]

# Deletes a given event / seg from the queue
# Make use of Python function remove() for lists 
def eqDelete(seg, queue):
	queue.remove(seg)
	return queue