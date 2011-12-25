define(function(require, exports) {

	var Backbone = require('../libs/backbone');

	var ReadingPageApp = Backbone.Router.extend({
		initialize: function() {
			var ReadingQuestionView = require('../views/practice/ReadingQuestionView');
			var ReadingQuestionModel = require('../models/practice/ReadingQuestionModel');
			var ReadingSectionModel = require('../models/practice/ReadingSectionModel');
            var $ = require('../libs/jquery');

            var data = JSON.parse($("#configData").html());
            this.testId = data.testId;
            this.sectionId = data.sectionId;

			this.readingSectionModel = new ReadingSectionModel({
				testid: this.testId,
				sectionid: this.sectionId
			});

			var ReadingSectionView = require('../views/practice/ReadingSectionView');
			this.readingSectionView = new ReadingSectionView({
				model: this.readingSectionModel
			});

			var that = this;
			this.readingSectionModel.fetch({"success": function(){that.readingSectionView.render();}});
            $("#next-question").bind("click", function(){
                    that.navigate(String(that.readingSectionView.getNextQuestionIdx()), true);
                    });
            $("#previous-question").bind("click", function(){
                    that.navigate(String(that.readingSectionView.getPreviousQuestionIdx()), true);
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
            this.readingSectionView.showQuestion(parseInt(questionId));
		}
	})

	var app = new ReadingPageApp();
    console.log( "start result is " + 
	Backbone.history.start({
        root: "/" + app.testId + "/reading/" + app.sectionId + "/"
	}));


	console.log('Main inilized.');
	return ReadingPageApp;
});

