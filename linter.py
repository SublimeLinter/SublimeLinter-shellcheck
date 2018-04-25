from SublimeLinter.lint import Linter
from shutil import which
import sublime


class Shellcheck(Linter):

    cmd = 'shellcheck --format gcc -'
    if sublime.platform() == 'windows' and which('wsl'):
        cmd = 'wsl ' + cmd

    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'(?:(?P<error>error)|(?P<warning>(warning|note))): '
        r'(?P<message>.+)$'
    )
    defaults = {
        'selector': 'source.shell - source.makefile',
        '--exclude=,': ''
    }
