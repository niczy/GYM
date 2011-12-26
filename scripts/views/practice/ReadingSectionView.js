define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var ReadingSectionView = Backbone.View.extend({
		el: '.practice-wrapper',

		initialize: function() {
			var ReadingQuestionView = require('./ReadingQuestionView');
			this.readingQuestionView = new ReadingQuestionView({
				model: this.model.readingQuestionCollection
			});

			var ReadingArticleView = require('./ReadingArticleView');
			this.readingArticleView = new ReadingArticleView({
				model: this.model.readingArticleModel
			});

			this.readingQuestionView.bind("showQuestion", this.readingArticleView.onQuestionShown, this.readingArticleView);
		},

		next: function() {
			this.readingQuestionView.currentQuestionIdx += 1;
			this.readingQuestionView.render();
		},

		previous: function() {
			this.readingQuestionView.currentQuestionIdx -= 1;
			this.readingQuestionView.render();
		},

		showQuestion: function(questionIdx) {
			this.readingQuestionView.currentQuestionIdx = questionIdx;
			this.readingQuestionView.render();
		},

		getNextQuestionIdx: function() {
			return this.readingQuestionView.currentQuestionIdx + 1;
		},

		getPreviousQuestionIdx: function() {
			return this.readingQuestionView.currentQuestionIdx - 1;
		},

		render: function() {
			var $ = require('../../libs/jquery');
			var view = new Backbone.View();

			if (this.model.dataFetched) {
				// Make sure the article view shown before the question view.
				this.readingArticleView.render();
				this.readingQuestionView.render();
			} else {
				console.log("no article");
			}
			return this;
		}
	});
	return ReadingSectionView;
});

