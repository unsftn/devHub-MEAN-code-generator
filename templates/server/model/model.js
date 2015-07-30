{% import 'macros.html' as macros %}
'use strict';

/**
 * Module dependencies.
 */
var mongoose = require('mongoose'),
  Schema = mongoose.Schema;



var ArticleSchema = new Schema({
    {% for property in item.properties %}
    {{macros.def_input(item, property)}}
    {% endfor %}
    permissions: {
    type: Array
  },
});
/**
 * Validations
 */

{% for property in item.properties %}
ArticleSchema.path('{{property.name}}').validate(function({{property.name}}) {
  return !!{{property.name}};
}, '{{property.name}} cannot be blank');
{% endfor %}
/**
 * Statics
 */
ArticleSchema.statics.load = function(id, cb) {
  this.findOne({
    _id: id
  }).populate('user', 'name username').exec(cb);
};

mongoose.model('{{item.name}}', ArticleSchema);

