define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var BaseQuestionModel = Backbone.Model.extend({
		name: 'This is the base model'
	});
	return BaseQuestionModel;
});

