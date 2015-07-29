'use strict';

/**
 * Module dependencies.
 */
var mongoose = require('mongoose'),
    {{Item}} = mongoose.model('{{Item}}'),
    _ = require('lodash');

module.exports = function({{Items}}) {

    return {
        /**
         * Find item by id
         */
        {{item}}: function(req, res, next, id) {
            {{Item}}.load(id, function(err, {{item}}) {
                if (err) return next(err);
                if (!{{item}}) return next(new Error('Failed to load {{item}} ' + id));
                req.{{item}} = {{item}};
                next();
            });
        },
        /**
         * Create an item
         */

        create: function(req, res) {
            var {{item}} = new {{Item}}(req.body);
            {{item}}.user = req.user;

            {{item}}.save(function(err) {
                if (err) {
                    return res.status(500).json({
                        error: 'Cannot save the item'
                    });
                }
                {{Items}}.events.publish('{{createAction}}', {
                    description: req.user.name + ' created ' + req.body.title + ' {{item}}.'
                });

                res.json({{item}});
            });
        },
        /**
         * Update an item
         */
        update: function(req, res) {
            var {{item}} = req.{{item}};

            {{item}} = _.extend({{item}}, req.body);


            {{item}}.save(function(err) {
                if (err) {
                    return res.status(500).json({
                        error: 'Cannot update the item'
                    });
                }

                {{Items}}.events.publish('{{editAction}}', {
                    description: req.user.name + ' updated ' + req.body.title + ' {{item}}.'
                });

                res.json({{item}});
            });
        },
        /**
         * Delete an item
         */
        destroy: function(req, res) {
            var {{item}} = req.{{item}};


            {{item}}.remove(function(err) {
                if (err) {
                    return res.status(500).json({
                        error: 'Cannot delete the item'
                    });
                }

                {{Items}}.events.publish('{{deleteAction}}', {
                    description: req.user.name + ' deleted ' + {{item}}.title + ' {{item}}.'
                });

                res.json({{item}});
            });
        },
        /**
         * Show an item
         */
        show: function(req, res) {

            {{Items}}.events.publish('{{readAction}}', {
                description: req.user.name + ' read ' + req.{{item}}.title + ' {{item}}.'
            });

            res.json(req.{{item}});
        },
        /**
         * List of {{Items}}
         */
        all: function(req, res) {
            var query = req.acl.query('{{Item}}');

            query.find({}).sort('-created').populate('user', 'name username').exec(function(err, {{items}}) {
                if (err) {
                    return res.status(500).json({
                        error: 'Cannot list the {{items}}'
                    });
                }

                res.json({{items}})
            });

        }
    };
}
