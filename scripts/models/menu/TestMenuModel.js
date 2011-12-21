define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var TestItemCollection = require('./TestItemCollection');
	var Utils = require('../../libs/utils');
	var TestMenuModel = Backbone.Model.extend({
		url: function() {
			return Utils.BuildUrl('/api/testmenu');
		},
		testnum: "0",
		name: "default",
		order: "default",
		description: "This is the test menu model",
		testitems: TestItemCollection,
		onChange: function() {
			this.set({ testitems : new TestItemCollection(this.get('testitems')) });
		},
		initialize: function() {
			this.bind('change', this.onChange);
		}
	});
	return TestMenuModel;
});

