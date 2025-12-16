"""
UzbekchaDasturlash - AL (Algoritm Tili)
O'zbekcha Dasturlash Tili - Python asosida to'liq o'zbekcha sintaksisga ega
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="uzbekchadasturlash",
    version="1.0.1",
    author="AL Team",
    author_email="uzbekchadasturlash@gmail.com",
    description="AL (Algoritm Tili) - O'zbekcha Dasturlash Tili",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yahyobekalfa-crypto/uzbekchadasturlash",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Natural Language :: Uzbek",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "mobil": ["kivy>=2.0.0"],
        "web": ["flask>=2.0.0"],
        "aql": ["numpy>=1.20.0", "scikit-learn>=1.0.0"],
        "full": ["kivy>=2.0.0", "flask>=2.0.0", "numpy>=1.20.0", "scikit-learn>=1.0.0"],
    },
    entry_points={
        "console_scripts": [
            "al=cli:main",
        ],
    },
    include_package_data=True,
    keywords="uzbek uzbekcha dasturlash tili programming language algorithm AL",
)
