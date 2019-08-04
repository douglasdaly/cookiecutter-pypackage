#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Commands for the {{ cookiecutter.package_name }} CLI.
"""
from click import group
from click import pass_context
from click import style
from click import version_option

from ..__version__ import __version__
from .base import MainCLI
from .settings import CONTEXT_SETTINGS


@group(cls=MainCLI, invoke_without_command=True,
       context_settings=CONTEXT_SETTINGS)
@pass_context
@version_option(prog_name=style('{{ cookiecutter.cli_name }}', bold=True),
                version=__version__)
def cli(ctx):
    """
    {{ cookiecutter.project_name }} CLI

      {{ cookiecutter.project_short_description }}

    """
    pass


if __name__ == '__main__':
    cli()
