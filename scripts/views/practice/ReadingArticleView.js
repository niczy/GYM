define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
    var $ = require('../../libs/jquery');
	var ReadingArticleView = Backbone.View.extend({
		el: '.practice_section, .article',
        render: function() {
            var View = new Backbone.View;
            var _ = require('../../libs/underscore');
            console.log($(this.el));
            var that = this;
            _.each(this.model.get('paragraphs'), function(paragraph){
                    $(that.el).append(View.make('p', {classname: "paragraph"}, paragraph));
                    console.log($(that.el));
                }
                );
            return this;
        }
	})
	return ReadingArticleView;
})

