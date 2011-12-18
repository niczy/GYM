define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
    var BaseQuestionModel = require('./BaseQuestionModel');
	var ReadiingQuestion = BaseQuestionModel.extend({
		description: "This is the description",
		answer: "This is the answer"
	});
	return ReadiingQuestion;
});

