.PHONY: build

build:
	arch -x86_64 python setup.py py2app --arch x86_64 

clean:
	rm -rf dist build