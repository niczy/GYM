define(function(require, exports) {
        var _ = require('../../libs/underscore');
        exports.startTestDialog =  _.template(
 '\
	<div class="dialog">\
	  <div class="title">\
        <h3>Starting Test: <%= test_title %></h3>\
      </div>\
	  <div class="content" id="test-status">\
        <div id="done">\
        	  <h3>You have done this test on <%= test_date %>.<br/>Try again or review?</h3>\
        	  <span id="retry" class="button">Retry</span>\
        	  <span id="review" class="button">Review</span>\
        	  <span id="cancel" class="button">Cancel</span>\
        	</div>\
      </div>\
      <div class="content" id="price">\
        	<h4>This will cost <b><%= price %></b> credits</h4>\
        	<label id="label-start">Are you sure to start?</label>\
        	<label id="label-buy">Buy credit now?</label>\
        	<h4>Your credits: <%= credit %></h4>\
        	<span id="start" class="button">Start</span>\
        <span id="buy" class="button">Buy credit</span>\
        	<span id="cancel" class="button">Cancel</span>\
      </div>\
	</div>\
	');
});
