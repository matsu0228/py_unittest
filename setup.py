from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

requires = [
]

setup(
    name='yourpachage',
    version='0.0.1',
    description='your package',
    long_description=readme,
    packages=find_packages(exclude=["tests"]),
    install_requires=requires,
    test_suite="tests",
)