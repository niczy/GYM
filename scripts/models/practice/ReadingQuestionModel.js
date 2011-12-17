define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var ReadiingQuestion = Backbone.Model.extend({
		description: "This is the description",
		answer: "This is the answer"
	});
	return ReadiingQuestion;
});

