
from setuptools import setup, find_packages

setup(
    name='j2exts',
    version='0.1',
    description='Random collection of Jinja2 extensions',
    author='Johann Schmitz',
    author_email='johann@j-schmitz.net',
    url='https://git.ercpe.de/ercpe/jinja2-extensions.git',
    packages=find_packages(exclude=('tests',)),
    install_requires=['Jinja2'],
    zip_safe=False,
    license='MIT',
)
