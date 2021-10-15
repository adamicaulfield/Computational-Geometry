# Segment comes in form [slope, intercept, currentY, ID]

def slsInsert(seg, sls):
	# Sorts w.r.t index=2, which holds the current Y of the segment on the sweep-line

	totalChecks = 1
	qSize = len(sls)
	# print("Size of sls: "+str(qSize))

	# If sls is empty, initialize sls
	if(qSize==0):
		# print("sls empty, appending seg: "+str(seg))
		sls.append(seg)
	
	else:	
		# New seg has smallest y of all segs in sls
		if(seg[2]+.9 >= sls[0][2]):
			# print("Seg:"+str(seg))
			# print("sls[0]"+str(sls[0]))
			# print("Adding to front of sls: "+str(seg))
			sls = [seg]+sls 

		else:
			# New seg has largest y of all segs in the sls
			if(seg[2] <= int(sls[qSize-1][2])-.9):
				# print("Adding to end of sls: "+str(seg))
				sls.append(seg)

			# Not an edge case
			else:
				mid = int(qSize/2)

				checkLeft = (seg[2] > sls[mid-1][2])
				checkRight = (seg[2] < sls[mid][2])
				rightEnd = qSize
				leftEnd = 0

				while(checkLeft or checkRight):
					# print("mid="+str(mid)
					# 	+"  leftEnd:"+str(leftEnd)
					# 	+"  rightEnd:"+str(rightEnd)
					# 	+"  "+str(seg[2])+"<"+str(sls[mid-1][1])
					# 	+"  "+str(seg[2])+">"+str(sls[mid][1]))
					# print(sls[0][2])
					# print(sls[qSize-1][2])
					totalChecks = totalChecks+1
					if(checkRight): #checkRight is true
						leftEnd=mid
						mid = int((rightEnd+mid)/2);
						
					else: # checkLeft is true
						rightEnd=mid
						mid = int((leftEnd+mid)/2)

					checkLeft = (seg[2]+.9 > sls[mid-1][2]-.9)
					checkRight = (seg[2] < sls[mid][2])

				sls = sls[:mid] + [seg] + sls[mid:]
				# print("Adding to  index "+str(mid)+": "+str(seg))
	# print("Comparisons Required for insert(): "+str(totalChecks))
	# print(sls)
	return sls

# Deletes a given entry in the sweep line status
# Make use of Python function remove() for lists 
def slsDelete(seg, sls):
	sls.remove(seg)
	return sls

# Swap two adjacent entries in the sweep-line status
def slsSwap(id1, id2, sls):

	tmp = sls[id1]
	sls[id1] = sls[id2]
	sls[id2] = tmp

	return sls

# Move the sweep line, swap events which are out of order due to sweep, and add new events if any swaps
def slsMove(sls,x):
	i = 0
	newEvents = []
	while i < len(sls)-1:
		if(sls[i][2]<sls[i+1][2]):
			print("x="+str(x)+":\tSwapping events: "+str(sls[i])+"  "+str(sls[i+1]))
			sls = slsSwap(i, i+1,sls)

			# Intersection happened between zero and one time stamp before
			eventX = x-.5
			eventY = sls[i+1][2]-.5*sls[i+1][0]
			newEvents.append([eventX, eventY, -1])

			i-=2
			if(i<0):
				i=0
		else:
			sls[i][2] = sls[i][2]+sls[i][0]
			i+=1
	return [sls,newEvents]