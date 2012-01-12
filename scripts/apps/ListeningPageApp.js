define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');

	var ListeningPageApp = Backbone.Router.extend({
		initialize: function() {
			var theApp = this;
			
			var ListeningView = require('../views/practice/ListeningView');
			var ListeningModel = require('../models/practice/ListeningModel');

			var testMenuModel = new TestMenuModel({
				description: "Hello",
				items: new Backbone.Collection()
			});
			
			testMenuModel.fetch({success:function(){console.log("Success!");}});
			
			theApp.startTestDialog = new StartTestDialog({
				el: '#start-test-dialog'
			});
			theApp.testItemClick = function(testItemModel, event) {
				if (event.target.nodeName == 'A') {
					return;
				}
				theApp.startTestDialog.render({
					price: testItemModel.get('price'),
					credit: 99,
					test_title: testItemModel.get('title'),
					test_date: testItemModel.get('lastUseTime'),
					test_status: testItemModel.get('status'),
					testid: testItemModel.get('testid')
				});	
			};
			
			var testMenuView = new TestMenuView({
				model: testMenuModel,
				el: '#test-menu',
				itemClick: theApp.testItemClick
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

	var app = new ListeningPageApp;
	console.log('Listening Main inilized.');
	return ListeningPageApp;
});

