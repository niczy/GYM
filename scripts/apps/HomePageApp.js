define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');
	var MenuControlBar = require('../controls/MenuControlBar');
	require('../controls/tabs.js');

	var HomePageApp = Backbone.Router.extend({
		reverse : false,
		initialize: function() {
			var TestMenuView = require('../views/menu/TestMenuView');
			var TestMenuModel = require('../models/menu/TestMenuModel');

			var testMenuModel = new TestMenuModel({
				description: "Hello",
				items: new Backbone.Collection()
			});
			
			testMenuModel.fetch({success:function(){console.log("Success!");}});
			var testMenuView = new TestMenuView({
				model: testMenuModel,
				el: '#test-menu'
			});

			var controlBar = new MenuControlBar({
				model: testMenuModel,
				el: '#control-bar',
				options: [
				   {key: 'testid', value: 'Default'},
				   {key: 'viewer', value: 'Num of Views'},
				   {key: 'buyer', value: 'Num of Buys'},
				   {key: 'price', value: 'Price'}]
			});
			
		}
	})

	var app = new HomePageApp;
	console.log('Main inilized.');
	return HomePageApp;
});

