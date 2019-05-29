#!/bin/env/python
# -*- coding: utf-8 -*-
"""
Post project generation hook.
"""
import os
import shutil


PROJECT_DIR = os.path.realpath(os.path.curdir)


def delete_file(path):
    """Delete the specified project file"""
    os.remove(os.path.join(PROJECT_DIR, path))
    return


def delete_dir(path):
    """Delete the specified project directory"""
    shutil.rmtree(os.path.join(PROJECT_DIR, path))
    return


def main():
    """Main post-gen hook method"""
    if '{{ cookiecutter.create_author_file }}' != 'y':
        delete_file('AUTHORS')
        delete_file('docs/contributors.rst')
        delete_file('doct/contributing.rst')

    if '{{ cookiecutter.create_notices_file }}' != 'y':
        delete_file('NOTICES')
        delete_dir('src/_vendored')

    if '{{ cookiecutter.license }}' == 'Not open source':
        delete_file('LICENSE')
        delete_file('docs/license.rst')

    return

if __name__ == '__main__':
    main()

