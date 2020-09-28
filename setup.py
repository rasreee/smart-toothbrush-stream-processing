"""
Package build, test, and install script.

"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="smart-toothbrush-stream-processing",
    version="0.0.1",
    author="Lesley Chang",
    author_email="lesleychang@berkeley.edu",
    description="Stream processing implementation for smart tootbrush device session data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    test_suite='tests'
)
