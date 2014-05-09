from setuptools import setup, find_packages

setup(
    name='hubstar',
    version='0.1',
    author='satojkovic',
    author_email='satojkovic@gmail.com',
    url='http://github.com/satojkovic/hubstar',
    description='hubstar is a command line tool to star/unstar a repository.',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "hubstar=hubstar.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python2.7",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords="github star unstar CLI",
    license="MIT",
    install_requires=[
        "PyGithub >= 1.24.1",
        "requests >= 2.2.1",
    ],
)
