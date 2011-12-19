define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var ReadingSectionView = Backbone.View.extend({
		el: '#reading-section',
		render: function() {
			var ReadingTemplates = require("../../templates/practice/ReadingTemplates");
			var $ = require('../../libs/jquery');
            console.log("render called");
			if (this.model.has("article")) {
				console.log("render");
				$(this.el).text(ReadingTemplates.readingSectionTemplate(this.model.toJSON()));
			} else {
                console.log("no article");
            }
			return this;
		}
	});
	return ReadingSectionView;
});

