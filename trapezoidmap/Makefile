CUR_DIR = $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

INCLUDES = -I$(CUR_DIR)/include/

default:
	g++ $(INCLUDES) -c ./src/Tree.cpp 
	g++ $(INCLUDES) -c ./src/Node.cpp
	g++ $(INCLUDES) -o ./bin/trapezoidmap ./src/main.cpp Node.o Tree.o
	rm *.o

clean:
	rm ./bin/trapezoidmap
	rm *.o