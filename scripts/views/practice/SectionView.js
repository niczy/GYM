define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');
	var SectionView = Backbone.View.extend({
		initialize: function() {
			this.type = this.options.type;
			this.sectionid = this.options.sectionid;
			if (this.type == 'reading') {
				var ReadingSectionModel = require('../../models/practice/ReadingSectionModel');
				var ReadingSectionView = require('./ReadingSectionView');
				this.sectionModel = new ReadingSectionModel({
					sectionid: this.sectionid
				});
				this.sectionView = new ReadingSectionView({
					model: this.sectionModel
				});
			} else if (this.type == 'listening') {
				var ListeningSectionModel = require('../../models/practice/ListeningSectionModel');
				var ListeningSectionView = reuqire('./ListeningSectionView');
				this.sectionModel = new ListeningSectionModel({
					sectionid: this.sectionid
				});
				this.sectionView = new ListeningSectionView({
					model: this.sectionModel
				});
			} else if (this.type == 'speaking') {
				var SpeakingSectionModel = require('../../models/practice/SpeakingSectionModel');
				var SpeakingSectionView = reuqire('./SpeakingSectionView');
				this.sectionModel = new SpeakngSectionModel({
					sectionid: this.sectionid
				});
				this.sectionView = new SpeakingSectionView({
					model: this.sectionModel
				});
			} else if (this.type == 'writing') {
				var WritingSectionMolde = require('../../models/practice/WritingSectionModel');
				var WritingSectionView = reuqire('./WritingSectionView');
				this.sectionModel = new WritingSectionMolde({
					sectionid: this.sectionid
				});
				this.sectionView = new WritingSectionView({
					model: this.sectionModel
				});
			}
		},

		getNextQuestionIdx: function() {
			return this.sectionView.getNextQuestionIdx();
		},

		getPreviousQuestionIdx: function() {
			return this.sectionView.getPreviousQuestionIdx();
		},

		showQuestion: function(questionIdx) {
			this.sectionView.showQuestion(questionIdx);

		},

		render: function() {
			var that = this;
			this.sectionModel.fetch({
				"success": function() {
					that.sectionView.render();
				}
			});
		}
	});
	return SectionView;
});

