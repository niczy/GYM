define(function(require, exports) {
	var Backbone = require('../../libs/backbone');

	var BaseMenuModel = Backbone.Model.extend({
		url: function() {
		},
		itemnum: 0,
		pagenum: 0,
		pageid: 0,
		order: "default",
		description: "This is the practice menu model",
		items: Backbone.Collection,
		onChange: function() {
			console.log('BaseMenuModel.onChange');
			// If items is an object array, convert it to a Backbone collection.
			if(this.get('items') && !this.get('items').each) {
				var type = this.items;
			    this.set({ items : new type(this.get('items')) });
			}
		},
		initialize: function() {
			this.bind('change', this.onChange);
		}
	});
	return BaseMenuModel;
});

