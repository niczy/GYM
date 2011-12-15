define(function(require, exports, module) {
    var $ = require('../lib/jquery')
    console.log($);
    $('body').innerHTML = 'Test jquery'
	exports.sayHello = function() {
	    alert("Hello from module : " + module.id);
	};
});
