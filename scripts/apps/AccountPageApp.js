define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');
	var Utils = require('../libs/utils');
	
	var AccountPageApp = Backbone.Router.extend({
		initialize: function() {
			var BaseMenuModel = require('../models/menu/BaseMenuModel');
			var BaseMenuView = require('../views/menu/BaseMenuView');
			
			var UserHistoryItemView = require('../views/site/UserHistoryItemView');
			var UserHistoryItemModel = Backbone.Model.extend({
				testid: 1,
				title: 'TPO',
				date: '2012-10-12 19:34'
			});

			
			var UserHistoryModel = BaseMenuModel.extend({
				url: function() {
					return Utils.BuildUrl('/api/userhistory');
				},
				items: Backbone.Collection.extend({
					model: UserHistoryItemModel
				})
			});
			
			var UserHistoryView = BaseMenuView.extend({
				itemView: UserHistoryItemView,
				paged: false
			});
			
			var theModel = new UserHistoryModel({items:new Backbone.Collection()});
			
			theModel.fetch({success:function(){console.log("Faq fetch Success!");}});
			var theView = new UserHistoryView({
				model: theModel,
				el: '#test-history-list'
			});
			theView.render();
		}
	});
	var app = new AccountPageApp();
	console.log('Main inilized.');
	return AccountPageApp;
});

