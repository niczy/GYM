define(function(require, exports) {
	var $ = require('../../libs/jquery');
	var Backbone = require('../../libs/backbone');
	var ReadingQuestionView = Backbone.View.extend({
		el: 'body',
		render: function() {
			$(this.el).text(this.model.description);
			return this;
		}
	});
	return ReadingQuestionView;
});
	
