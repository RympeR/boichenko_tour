
content = """
    {% extends 'basics.html' %}

    {% block style %}
    <link rel = "stylesheet" href = "{{ url_for('static',filename='css/Delete_Service.css') }}">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
    {% endblock %}
{% block title %}Statistics{% endblock title %}
{% block main_content %}
    <div class = "intro">
        <h1>Посмотреть стоимость</h1>
<div class = "container">
</div>
</div>    
{% endblock main_content %}
"""

names = [
    'order_transfer.html',
    'remove_staff.html',
    'change_password.html',
    'info_retrieve.html',
    'status_change.html',
    'insurancepolicy_change.html',
    'price_change.html',
    'status_change.html',
    'status_retrieve.html',
    'order_tour.html',
    'order_room.html',
    'retrieve_users.html',
    'retrieve_users_orders.html',
    'order_transfer.html',
]

for name in names:
    with open(name, 'w') as f:
        f.writelines(content)
