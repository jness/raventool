from setuptools import setup, find_packages
from glob import glob

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

version = '0.0.1'


setup(
    name='raventool',
    version=version,
    description="Tools for working with ravencoin core wallet json rpc",
    author='Jeffrey Ness',
    author_email='jness@nessy.info',
    license='Apache License, Version 2.0',
    packages=find_packages(
        exclude=['ez_setup', 'tests']
    ),
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
    ]
)
