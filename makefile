dev:	
	if [ -d static/js ] ; then rm -r static/js ; fi
	mkdir static/js ;
	cp -r scripts/* static/js ;
	python stylesheets/merge-css.py > gym.less ;
	lessc gym.less > static/css/gym.css ;
	rm gym.less ;
	dev_appserver.py . ;

