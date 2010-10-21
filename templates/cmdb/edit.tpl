{% extends 'base.tpl' %}
{% block main %}
    <div class='span-10 last'>
        {% if messages %}
            {% for message in messages %}
                {{message}}
            {% endfor %}
        {%endif %}
    </div>
    <div class='span-10 last'>
        <form method="post" action="">
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>Hostname:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.Hostname }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>Location:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.Rack }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>IP Address:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.NetworkInterface }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>Asset Number:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.Asset }}
	    </div>
	</div>
	<div class='span-8 last'>
	    <div class='span-2'>
	         <label for='Hostname'>Support Tag:</label>
            </div>
	    <div class='span-4 last'>
		{{ form.SupportTag }}
	    </div>
	</div>
	<div class='span-8 last'>
                <button class="button positive">
                <img src="/media/images/icons/tick.png" alt=""/>Update
                </button>
                <input type="hidden" name="next" value="/" />
            </div>
        </form>
    </div>
{% endblock %}
