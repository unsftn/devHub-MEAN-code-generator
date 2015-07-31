{% import 'macros.html' as macros %}
'use strict';

/**
 * Module dependencies.
 */
var mongoose = require('mongoose'),
  Schema = mongoose.Schema;



var {{item.name}}Schema = new Schema({
    {% for property in item.properties %}
    {{macros.def_input(item, property)}}
    {% endfor %}
    permissions: {
        type: Array
    }
});
/**
 * Validations
 */

{% for property in item.properties %}
{{item.name}}Schema.path('{{property.name}}').validate(function({{property.name}}) {
  return !!{{property.name}};
}, '{{property.name}} cannot be blank');
{% endfor %}
/**
 * Statics
 */
{{item.name}}Schema.statics.load = function(id, cb) {
  this.findOne({
    _id: id
  }).populate('user', 'name username').exec(cb);
};

mongoose.model('{{item.name}}', {{item.name}}Schema);

