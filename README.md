# flask-example
Flask example for vapor framework comparison

Install requirements (see below for instructions using virtualenv):
```
pip install -r requirements.txt
```

If `pip` is not available, install it as follows for example on Ubuntu:
```
apt-get install python-pip
```
See [the installation instructions](https://pip.pypa.io/en/stable/installing/) for details. `pip` is already installed for Python 2 versions >= 2.7.9 and Python 3 versions >= 3.4

Run with
```
python run.py
```

Note that [Flask’s built-in server is not suitable for production](http://flask.pocoo.org/docs/0.11/deploying/#deployment) and
this set-up is therefore not suitable for performance comparisons as-is. Proper deployment options are listed on the page linked to.

The example as-is does allow comparing the development aspect of frameworks.

## Virtualenv

Provided `virtualenv` has been installed via `pip install virtualenv` run

```
virtualenv venv
source venv/bin/activate
```

to set up a virtual env before installing the dependecies:

```
pip install -r requirements.txt
```

This will install everything locally.
