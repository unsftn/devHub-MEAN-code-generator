'use strict';

//{{ Items }} service used for {{ items }} REST endpoint
angular.module('mean.{{ items }}').factory('{{ Items }}', ['$resource',
  function($resource) {
    return $resource('api/{{ items }}/:{{ item }}Id', {
      {{ item }}Id: '@_id'
    }, {
      update: {
        method: 'PUT'
      }
    });
  }
]);
