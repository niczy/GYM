define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var TestItemCollectionView = Backbone.View.extend({
	  initialize : function() {
	    var that = this;
	    this._itemViews = [];
	 
	    this.collection.each(function(item) {
	      that._itemViews.push(new TestItemView({
	        model : item,
	        tagName : 'li'
	      }));
	    });
	  },
	 
	  render : function() {
	    var that = this;
	    // Clear out this element.
	    $(this.el).empty();
	 
	    // Render each sub-view and append it to the parent view's element.
	    _(this._itemViews).each(function(iv) {
	      $(that.el).append(iv.render().el);
	    });
	  }
	});
    return TestItemCollectionView;
});

