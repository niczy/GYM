dev : 
	if [ -e js ] ; then	rm -r js ; fi ;
	ln -s ../scripts/ js ;
	mv js static/js ; 
	python stylesheets/merge-css.py > gym.less ;
	lessc gym.less > static/css/gym.css ;
	rm gym.less ;
	dev_appserver.py . ;

test:
	nosetests --with-gae --without-sandbox

