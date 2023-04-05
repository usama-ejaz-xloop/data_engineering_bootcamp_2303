# Writing robust readable and maintainable code

## Documentation

### Task description

In this task you will learn how to create documentation with Sphinx. Firstly you will create a simple "positive" calculator application (positive because it can deal only with positive numbers). Afterwards you will document it using docstrings. At the end you will generate documentation (e.g. in html format).

### Sub-task 1 - Sphinx documentation for a calculator - project structure

1. In the root of your project create the following sub-directories/files:
```
    src/
    │
    ├── calculator/
    │   ├── calculator.py
	│	└── __init__.py
    │
    ├── arithmetic/
    │   ├── product.py
    │   ├── sum.py
    │	├── __init__.py
    ├── common/
        ├── constants.py
        └── __init__.py
```

### Sub-task 2 - Sphinx documentation for a calculator - implementation


1. In `sum.py` create a function `add` which takes as argument two numbers (number is of `float` or `int` type) and returns the sum of these arguments converted to `float` type.
2. Analogously in `product.py` create a function `multiply` which takes as argument two numbers (number is of `float` or `int` type) and returns the product of these arguments converted to `float` type.
3. In the `constants.py` file define variable `ERROR_VALUE` of type `float` equal to `-1`.
4. In `calculator.py` create `class calculator`. Ensure that `class calculator`:
	1. Has an attribute `error` of type `float` with default value `ERROR_VALUE`.
	2. Has a constructor which adds an instance attribute `name` of type `str` and sets its value to `"Positive calculator"`.
	3. Provides the following methods:
		1. `add_positive` which takes two arguments and returns result of our `add` function if both arguments are positive and `error` otherwise.
		2. `multiply_positive` which takes two arguments and returns result of our `multiply` function if both arguments are positive and `error` otherwise.


### Sub-task 3 - Sphinx documentation for a calculator - documentation preparation

3. Document all `.py` files using docstrings. This includes description of all modules, functions, classes, methods, constants etc. Recommendation for docstrings: use e.g. Google style (see [napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)) - it seems to be much more modern and user-friendly than native Sphinx style ([example of Google documentation](https://gist.github.com/redlotus/3bc387c2591e3e908c9b63b97b11d24e)).
Moreover, provide at least one section `Examples` (or an equivalent in non-Google style) which will be used later on doctest Sphinx's extension (should be written in [doctest format](https://docs.python.org/3/library/doctest.html)).

4. Create virtual environment, activate it. Add to requirements the following libraries: Sphinx, rinohtype
(the latter one allows to generate pdf documentation).

5. Take a look at [sphinx-quickstart](https://www.sphinx-doc.org/en/master/man/sphinx-quickstart.html). Create a directory `docs`, enter it and execute bash command:

`sphinx-quickstart`

Now go through the settings:
```
> Separate source and build directories (y/n) [n]: y
> Project name: Calculator
> Author name(s): <your_name>
> Project release []: 0.0.1
> Project language [en]:
```

Go to `source` directory. Note that there are the following files:
- `conf.py` - this is a [build configuration file](https://www.sphinx-doc.org/en/master/usage/configuration.html) which contains (almost) all configuration needed to customize Sphinx input and output behavior.
- `index.rst` - this is the index file for the documentation which binds together all other documentation files (typically it contains a Table of Contents that will link to all other pages of the documentation).
- `Makefile` - provides a list of documentation commands e.g. `make html` creates documentation in html format.

The other files are irrelevant for us in this task. However, if you are curious what they are used for visit [Sphinx-start](https://sphinx-tutorial.readthedocs.io/start/).

### Sub-task 4 - Sphinx documentation for a calculator - auto documentation generation


1. Take a quick glance at `conf.py` to get familiar with raw template, before performing changes. Update `conf.py`:
	- paths - uncomment `sys.path.insert(0, os.path.abspath('.'))` and change `'.'` to `'../'` so that it points to the root of your project. Moreover, add the following:
	```
	sys.path.insert(0, os.path.abspath("../src"))
	sys.path.insert(0, os.path.abspath("../src/arithmetic"))
	sys.path.insert(0, os.path.abspath("../src/common"))
	```
	- extensions -
	```
	extensions = [
    "rinoh.frontend.sphinx",  # to generate pdf documentation
    "sphinx.ext.doctest",  # `make doctest` is available now
    "sphinx.ext.autodoc",  # for auto documentation
    "sphinx.ext.duration",  # duration report
    "sphinx.ext.autosummary",  # for generating comprehensive API references
    "sphinx.ext.napoleon",  # for support of Google and NumPy styles in docstrings
    ]
    ```
    - broken references warning - add the following code
    ```
	nitpicky = (
    True  # Sphinx will warn you now about all references where the target cannot be found
	)
	```
	- [html theme](https://www.sphinx-doc.org/en/master/usage/theming.html) - choose your favorite theme e.g. `html_theme = "bizstyle"`.
	- [Napoleon settings](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) - Add the following code to the end of `conf.py` (feel free to adjust these setting):
	```
	napoleon_google_docstring = True
	napoleon_numpy_docstring = True
	napoleon_include_init_with_doc = False
	napoleon_include_private_with_doc = False
	napoleon_include_special_with_doc = True
	napoleon_use_admonition_for_examples = False
	napoleon_use_admonition_for_notes = False
	napoleon_use_admonition_for_references = False
	napoleon_use_ivar = False
	napoleon_use_param = True
	napoleon_use_rtype = True
	napoleon_preprocess_types = False
	napoleon_type_aliases = None
	napoleon_attr_annotations = True
	```
1. Now we use [sphinx apidoc](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html) command line command to auto document our project.
Ensure that you are in the `docs` directory and execute:
`sphinx-apidoc -o source ../src`

This command places all output files to `source` directory and makes the documentation for packages/modules/files/classes/functions from our `src` directory. Note that if you use implicit namespaces then you need to add `--implicit-namespaces` flag to this command.

Depending on the desired output execute one of the following:
- `make html`
- `make latex`
- `sphinx-build -b rinoh source build/pdf`
Now the respective builds can be found in appropriate sub-directories of `build` directory. To see e.g. the html documentation run:
`firefox ./build/html/index.html &`

3. Doctest. To run previously written documentation examples sections as tests execute:
`make doctest`

