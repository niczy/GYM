define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
    var $ = require('../../libs/jquery');
	var ReadingSectionView = Backbone.View.extend({
		el: '#practice-section',
		
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
			this.readingQuestionView.bind("showQuestion", this.onQuestionShown, this);
		},

		onQuestionShown: function(data) {
            var questionModel = data.question;

			var hideArticle = questionModel.get("hide_article");
			if (hideArticle) {
				$(this.el).removeClass("practice-section");
				$(this.el).addClass("practice-section-no-article");
			} else {
				$(this.el).removeClass("practice-section-no-article");
				$(this.el).addClass("practice-section");
			}
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
			var View = new Backbone.View();
            var el_question = View.make("div", {"id" : "question"});
            $(this.el).append(el_question);
            var el_article = View.make('div', {"id" : "article"});
            $(this.el).append(el_article);
            this.readingArticleView.el = el_article;
            this.readingQuestionView.el = el_question;

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

