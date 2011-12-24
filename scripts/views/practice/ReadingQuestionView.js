define(function(require, exports) {
	var $ = require('../../libs/jquery');
	var Backbone = require('../../libs/backbone');
	var ReadingQuestionView = Backbone.View.extend({
		el: '.practice_section, .question',
        currentQuestionIdx: 0,
		render: function() {
            var readingQuestionModel = this.model.at(this.currentQuestionIdx);
            if (!readingQuestionModel) {
                return;
            }
            console.log("ReqdingQuestionView render called" + readingQuestionModel.get("description"));
		//	$(this.el).text(this.model.get("description"));
            var View = new Backbone.View;
            var description = View.make('p', {class: "description"}, readingQuestionModel.get('description'));
            $(this.el).empty();
            $(this.el).append(description);
            var options = View.make('ol', {class: 'options'});
            var _ = require('../../libs/underscore');
            _.each(readingQuestionModel.get("options"), function(op) {
                $(options).append(View.make('li', {class: 'option'}, op));
            });
            $(this.el).append(options);
			return this;
		}
	});
	return ReadingQuestionView;
});
	
