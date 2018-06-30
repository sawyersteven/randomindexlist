import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="RandomIndexList",
    version="1.1",
    author="SawyerSteven",
    author_email="sawyerstevenk@gmail.com",
    description="Start a list at any index. Because you can!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sawyersteven/randomindexlist",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
