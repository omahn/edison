{% extends 'base.tpl' %}
{% block main %}
<div class='span-10 last'>
{% if messages %}
{% for message in messages %}
{{message}}
{% endfor %}
{%endif %}
<div class='span-10 last'>
<form method="post" action="">
    {{ formset.management_form }}
    {% for form in formset.forms %}
        {% for field in form %}
	<div class='span-8 last'>
            <div class='span-2'>{{ field.label_tag }}:</div>
            <div class='span-4 last'> {{ field }}</div>
	</div>
        {% endfor %}
            <div class="span-8 last">
		<button class="button positive">
	  		<img src="/media/images/icons/tick.png" alt=""/>Add
			</button>
                <input type="hidden" name="next" value="/" />
            </div>
    {% endfor %}
</form>
</div>
{% endblock %}

