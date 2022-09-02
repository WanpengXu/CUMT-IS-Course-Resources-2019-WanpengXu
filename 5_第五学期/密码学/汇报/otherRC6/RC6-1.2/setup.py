from setuptools import setup, find_packages
from os.path import join, dirname


PACKAGE = "RC6"
NAME = "RC6"
DESCRIPTION = "RC6 encode-decoder"
AUTHOR = "Mikhail Bityutsky"
AUTHOR_EMAIL = "darmollive@gmail.com"
URL = ""
VERSION = __import__(PACKAGE).__version__
 
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open(join(dirname(__file__), "README.rst")).read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
) 
