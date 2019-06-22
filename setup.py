#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="statshot",
    packages=find_packages(),
    version="1.0",
    author="Kirill_Shevchenko",
    author_email="Kirill_Shevchenko1@epam.com",
    description="Phyton.HomeTask.3",
    include_package_data=True,
    install_requires=['psutil'],
    license="EPAM"
)
