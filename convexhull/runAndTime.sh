#
# Adam Caulfield (ac7717)
# CSCI716 - Computational Geometry - Coding Assignment 1
#
# runAndTime.sh
# 
# This bash script runs both the Brute Force and Grahams scan 50 times 
# to find the convex hulls and record the execution time.
#
# After running 50 times, this script finds the average run time and prints to console.
#

iters=$1 

if test -f "bruteForce.log"; then
	rm bruteForce.log
fi

if test -f "graham.log"; then
	rm graham.log
fi

touch bruteForce.log

echo "Starting $iters Iterations of Brute Force Method"
for ((i=0; i<iters; i++))
do
	python3 bruteForce.py >> bruteForce.log
done

touch graham.log
echo "Starting $iters Iterations of Grahams Scan"
for ((i=0; i<iters; i++))
do
	python3 graham.py >> graham.log
done

awk '{s+=$1; count++}END{print "Average Run Time for Brute Force Method:",s/count}' RS=" " bruteForce.log

awk '{s+=$1; count++}END{print "Average Run Time for Grahams Scan:",s/count}' RS=" " graham.log

