# -*- coding: utf-8 -*-
"""
Click settings and constants for the CLI interface.
"""
CONTEXT_SETTINGS = {
    'help_option_names': ['-h', '--help'],
    'auto_envvar_prefix': '{{ cookiecutter.cli_name.upper() }}',
}
