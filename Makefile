all: Optimus.so

Optimus.so: build.so
	python setup.py bdist_rpm

build.so: setup.py
	python3 setup.py build_ext --inplace

clean:
	rm -rf pySPH_chocktube/*.so build dist pySPH_chocktube/pyParticle.cpp MANIFEST 
