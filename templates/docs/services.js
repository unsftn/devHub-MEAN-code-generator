'use strict';

exports.load = function(swagger, parms) {

  var searchParms = parms.searchableOptions;

  var list = {
    'spec': {
      description: '{{ Item }} operations',
      path: '/{{ items }}',
      method: 'GET',
      summary: 'Get all {{ Item }}s',
      notes: '',
      type: '{{ Item }}',
      nickname: 'get{{ Item }}s',
      produces: ['application/json'],
      params: searchParms
    }
  };

  var create = {
    'spec': {
      description: 'Device operations',
      path: '/{{ items }}',
      method: 'POST',
      summary: 'Create items',
      notes: '',
      type: '{{ Item }}',
      nickname: 'create{{ Item }}',
      produces: ['application/json'],
      parameters: [{
        name: 'body',
        description: '{{ Item }} to create.  User will be inferred by the authenticated user.',
        required: true,
        type: '{{ Item }}',
        paramType: 'body',
        allowMultiple: false
      }]
    }
  };

  swagger.addGet(list)
    .addPost(create);

};
