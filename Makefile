# Usage:
# make install	# install required gems
# make update	# upgrade outdated gems
# make serve	# build site and start local server

.PHONY: all install update serve

all: serve

serve: install
	bundle exec jekyll liveserve --config "_config.yml,_config.dev.yml"

update:
	bundle update

install: 
	bundle install