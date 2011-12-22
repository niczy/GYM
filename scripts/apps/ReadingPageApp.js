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

			readingSectionModel.bind("change", function() {
				console.log(readingSectionModel.get("article"));
			});

			var ReadingSectionView = require('../views/practice/ReadingSectionView');
			readingSectionView = new ReadingSectionView({
				model: readingSectionModel
			});

			readingSectionModel.fetch({"success": function(model, response) {
                console.log("success " + response);
				readingSectionView.render();
			}});
		}
	})

	var app = new ReadingPageApp;

	console.log('Main inilized.');
	return ReadingPageApp;
});

