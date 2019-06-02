{% set is_open_source = cookiecutter.license != 'Not open source' -%}
############
Contributors
############

All contributors to the project are listed in the ``AUTHORS`` file{% if is_open_source %} (and :doc:`contributions <contributing>` are always welcome){% endif %}.
The contents of that file can also be found here:

    .. include:: ../AUTHORS

