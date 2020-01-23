test:
	PYTHONPATH="." python -m pytest tests/ -rxsw -v

compile:
	@echo Compiling python code
	python -O -m compileall j2exts

clean:
	find -name "*.py?" -delete
	rm -rf .pytests_cache */__pycache__

install_deps:
	pip install -r requirements.txt
	pip install -r requirements_dev.txt

all: clean compile test
