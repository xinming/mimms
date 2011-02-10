PYTHON=python
DESTDIR=/

all:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install --root $(DESTDIR)

clean:
	$(PYTHON) setup.py clean
	rm -rf build
	find . \( -name "*.pyc" -or -name "*~" \) -exec rm {} \;
