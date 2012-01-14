define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');

	var ListeningPageApp = Backbone.Router.extend({
		initialize: function() {
			var theApp = this;
			
			var ListeningView = require('../views/practice/ListeningView');
			var ListeningModel = require('../models/practice/ListeningModel');

			var listeningModel = new ListeningModel({
				question: new Backbone.Collection()
			});
			
			listeningModel.fetch({success:function(){console.log("Success!");}});
			
			
			var listeningView = new ListeningView({
				model: listeningModel,
				el: '#practice-section'
			});
		}
	})

	var app = new ListeningPageApp;
	console.log('Listening Main inilized.');
	return ListeningPageApp;
});

