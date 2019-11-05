import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GeVhoo_brain_games",
    version="0.1.0",
    author="GeVhoo",
    author_email="gvahrushev@mail.ru",
    description="Simple game - Hexlet project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GeVhoo/python-project-lvl1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
