define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var UploadPageApp = Backbone.Router.extend({
		initialize: function() {
			var CreateTestView = require('../views/site/CreateTestView');
			this.createTestView = new CreateTestView();
			this.createTestView.render();

			var CreateSectionView = require('../views/site/CreateSectionView');
			this.createSectionView = new CreateSectionView();
			this.createSectionView.render();
		}
	});
	var app = new UploadPageApp();
	console.log('upload app initialized.');
	return UploadPageApp;
});

