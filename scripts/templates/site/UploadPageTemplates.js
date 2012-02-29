define(function(require, exports) {
        var _ = require('../../libs/underscore');
        exports.createTestTemplate =  _.template(
            '<div> Create the test </div> <textarea id="test_data" rows = "10"> </textarea><div id="submit_test">submit</div>');
        exports.createSectionTemplate = _.template('<div> Create the Section </div> <textarea id="section_data" rows = "10"> </textarea><div id="submit_section">submit</div>');
});
