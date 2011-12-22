define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var ReadingSectionView = Backbone.View.extend({
		el: '.practice-section',
		render: function() {
			var ReadingTemplates = require("../../templates/practice/ReadingTemplates");
			var $ = require('../../libs/jquery');
			var view = new Backbone.View;

			console.log("render called");
			if (this.model.has("article")) {
				var questions = this.model.get("questions");

				var ReadingQuestionView = require('./ReadingQuestionView');
				var ReadingQuestionModel = require('../../models/practice/ReadingQuestionModel');
				var readingQuestionModel = new ReadingQuestionModel({
					"description": questions[0].description,
					"options": questions[0].options
				});
				this.readingQuestionView = new ReadingQuestionView({
					model: readingQuestionModel
				});
				var ReadingArticleView = require('./ReadingArticleView');
				var ReadingArticleModel = require('../../models/practice/ReadingArticleModel');
				var readingArticleModel = new ReadingArticleModel({
					"paragraphs": this.model.get('article')
				});
				this.readingArticleView = new ReadingArticleView({
					model: readingArticleModel
				});

				this.readingQuestionView.render();
				this.readingArticleView.render();
				console.log("render");
				//$(this.el).text(ReadingTemplates.readingSectionTemplate(this.model.toJSON()));
			} else {
				console.log("no article");
			}
			return this;
		}
	});
	return ReadingSectionView;
});

