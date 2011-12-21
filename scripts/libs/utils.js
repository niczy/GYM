define(function(require, exports, module) {
	exports.BuildUrl = function(base, params) {
	    var res = base;
	    var first = true;
	    for (var key in params) {
		   if (first) {
			   res += "?";
			   first = false;
		   } else {
			   res += "&";
		   }
		   res += key + '=' + params[key];
	    }
	    return res;
	};
});
