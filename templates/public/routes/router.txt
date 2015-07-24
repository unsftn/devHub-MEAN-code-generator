'use strict';

//Setting up route
angular.module('mean.{{ items }}').config(['$stateProvider',
  function($stateProvider) {

    // states for my app
    $stateProvider
      .state('all {{ items }}', {
        url: '/{{ items }}',
        templateUrl: '/{{ items }}/views/list.html',
        resolve: {
          loggedin: function(MeanUser) {
            return MeanUser.checkLoggedin();
          }
        }
      })
      .state('create {{ item }}', {
        url: '/{{ items }}/create',
        templateUrl: '/{{ items }}/views/create.html',
        resolve: {
          loggedin: function(MeanUser) {
            return MeanUser.checkLoggedin();
          }
        }
      })
      .state('edit {{ item }}', {
        url: '/{{ items }}/:{{ item }}Id/edit',
        templateUrl: '/{{ items }}/views/edit.html',
        resolve: {
          loggedin: function(MeanUser) {
            return MeanUser.checkLoggedin();
          }
        }
      })
      .state('{{ item }} by id', {
        url: '/{{ items }}/:{{ item }}Id',
        templateUrl: '/{{ items }}/views/view.html',
        resolve: {
          loggedin: function(MeanUser) {
            return MeanUser.checkLoggedin();
          }
        }
      });
  }
]);
