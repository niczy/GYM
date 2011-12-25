define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');

	var PracticeItemView = require('./PracticeItemView');

	var PracticeMenuView = Backbone.View.extend({
		render: function() {

			var items = this.model.get('practiceitems');
			console.log('practiceitems: ' + JSON.stringify(items));
			console.log(items);
			var that = this;
			this._itemViews = [];

			items.each(function(item) {
				that._itemViews.push(new PracticeItemView({
					model: item,
					tagName: 'li'
				}));
			});

			console.log('Draw element');
			var $ = require('../../libs/jquery');

			var itemsNode = $('#practiceitems');

			// Clear out this element.
			itemsNode.empty();
			itemsNode.text("Total: " + this.model.get('practicenum') + " Tests.");

			// Render each sub-view and append it to the parent view's element.
			_(this._itemViews).each(function(iv) {
				itemsNode.append(iv.render().el);
			});

			return this;
		},
		initialize: function(options) {
			console.log('PracticeMenuView.Init');
			this.render = _.bind(this.render, this);
			this.model.bind('change', this.render);

			return this;
		}
	});
	return PracticeMenuView;
});

