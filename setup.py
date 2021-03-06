import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seqhash", 
    version="1.0.0",
    author="Keoni Gandall",
    author_email="koeng101@gmail.com",
    description="The seqhash algorithm implemented in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Koeng101/seqhash",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

