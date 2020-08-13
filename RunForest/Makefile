IDIR =include
ODIR=obj
LDIR =lib
LIBS=-lm
SRC = src
VPATH := src

CXX=g++
CPPFLAGS=-I$(IDIR)

_DEPS = RunForest.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = RunForest.o Requests.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


RunForest.dll: $(OBJ)
	$(CXX) -shared -o $@ $^ $(CPPFLAGS) $(LIBS)
$(ODIR)/%.o: $(SRC)/%.cpp $(DEPS)
	$(CXX) -c -DBUILDING_EXAMPLE_DLL -o $@ $< $(CPPFLAGS) -Wl,--out-implib,libexample_dll.a

#RunForest: $(OBJ)
#	$(CXX) -o $@ $^ $(CPPFLAGS) $(LIBS)
#$(ODIR)/%.o: $(SRC)/%.cpp $(DEPS)
#	$(CXX) -c -o $@ $< $(CPPFLAGS)

	
.PHONY: clean

clean:
	rm -r $(ODIR)  
	mkdir $(ODIR)


