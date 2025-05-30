from setuptools import setup, find_packages

setup(
    name="rossmann_oltp",
    version="0.4",
    packages=find_packages(include=[
        "rossmann_oltp_models",
        "rossmann_oltp_models.*",
        "rossmann_sync_schemas",
        "rossmann_sync_schemas.*",
    ]),
    install_requires=[
        "pydantic",
        "sqlalchemy"
    ]
)
