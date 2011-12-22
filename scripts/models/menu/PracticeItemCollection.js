define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var PracticeItemModel = require('./PracticeItemModel');
	var PracticeItemCollection = Backbone.Collection.extend({
		model: PracticeItemModel
	});
    return PracticeItemCollection;
});

