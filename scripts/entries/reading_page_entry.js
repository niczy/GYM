define(function(require, exports) {
        var ReadingQuestionView = require('../views/practice/ReadingQuestionView');
        var ReadingQuestionModel = require('../models/practice/ReadingQuestionModel');
        var readingQuestionView = new ReadingQuestionView(
            {
                model: new ReadingQuestionModel
            }
            );
        readingQuestionView.render();
        console.log('Main inilized.');
    }
);
