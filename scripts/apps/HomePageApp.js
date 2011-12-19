define(function(require, exports) {

	var Backbone = require('../libs/backbone');
	var HomePageApp = Backbone.Router.extend({
		initialize: function() {
			var TestMenuView = require('../views/menu/TestMenuView');
			var TestMenuModel = require('../models/menu/TestMenuModel');

			var testMenuModel = new TestMenuModel({
				testnum: "23",
				name: "default"
			});
			console.log(testMenuModel.get('testnum'));
			testMenuModel.fetch();

			testMenuView = new TestMenuView({
				model: testMenuModel 
			});
			testMenuView.render();
		}
	})

	var app = new HomePageApp;

	console.log('Main inilized.');
	return HomePageApp;
});

