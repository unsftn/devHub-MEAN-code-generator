'use strict';

angular.module('mean.{{ items }}').controller('{{ ControllerName }}', ['$scope', '$stateParams', '$location', 'Global', '{{ Items }}', 'MeanUser', 'Circles',
  function($scope, $stateParams, $location, Global, {{ Items }}, MeanUser, Circles) {
    $scope.global = Global;


    $scope.hasAuthorization = function({{ item }}) {
      if (!{{ item }} || !{{ item }}.user) return false;
      return MeanUser.isAdmin || {{ item }}.user._id === MeanUser.user._id;
    };


    $scope.availableCircles = [];

    Circles.mine(function(acl) {
        $scope.availableCircles = acl.allowed;
        $scope.allDescendants = acl.descendants;
    });

    $scope.showDescendants = function(permission) {
        var temp = $('.ui-select-container .btn-primary').text().split(' ');
        temp.shift(); //remove close icon
        var selected = temp.join(' ');
        $scope.descendants = $scope.allDescendants[selected];
    };

    $scope.selectPermission = function() {
        $scope.descendants = [];
    };

    $scope.create = function(isValid) {
      if (isValid) {
        // $scope.{{ item }}.permissions.push('test test');
        var {{ item }} = new {{ Items }}($scope.{{ item }});

        {{ item }}.$save(function(response) {
          $location.path('{{ items }}/' + response._id);
        });

        $scope.{{ item }} = {};

      } else {
        $scope.submitted = true;
      }
    };

    $scope.remove = function({{ item }}) {
      if ({{ item }}) {
        {{ item }}.$remove(function(response) {
          for (var i in $scope.{{ items }}) {
            if ($scope.{{ items }}[i] === {{ item }}) {
              $scope.{{ items }}.splice(i, 1);
            }
          }
          $location.path('{{ items }}');
        });
      } else {
        $scope.{{ item }}.$remove(function(response) {
          $location.path('{{ items }}');
        });
      }
    };

    $scope.update = function(isValid) {
      if (isValid) {
        var {{ item }} = $scope.{{ item }};
        if (!{{ item }}.updated) {
          {{ item }}.updated = [];
        }

        // {{ item }}.updated.push(new Date().getTime());

        {{ item }}.$update(function() {
          $location.path('{{ items }}/' + {{ item }}._id);
        });
      } else {
        $scope.submitted = true;
      }
    };

    $scope.find = function() {
      {{ Items }}.query(function({{ items }}) {
        $scope.{{ items }} = {{ items }};
      });
    };

    $scope.findOne = function() {
      {{ Items }}.get({
        {{ item }}Id: $stateParams.{{ item }}Id
      }, function({{ item }}) {
        $scope.{{ item }} = {{ item }};
      });
    };
  }
]);