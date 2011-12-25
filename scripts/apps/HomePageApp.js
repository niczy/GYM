define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');
	require('../action/tabs.js');

	var HomePageApp = Backbone.Router.extend({
		reverse : false,
		initialize: function() {
			var TestMenuView = require('../views/menu/TestMenuView');
			var TestMenuModel = require('../models/menu/TestMenuModel');

			var testMenuModel = new TestMenuModel({
				testnum: "23",
				name: "default",
				description: "Hello",
				testitems: new Backbone.Collection()
			});
			
			testMenuModel.fetch({success:function(){console.log("Success!");}});
			var testMenuView = new TestMenuView({
				model: testMenuModel,
				el: '#test-menu'
			});
			testMenuView.render();
			
			var GetSortField = function() {
				var select = $("#menu-order-select");
		        var str = "";
		        $("select option:selected").each(function () {
		              str = $(this).attr('value');
		        });
		        return str;
			};
			var that = this;
			var SortMenuBy = function(field) {

	            console.log("Sort By: " + field);
	            testMenuModel.get('testitems').comparator = function(item) {
	        	      if (!that.reverse) {
	        	    	      return item.get(field);
	        	      } else {
	        	    	      return -item.get(field);
	        	      }
	            };
	            testMenuModel.get('testitems').sort();
	            testMenuView.render();      
			};
			
			
			$("#reverse-menu").click(function() {
				that.reverse = !that.reverse;
				SortMenuBy(GetSortField());
			});

			$("#menu-order-select").change(function () {
				SortMenuBy(GetSortField());
	        }).trigger('change');
		}
	})

	var app = new HomePageApp;
	console.log('Main inilized.');
	return HomePageApp;
});

