{% import 'macros.html' as macros %}
'use strict';

/**
 * Module dependencies.
 */
var mongoose = require('mongoose'),
  Schema = mongoose.Schema;


// TODO resiti ostale stvari

var ArticleSchema = new Schema({
    {% for property in item.properties %}
    {{macros.def_input(item, property)}}
    {% endfor %}
});
/**
 * Validations
 */
    {% for property in item.properties %}

ArticleSchema.path('{{property.name}}').validate(function({{property.name}}) {
  return !!{{property.name}};
}, '{{property.name}} cannot be blank');

ArticleSchema.path('{{property.name}}').validate(function({{property.name}}) {
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

