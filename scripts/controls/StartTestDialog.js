define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var _ = require('../libs/underscore');
    var $ = require('../libs/jquery');


	var StartTestDialog = Backbone.View.extend({
		params: {},
		checkPrice: function() {
			$('#test-status').hide();
			if (this.params.price <= 0) {
				this.startTest();
			} else {
				$('#price').show();
				if (this.params.price > this.params.credit) {
					$('#buy').show();
					$('#label-buy').show();
					$('#start').hide();
					$('#label-start').hide();
				} else {
					$('#buy').hide();
					$('#label-buy').hide();
					$('#start').show();
					$('#label-start').show();
				}
			}
		},
		startTest: function() {
			console.log('StartTest: ' + this.params.testid);
			window.location = "/starttest/" + this.params.testid;
		},
		reviewTest: function() {
			console.log('ReviewTest: ' + this.params.testid);
			window.location = "/reviewtest/" + this.params.testid;
		},
		render: function(params) {
			console.log('ControlBar.Render');
		    var Templates = require('../templates/site/HomePageTemplates');
		    var compiled = Templates.startTestDialog;
		    var theView = this;
		    theView.params = params;
		    $(this.el).html(compiled({
		    		price : params.price,
		    		test_title : params.test_title,
		    		credit: params.credit,
		    		test_date : params.test_date
		    }));
		    
		    $('#cancel').click(function(){
		    		$(theView.el).hide();
		    });
		    
		    if (params.test_status == 'done') {
	    			$('#price').hide();
	    			$('#retry').click(function(){
	    				theView.checkPrice();
	    			});
	    			$('#review').click(function(){
	    				theView.reviewTest();
	    			});
		    }
		    
		    if (params.test_status == 'new') {
		    		$('#test-status').hide();
		    		this.checkPrice();
		    }
		    
		    $('#start').click(function() {
		    		theView.startTest();
		    });
		    $('#buy').click(function() {
	    			window.location = '/buycredit';
		    });
		    $(this.el).show();
			return this;
		},
		initialize: function(options) {
			console.log('StartTestDialog.Init');
				
		    return this;
		}
	});
    return StartTestDialog;
});

