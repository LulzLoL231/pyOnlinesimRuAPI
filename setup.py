# -*- coding: utf-8 -*-
#
#  onlinesim.ru - Lib setup file.
#  Created by LulzLoL231 at 02/07/22
#
import re
from setuptools import setup


init_data = open('onlinesim/__init__.py').read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, init_data, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError('Unable to find version string in "onlinesim/__init__.py"')


def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


def requirements():
    reqs_list = []
    with open("requirements.txt", encoding='utf-8') as reqs:
        for req in reqs:
            reqs_list.append(req.strip())
    return reqs_list


setup(
    name='pyOnlinesimRuAPI',
    version=verstr,
    long_description=long_description(),
    long_description_content_type='text/markdown',
    description='Python client for onlinesim.ru API',
    author='Maxim Mosin',
    author_email='max@mosin.pw',
    license='Apache License, Version 2.0, see LICENSE file',
    keywords=['onlinesim', 'onlinesim.ru', 'sim-rent', 'phone-rent'],
    url='https://github.com/LulzLoL231/pyOnlinesimRuAPI',
    download_url='https://github.com/LulzLoL231/pyOnlinesimRuAPI/archive/master.zip',
    packages=['onlinesim'],
    install_requires=requirements(),
    setup_requires=['wheel'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10'
        'Programming Language :: Python :: 3 :: Only',
    ]
)
