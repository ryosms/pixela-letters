import os

from setuptools import setup, find_packages

readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
description = ''
with open(readme_path) as f:
    description = f.read()

setup(
    name='pixela_letters',
    varsion='2018.1',
    author='ryosms',
    url='https://github.com/ryosms/pixela-letters',
    description="Let's writer poems on the Pixela graph!",
    long_description=description,
    license='MIT',
    packages=find_packages(exclude=['tests']),
    package_dir={'': '.'},
    install_requires=['requests', 'python-dotenv'],
)
