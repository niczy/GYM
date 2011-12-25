define(function(require, exports, module) {
    var $ = require('../libs/jquery');
	exports.init = function() {
    	$(document).ready(function(){
			errorify = function(input, data) {
    				//input.css("background-image", "url(/static/images/error.png)");
				input.attr('class', 'bad');

				var err_msg = '#' + input.attr('err-msg');
    				if (!err_msg) { return; }
    				$(err_msg).text(data);
				$(err_msg).show('fast');   				
    			};
    			unErrorify = function(input) {
    				input.attr('class', 'input none');
    				var err_msg = '#' + input.attr('err-msg');
    				if (!err_msg) { return; }
				$(err_msg).hide('fast');
    			};
    			goodify = function(input) {
    				unErrorify(input);
    				input.attr('class', 'input good');
    			};
    			$('input').blur(function(){
    				var url = $(this).attr('check-url');
    				var err_msg = '#' + $(this).attr('err-msg');
    				if (!url) return;
    				var input = $(this);
    				input.attr('class', 'input loading');
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
