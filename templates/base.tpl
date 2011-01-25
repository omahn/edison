<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en">
<head>
    <title>Edison - {{ title }}</title>
    <style type='text/css' media='all'>
        @import url('/media/css/screen.css');
        @import url('/media/css/edison.css');
    </style>
    <script type="text/javascript" src="/media/js/jquery-1.4.3.min.js"></script>
    <script type="text/javascript" src="/media/js/jquery.collapser.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            $(" #nav ul ").css({display: "none"}); // Opera Fix
            $(" #nav li").hover(function(){
                    $(this).find('ul:first').css({visibility: "visible",display: "none"}).show(400);
                    },function(){
                    $(this).find('ul:first').css({visibility: "hidden"});
                });
            $(".expand").collapser({
            		effect: 'fade',
            		changeText: false,
            		expandHtml: 'Expand',
            		collapseHtml: 'Collapse',
            	})
        });
    </script>
</head>
<body>
<div id='page' class='container'>
    <div id='header' class='span-24'>
        <div id='logo' class='span-5'>
            <img src='/media/images/edison_small.jpg' />
        </div>
        <div id='branding' class='span-12 last'>
            <h1>Edison</h1>
            <p><i>"The Hamster that keeps your infrastructure running..."</i></p>
        </div>
        <div id='message' class='span-24 last'> 
        {% if user.is_authenticated %}
            <p>Welcome {{ user.first_name }} {{ user.last_name }}</p>
        {% endif %}
        </div>
        <div  class='clear'></div>
    </div>
    <div id='content' class='span-24 last'>
        {% block navigation %}
            {% include 'nav.tpl' %}
        {% endblock %}
        {% block main %}
            <div id='main' class='span 22 last'>
                <h2>{{ title }}</h2>
            </div>
        {% endblock %}
        <div  class='clear'></div>
    </div>
</div>
</body>
</html>

