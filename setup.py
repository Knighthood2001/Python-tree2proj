from setuptools import setup, find_packages

setup(
    name="tree2proj",
    version="0.1.0",
    description="Generate project folders/files from JSON tree (via tree2json)",
    author="knighthood",
    author_email="2109695291@qq.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tree2json>=0.1.3",
        "pyperclip>=1.8.0"
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "tree2proj=tree2proj.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
