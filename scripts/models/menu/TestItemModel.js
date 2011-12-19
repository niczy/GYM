define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var TestItemModel = Backbone.Model.extend({
		testid: "1",
		title: "TPO 1",
		viewer: "1421",
		uploader: "Zero"
	});
	return TestItemModel;
});

