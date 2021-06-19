# -*- coding: utf-8 -*-
"""Installer for the plone.microsite package."""

from setuptools import find_packages
from setuptools import setup
import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = '1.0.0.dev0'

long_description = '\n\n'.join([
    read('README.rst'),
    read('CONTRIBUTORS.rst'),
    read('CHANGES.rst'),
])


setup(
    name='plone.microsite',
    version=version,
    description="A basic Dexterity-based container to be used as a microsite in Plone 5.",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS Microsite',
    author='ForContent',
    author_email='suporte@forcontent.com.br',
    url='https://github.com/collective/plone.microsite',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/plone.microsite',
        'Source': 'https://github.com/collective/plone.microsite',
        'Tracker': 'https://github.com/collective/plone.microsite/issues',
        # 'Documentation': 'https://plone.microsite.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['plone'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7, >=3.9",
    install_requires=[
        'Products.CMFPlone>=5.2',
        'collective.behavior.localdiazo',
        'collective.behavior.localregistry',
        'setuptools',
        'six',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = plone.microsite.locales.update:update_locale
    """,
)
