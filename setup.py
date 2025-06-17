from setuptools import setup, find_packages

setup(
    name="shodan-mcp",
    version="0.1.0",
    description="A Model Context Protocol (MCP) toolkit for Shodan API integration.",
    author="Jak Bin",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[
        "shodan",
        "mcp"
    ],
    entry_points={
        "console_scripts": [
            "shodan-mcp=main:mcp.run"
        ]
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
