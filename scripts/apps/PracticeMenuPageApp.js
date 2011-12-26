define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	
	var $ = require('../libs/jquery');
	var _ = require('../libs/underscore');
	require('../controls/tabs.js');
	var PracticeMenuView = require('../views/menu/PracticeMenuView');
	var PracticeMenuModel = require('../models/menu/PracticeMenuModel');
	var MenuControlBar = require('../controls/MenuControlBar');

	
	var PracticeMenuPageApp = Backbone.Router.extend({
		practice_type: 'reading',
		initialize: function() {
			
			var theApp = this;
			console.log(theApp);
			console.log('theApp.practice_type: ' + theApp.practice_type);
			this.readingMenuModel = new PracticeMenuModel({
				practice_type: 'reading', 
				items: new Backbone.Collection()
			});
			this.writingMenuModel = new PracticeMenuModel({
				practice_type: 'writing', 
				items: new Backbone.Collection()
			});
			this.listeningMenuModel = new PracticeMenuModel({
				practice_type: 'listening', 
				items: new Backbone.Collection()
			});
			this.speakingMenuModel = new PracticeMenuModel({
				practice_type: 'speaking', 
				items: new Backbone.Collection()
			});

			this.practiceMenuView = new PracticeMenuView({
				model: this.practiceMenuModel(),
				el: '#practice-menu'
			});

			$("#subnav-bar > ul > li").click(function() {
				theApp.navigate($(this).attr("name"), true);
			});
			
			var controlBar = new MenuControlBar({
				getModel: function() {
					return theApp.practiceMenuModel();
				},
				el: '#control-bar',
				options: [
				   {key: 'practiceid', value: 'Default'},
				   {key: 'viewer', value: 'Num of Views'}]
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
			console.log('ResetView');
			this.practiceMenuView = new PracticeMenuView({
				model: theModel,
				el: '#practice-menu'
			});
			//this.practiceMenuModel = theModel;
			if (!theModel.get('fetched')) {
				theModel.fetch();
				theModel.set({'fetched': true});
			} else {
				theModel.change();
				//this.practiceMenuView.render();
			}
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

