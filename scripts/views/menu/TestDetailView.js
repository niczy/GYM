define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');
	var $ = require('../../libs/jquery');
	var TestHistoryItemView = Backbone.View.extend({
		render: function() {
	        var compiled = _.template(
	        		'<div>\
	        		  <h3>Username: <%= user %></h3>\
	        		  <br/>\
	        		  <h3>Used on: <%= date %></h3>\
	        		</div>');

			$(this.el).html(compiled({
				user : this.model.get('user'),
				date : this.model.get('date')
			}));
			
			return this;
		},
		initialize: function(options) {
			console.log('TestHistoryItemView.Init');
			this.render = _.bind(this.render, this); 
		    this.model.bind('change', this.render);
	        return this;
		}});
	
	/*var TestDetailView = Backbone.View.extend({
	render: function() {

		var items = this.model.get('items');
		console.log('TestDetailView Items: ' + JSON.stringify(items));
		var theView = this;
	    this._itemViews = [];
	 
	    items.each(function(item) {
	      theView._itemViews.push(new TestHistoryItemView({
	        model : item,
	        tagName : 'li'
	      }));
	    });
	    $(this.el).empty();
	    // Render each sub-view and append it to the parent view's element.
	    _(this._itemViews).each(function(iv) {
	    		$(theView.el).append(iv.render().el);
	    });
		return this;
	},
	initialize: function(options) {
		console.log('FaqView.Init');
		this.render = _.bind(this.render, this); 
	    this.model.bind('change', this.render);
        return this;
	}});*/
	var BaseMenuView = require("./BaseMenuView");
	var TestDetailView = BaseMenuView.extend({
		itemView: TestHistoryItemView,
		paged: true
	});
    return TestDetailView;
});

