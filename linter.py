#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by NotSqrt
# Copyright (c) 2013 NotSqrt
#
# License: MIT
#

"""
This module exports the Shellcheck plugin class.

Example output with --format gcc

-:230:7: warning: Quote this to prevent word splitting. [SC2046]
-:230:7: note: Useless echo? Instead of 'echo $(cmd)', just use 'cmd'. [SC2005]
-:230:158: note: Double quote to prevent globbing and word splitting. [SC2086]
-:234:10: error: Add double quotes around ${VAR[@]}, otherwise it's just like $* and breaks on spaces. [SC2068]

"""

from SublimeLinter.lint import Linter


class Shellcheck(Linter):

    """Provides an interface to shellcheck."""

    syntax = 'shell-unix-generic'
    cmd = 'shellcheck --format gcc -'
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>error)|(?P<warning>(warning|note))): (?P<message>.+)$'

    defaults = {
        '--exclude=,': ''
    }
    inline_settings = 'exclude'
    inline_overrides = 'exclude'
    comment_re = r'\s*#'
