define(function(require, exports, module) {
    var $ = require('../lib/jquery')
	exports.sayHello = function() {
	    alert("Hello from module : " + module.id);
	};
});
