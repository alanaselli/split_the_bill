# Learnings throughout this project

## Python paths
If I run:
`python src/main.py`

It works. If I run:
`python tests/test_01.py`

I get the error:
> ModuleNotFoundError: No module named 'src'

### Why this happens:
The  ModuleNotFoundError: No module named 'src' error occurs because when you run a script directly (e.g. python tests/test_01.py), Python adds the script's directory (tests/) to its search path (sys.path), but it does not add the project root directory. As a result, Python cannot find the root-level src directory.

### Why running `python -m unittest tests/test_01.py` works:
The `-m` switch tells Python to locate a library module (in this case, unittest https://docs.python.org/3/library/unittest.html) and run it as a script.
  • When running in this mode, Python initializes sys.path[0]  with the current working directory (the project root,  split_the_bill/) instead of the script's directory.
  • Since split_the_bill/ is the search root, Python can successfully locate the src directory, allowing `from src.main` import Bill in test_01.py to resolve properly.