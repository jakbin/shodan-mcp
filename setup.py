from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="shodan-mcp",
    version="0.1.0",
    description="A Model Context Protocol (MCP) toolkit for Shodan API integration.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Jak Bin",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[
        "shodan",
        "mcp"
    ],
    entry_points={
        "console_scripts": [
            "shodan-mcp=main:main"
        ]
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
