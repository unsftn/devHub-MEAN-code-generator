exports.models = {

  {{ Item }}: {
    id: '{{ Item }}',
    required: [{% for property in properties %} '{{ property.name }}' {% if !loop.last %} , {% endif %}{% endfor %}],
    properties: {
      {% for property in properties %}
      {{ property.name }}: {
        type: '{{ property.type }}',
        description: '{{ property.description }}'
      }{% if !loop.last %},{% endif %}
      {% endfor %}
    }
  }
};