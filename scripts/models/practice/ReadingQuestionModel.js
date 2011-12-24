define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var BaseQuestionModel = require('./BaseQuestionModel');
	var ReadiingQuestionModel = BaseQuestionModel.extend({
		getOptionNumber: function() {
			if (this.has("option_number")) {
				return this.get("option_number");
			} else {
				return 1;
			}
		}
	});
	return ReadiingQuestionModel;
});

