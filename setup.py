import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="RandomIndexList",
    version="1.3",
    author="SawyerSteven",
    author_email="sawyerstevenk@gmail.com",
    description="Start lists at any position. Because you can!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sawyersteven/randomindexlist",
    packages=setuptools.find_packages(),
    classifiers=(
		"Programming Language :: Python ",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
