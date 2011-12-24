define(function(require, exports) {
	var $ = require('../../libs/jquery');
	var Backbone = require('../../libs/backbone');
    var _ = require('../../libs/underscore');
	var ReadingQuestionView = Backbone.View.extend({

		el: '.practice_section, .question',
		events: {
			"change .option input": "onOptionCheck"
		},
		optionCheckbox: [],

		currentQuestionIdx: 0,

		onOptionCheck: function(event) {
			var targetElement = event.currentTarget;
			if (targetElement.checked) {
                var that = this;
                _.each(this.optionCheckbox, function(option){
                       if (option.id != targetElement.id) {
                            option.checked = false;
                       }

                    });
				}
			console.log("option state chenged");
		},

		render: function() {
			var readingQuestionModel = this.model.at(this.currentQuestionIdx);
			if (!readingQuestionModel) {
				return;
			}
			//	$(this.el).text(this.model.get("description"));
			var View = new Backbone.View;
			var description = View.make('p', {
				class: "description"
			},
			readingQuestionModel.get('description'));
			$(this.el).empty();
			$(this.el).append(description);
			var options = View.make('ol', {
				class: 'options'
			});
			var _ = require('../../libs/underscore');
			var i = 0;
			var that = this;
			this.optionCheckbox.length = 0;
			_.each(readingQuestionModel.get("options"), function(op) {
				var optionId = 'option' + i;
				var liElement = View.make('li', {
					class: 'option'
				});
				var inputElement = View.make('input', {
					type: 'checkbox',
					id: optionId
				});

				$(liElement).append(inputElement);
				that.optionCheckbox.push(inputElement);

				var labelElement = View.make("label", {
					for: optionId
				},
				op);
				$(liElement).append(labelElement);
				$(options).append(liElement);
				i++;
			});
			$(this.el).append(options);
			return this;
		}
	});
	return ReadingQuestionView;
});

