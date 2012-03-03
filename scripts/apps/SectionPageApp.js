define(function(require, exports) {

	var Backbone = require('../libs/backbone');

	var SectionPageApp = Backbone.Router.extend({
		initialize: function() {
            var $ = require('../libs/jquery');
            $('#practice-section').html("hello world");
            var data = JSON.parse($('#configData').html()); 
            console.log("Section Page got section id is " + data.sectionid);
            self.sectionid = data.sectionid;


			},

        routes: {
			"help": "help",
			":questionId": "showQuestion"

		},

		help: function() {
			console.log("help called.");
		},

		showQuestion: function(questionId) {
            this.readingSectionView.showQuestion(parseInt(questionId, 10));
		}
	});

	var app = new SectionPageApp();
    console.log( "start result is " + 
	Backbone.history.start({
        root: "/section/" + app.sectionId
	}));


	console.log('Main inilized.');
	return SectionPageApp;
});

