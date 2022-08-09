"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(

    name="your-project",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9, <4",
    # list runtime dependencies 
    # install_requires=["jsonschema"],
    # development tools 
    extras_require={  
        "dev": [
            "flake8",                       # linters
            "pytest", "coverage", "tox",    # testing tools
        ],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # package_data={  # Optional
    #    "your-project": ["*.json"],
    # },
    # cli commend line
    # entry_points={  # Optional
    #    "console_scripts": [
    #        "mycommand=your-project.cli:commands",
    #    ],
    # },
)
