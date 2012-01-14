define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');

	var ListeningView = Backbone.View.extend({
		render: function() {
			
		},
		initialize: function(options) {
			console.log('ListeningView.Init');
			this.render = _.bind(this.render, this); 
		    this.model.bind('change', this.render);
	        return this;
		}
	});
    return ListeningView;
});

