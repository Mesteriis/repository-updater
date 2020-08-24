#
# MIT License
#
# Copyright (c) 2018-2020 Franck Nijhof
# Copyright (c) 2020 Andrey "Limych" Khrolenok
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Home Assistant add-ons repository updater setup."""
import os
import re
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from repositoryupdater import (
    APP_NAME,
    APP_VERSION,
    APP_DESCRIPTION,
    __author__,
    __email__,
    __license__,
    __url__,
    __download__,
    __keywords__,
)


class PyTest(TestCommand):
    """PyTest controller."""

    # Code from here:
    # https://docs.pytest.org/en/latest/goodpractices.html#manual-integration

    # pylint: disable=consider-using-sys-exit,attribute-defined-outside-init
    def finalize_options(self):
        """Finalize."""
        TestCommand.finalize_options(self)
        # we don't run integration tests
        self.test_args = ["-m", "not integration"]
        self.test_suite = True

    # pylint: disable=consider-using-sys-exit,import-outside-toplevel
    def run_tests(self):
        """Run tests."""
        # import here, cause outside the eggs aren't loaded
        import pytest
        import shlex

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


def load_requirements(filename: str) -> list:
    """Load requirements from file."""
    path = os.path.join(os.path.dirname(__file__), filename)
    imp = re.compile(r"^(-r|--requirement)\s+(\S+)")
    reqs = []
    with open(path, encoding="utf-8") as fptr:
        for i in fptr:
            # pylint: disable=invalid-name
            m = imp.match(i)
            if m:
                reqs.extend(load_requirements(m.group(2)))
            else:
                reqs.append(i)

    return reqs


with open("README.md", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()
    LONG_DESCRIPTION_TYPE = "text/markdown"

REQUIREMENTS = load_requirements("requirements.txt")
TEST_REQUIREMENTS = load_requirements("requirements-tests.txt")

setup(
    name=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION.split("\n")[0],
    author=__author__,
    author_email=__email__,
    license=__license__,
    url=__url__,
    platforms="any",
    download_url=__download__,
    keywords=__keywords__,
    install_requires=REQUIREMENTS,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_TYPE,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
    cmdclass={"pytest": PyTest},
    tests_require=TEST_REQUIREMENTS,
    packages=find_packages(),
    entry_points="""
    [console_scripts]
        repository-updater=repositoryupdater.cli:repository_updater
        repository-updater-git-askpass=repositoryupdater.cli:git_askpass
""",
)
