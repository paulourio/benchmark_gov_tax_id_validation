.PHONY: build
build:
	python setup.py build_ext --inplace && python -m pytest -o log_cli=true -vvv
	
benchmark: build 
	PYTHONPATH=. python scripts/benchmark.py