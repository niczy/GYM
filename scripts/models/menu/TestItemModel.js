define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var TestItemModel = Backbone.Model.extend({
		testid: "1",
		title: "TPO 1",
		viewer: 1421,
		buyer: 12,
		uploader: "Zero",
		uploadTime: "2011-12-03",
		uploaderPortrait: "/asd/asd",
		rating: 3.8,
		price: 0,
		status: "done"
	});
	return TestItemModel;
});

