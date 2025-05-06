from setuptools import setup, find_packages

setup(
    name="rossmann_oltp",
    version="0.1",
    packages=find_packages(include=[
        "rossmann_oltp.models",
        "rossmann_oltp.models.*"
    ]),
    install_requires=[line.strip() for line in open("requirements.txt") if line.strip() and not line.startswith("#")],
)