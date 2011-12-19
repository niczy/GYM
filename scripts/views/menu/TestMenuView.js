define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var TestMenuView = Backbone.View.extend({
	el: '#test-menu', render: function() {
        var $ = require('../../libs/jquery');
		$(this.el).text(this.model.get('testnum') + " " + this.model.get('name'));
        return this;
	}});
    return TestMenuView;
});

