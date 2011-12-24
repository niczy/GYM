define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
    var BaseQuestionModel = require('./BaseQuestionModel');
	var ReadiingQuestionModel = BaseQuestionModel.extend();
	return ReadiingQuestionModel;
});

