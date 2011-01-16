{% extends 'home.tpl' %}
{% block main %}
	<h1>{{ title }}</h1>
<!-- Hardware Information -->
{% if data_list %}
	<h3>Hardware:</h3>
	<table>
		<tr><td>Datacentre:</td><td>{{ data_list.Rack.Room.DataCentre.Name }}</td></tr>
		<tr><td>Room:</td><td>{{ data_list.Rack.Room.RoomName }}</td><td>Manufacturer: </td><td>{{data_list.Manufacturer.Name}}</td></tr>
		<tr><td>Suite:</td><td>{{ data_list.Rack.Suite.SuiteName }}</td><td>Asset Number: </td><td>{{data_list.Asset}}</td></tr>
		<tr><td>Rack:</td><td>{{ data_list.Rack.RackName }}</td><td>Serial Number/Service Tag: </td><td>{{data_list.SupportTag}}</td></tr>
	</table>
{% endif %}
<!-- End hardware Information -->
<!-- Configuration Management (puppet) Information -->
{% if orchestra_classes %}
	<h3>Configuration Management Classes</h3>
	<table>
		<tr>
			<td>
			<ul>
			{% for config_class in orchestra_classes %}
				<li>{{ config_class.Name }} {% if user.is_staff %} (<a href="http://localhost:8000/admin/orchestra/orchestraclass/{{config_class.id }}/" >edit</a>) {% endif %}</li>
			{% endfor %}
			</ul>
			</td>
		</tr>
	</table>
{% endif %}
<!-- End Configuration Management (puppet) Information -->
<!-- Configuration Metadata -->
{% if orchestra_meta %}
	<h3>Configuration Metadata</h3>
	<table>
			{% for metadata in orchestra_meta %}
				<tr><td>{{ metadata.Name }}</td><td>{{metadata.Value}}</td></tr>
			{% endfor %}
	</table>
{% endif %}
{% if open_change_requests %}
<h3>Change Requests</h3>
<ul>
<li>{{ open_change_requests }} open</li>
<li>{{ closed_change_requests }} closed</li>
</ul>
{% endif %}
{% endblock %}

