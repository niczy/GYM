define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var PracticeItemModel = Backbone.Model.extend({
		practiceid: "1",
		title: "READING1",
		viewer: 15623,
		uploader: "Zero",
		uploadTime: "2011-12-03",
		uploaderPortrait: "/asd/asd",
		rating: 3.8,
		status: "done"
	});
	return PracticeItemModel;
});

