define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var $ = require('../../libs/jquery');
	var _ = require('../../libs/underscore');

	var ReadingArticleView = Backbone.View.extend({

		events: {
			'click .insert-pos': 'insertSentence'
		},

		el: '#article',

		insertSentence: function(evt) {
            if (this.sentence) {
                _.each($('.insert-pos'), function(el) {
                        el.textContent = '_';
                    });
                var target = evt.currentTarget;
                target.textContent = this.sentence;
            }
		},

		clearPreviousClass: function() {
			_.each($('.bold'), function(el) {
				$(el).removeClass('bold');

			});
			_.each($('.insert-pos'), function(el) {
				$(el).removeClass('insert-pos');
				el.textContent = "";
			});
		},

		onQuestionShown: function(data) {
			var questionIdx = data.questionIdx;
			var questionModel = data.question;
			var that = this;
			this.clearPreviousClass();
			var type = questionModel.get("type");
			if (type === 0) { //Single choice question
				_.each(this.gymElements[questionIdx], function(el) {
					$(el).addClass('bold');
					if (!that.boldElements) {
						that.boldElements = [];
					}
					that.boldElements.push(el);
				});
			} else if (type === 2) { // The insert question
                this.sentence = questionModel.get('inserted_sentence');
				_.each(this.gymElements[questionIdx], function(el) {
					$(el).addClass('insert-pos');
					el.textContent = '_';
				});
			} 
			console.log(questionModel);
		},

		render: function() {
			var View = new Backbone.View();
			var _ = require('../../libs/underscore');
			//console.log($(this.el));
			var that = this;
			_.each(this.model.get('paragraphs'), function(paragraph) {
				$(that.el).append(View.make('p', {
					class: "paragraph"
				},
				paragraph));
				console.log($(that.el));
			});

			that.gymElements = {};

			_.each($('.paragraph gym'), function(el) {
				var referenceId = parseInt(el.getAttribute("reference-id"), 10);
				if (!that.gymElements[referenceId]) {
					that.gymElements[referenceId] = [];
				}
				that.gymElements[referenceId].push(el);
			});
			return this;
		}
	});
	return ReadingArticleView;
});

