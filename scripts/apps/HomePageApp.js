define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');
	var test_collection = new Backbone.Collection([
	                                          {testid: "1", title: "TPO1"},
	                                          {testid: "2", title: "TPO2"},
	                                          {testid: "3", title: "TPO3"}
	                                        ]);

	                                       // alert(JSON.stringify(collection));
	                                       // collection.each(function(e){alert(JSON.stringify(e))})
	var HomePageApp = Backbone.Router.extend({
		initialize: function() {
			var TestMenuView = require('../views/menu/TestMenuView');
			var TestMenuModel = require('../models/menu/TestMenuModel');

			var testMenuModel = new TestMenuModel({
				testnum: "23",
				name: "default",
				description: "Hello",
				testitems: test_collection
			});
			
			//testMenuModel = new TestMenuModel();
			testMenuModel.fetch({success:function(){console.log("Success!");}});
			var testMenuView = new TestMenuView({
				model: testMenuModel,
				el: '#test-menu'
			});
			testMenuView.render();
			
			$("#menu-order-select").change(function () {
	          var str = "";
	          $("select option:selected").each(function () {
	                str = $(this).attr('value');
	           });
	          console.log("Sort By: " + str);
	          testMenuModel.get('testitems').comparator = function(item) {
	        	  	return item.get(str);
	          };
	          testMenuModel.get('testitems').sort();
	          testMenuView.render();
	          /*var oldItems = testMenuModel.get('testitems');
	          console.log(oldItems);
	          var sortedItems = _.sortBy(oldItems, function(item) {
	        	     console.log('sort key: ' + item.get(str));
	        	  	return item.get(str);
	          });
			 console.log('Sorted: ' + sortedItems);
	          testMenuModel.set({testitems: sortedItems});*/

	        })
	        .trigger('change');
		}
	})

	var app = new HomePageApp;

	console.log('Main inilized.');
	return HomePageApp;
});

