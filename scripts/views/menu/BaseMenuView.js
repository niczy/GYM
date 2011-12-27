define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');
    var $ = require('../../libs/jquery');

	var BaseMenuView = Backbone.View.extend({
	itemView: Backbone.View,
	render: function() {
		var theView = this;
		var items = this.model.get('items');
		console.log('baseViewItems: ' + JSON.stringify(items));

	    this._itemViews = [];
	 
	    items.each(function(item) {
	    	  theView._itemViews.push(new theView.itemView({
	        model : item,
	        tagName : 'li'
	      }));
	    });
	    
	    console.log('BaseMenuView' + this.el);
	    console.log($(this.el));
	    // Clear out this element.
		$(this.el).empty();

	    // Render each sub-view and append it to the parent view's element.
	    _(this._itemViews).each(function(iv) {
	    		$(theView.el).append(iv.render().el);
	    });
		
	    if (this.paged) {
	    		$(this.el).append('<div class="page-bar"></div>');
	    		var bar = $('.page-bar');
	    		bar.append('<span class="prev-page"> Previous </span>');
	    		for (var i = 1; i <= this.model.get('pagenum'); ++i) {
	    			bar.append('<span> ' + i + ' </span>');
	    			if (i == this.model.get('pageid')) {
	    				bar.children().last().addClass('cur-page');
	    			}
	    		}
	    		bar.append('<span class="next-page"> Next </span>');
	    		var curPage = this.model.get('pageid');
	    		if (curPage > 1) {
		    		bar.find('.prev-page').click(function(){
		    			theView.model.set({'pageid': curPage - 1});
		    			theView.model.fetch();
		    		});
	    		}
	    		
	    		if (curPage < this.model.get('pagenum')) {
		    		bar.find('.next-page').click(function(){
		    			theView.model.set({'pageid': curPage + 1});
		    			theView.model.fetch();
		    		});
	    		}
	    }
	    
		return this;
	},
	initialize: function(options) {
		console.log('BaseMenuView.Init');
		//this.itemView = options.itemView;
		this.render = _.bind(this.render, this); 
	    this.model.bind('change', this.render);
        return this;
	}});
    return BaseMenuView;
});

