define(function(require, exports, module) {
	exports.sayHello = function() {
	    alert("Hello from module : " + module.id);
	};
});
