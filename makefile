dev:	
	if [ -d static/js ] ; then rm -r static/js ; fi
	mkdir static/js ;
	cp -r scriptes/* static/js ;
	dev_appserver.py . ;

