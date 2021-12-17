#!/usr/bin/env python

# # Leaflet cluster map of talk locations
# 
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
# 
# Run this from the _talks/ directory, which contains .md files of all your talks. This scrapes the location YAML field from each .md file, geolocates it with geopy/Nominatim, and uses the getorg library to output data, HTML, and Javascript for a standalone cluster map.
# 
# Requires: glob, getorg, geopy
#!pip install getorg python-frontmatter

#import os
import glob
import getorg
#import shutil
from geopy import Nominatim

g = glob.glob("_talks/*.md")

geocoder = Nominatim(user_agent="my-application1") # small hack, as `user_agent="my-application"` (default) returns an error
location_dict = {}
location = ""
permalink = ""
title = ""
venue = ""

count=0
for file in g:
    with open(file, 'r') as f:
        lines = f.read()
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
        if lines.find('title: "') > 1:
            loc_start = lines.find('title: "') + 8
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            title = lines_trim[:loc_end]
        if lines.find('venue: "') > 1:
            loc_start = lines.find('venue: "') + 8
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            venue = lines_trim[:loc_end]

        key = str(title + " | " + venue + ", " + location)

        if location.endswith("(online)"): # special case for online talks
            location = location.rstrip(" (online)")
        
        location_dict[key] = geocoder.geocode(location, timeout=60)
        
        print(key, "\n", location_dict[key], "\n")
    
    count += 1
print(count, "talks")

# remove old org-locations.js first, otherwise changed entries just get appended
#os.remove("talkmap/org-locations.js")

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap/", hashed_usernames=False)

# some files include manual changes but are overwitten by getorg, like map.html and leaflet_dist/screen.css
# thus a backup version is kept in restore/ and copied to replace the newly created ones
#print('copying files from restore/ directory')
#shutil.copytree("./talkmap/restore/","./talkmap/", dirs_exist_ok=True)