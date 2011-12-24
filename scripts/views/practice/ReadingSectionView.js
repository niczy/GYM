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
			var view = new Backbone.View;

			console.log("render called");
			if (this.model.dataFetched){
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

