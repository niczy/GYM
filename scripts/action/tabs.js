define(function(require, exports, module) {
    var $ = require('../libs/jquery')
    $("#main-tabs > li > a").mouseover(function() {
    		if ($(this).hasClass('selected')) {
    			return;
    		}
    		$(this).addClass('hover');
    }).mouseout(function(){
        $(this).removeClass("hover");
    });;
});
