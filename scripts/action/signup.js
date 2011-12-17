define(function(require, exports, module) {
    var $ = require('../lib/jquery');
	exports.init = function() {
    	$(document).ready(function(){
			errorify = function(input, data) {
    				input.css("background-image", "url(/static/images/error.png)");
    				var err_msg = '#' + input.attr('err-msg');
    				if (!err_msg) { return; }
    				$(err_msg).text(data);
				$(err_msg).show('fast');   				
    			};
    			unErrorify = function(input) {
    				input.css("background-image", "none");
    				var err_msg = '#' + input.attr('err-msg');
    				if (!err_msg) { return; }
				$(err_msg).hide('fast');
    			};
    			goodify = function(input) {
    				unErrorify(input);
    				input.css("background-image", "url(/static/images/success.png)");
    			};
    			$('input').css('background-repeat', 'no-repeat');
    			$('input').css('background-position', 'right'); 
    			$('input').blur(function(){
    				var url = $(this).attr('check-url');
    				var err_msg = '#' + $(this).attr('err-msg');
    				if (!url) return;
    				$(this).css("background-image", "url(/static/images/indicator.gif)");  
    				var input = $(this);
    				$.post(url, {value:$(this).val()}, function(data){
    					if (data == 'good'){
    						goodify(input);
    					} else {
    						errorify(input, data);
    					}
    				});
    			});
    			$('input').click(function(){
    				unErrorify($(this));
    			});
    			$('#confirm').blur(function(){
    				if ($(this).val() && $(this).val() != $('#password').val()) {
    					errorify($(this), 'Password not equal!');
    				}
    			})
	});
	};
});
