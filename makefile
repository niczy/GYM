dev:	
	if [ -d static/js ] ; then rm -r static/js ; fi
	mkdir static/js ;
	cp -r scripts/* static/js ;
	dev_appserver.py . ;

