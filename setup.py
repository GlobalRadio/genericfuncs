from setuptools import setup
from os import path

_here = path.dirname(path.abspath(__file__))
_readme = open(path.join(_here, 'README.rst')).read()

setup(
    name='genericfuncs',
    description='Dynamic dispatch over arbitrary predicates',
    long_description=_readme,
    version='0.2.1pr1',
    url='https://github.com/AvivC/genericfuncs',
    author='Aviv Cohn',
    author_email='avivcohn123@yahoo.com',
    license='MIT',
    platform='any',
    py_modules=['genericfuncs'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='generic functions utility programming development'
)
