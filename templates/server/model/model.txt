'use strict';

/**
 * Module dependencies.
 */
var mongoose = require('mongoose'),
  Schema = mongoose.Schema;


// TODO resiti ostale stvari

var ArticleSchema = new Schema({
{%for propertie in part.properties}
  {{propertieName}}: {
    {{propertieField}}: Date,
    {{propertieField}}: Date.now
  },
  {{propertieName}}: {
    {{propertieField}}: String,
    {{propertieField}}: true,
    {{propertieField}}: true
  },
  {{propertieName}}: {
    {{propertieField}}: String,
    {{propertieField}}: true,
    {{propertieField}}: true
  },
  {{propertieName}}: {
    {{propertieField}}: Schema.ObjectId,
    {{propertieField}}: 'User'
  },
  {{propertieName}}: {
    {{propertieField}}: Array
  },
  {{propertieName}}: {
    {{propertieField}}: Array
  }
});
{%endfor %}

/**
 * Validations
 */
 {% for propertie in part.properties %}

ArticleSchema.path('{{propertieName}}').validate(function({{propertieName}}) {
  return !!{{propertieName}};
}, '{{propertieName}} cannot be blank');

ArticleSchema.path('{{propertieName}}').validate(function({{propertieName}}) {
  return !!{{propertieName}};
}, '{{propertieName}} cannot be blank');

{%endfor %}

/**
 * Statics
 */
ArticleSchema.statics.load = function(id, cb) {
  this.findOne({
    _id: id
  }).populate('user', 'name username').exec(cb);
};

mongoose.model('{{part.name}}', ArticleSchema);

