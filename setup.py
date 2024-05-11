from setuptools import setup, find_packages
import os

# Read the README.md file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="SQLibEngine",
    version="0.1.2",
    author="AK",
    author_email="ak@stellar-code.com",
    url="https://github.com/TRC-Loop/SQLib",
    description="A simple SQLite3 wrapper for Python",
    long_description=long_description,  # Set the long description
    long_description_content_type="text/markdown",  # Specify the content type
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.6",
)
