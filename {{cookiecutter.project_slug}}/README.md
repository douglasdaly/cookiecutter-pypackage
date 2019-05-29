{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

*{{ cookiecutter.project_short_description }}*

{% if is_open_source %}
[![PyPI Version](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg)](https://pypi.org/project/{{ cookiecutter.package_name }}/ "PyPI Page")
[![Build Status](https://travis-ci.org/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }} "Travis CI")
[![Coverage Status](https://coveralls.io/repos/github/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}/badge.svg)](https://coveralls.io/github/{{ cookiecutter.github_user }}/{{cookiecutter.project_slug }} "Coveralls")
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest)](https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest "Documentation")
[![Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}.svg)](https://pypi.org/project/{{ cookiecutter.package_name }} "PyPI Page")

- Free software: [{{ cookiecutter.license }} License](./LICENSE "License File")
- Documentation: https://{{ cookiecutter.project_slug }}.readthedocs.io/


## Installation

Install using your package manager of choice, `pipenv` for instance:

```bash
$ pipenv install {{ cookiecutter.package_name }}
```
{%- endif %}


## Features

- List your features here


## License

{{ cookiecutter.project_name }} &copy; Copyright {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}.  ALl rights reserved. {% if is_open_source %}This project is licensed under the {{ cookiecutter.license }} License, see the [`LICENSE`](./LICENSE "License File") file for more details.{% endif %}

