

<!---Replace this with your actual paper if you have one! -->
[![arXiv](https://img.shields.io/badge/arXiv-999.9999-b31b1b.svg)](https://arxiv.org/abs/999.9999)

<!--- Update these with your own repo's link -->

[![Test](https://github.com/deepskies/DeepTemplate-Tools/actions/workflows/deep-test.yml/badge.svg)](https://github.com/deepskies/DeepTemplate-Tools/actions/workflows/deep-test.yml)

<!--- Select your actual license  -->
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

<!--- Insert the correct PyPi package. DeepBench PyPi link being used as an example. -->
[![PyPI version](https://badge.fury.io/py/deepbench.svg)](https://badge.fury.io/py/deepbench)

# DeepTemplate-Tools
A template repository for DeepSkies toolset items.

## How to use this template
1. When you make a new repository, use the *Repository Template* dropdown, and select `deepskies/DeepTemplate-Tools`
2. Change the links and paths in this readme for updated badges
3. Change the name of `example_envoriment` to match your project; update the tests to match
4. Update the pyproject.toml with the project name and your name.
5. Start using the pyproject.toml to track your depedencies.
6. Install the [`pre-commit`](/workspaces/DeepTemplate-Tools/.pre-commit-config.yaml)
7. Run `pytest --cov` to verify things have been configured correctly.


### Installing with pyproject.toml and `poetry`

The included pyproject here recommends `poetry`.
To install the project and use poetry -

```
pip install poetry
poetry shell
poetry install
pytest --cov
```

Running pytest just verifies things are in order as they should be.
If you get a failed test here, that is not a problem, just go and fix the test. If the tests fail to run at all, then verify everything is correctly called.

Using poetry overall requires a few commands, very similar to `conda` or `virtual envoriment`, which we cover in the [`deepskies Wiki`](https://github.com/deepskies/DeepWiki/wiki/Basics-of-Virtual-Environments#poetry)

### Installing and using the `pre-commit`

`pre-commit` checks basic code structure and does things like verify no passwords or secret keys are shared, and automically cleans up your code to follow pep-8.

To use this - run

```
pip install pre-commit
pre-commit install
```

This installs the pre-commit to your local directory. Now, the next time you run `git commit -m "message"`, it will run and check your code, and make the changes required to keep everything in line with pep-8. You will have to add changes again, and then commit a second time to keep your changes.

Hint: If you **know** you want to get around the pre-commit, run `git commit -m 'message' --no-verify`. Be warned, use this only in extreme cases. Avoiding it for the sake of avoiding it will make your collaborator work more difficult.


## Using Autodocs/ReadTheDocs 

This repository also includes some auto-documentation functionality. 
The will build documentation from your docstrings into webpages with nice formatting. 
Further documentation, beyond what's talked about here, [can be found be found here](https://www.sphinx-doc.org/en/master/index.html)

In order to rebuild the documentation that exists - run `cd docs; sphinx-build . _build`. 
This looks at the `conf.py` file to figure out how the documentation is build up, and makes each `.rst` file into an html file. Your `conf.py` file will need to be updated with the name of the package and your name as well. 

Each `.rst` file corresponds to a page of html. 

In order to update this with your own code, make a new file, in this case named `file.rst`, and fill it with the documention for your module using the block of code: 

```
{Page Title} 
=================

.. autoclass:: {package name}.{module name}.{class name}
    :members:
```

In order to make sure this is added to your documentation index, make sure your `index.rst` is updated to be: 

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   example
   file

```