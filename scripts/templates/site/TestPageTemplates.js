define(function(require, exports) {
        var _ = require('../../libs/underscore');
        exports.testHistoryItem =  _.template(
        		'<div>\
      		  <h3>Username: <a target="_blank" href="/userinfo/<%= user %>"><%= user %></a></h3>\
      		  <br/>\
      		  <h3>Used on: <%= date %></h3>\
      		</div>');
});
