# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="flask-tutorial",
    url="https://github.com/zobayer1/flask-tutorial",
    license="MIT",
    author="Zobayer Hasan",
    author_email="zobayer1@gmail.com",
    description="RESTful application server development with python flask",
    keywords="python flask restful api server development",
    use_scm_version=True,
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    zip_safe=True,
    platforms=["posix"],
    entry_points={
        "console_scripts": [
            "myapi = myapi.manage:cli",
        ],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
