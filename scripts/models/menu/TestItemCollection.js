define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var TestItemModel = require('./TestItemModel');
	var TestItemCollection = Backbone.Collection.extend({
		model: TestItemModel
	});
    return TestItemCollection;
});

