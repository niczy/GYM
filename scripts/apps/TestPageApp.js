define(function(require, exports) {

	var Backbone = require('../libs/backbone');

	var TestPageApp = Backbone.Router.extend({
		initialize: function() {
			var $ = require('../libs/jquery');
			var data = JSON.parse($('#configData').html());
            this.test = data; 
            console.log("got test info" + data);
            var SectionView = require('../views/practice/SectionView');
            this.sectionView = new SectionView({
                    sectionid : this.sectionid,
                    type : this.type
                });
            this.sectionView.render();
            that = this;
			$("#next-question").bind("click", function(){
                    that.navigate(String(that.sectionView.getNextQuestionIdx()), true);
                    });
            $("#previous-question").bind("click", function(){
                    that.navigate(String(that.sectionView.getPreviousQuestionIdx()), true);
                    });

		},

		routes: {
			"help": "help",
			":questionId": "showQuestion"

		},

		help: function() {
			console.log("help called.");
		},

		showQuestion: function(questionId) {
			this.sectionView.showQuestion(parseInt(questionId, 10));
		}
	});

	var app = new SectionPageApp();
	console.log("start result is " + Backbone.history.start({
		root: "/section/" + app.sectionId
	}));

	console.log('Main inilized.');
	return SectionPageApp;
});

