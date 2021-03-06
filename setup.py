# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup script for Deputy client package."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

DEPENDENCIES = (
    "absl-py",
    "urllib3",
    "pytype",
    "attrs>=19",
    "parameterized",
    "python-dateutil",
)

setuptools.setup(
    name="google-deputy-api-python-client",
    version="0.0.1",
    author="Google",
    description="A pythonic library for interacting with Deputy.com's API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/google/deputy-api-python-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=DEPENDENCIES,
    python_requires='>=3.6',
)
