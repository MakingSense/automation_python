## Install Pytest
1. Execute the following command
```
$ pip3 install -U pytest
```
2. Check that you installed the correct version
```
$ pytest --version
This is pytest version 5.x.y, imported from $PYTHON_PREFIX/lib/python3.7/site-packages/pytest.py
```
## Install from requirements.txt
```
$ pip3 install -r config/requirements.txt
```
# Pytest commands
"-v" argument is for verbose execution.
## Basic execution
```
$ pytest -v
```
## Executing tests with marks
```
$ pytest -m <mark> -v
```
## Executing with details about skipped and expected fail tests
```
$ pytest -rxs -v
```
## Important NOTE
Make sure that the python environment is activated. If not, please follow these steps before any of the steps mentioned above
1. setup a virtual env to install the package (recommended):
```
$ python3 -m venv venv
$ source ./env/bin/activate
$ python -m pip install pytest
```
