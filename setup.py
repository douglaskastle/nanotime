#!/usr/bin/env python

from distutils.core import setup

setup(name='nanotime',
      version='0.1',
      description=' This is a subclass of the datetime module but adding nanosecond resolution',
      author='Douglas Kastle',
      author_email='douglas.kastle@gmail.com',
      url='https://github.com/douglaskastle/nanotime',
      packages=['nanotime',],
      long_description=open('README.md', 'rt').read(),
      classifiers =['Programming Language :: Python',
                    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                    'Operating System :: OS Independent',
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Libraries :: Python Modules',
                    ],
     )
