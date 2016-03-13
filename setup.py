# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="http-server",
    description="An http server",
    version=0.1,
    author="Hannah Krager and Michael Sullivan",
    author_email="hannahkrager@gmail.com",
    license="MIT",
    py_modules=["server", "client"],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
