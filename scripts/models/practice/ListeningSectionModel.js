define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var Utils = require('../../libs/utils');
	var ListeningQuestionCollection = Backbone.Collection.extend({
		model: Backbone.Model.extend({
			question: "question",
			answer: "answer",
			user: "user",
			date: "2012-1-2"
		})
	});
	var FaqModel = Backbone.Model.extend({
		url: function() {
			return Utils.BuildUrl('/api/faqlist');
		},
		
		items: ItemCollection,
		onChange: function() {
			this.set({ items : new ItemCollection(this.get('items')) });
		},
		initialize: function() {
			this.bind('change', this.onChange);
		}
	});
	return FaqModel;
});

