{% import 'macros.html' as macros %}
exports.models = {

  {{ Item }}: {
    id: '{{ Item }}',
    {% for property in item.properties %}
    {{macros.def_input(item, property)}}
    {% endfor %}
    }
  }
};