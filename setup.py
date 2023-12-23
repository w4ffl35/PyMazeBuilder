from setuptools import setup, find_packages

setup(
    name='pymaze',
    version="0.0.1",
    author="w4ffl35",
    description="Python maze generator",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="maze, generator, procedural, dungeon, game, roguelike, procedural generation, procedural dungeon, procedural maze, procedural game, procedural roguelike, procedural dungeon generator, procedural maze generator, procedural game generator, procedural roguelike generator",
    license="AGPL-3.0",
    author_email="",
    url="https://github.com/w4ffl35/pymaze",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.10.0",
    install_requires=[
    ],
    dependency_links=[]
)
