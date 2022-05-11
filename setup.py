#!/usr/bin/env python
#
# Copyright 2016 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup
import versioneer


DISTNAME = "empyrical"
DESCRIPTION = """empyrical is a Python library with performance and risk \
statistics commonly used in quantitative finance"""
LONG_DESCRIPTION = """empyrical is a Python library with performance and risk
statistics commonly used in quantitative finance by `Quantopian Inc`_.

.. _Quantopian Inc: https://www.quantopian.com
.. _Zipline: https://zipline.io
.. _pyfolio: https://quantopian.github.io/pyfolio/
"""

test_reqs = [
    "pytest>=7.1.2",
]

requirements = [
    'numpy>=1.9.2',
    'pandas>=0.16.1',
    'scipy>=0.15.1',
]

extras_requirements = {
    "dev": [
        "flake8==2.5.1"
    ]
}

if __name__ == "__main__":
    setup(
        name=DISTNAME,
        cmdclass=versioneer.get_cmdclass(),
        version=versioneer.get_version(),
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=["empyrical", "empyrical.tests"],
        install_requires=requirements,
        extras_require=extras_requirements,
        tests_require=test_reqs,
        test_suite="nose.collector"
    )
