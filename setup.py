from setuptools import setup, find_packages
import pathlib

# Direktori saat ini
HERE = pathlib.Path(__file__).parent

# Baca README.md sebagai long_description
long_description = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="didactic-train",  
    version="0.1.0",
    description="A modular decision framework combining entropy and utility for intelligent systems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Muhammad Dimas Prabowo",
    author_email="muhammadprabowo828@gmail.com", 
    url="https://github.com/Redazn/didactic-train",
    project_urls={
        "Documentation": "https://github.com/Redazn/didactic-train/wiki",
        "Source": "https://github.com/Redazn/didactic-train",
        "Tracker": "https://github.com/Redazn/didactic-train/issues",
    },
    license="MIT",  
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    keywords="entropy utility decision-framework ai-agent",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "spacy"
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'didactic-train = src.main:main',
        ],
    },
)