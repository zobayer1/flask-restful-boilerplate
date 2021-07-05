Flask RESTful Boilerplate
=========================
A Flask RESTful demo application. The goal of this application is to demonstrate the steps of building a Flask server application ground up following the best RESTful API development practices.

Environment
-----------
This demo application is primarily built for POSIX platforms and compatible with Python 3.8 or higher. However, you can easily build this application for older python versions with minimal changes. Development dependencies are listed in [`setup.cfg`](./setup.cfg).

    python3.8 -m venv venv  # if not already created
    source venv/bin/activate
    pip install --upgrade pip
    pip install wheel
    pip install -e .[dev,test]

After dependencies have been installed, enable pre-commit for your local repository:

    pre-commit install
    pre-commit autoupdate
    pre-commit run --all-files

### Environment Variables:

| Variable Name            | Description                            |
|--------------------------|----------------------------------------|
| `FLASK_ENV`              | Flask app instance name                |
| `FLASK_APP`              | Flask app target module                |
| `FLASK_SECRET`           | Flask app secret key                   |

**Note:** There are some dependencies that will not work on Windows, for example `gunicorn`. You have to exclude that from dependencies and add in your own workarounds if a WSGI server is required for Windows platform.

Development
-----------
In order to use this demo application to build a RESTful server for your project, simply clone the repository, rename packages as necessary, update application information in [`setup.py`](./setup.py) file, add your own test and source packages, and you are good to go.

Dependencies should be added to [`setup.cfg`](./setup.cfg) file with pinned versions to keep the system as stable as possible. This file allows us to add dependencies based on build profiles. We do not use `requirements.txt` file because it is quite difficult to properly manage dependencies using a simple requirements file.

Default configurations for your flask application can be defined in [`myapi/config.py`](myapi/config.py). However, you can and should use instance relative configurations. Our demo application can utilize the following instance directory structure:

    instance
    ├── development
    │   ├── application.cfg
    │   └── logging.yaml
    ├── production
    │   ├── application.cfg
    │   └── logging.yaml
    └── testing
        ├── application.cfg
        └── logging.yaml

**Note:** Instance directories can contain sensitive information such as secret keys, access tokens, production configurations, etc. Therefore, you should consider keeping the instance directories out of your VCS. Consider removing `!instance/testing` from [.gitignore](./.gitignore) file, this has been added to keep testing instance for reference.

To install the application in the editable mode with all dependencies:

    pip install -e .[dev,test]

To start a development server, run:

    export FLASK_ENV=development
    export FLASK_APP=myapi.wsgi:app
    export FLASK_SECRET=bb9ba2817ef62e261d3adaf90c2727bb
    export LOGGING_ROOT=logs
    flask run -h 0.0.0.0 -p 5000

**Note:** This project utilizes `python-dotenv` library to read environment variables from `.env`, or, [`.flaskenv`](./.flaskenv) files. You can move all your export commands to such a file to avoid having to type them repeatedly. Be careful when running tests using tox, or running application with WSGI tools like gunicorn, as environment variables must be set explicitly to work with these environments.

**Note:** `.flaskenv` file may contain sensitive information about system variables for your system and should be excluded from VCS. Consider removing `!.flaskenv` from [.gitignore](./.gitignore) file.

### Directory Structure

- `apis`: Your main API blueprints packages. You can add more according to your application requirements.
  - `admin`: The admin blueprints, usually endpoints that is used by administrative clients.
  - `apiv1`: The V1 API blueprints, usually your main consumer endpoints with simple API versioning.
  - `local`: The local blueprints, usually endpoints that are accessed from the server machine locally, for example, by monitoring tools.
- `commons`: Common packages used by other resources or services.
  - `enums`: Your enum classes and application constants go in this package.
  - `errors`: Your custom exception classes and errono constants go in this package.
  - `utils`: Utility functionalities go in this package.
- `extensions`: Package for holding 3rd party app extension factories.
- `internals`: Package holding your main business logic, such as models, schemas, services, etc.
  - `models`: Your SQL or other database model classes go in this package.
  - `schemas`: Your marshmallow or custom schema classes go in this package.
  - `services`: Your business logic implementations go in this package.

**Note:** These are just some conventions commonly followed in server application development, feel free to rearrange or re-organize to your liking, or project requirements.

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
3. Install application with `pip`: `pip install -e .`

**From Wheel:**

1. Setup a virtual environment
2. Install wheel package with `pip`: `pip install myapi-{tags}.whl`

Then, place instance directories, set environment variables, and serve with `gunicorn`:

    gunicorn -w 4 -b 0.0.0.0:5000 myapi.wsgi:app

License
-------
This repository is distributed under [MIT License](./LICENSE)
