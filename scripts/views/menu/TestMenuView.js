define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');

	var TestItemView = require('./TestItemView');
	
	var TestMenuView = Backbone.View.extend({
	render: function() {
		/*console.log('Draw element');
        var $ = require('../../libs/jquery');
		$(this.el).text("Total: " + this.model.get('testnum') + " Tests. Ordered by: " + this.model.get('description'));
		var that = this;
		this.collection.each(function(item) {
			var itemView = new TestItemView({
				model: item,
				tagName: 'li'
			});
			$(that.el).append(itemView.render().el);
		});*/
		var items = this.model.get('testitems');
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
		itemsNode.text("Total: " + this.model.get('testnum') + " Tests.");

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
	}});
    return TestMenuView;
});

