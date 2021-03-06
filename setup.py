from os import path
import re
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))


def get_version():
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(path.join(here, 'jesFinance', '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version()
long_description = """jesFinance is a Django based webapp to help you
manage your personal finances.
"""

setup(
    name='jesFinance',
    version=version,
    description='Django webapp to manage personal finances',
    long_description=long_description,
    author='Simon Hanna',
    url='https://github.com/agstrike/jesFinance',
    license='MIT',
    packages=['jesFinance'],
    include_package_data=True,
    install_requires=[
        'django>=2.2',
        'djangorestframework>=3.10',
        'django-widgets-improved',
        'django-allauth>=0.40',
        'python-dateutil',
        'django-cors-headers>=3.1',
    ],
    extras_require={
        'OFX Importing': ['ofxparse'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='finance django money money-manager',
    python_requires='>=3.5',
)

