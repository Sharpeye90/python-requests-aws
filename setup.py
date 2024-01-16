"""python-requests-aws installation script."""

from __future__ import unicode_literals
from setuptools import setup


if __name__ == "__main__":
    with open("README.md", encoding='utf-8') as readme:
        setup(
            name='requests-aws',
            version='0.1.5',
            author='Paul Tax',
            author_email='paultax@gmail.com',
            install_requires=['requests>=0.14.0'],
            py_modules=['awsauth'],
            url='https://github.com/tax/python-requests-aws',
            license='BSD licence, see LICENCE.txt',
            classifiers = [
                "Development Status :: 4 - Beta",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: BSD licence",
                "Operating System :: MacOS :: MacOS X",
                "Operating System :: POSIX",
                "Operating System :: Unix",
                "Programming Language :: Python :: 2",
                "Programming Language :: Python :: 3",
                "Topic :: Software Development :: Libraries :: Python Modules",
            ],
            description=readme.readline().strip(),
            long_description=readme.read().strip() or None,
        )