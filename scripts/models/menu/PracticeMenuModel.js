define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var PracticeItemCollection = require('./PracticeItemCollection');
	var Utils = require('../../libs/utils');
	var PracticeMenuModel = Backbone.Model.extend({
		practice_type: '',
		url: function() {
			console.log('BuildingUrl: ' + this.get('practice_type'));
			return Utils.BuildUrl('/api/practicemenu', {practice_type: this.get('practice_type')});
		},
		practicenum: "0",
		name: "default",
		order: "default",
		description: "This is the practice menu model",
		practiceitems: PracticeItemCollection,
		onChange: function() {
			this.set({ practiceitems : new PracticeItemCollection(this.get('practiceitems')) });
		},
		initialize: function() {
			this.bind('change', this.onChange);
		}
	});
	return PracticeMenuModel;
});

