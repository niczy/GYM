define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var ReadingArticleModel = require('./ReadingArticleModel');
	var ReadingQuestionCollection = require('./ReadingQuestionCollection');

	var ReadingSectionModel = Backbone.Model.extend({

		initialize: function() {
			this.readingQuestionCollection = new ReadingQuestionCollection();
			this.readingArticleModel = new ReadingArticleModel();
            this.dataFetched = false;
		},

		url: function() {
			return "/api/get/" + this.get('testid') + "/reading/" + this.get('sectionid');
		},

		parse: function(response) {
            this.readingQuestionCollection.add(response.questions);
            this.readingArticleModel.set({"paragraphs": response.article});
            this.dataFetched = true;
            return;
		},

		name: "This is the reading section model"

	});
	return ReadingSectionModel;
});

