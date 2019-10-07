from SublimeLinter.lint import Linter
from shutil import which
import sublime


class Shellcheck(Linter):

    def cmd(self):
        cmd = []
        if sublime.platform() == 'windows' and not which('shellcheck') and which('wsl'):
            cmd.append('wsl')

        cmd.extend([
            'shellcheck',
            '--format=gcc',
        ])

        if self.filename.endswith('.ebuild'):
            cmd.append('--shell=bash')

        cmd.append('${args}')
        cmd.append('-')

        return cmd

    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'(?:(?P<error>error)|(?P<warning>(warning|note))): '
        r'(?P<message>.+)$'
    )
    defaults = {
        'selector': 'source.shell.bash - source.makefile - source.shell.fish - text.html',
        '--exclude=,': ''
    }
