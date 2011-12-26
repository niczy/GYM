define(function(require, exports) {
	var Backbone = require('../libs/backbone');
	var _ = require('../libs/underscore');
    var $ = require('../libs/jquery');


	var MenuControlBar = Backbone.View.extend({
		orderEnabled: false,
		reverseEnabled: false,
		reversed: false,
		paged: false,
		orderSelector: '#menu-order-selector',
		reverseButton: '#menu-reverse-button',
		render: function() {
			console.log('ControlBar.Render');
		    
		    var compiled = _.template(
		    		'<label>Order By:(controls)</label>\
		    		<select id="menu-order-selector">\
		    		</select>\
		    		<button id="menu-reverse-button">Reverse</button>');
		   
		    $(this.el).html(compiled);

		    for (var i = 0; i < this.options.length; ++i) {
		    	 	$(this.orderSelector).append(
		    	 			'<option value=' + this.options[i].key + '>'
		    	 			+ this.options[i].value + '</option>');
		    }
		
			//$(this.el).text("Title: " + this.model.get('title'));
			
		
			var theBar = this;
			$(this.reverseButton).click(function() {
				console.log('ControlBar.ReverseBtn.Click');
				theBar.reversed = !theBar.reversed;
				theBar.SortMenuBy(theBar.GetSortField());
			});

			$(this.orderSelector).change(function () {
				console.log('ControlBar.Selector.Change');
				theBar.SortMenuBy(theBar.GetSortField());
	        }).trigger('change');
			
			return this;
		},
		initialize: function(options) {
			console.log('ControlBar.Init');
			this.options = options.options;
			if (options.getModel) {
				this.getModel = options.getModel;
			}
			this.render();
			
		    return this;
		},
		GetSortField: function() {
			var select = $(this.orderSelector);
	        var str = "";
	        $("select option:selected").each(function () {
	              str = $(this).attr('value');
	        });
	        return str;
		},
		SortMenuBy: function(field) {
            console.log("Sort By: " + field);
            var that = this;
            var model = this.model || this.getModel();
            model.get('items').comparator = function(item) {
        	      if (!that.reversed) {
        	    	      return item.get(field);
        	      } else {
        	    	      return -item.get(field);
        	      }
            };
            model.get('items').sort();
			console.log('ControlBar: items: ' + JSON.stringify(model.get('items')));

            model.change();      
		}
	});
    return MenuControlBar;
});

