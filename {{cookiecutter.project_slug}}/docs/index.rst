{% for _ in cookiecutter.project_name %}#{% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}#{% endfor %}

*{{ cookiecutter.project_short_description }}*

|pypi| |nbsp| |travis| |nbsp| |cov| |nbsp| |docs| |nbsp| |pyvers|


Installation
============

Install with your favorite package manager, for instance, ``pipenv``:

.. code-block:: bash

    $ pipenv install {{ cookiecutter.package_name }}


About
=====

*Describe your project here.*


.. toctree::
    :maxdepth: 2
    :caption: Getting Started
    :hidden:

    installation
    quickstart


.. toctree::
    :maxdepth: 2
    :caption: Usage
    :hidden:


.. toctree::
    :maxdepth: 2
    :caption: Reference
    :hidden:

    api/modules
    contributing
    conduct
    authors
    changelogs/changelogs
    license


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. |pyvers| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}.svg
    :target: https://pypi.org/projects/{{ cookiecutter.package_name }}/
    :alt: Supported Python Versions
.. |pypi| image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg
    :target: https://pypi.org/projects/{{ cookiecutter.package_name }}/
    :alt: PyPI Page
.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
    :target: https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/
    :alt: Documentation
.. |travis| image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
    :alt: Travis-CI
.. |cov| image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/badge.svg
    :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
    :alt: Coverage
.. |nbsp| unicode:: 0xA0
   :trim:
