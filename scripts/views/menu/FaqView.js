define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');
	var $ = require('../../libs/jquery');
	var FaqItemView = Backbone.View.extend({
		render: function() {
			console.log('Item::Draw Faq item ' + this.el);
	        var $ = require('../../libs/jquery');
	        
	        var compiled = _.template(
	        		'<div>\
	        		  <h3><%= question %></h3>\
	        		  <br/>\
	        		  <h3><%= answer %></h3>\
	        		</div>');
	       var answer = this.model.get('answer');
	       if (answer == '') answer = 'No Answer.';
      	//$(this.el).text("Title: " + this.model.get('title'));
			$(this.el).html(compiled({
				question : this.model.get('question'),
				answer : answer
			}));
			return this;
		},
		initialize: function(options) {
			console.log('ItemView.Init');
			this.render = _.bind(this.render, this); 
		    this.model.bind('change', this.render);
	        return this;
		}});
	
	var FaqView = Backbone.View.extend({
	render: function() {

		var items = this.model.get('items');
		console.log('Faq Items: ' + JSON.stringify(items));
		var theView = this;
	    this._itemViews = [];
	 
	    items.each(function(item) {
	      theView._itemViews.push(new FaqItemView({
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
	}});
    return FaqView;
});

