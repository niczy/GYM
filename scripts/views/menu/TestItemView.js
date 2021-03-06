define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');

	var TestItemView = Backbone.View.extend({
	render: function() {
		console.log('TestItemView::Render item ' + this.el);
        var $ = require('../../libs/jquery');
        
        var compiled = _.template(
        		'<div class="testitem">\
        		  <h4><%= title %></h4>\
        		   <div class="price">\
        		     <label>Price: <span><%= price %></span></label>\
        		   </div>\
        		   <div class="uploader">\
        		    <img src="<%= portrait %>"/>\
        		    <label>Uploader: <a href="/userinfo/<%= uploader %>" target="_blank"><%= uploader %></a></label>\
        		  </div>\
        		  <a target="_blank" href="/testdetail/<%= testid %>">details >>></a>\
        		</div>');
       
        

		//$(this.el).text("Title: " + this.model.get('title'));
		$(this.el).html(compiled({
			title : this.model.get('title'),
			portrait : this.model.get('uploaderPortrait'),
			uploader: this.model.get('uploader'),
			price: this.model.get('price'),
			testid: this.model.get('testid')
		}));

		return this;
	},
	initialize: function(options) {
		console.log('ItemView.Init');
		this.render = _.bind(this.render, this); 
	    this.model.bind('change', this.render);
		//_.bindAll(this, 'render');
        //this.model.bind('change:testnum', this.render);
        //this.model.bind("change", this.render);
        
        return this;
	}});
    return TestItemView;
});

