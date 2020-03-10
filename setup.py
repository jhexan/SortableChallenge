import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires=[
]

setuptools.setup(
    name="SortableChallenge",
    version="0.0.1",
    author="John Hexan",
    author_email="john.hexan@gmail.com",
    description="Sortable coding challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhexan/SortableChallenge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Documentation": "https://jhexan.github.io/SortableChallenge/_build"
                         "/html/index.html",
        "Source Code": "https://github.com/jhexan/SortableChallenge/tree"
                       "/master/auction",
    },
    python_requires='>=3.6',
    install_requires=install_requires
)