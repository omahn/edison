{% block navigation %} 
<div id='nav' class='span-5'>
<p>{% if user.is_authenticated %} Welcome {{ user.first_name }} {% endif %}</p>
<a href='/cmdb/'>Configuration Management</a><br />
<a href='/changemanagement/'>Change Management</a><br />
<a href='/orchestra/'>Orchestration</a><br />
{% if user.is_authenticated %}
	<a href='/accounts/logout'>Logout</a>
{% else %}
	<a href='/accounts/login'>Login</a>
{% endif %}
</div>
{% endblock %}
