define(function(require, exports) {

	var ReadingPageApp = Backbone.Router.extend({
		initialize: function() {
			var ReadingQuestionView = require('../views/practice/ReadingQuestionView');
			var ReadingQuestionModel = require('../models/practice/ReadingQuestionModel');
			var readingQuestionView = new ReadingQuestionView({
				model: new ReadingQuestionModel
			});
			readingQuestionView.render();
		}
	})

	var app = new ReadingPageApp;

	console.log('Main inilized.');
	return ReadingPageApp;
});

