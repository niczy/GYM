define(function(require, exports) {
	var Backbone = require('../../libs/backbone');
	var _ = require('../../libs/underscore');
	var $ = require('../../libs/jquery');
	var CreateSectionView = Backbone.View.extend({

		el: '#create_section',

		events: {
			"click #submit_section": "submitSection"

		},

		submitSection : function() {
            console.log($('#section_data').val());
            console.log('submit test called.');
            $.post('/api/createsection', {'section': $('#section_data').val()}, function(data) {
                        console.log('return data is ' + data.result); 
                    });

        },

		render: function() {
			var Templates = require('../../templates/site/UploadPageTemplates');
			$(this.el).html(Templates.createSectionTemplate());
		}
	});
	return CreateSectionView;
});

