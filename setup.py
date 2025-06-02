from setuptools import setup, find_packages

setup(
    name="cognitive_framework",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "spacy",
        "scipy"
    ],
    entry_points={
        'console_scripts': [
            'didactic-train = src.main:main',
        ],
    },
)
