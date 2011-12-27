define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');

	var TestItemView = require('./TestItemView');
	
	/*var TestMenuView = Backbone.View.extend({
	render: function() {

		var items = this.model.get('items');
		console.log('testItems: ' + JSON.stringify(items));
		console.log(items);
		var that = this;
	    this._itemViews = [];
	 
	    items.each(function(item) {
	      that._itemViews.push(new TestItemView({
	        model : item,
	        tagName : 'li'
	      }));
	    });
	    
	    
		console.log('Draw element');
        var $ = require('../../libs/jquery');

		
		var that = this;
		var itemsNode = $('#testitems');

	    // Clear out this element.
		itemsNode.empty();
		itemsNode.text("Total: " + this.model.get('itemnum') + " Tests.");

	    // Render each sub-view and append it to the parent view's element.
	    _(this._itemViews).each(function(iv) {
	    		itemsNode.append(iv.render().el);
	    });
		
		return this;
	},
	initialize: function(options) {
		console.log('TestMenuView.Init');
		this.render = _.bind(this.render, this); 
	    this.model.bind('change', this.render);
        
        return this;
	}});*/
	var BaseMenuView = require("./BaseMenuView");
	var TestMenuView = BaseMenuView.extend({
		itemView: TestItemView,
		paged: true
	});
    return TestMenuView;
});

