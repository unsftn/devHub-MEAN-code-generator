'use strict';

/*
 * Defining the Package
 */
var Module = require('meanio').Module;

var {{ ModuleName }} = new Module('{{ DBName }}');

/*
 * All MEAN packages require registration
 * Dependency injection is used to define required modules
 */
{{ ModuleName }}.register(function(app, auth, database, circles, swagger) {

  //We enable routing. By default the Package Object is passed to the routes
  {{ ModuleName }}.routes(app, auth, database);

  {{ ModuleName }}.aggregateAsset('css', '{{ PartNamePlural }}.css');


  //We are adding a link to the main menu for all authenticated users
  {{ ModuleName }}.menus.add({
    'roles': ['authenticated'],
    'title': '{{ ModuleName }}',
    'link': 'all {{ PartNamePlural }}'
  });
  {{ ModuleName }}.menus.add({
    'roles': ['authenticated'],
    'title': 'Create new {{ PartNameSingular }}',
    'link': 'create {{ PartNameSingular }}'
  });

  {{ ModuleName }}.events.design({
    //http://fontawesome.io/icons
    icon: 'fa-file-text',
    color: '#8FD5FF'
  });


  /*
    //Uncomment to use. Requires meanio@0.3.7 or above
    // Save settings with callback
    // Use this for saving data from administration pages
    {{ ModuleName }}.settings({'someSetting':'some value'},function (err, settings) {
      //you now have the settings object
    });

    // Another save settings example this time with no callback
    // This writes over the last settings.
    {{ ModuleName }}.settings({'anotherSettings':'some value'});

    // Get settings. Retrieves latest saved settings
    {{ ModuleName }}.settings(function (err, settings) {
      //you now have the settings object
    });
    */

  // Only use swagger.add if /docs and the corresponding files exists
  swagger.add(__dirname);

  return {{ ModuleName }};
});