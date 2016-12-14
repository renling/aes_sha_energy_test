TARGET = energy_test
SRC = energy_test.cpp
CRYPTOPPDIR = ../cryptopp563/
INC = -I. -I$(CRYPTOPPDIR) 
LDFLAGS = -L$(CRYPTOPPDIR) -lcryptopp -lpthread

$(TARGET): $(SRC)
	g++ -O3 -fopenmp -std=c++11 -o $@ $< $(INC) $(LDFLAGS)

clean:
	rm -f $(TARGET) *~
