define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');

	var PracticeItemView = Backbone.View.extend({
	render: function() {
		console.log('Item::Draw item ' + this.el);
        var $ = require('../../libs/jquery');
        
        var compiled = _.template(
        		'<div class="item">\
        		  <h4><%= title %></h4>\
        		   <div class="price">\
        		     <label>Num of View: <span><%= viewer %></span></label>\
        		   </div>\
        		   <div class="uploader">\
        		    <label>Uploader: <%= uploader %></label>\
        		  </div>\
        		</div>');
       
        

		//$(this.el).text("Title: " + this.model.get('title'));
		$(this.el).html(compiled({
			title : this.model.get('title'),
			uploader: this.model.get('uploader'),
			viewer: this.model.get('viewer')
		}));

		return this;
	},
	initialize: function(options) {
		console.log('ItemView.Init');
		this.render = _.bind(this.render, this); 
	    this.model.bind('change', this.render);
        
        return this;
	}});
    return PracticeItemView;
});

