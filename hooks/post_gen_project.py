#!/bin/env/python
# -*- coding: utf-8 -*-
"""
Post project generation hook.
"""
import os
import shlex
import shutil
import subprocess


PROJECT_DIR = os.path.realpath(os.path.curdir)


def delete_file(path):
    """Delete the specified project file"""
    os.remove(os.path.join(PROJECT_DIR, path))
    return

def copy_file(src, dst):
    """Copy a file from `src` to `dst`"""
    return shutil.copy(
        os.path.join(PROJECT_DIR, src), os.path.join(PROJECT_DIR, dst)
    )

def delete_dir(path):
    """Delete the specified project directory"""
    shutil.rmtree(os.path.join(PROJECT_DIR, path))
    return

def run_cmd(cmd, timeout=None, display=False):
    """Runs a command in the local shell"""
    cmd_args = shlex.split(cmd)
    if not shutil.which(cmd_args[0]):
        return -1

    kws = {}
    if not display:
        kws['stdout'] = subprocess.DEVNULL

    p = subprocess.Popen(cmd_args, cwd=PROJECT_DIR, **kws)
    return p.wait(timeout=timeout)


def main():
    """Main post-gen hook method"""
    # Initialization
    if '{{ cookiecutter.create_author_file }}' != 'y':
        delete_file('AUTHORS')
        delete_file('docs/contributors.rst')

    if '{{ cookiecutter.create_notices_file }}' != 'y':
        delete_file('NOTICES')
        delete_dir('src/{{ cookiecutter.package_name }}/_vendored')

    if '{{ cookiecutter.license }}' == 'Not open source':
        delete_file('LICENSE')
        delete_file('docs/license.rst')

    # Setup
    git_ok = run_cmd("git init .") == 0
    if not git_ok:
        print("Could not initialize git repository")
    else:
        run_cmd("git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git")
        hook_names = next(os.walk(os.path.join(PROJECT_DIR, '.githooks')))[1]
        for hk_nm in hook_names:
            copy_file('.githooks/hook.sh', '.git/hooks/%s' % hk_nm)

    # Post-setup
    run_cmd("direnv allow")

    if run_cmd("pipenv install --dev", display=True) != 0:
        print("Could not create Pipenv environment")
    else:
        run_cmd("make generate-docs")

    if git_ok:
        run_cmd("git add .")
        run_cmd('git commit --message="Initial project skeleton."')

    return


if __name__ == '__main__':
    main()

