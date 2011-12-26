define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var Utils = require('../../libs/utils');
	var PracticeItemModel = require('./PracticeItemModel');
	var BaseMenuModel = require('./BaseMenuModel');
	
	var PracticeMenuModel = BaseMenuModel.extend({
		practice_type: '',
		url: function() {
			console.log('BuildingUrl: ' + this.get('practice_type'));
			return Utils.BuildUrl('/api/practicemenu', {practice_type: this.get('practice_type')});
		},
		fetched: false,
		items: Backbone.Collection.extend({
			model: PracticeItemModel
		})
	});
	return PracticeMenuModel;
});

