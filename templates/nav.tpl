<ul id="nav" class='span-24 last'>
    <li><a href="/cmdb/">Configuration Management</a>
        <ul>
            <li><a href="/cmdb/assetlist">Asset List</a></li>
        </ul>
    </li>
    <li>
        {% if user.is_authenticated %}
            <a href='/accounts/logout'>Logout</a>
        {% else %}
            <a href='/accounts/login'>Login</a>
        {% endif %}
    </li>
</ul>
<div  class='clear'></div>
