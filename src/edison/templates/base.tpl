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
<div id='page' class='showgrid'>
    <div id='header' class='clearfix'>
        <div id='branding'><h1>Edison</h1><p><i>"Because the hamster keeps on running..."</i></p><p>Welcome {{ user.username }}</p></div>
    </div>
    <div id='content' class='clearfix'>
	<div id='main'>
    {% block main %}
    {% endblock %}
	</div>
        <div id='local'>
            {% block local %}{% endblock %}
        </div>
        <div id='nav'>
            {% block navigation %} 
	<a href='/cmdb/'>Configuration Database</a>
	<a href='/changemanagement/'>Change Management</a>
	<a href='/orchestra/'>Configuration Management</a>
	{% if user.is_authenticated %}
 	<a href='/accounts/logout'>Logout</a>&nbsp;
 	{% else %}
 	<a href='/accounts/login'>Login</a>&nbsp;
 	{% endif %}{% endblock %}
        </div>
    </div>
    </div>
</div>
</body>
</html>

