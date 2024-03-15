from setuptools import setup, find_packages

setup(
    name='pymazebuilder',
    version='1.1.0',
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'pymazebuilder=pymazebuilder.src.pymazebuilder.main:main',
        ],
    },
    install_requires=[
        'pygame',
    ],
)
