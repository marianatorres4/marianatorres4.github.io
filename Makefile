# Usage:
# make install	# install required gems
# make update	# upgrade outdated gems
# make serve	# build site and start local server
# make talkmap	# build talkmap (org-locations.js)

.PHONY: all install update serve talkmap

all: serve

serve: install talkmap
	bundle exec jekyll liveserve --config "_config.yml,_config.dev.yml"

update:
	bundle update

install: 
	bundle install

talkmap: talkmap.py
	# remove old org-locations.js first, otherwise changed entries just get appended
	rm -rf talkmap/org-locations.js
	
	# create new org-locations.js
	python talkmap.py
	
	# restore customized version of some files
	cp -rf talkmap/restore/* talkmap/
