define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');
	require('../controls/tabs.js');
	var PracticeMenuView = require('../views/menu/PracticeMenuView');
	var PracticeMenuModel = require('../models/menu/PracticeMenuModel');
	
	var PracticeMenuPageApp = Backbone.Router.extend({
		practice_type: 'reading',
		initialize: function() {
			
			var theApp = this;
			console.log(theApp);
			console.log('theApp.practice_type: ' + theApp.practice_type);
			this.readingMenuModel = new PracticeMenuModel({
				practice_type: 'reading', 
				practiceitems: new Backbone.Collection()
			});
			this.writingMenuModel = new PracticeMenuModel({
				practice_type: 'writing', 
				practiceitems: new Backbone.Collection()
			});
			this.listeningMenuModel = new PracticeMenuModel({
				practice_type: 'listening', 
				practiceitems: new Backbone.Collection()
			});
			this.speakingMenuModel = new PracticeMenuModel({
				practice_type: 'speaking', 
				practiceitems: new Backbone.Collection()
			});
			//this.practiceMenuModel = this.readingMenuModel;
			//testMenuModel = new TestMenuModel();
			//this.practiceMenuModel.fetch({success:function(){console.log("Success!");}});
			this.practiceMenuView = new PracticeMenuView({
				model: this.practiceMenuModel(),
				el: '#practice-menu'
			});
			//this.practiceMenuView.render();
			
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
	            theApp.practiceMenuModel().get('practiceitems').comparator = function(item) {
	        	      if (!that.reverse) {
	        	    	      return item.get(field);
	        	      } else {
	        	    	      return -item.get(field);
	        	      }
	            };
	            theApp.practiceMenuModel().get('practiceitems').sort();
	            theApp.practiceMenuView.render();      
			};
			
			
			$("#reverse-menu").click(function() {
				that.reverse = !that.reverse;
				SortMenuBy(GetSortField());
			});

			$("#menu-order-select").change(function () {
				SortMenuBy(GetSortField());
	        }).trigger('change');

			$("#subnav-bar > ul > li").click(function() {
				theApp.navigate($(this).attr("name"), true);
			});
		},
		getModelByType: function(type) {
			if (type == "reading") return this.readingMenuModel;
			else if (type == "writing") return this.writingMenuModel;
			else if (type == "speaking") return this.speakingMenuModel;
			else if (type == "listening") return this.listeningMenuModel;
			else return this.readingMenuModel;
		},
		practiceMenuModel: function() {
			return this.getModelByType(this.practice_type);
		},
		
		routes: {
			":practice_type": "selectType"
		},
		
		selectType: function(type) {
			if (type == '') type = 'reading';
			console.log('SelectType(): ' + type);
			this.practice_type = type;
			$("#subnav-bar > ul > li").removeClass("selected");
			$("#subnav-bar > ul > li").each(function() {
				if ($(this).attr('name') == type) {
					$(this).addClass("selected");
				}
 			});
			
			var theModel = this.getModelByType(type);
			//this.practiceMenuModel = theModel;
			if (!theModel.get('fetched')) {
				theModel.fetch();
				theModel.set({'fetched': true});
			} 
			console.log('ResetView');
			this.practiceMenuView = new PracticeMenuView({
				model: theModel,
				el: '#practice-menu'
			});
			this.practiceMenuView.render();
		}
	});
	var app = new PracticeMenuPageApp;
	console.log( "start result is " + 
	Backbone.history.start({
        root: "/practices/"
	}));
	console.log('Practice Page Main inilized.');
	return PracticeMenuPageApp;
});

