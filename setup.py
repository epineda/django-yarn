from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from os import path

here = path.abspath(path.dirname(__file__))

try:
    from collections import OrderedDict
    requirements = []
except ImportError:
    requirements = ['ordereddict']

setup(
    name='django-yarn',
    version='1.0.0',
    description='A django staticfiles finder that uses yarn. Based on django-npm from Kevin McCarthy https://github.com/kevin1024/django-npm.',
    url='https://github.com/epineda/django-yarn',
    author='Edgard Pineda',
    author_email='edgard.pineda@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='django yarn npm staticfiles',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
    extras_require={
        'test': ['pytest'],
    },
)
