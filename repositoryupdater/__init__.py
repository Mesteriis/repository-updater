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

"""
Community Hass.io Add-ons Repository Updater.

Reads remote add-on repositories, determines versions and generates
changelogs to update the add-on repository fully automated.

Mainly used by the Community Home Assistant Add-ons project.

Please note, this program cannot be used with the general documented
Home Assistant add-on repository approach.
"""

__version__ = "0.5.2"

APP_NAME = "hassio-repo-updater"
APP_FULL_NAME = "Community Hass.io Add-ons Repository Updater"
APP_VERSION = __version__
APP_DESCRIPTION = __doc__

__author__ = "Andrey Khrolenok"
__email__ = "andrey@khrolenok.ru"
__copyright__ = "Copyright 2020, Andrey Khrolenok; 2018-2020, Franck Nijhof"
__license__ = "MIT"
__url__ = "https://github.com/Limych/repository-updater"
__download__ = (
    "https://github.com/Limych/repository-updater/archive/" + __version__ + ".tar.gz"
)
__keywords__ = [
    "hassio",
    "hass.io",
    "addons",
    "repository",
    "home assistant",
    "home-assistant",
    "add-ons",
    "limych",
]
