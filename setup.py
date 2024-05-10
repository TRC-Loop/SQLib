from setuptools import setup, find_packages

setup(
    name="SQLib",
    version="0.1.0",
    author="AK",
    author_email="ak@stellar-code.com",
    url="https://github.com/TRC-Loop/SQLib",
    description="A simple SQLite3 wrapper for Python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.6",
)