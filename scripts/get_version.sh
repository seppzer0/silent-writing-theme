#!/bin/sh
#
# This is an SH version of get_version.py, usually used for cases when Python interpreter is unavailable.
#

cat $(dirname $(realpath "$0"))/../package.json | grep '"version": "' | cut -d'"' -f 4
