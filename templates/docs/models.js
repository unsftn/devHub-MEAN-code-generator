{% import 'macrosz.html' as macros %}
exports.models = {

  {{ item.name }}: {
    id: '{{ item.name }}',
    {% for property in item.properties %}{{macros.def_model(item, property)}}{% endfor %}
    properties:
    {%for property in item.properties %}
    {{property.name}}: {
        type: '{{property.type |inputType}}',
        description : 'This is cool'
    {% if not loop.last %}
    },
    {% endif %}
    {% endfor %}
    }
  }
};