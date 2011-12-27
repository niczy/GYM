define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var Utils = require('../../libs/utils');
	var BaseMenuModel = require('./BaseMenuModel');

	var TestHistoryItemModel = Backbone.Model.extend({
		user: "user",
		date: "2011-1-2"
	})
	
	var TestDetailModel = BaseMenuModel.extend({
		testid: '2',
		url: function() {
			return Utils.BuildUrl('/api/testhistory',
				{
				'testid': this.get('testid'),
				'pageid': this.get('pageid')
				});
		},
		items: Backbone.Collection.extend({
			model: TestHistoryItemModel
		})
	});
	return TestDetailModel;
});

