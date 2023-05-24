# Docstring and Pydoc example

A simple example of using docstrings and pydoc.

## Docstrings

To see the values of `__doc__` for the implemented functions, run
```
python sum_func.py
```

Run
```
$ python
>>> from sum_func import *
>>> help(add)
```
to see help for the `add` function (replace `add` with other functions' names to see their help).

Run
```
$ python
>>> import math
>>> help(math)
```
to see an example of a docstring for built-in package.

## Pydoc

Run
* `python -m pydoc sum_func` to show documentation for `sum_func` module.
* `python -m pydoc -w sum_func` to create a `sum_func.html` file with the documentation.
* `python -m pydoc -b` to start a server with an HTML version of documentation.