# Assumes the inputs of 
# 		- seg list of 2 elements [x,y]
#		- a queue which lists the segs added sorted by x coordinate as a 2D list,
#		- returns updated queue

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
		# print("Queue empty, appending seg: "+str(seg))
		queue.append(seg)
	
	else:	
		# New seg has smallest x of all segs in queue
		if(seg[0] <= queue[0][0]):
			# print("Adding to front of queue: "+str(seg))
			queue = [seg]+queue 

		else:
			# New seg has largest x of all segs in the queue
			if(seg[0] >= queue[qSize-1][0]):
				# print("Adding to end of queue: "+str(seg))
				queue.append(seg)

			# Not an edge case
			else:
				mid = int(qSize/2)

				checkLeft = (seg[0] < queue[mid-1][0])
				checkRight = (seg[0] > queue[mid][0])
				rightEnd = qSize
				leftEnd = 0

				while(checkLeft or checkRight):
					# print("mid="+str(mid)
					# 	+"  leftEnd:"+str(leftEnd)
					# 	+"  rightEnd:"+str(rightEnd)
					# 	+"  "+str(seg[0])+"<"+str(queue[mid-1][0])
					# 	+"  "+str(seg[0])+">"+str(queue[mid][0]))

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
				# print("Adding to  index "+str(mid)+": "+str(seg))
	# print("Comparisons Required for insert(): "+str(totalChecks))
	# print(queue)
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