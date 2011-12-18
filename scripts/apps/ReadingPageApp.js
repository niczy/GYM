define(function(require, exports) {

	var Backbone = require('../libs/backbone');
	var ReadingPageApp = Backbone.Router.extend({
		initialize: function() {
			var ReadingQuestionView = require('../views/practice/ReadingQuestionView');
			var ReadingQuestionModel = require('../models/practice/ReadingQuestionModel');
			var ReadingSectionModel = require('../models/practice/ReadingSectionModel');

			var readingSectionModel = new ReadingSectionModel({
				testid: "4",
				sectionid: "5"
			});
			console.log(readingSectionModel.get('testid'));
			readingSectionModel.fetch();

			var ReadingSectionView = require('../views/practice/ReadingSectionView');
			readingSectionView = new ReadingSectionView({
				model: readingSectionModel 
			});
			readingSectionView.render();
		}
	})

	var app = new ReadingPageApp;

	console.log('Main inilized.');
	return ReadingPageApp;
});

