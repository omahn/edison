<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en">
<head>
    <title>Edison - {{ title }}</title>
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
            <p><i>"The Hamster that keeps your infrastructure running..."</i></p>
        </div>
        <div id='content' class='span-24'>
            {% block navigation %}
                <div id='nav' class='span-5'>
                    {% include 'nav.tpl' %}
                </div>
            {% endblock %}
            {% block main %}
                <div id='main' class='span-18 last'>
                    <h2>{{ title }}</h2>
                </div>
            {% endblock %}
        </div>
    </div>
</div>
</body>
</html>

