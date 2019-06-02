{% for _ in cookiecutter.package_name %}#{% endfor %}
{{ cookiecutter.package_name }}
{% for _ in cookiecutter.package_name %}#{% endfor %}

.. automodule:: {{ cookiecutter.package_name }}
    :members:
    :undoc-members:
    :show-inheritance:

