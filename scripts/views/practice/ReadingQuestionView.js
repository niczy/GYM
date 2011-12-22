define(function(require, exports) {
	var $ = require('../../libs/jquery');
	var Backbone = require('../../libs/backbone');
	var ReadingQuestionView = Backbone.View.extend({
		el: '.practice_section, .question',
		render: function() {
            console.log("ReqdingQuestionView render called" + this.model.get("description"));
		//	$(this.el).text(this.model.get("description"));
            var View = new Backbone.View;
            var description = View.make('p', {classname: "description"}, this.model.get('description'));
            $(this.el).append(description);
            var options = View.make('ol', {classname: 'options'});
            var _ = require('../../libs/underscore');
            _.each(this.model.get("options"), function(op) {
                $(options).append(View.make('li', {classname: 'option'}, op));
            });
            $(this.el).append(options);
			return this;
		}
	});
	return ReadingQuestionView;
});
	
