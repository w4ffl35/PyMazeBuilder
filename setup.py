from setuptools import setup, find_packages

setup(
    name='pymazebuilder',
    version='1.4.2',
    author="w4ffl35",
    description="RPG",
    long_description=open(
        "README.md",
        "r",
        encoding="utf-8"
    ).read(),
    long_description_content_type="text/markdown",
    keywords="maze, builder, generator, rpg, game, development",
    license="AGPL-3.0",
    author_email="contact@capsizegames.com",
    url="https://github.com/w4ffl35/PyMazeBuilder",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'pymazebuilder=pymazebuilder.src.pymazebuilder.main:main',
        ],
    },
    install_requires=[
    ],
)
