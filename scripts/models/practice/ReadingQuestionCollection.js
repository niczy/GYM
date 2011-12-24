define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var ReadingQuestionModel = require('./ReadingQuestionModel');
	var ReadingQuestionCollection = Backbone.Collection.extend({
		model: ReadingQuestionModel
	});
    return ReadingQuestionCollection;
});

