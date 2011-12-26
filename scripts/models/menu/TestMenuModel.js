define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var TestItemModel = require('./TestItemModel');
	var Utils = require('../../libs/utils');
	var BaseMenuModel = require('./BaseMenuModel');

	var TestMenuModel = BaseMenuModel.extend({
		url: function() {
			return Utils.BuildUrl('/api/testmenu');
		},
		items: Backbone.Collection.extend({
			model: TestItemModel
		})
	});
	return TestMenuModel;
});

