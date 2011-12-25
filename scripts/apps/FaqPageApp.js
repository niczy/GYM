define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');

	var FaqPageApp = Backbone.Router.extend({
		initialize: function() {
			var FaqView = require('../views/menu/FaqView');
			var FaqModel = require('../models/menu/FaqModel');

			var faqModel = new FaqModel({items:new Backbone.Collection()});
			
			faqModel.fetch({success:function(){console.log("Faq fetch Success!");}});
			var faqView = new FaqView({
				model: faqModel,
				el: '#faq'
			});
			faqView.render();
			
			$('#submit_button').click(function() {
				$('#submit_button').attr('value', 'Submitting...');
			});
		}
	});
	var app = new FaqPageApp;
	console.log('Main inilized.');
	return FaqPageApp;
});

