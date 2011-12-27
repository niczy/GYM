define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');
	require('../controls/tabs.js');
	var MenuControlBar = require('../controls/MenuControlBar');

	var TestDetailApp = Backbone.Router.extend({
		initialize: function() {
			var TestDetailView = require('../views/menu/TestDetailView');
			var TestDetailModel = require('../models/menu/TestDetailModel');

			console.log("TESTID: " + $("#testid").attr('value'));
			var testDetailModel = new TestDetailModel({
				testid: $("#testid").attr('value'),
				pageid: 1,
				items: new Backbone.Collection()
			});
			
			testDetailModel.fetch({success:function(){console.log("Success!");}});
			var testDetailView = new TestDetailView({
				model: testDetailModel,
				el: '#test-history-list'
			});

			var controlBar = new MenuControlBar({
				model: testDetailModel,
				el: '#control-bar',
				options: [
				   {key: 'testid', value: 'Default'},
				   {key: 'viewer', value: 'Num of Views'},
				   {key: 'buyer', value: 'Num of Buys'},
				   {key: 'price', value: 'Price'}]
			});
			
		}
	})

	var app = new TestDetailApp;
	console.log('Test Detail Main inilized.');
	return TestDetailApp;
});

