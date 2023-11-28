import setuptools
from setuptools import setup

setup(
    name="sdRDM",
    version="0.0.5",
    author="Range, Jan",
    author_email="jan.range@simtech.uni-stuttgart.de",
    license="MIT License",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["sdrdm=sdRDM.cli:app"]},
    include_package_data=True,
    install_requires=[
        "pydantic <= 1.10.11",
        "numpy",
        "pandas",
        "lxml",
        "jinja2",
        "black",
        "typer",
        "pyyaml",
        "toml",
        "anytree",
        "typing_utils",
        "joblib",
        "nob",
        "validators",
        "GitPython",
        "termcolor",
        "redbaron==0.9.2",
        "dotted-dict==1.1.3",
        "markdown-it-py==2.1.0",
        "autoflake==2.0.0",
        "graphql-core==3.2.3",
        "bigtree",
        "anytree",
        "email-validator",
        "astropy",
        "rich",
    ],
    extras_require={
        "test": ["pytest"],
        "dataverse": ["easyDataverse"],
        "hdf5": ["h5py", "deepdish"],
    },
)
