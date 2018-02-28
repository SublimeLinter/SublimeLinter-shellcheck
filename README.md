SublimeLinter-shellcheck
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-shellcheck.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-shellcheck)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [shellcheck](http://www.shellcheck.net/about.html). It will be used with files that have the “Shell-Unix-Generic” syntax (aka Shell Script (Bash)).

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `shellcheck` is installed on your system.

To install `shellcheck`, follow the instructions on [the shellcheck GitHub repository](https://github.com/koalaman/shellcheck).

`shellcheck` can be installed with ``apt-get`` on Debian sid, ``brew`` on Mac OS X, or compiled from its Haskell sources (manually, or through `cabal`). 

On Windows, the Linux Subsystem must be enabled. See [Microsoft's guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10), then run `wsl sudo apt install shellcheck` to install Shellcheck (if you installed ubuntu).

On native Linux systems, in order for `shellcheck` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-shellcheck settings:

|Setting|Description|
|:------|:----------|
|exclude|A comma-delimited list of codes to exclude.|

E.g. you can use a single string (ex: ``"SC2034,SC2086"``), or an array of strings if not inline (ex: ``["SC2034", "SC2086"]``).

