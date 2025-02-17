import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "fibonacci2_python_project",
    version = "1.0.0",
    author = "Billy Chan",
    author_email = "billychl@outlook.com",
    description = ("A RESTful service in Python that features the fibonacci2 endpoints. "),
    license = "BSD",
    keywords = "RESTful service",
    url = "https://github.com/billychl1/fibonacci2_python",
    packages=['fibonacci2_python', 'tests'],
    package_dir = { 'fibonacci2_python' : './' }, 
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)