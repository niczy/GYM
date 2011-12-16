dev:	
	if [ -d static/js ] ; then rm -r static/js ; fi
	mkdir static/js ;
	cp -r scripts/* static/js ;
	lessc stylesheets/gym.less > static/css/gym.css
	dev_appserver.py . ;

