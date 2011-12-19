define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var TestItemCollection = require('./TestItemCollection');

	var TestMenuModel = Backbone.Model.extend({
		url: function() {
			return "/testmenu/" + this.get('name');
		},
		name: "This is the test menu model",
		items: TestItemCollection
	});
	return TestMenuModel;
});

