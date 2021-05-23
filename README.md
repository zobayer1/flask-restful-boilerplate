Flask Tutorial
==============
A Flask RESTful demo application. The goal of this application is to demonstrate the steps of building a Flask server
application ground up following the best RESTful API development practices.

Environment
-----------
This demo application is primarily built for POSIX platforms and compatible with Python 3.8 or higher. However, you can
easily build this application for older python versions with minimal changes. Development dependencies are
listed in [setup.py](./setup.py), [requirements.txt](./requirements.txt) contains the collection of all development,
testing and distribution dependencies, therefore, should be used to set up virtual environments if necessary.

    python3.8 -m venv venv  # if not already created
    source venv/bin/activate
    pip install --upgrade pip
    pip install wheel
    pip install -r requirements.txt

Enable pre-commit for your local repository:

    pre-commit install
    pre-commit autoupdate
    pre-commit run --all-files

Environment Variables:

| Variable Name            | Description                            |
|--------------------------|----------------------------------------|
| `FLASK_ENV`              | Flask app instance name                |
| `FLASK_APP`              | Flask app target module                |
| `FLASK_SECRET`           | Flask app secret key                   |
| `LOGGING_ROOT`           | Logging directory path                 |

Development
-----------
In order to use this demo application to build a RESTful server for your project, simply clone the repository, rename
packages as necessary, update application information in [setup.py](./setup.py) file, add your own test and source
packages, and you are good to go.

Default configurations for your flask application can be defined in [myapi/config.py](myapi/config.py). However, you
can and should use instance relative configurations. Our demo application can utilize the following instance directory
structure:

    instance
    ├── development
    │   └── application.cfg
    ├── production
    │   └── application.cfg
    └── testing
        └── application.cfg

**Note:** Instance directories can contain sensitive information such as secret keys, access tokens, production
configurations, etc. Therefore, you should consider keeping the instance directories out of your VCS.

To install the application in the editable mode:

    pip install -e .

To start a development server, run:

    export FLASK_ENV=development
    export FLASK_APP=myapi.wsgi:app
    export FLASK_SECRET=bb9ba2817ef62e261d3adaf90c2727bb
    export LOGGING_ROOT=logs
    flask run -h 0.0.0.0 -p 5000

**Note:** This project utilizes `python-dotenv` library to read environment variables from `.env`, or, [`.flaskenv`](./.flaskenv) files. You can move all your export commands to such a file to avoid having to type them repeatedly. Be
careful when running tests using tox, or running application with WSGI tools like gunicorn, as environment variables
must be set explicitly to work with these environments.

Testing
-------
You can run all tests simply by running:

    pytest -s

To run tests with Tox with coverage:

    tox -e py38
    tox -e lint

If you have updated dependencies, use the `--recreate` flag with Tox commands:

    tox --recreate

Distribution
------------
### Repository:
Simply share the repository with collaborators.

### Headless:
To create a source distribution, run:

    python setup.py sdist

### Wheel:
To create a wheel package, run:

    python setup.py bdist_wheel

**Note:** This application uses setuptools-scm which will automatically pull package version from git tags.

Deployment
----------
First, extract or install your application packages. This can be done in two ways.

**From Source:**

1. Change directory into the root of your source directories.
2. Setup a virtual environment

**From Wheel:**

1. Setup a virtual environment
2. Install wheel package with `pip`

Then, place instance directories, set environment variables, and serve with `gunicorn`:

    gunicorn -w 4 -b 0.0.0.0:5000 myapi.wsgi:app

License
-------
This repository is distributed under [MIT License](./LICENSE)
