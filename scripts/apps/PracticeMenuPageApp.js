define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');
	require('../action/tabs.js');
	var PracticeMenuPageApp = Backbone.Router.extend({
		practice_type: $('#practice-menu').attr('name'),
		initialize: function() {
			var PracticeMenuView = require('../views/menu/PracticeMenuView');
			var PracticeMenuModel = require('../models/menu/PracticeMenuModel');
			var theApp = this;
			console.log('theApp.practice_type: ' + theApp.practice_type);
			var practiceMenuModel = new PracticeMenuModel({
				practice_type: theApp.practice_type, 
				practicenum: "12",
				name: "default",
				description: "Hello",
				practiceitems: new Backbone.Collection()
			});
			
			//testMenuModel = new TestMenuModel();
			practiceMenuModel.fetch({success:function(){console.log("Success!");}});
			var practiceMenuView = new PracticeMenuView({
				model: practiceMenuModel,
				el: '#practice-menu'
			});
			practiceMenuView.render();
			
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
	            practiceMenuModel.get('practiceitems').comparator = function(item) {
	        	      if (!that.reverse) {
	        	    	      return item.get(field);
	        	      } else {
	        	    	      return -item.get(field);
	        	      }
	            };
	            practiceMenuModel.get('practiceitems').sort();
	            practiceMenuView.render();      
			};
			
			
			$("#reverse-menu").click(function() {
				that.reverse = !that.reverse;
				SortMenuBy(GetSortField());
			});

			$("#menu-order-select").change(function () {
				SortMenuBy(GetSortField());
	        }).trigger('change');
		}
	});
	var app = new PracticeMenuPageApp;
	console.log('Practice Page Main inilized.');
	return PracticeMenuPageApp;
});

