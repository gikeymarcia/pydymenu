# https://realpython.com/pypi-publish-python-package/#a-small-python-package
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


# https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use
setup(
    name="pydymenu",
    version="0.4.0",
    description="A pythonic wrapper interface for fzf, dmenu, and rofi.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gikeymarcia/pydymenu",
    author="Mikey Garcia",
    author_email="gikeymarcia@gmail.com",
    license="GPL-3.0",
    packages=find_packages(exclude="test"),
    install_requires=["rich"],
)
