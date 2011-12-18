define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var ReadingSectionView = Backbone.View.extend({
	el: '#reading-section', render: function() {
        var $ = require('../../libs/jquery');
		$(this.el).text(this.model.get('testid') + " " + this.model.get('sectionid'));
        return this;
	}});
    return ReadingSectionView;
});

