.PHONY: build

build:
	arch -x86_64 python setup.py py2app --arch x86_64 

clean:
	rm -rf dist build

install_deps:
	arch -x86_64 pip3 install -r requirements.txt