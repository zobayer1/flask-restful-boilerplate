# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="flask-tutorial",
    url="https://github.com/zobayer1/flask-tutorial",
    author="Zobayer Hasan",
    author_email="zobayer1@gmail.com",
    description="RESTful application server development with python flask",
    keywords="python flask restful api server development",
    license="MIT",
    packages=find_packages(exclude=["docs", "tests"]),
    use_scm_version=True,
    platforms=["posix"],
    entry_points={
        "console_scripts": [
            "myapi = myapi.manage:cli",
        ],
    },
)
