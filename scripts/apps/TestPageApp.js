define(function(require, exports) {

	var Backbone = require('../libs/backbone');

	var TestPageApp = Backbone.Router.extend({
		initialize: function() {
			var $ = require('../libs/jquery');
			this.testInfo = JSON.parse($('#test_info').html());
            this.type = $('#current_section').html().trim();
            var SectionView = require('../views/practice/SectionView');
            this.sectionView = new SectionView({
                    sectionid : this.testInfo.readings[0],
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

	var app = new TestPageApp();
	console.log("start result is " + Backbone.history.start({
		root: "/section/" + app.sectionId
	}));

	console.log('Main inilized.');
	return TestPageApp;
});

