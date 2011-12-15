$(document).ready(function(){
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
				//alert('Good!');
				input.css("background-image", "url(/static/images/success.png)");
			} else {
				input.css("background-image", "url(/static/images/error.png)");
				$(err_msg).text(data);
				$(err_msg).show('fast');
			}
		});
	});
	$('input').click(function(){
		var err_msg = '#' + $(this).attr('err-msg');
		if (!err_msg) return;
		$(err_msg).hide('fast');
	});
	$('#confirm').blur(function(){
		if ($(this).val() && $(this).val() != $('#password').val()) {
			$('#confirm_err_msg').show('fast');
		}
	})
});