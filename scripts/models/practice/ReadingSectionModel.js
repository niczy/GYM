define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var ReadingArticleModel = require('./ReadingArticleModel');
	var ReadingQuestionCollection = require('./ReadingQuestionCollection');

	var ReadingSectionModel = Backbone.Model.extend({
		url: function() {
			return "/" + this.get('testid') + "/reading/" + this.get('sectionid');
		},
		name: "This is the reading section model"
	});
	return ReadingSectionModel;
});

