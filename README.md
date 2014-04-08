SublimeLinter-shellcheck
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-shellcheck.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-shellcheck)

This linter plugin for [SublimeLinter][docs] provides an interface to [shellcheck](http://www.shellcheck.net/about.html). It will be used with files that have the “Shell-Unix-Generic” syntax (aka Shell Script (Bash)).

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `shellcheck` is installed on your system.

***Warning : `shellcheck` has to be compiled from its Haskell sources. There is no Windows installer.***

To install `shellcheck`, do the following:

1. Go to [the shellcheck GitHub repository](https://github.com/koalaman/shellcheck).
1. Clone the git repo or download it as a ZIP archive; make sure to use a version more recent than commit 376d407ea10b55 (2013-11-13 17:28:08), where an easily parseable output was added.
1. Follow instructions in the [shellcheck README](https://github.com/koalaman/shellcheck).

On Mac OS X, there is a homebrew version available via a pull request:

```bash
brew install https://github.com/Homebrew/homebrew/pull/23839
```

Once `shellcheck` is installed, you must ensure it is in your system PATH so that SublimeLinter can find it. This may not be as straightforward as you think, so please read about [how linter executables are located][locating-executables] in the documentation.

### Linter configuration
In order for `shellcheck` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `shellcheck`, you can proceed to install the SublimeLinter-shellcheck plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `shellcheck`. Among the entries you should see `SublimeLinter-shellcheck`. If that entry is not highlighted, use the keyboard or mouse to select it.

2. In the console, you should see a message stating `SublimeLinter: shellcheck activated: /usr/local/bin/shellcheck`

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-shellcheck provides its own settings. Those marked as “Inline Override” may also be [used inline][inline-settings].

|Setting|Description|Inline Override|
|:------|:----------|:-------------:|
|exclude|A comma-delimited list of codes to exclude.|&#10003;|

### Examples

You can use a single string (ex: ``"SC2034,SC2086"``), or an array of strings if not inline (ex: ``["SC2034", "SC2086"]``).

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
