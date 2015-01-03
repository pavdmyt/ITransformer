flake:
	flake8 parse.py main.py
	
clean:
	rm -f `find . -type f -name '*.py[co]'`

