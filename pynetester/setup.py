# setup.py for pynetester
#
# Direct install (all systems):
#   "python setup.py install"
#
# For Python 3.x use the corresponding Python executable,
# e.g. "python3 setup.py ..."
#
# (C) 2018-2020 ZouMingzhe <zoumingzhe@qq.com>
#
# SPDX-License-Identifier:    MIT

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="pynetester",
    description="network tester for python",
    version="0.0.1",
    author="Zou Mingzhe",
    author_email="zoumingzhe@qq.com",
    url="https://github.com/zoumingzhe/pynetester",
    packages=[
        'pynetester',
    ],
    license="MIT",
    long_description=open('..\README.rst', mode='r', encoding='UTF-8').read(),
    install_requires=[
        'PyYaml',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
)