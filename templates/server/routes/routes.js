'use strict';

// Article authorization helpers

var hasAuthorization = function(req, res, next) {
  if (!req.user.isAdmin && !req.article.user._id.equals(req.user._id)) {
    return res.status(401).send('User is not authorized');
  }
  next();
};

var hasPermissions = function(req, res, next) {

    req.body.permissions = req.body.permissions || ['authenticated'];

    req.body.permissions.forEach(function(permission) {
        if (req.acl.user.allowed.indexOf(permission) === -1) {
            return res.status(401).send('User not allowed to assign ' + permission + ' permission.');
        };
    });

    next();
};
// proveriti za {{part.do.create}} i {{part.do.destroy}}
module.exports = function({{Items}}, app, auth) {
  
  var {{items}} = require('../controllers/{{items}}')({{Items}});

  app.route('/api/{{items}}')
    .get({{items}}.all)
    .post(auth.requiresLogin, hasPermissions, {{items}}.{{part.do.create}});
  app.route('/api/{{items}}/:{{item}}Id')
    .get(auth.isMongoId, {{items}}.show)
    .put(auth.isMongoId, auth.requiresLogin, hasAuthorization, hasPermissions, {{items}}.{{part.do.update}})
    .delete(auth.isMongoId, auth.requiresLogin, hasAuthorization, {{items}}.{{part.do.destroy}});

  // Finish with setting up the articleId param
  app.param('{{item}}Id', {{items}}.{{item}});
};

