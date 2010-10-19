{% extends 'base.tpl' %}
{% block main %}
{% if data_list %}
<p>Please choose a {{ link_desc }} from the list below</p>
<ul>
{% for item in data_list %}
    <li><a href='../edit/{{ item.id }}/'>{{ item.Hostname }}</a></li>
{% endfor %}
{% else %}
<p>No items are available in this dataset.</p>
{% endif %}
{% endblock %}

