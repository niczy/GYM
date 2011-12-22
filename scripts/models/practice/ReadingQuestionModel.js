define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
    var BaseQuestionModel = require('./BaseQuestionModel');
	var ReadiingQuestion = BaseQuestionModel.extend();
	return ReadiingQuestion;
});

