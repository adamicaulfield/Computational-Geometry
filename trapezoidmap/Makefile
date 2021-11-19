CUR_DIR = $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

INCLUDES = -I$(CUR_DIR)/include/

default:
	g++ $(INCLUDES) -c ./src/Node.cpp
	g++ $(INCLUDES) -c ./src/Segment.cpp
	g++ $(INCLUDES) -c ./src/Tree.cpp 
	g++ $(INCLUDES) -o ./bin/trapezoidmap ./src/main.cpp Segment.o Tree.o Node.o
	rm *.o
clean:
	rm ./bin/trapezoidmap