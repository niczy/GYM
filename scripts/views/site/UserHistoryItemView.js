define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');

	var UserHistoryItemView = Backbone.View.extend({
	render: function() {
		console.log('UserHistoryItemView::Render item ' + this.el);
        var $ = require('../../libs/jquery');
        
        var Templates = require('../../templates/site/AccountPageTemplates');
        
		$(this.el).html(Templates.userHistoryItem({
			title : this.model.get('title'),
			testid : this.model.get('testid'),
			date: this.model.get('date')
		}));

		return this;
	},
	initialize: function(options) {
		console.log('UserHistoryItemView.Init');
		this.render = _.bind(this.render, this); 
	    this.model.bind('change', this.render);
        
        return this;
	}});
    return UserHistoryItemView;
});

