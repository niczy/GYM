define(function(require, exports) {
        var _ = require('../../libs/underscore');
        exports.userHistoryItem = _.template(
        		'<div>\
      		  <h4><a href="/testdetail/<%= testid %>"><%= title %></a></h4>\
      		  <h3>Date: <%= date %>\
      		</div>');
});
