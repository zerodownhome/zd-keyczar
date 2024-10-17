from setuptools import setup, find_packages

setup(
    name="zd_keyczar",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Hari",
    author_email="harikrishna@zerodown.com",
    description="Keyczar",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zerodownhome/zd-keyczar",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
