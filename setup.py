import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EastMoney",
    version="1.0.0",
    author="Hurin Hu",
    author_email="hurin@live.ca",
    description="Retrieve A-share information from EastMoney for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HurinHu/EastMoney",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
