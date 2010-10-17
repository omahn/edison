<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en">
<head>
<title>{% block title %}{% endblock %}</title>
<link rel="stylesheet" href="/media/css/screen.css" type="text/css" media="screen, projection">
<link rel="stylesheet" href="/media/css/print.css" type="text/css" media="print">
<!--[if IE]>
  <link rel="stylesheet" href="/media/css/ie.css" type="text/css" media="screen, projection">
<![endif]-->
<link rel="stylesheet" href="/media/css/style.css" type="text/css" media="screen, projection">

</head>
<body>
<div id='page' class='container'>
    <div id='header' class='span-24 last'>
        <div id='branding'>
		<h1>Edison</h1>
		<p><i>"Because the hamster keeps on running..."</i></p>
		<p>{% if user.is_authenticated %} Welcome {{ user.username }} {% endif %}</p></div>
    </div>
    <div id='content' class='span-24'>
        <div id='nav' class='span-5'>
            {% block navigation %} 
	<a href='/cmdb/'>Configuration Database</a><br />
	<a href='/changemanagement/'>Change Management</a><br />
	<a href='/orchestra/'>Configuration Management</a><br />
	{% if user.is_authenticated %}
 	<a href='/accounts/logout'>Logout</a>&nbsp;
 	{% else %}
 	<a href='/accounts/login'>Login</a>&nbsp;
 	{% endif %}{% endblock %}
        </div>
	<div id='main' class='span-18 last'>
    {% block main %}
    {% endblock %}
	</div>
        <div id='local'>
            {% block local %}{% endblock %}
        </div>
    </div>
    </div>
</div>
</body>
</html>

