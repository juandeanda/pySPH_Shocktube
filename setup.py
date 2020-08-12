import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pySEED",
    version="1.0",
    author="Juan de Anda Suarez",
    author_email="m.c.juandeanda@gmail.com",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/juandeanda/pySPH_Shocktube.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5.2',
    install_requires=[
   'numpy>=1.18.2',
   ]
)
