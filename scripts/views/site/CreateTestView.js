define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');
	var $ = require('../../libs/jquery');
	var CreateTestView = Backbone.View.extend({

		el: '#create_test',

		events: {
			"click #submit_test": "submitTest"

		},

		submitTest: function() {
            console.log($('#test_xml').val());
            console.log('submit test called.');
            $.post('/api/createtest', {'test': $('#test_xml').val()}, function(data) {
                        console.log('return data is ' + data.result); 
                    });

        },

		render: function() {
			var Templates = require('../../templates/site/UploadPageTemplates');
			$(this.el).html(Templates.createTestTemplate());
		}
	});
	return CreateTestView;
});

