from setuptools import setup, find_packages

setup(
    name="rossmann_oltp",
    version="0.3",
    packages=find_packages(include=[
        "rossmann_oltp_models",
        "rossmann_oltp_models.*"
        "sync_schemas",
        "sync_schemas.*",
    ]),
    install_requires=[
        "fastapi",
        "sqlalchemy"
    ]
)