#!/usr/bin/python
#
# search script for the blender bug tracker
# brought to you by #blendercoders guibou, litilu & lmg
#
# CHANGES
# 2010_08_31:
#	added proper handling of wrong login/password
#	better windows support (tempdir + default colors off)
# 2010_09_03:
#	added flag for displaying the bug category
#	added flag for displaying the link to bug details

from __future__ import print_function
import os
import sys
import platform
import getpass
import math
from datetime import datetime
import re
import csv
import optparse
import io
import tempfile


###### SETTINGS ######
#
LOCALCSV = tempfile.gettempdir() + "/blender_bugtracker_report.csv" 	# local CSV copy
CACHETIME = 900 	# max age of local copy in seconds, 900 = 15min
USECOLORS = True	# Linux only, use console colorcodes to highlight search results

URLLOGIN = "https://projects.blender.org/account/login.php"
URLCSV = "https://projects.blender.org/tracker/?func=downloadcsv&group_id=9&atid=498"
URLDETAIL = "https://projects.blender.org/tracker/index.php?func=detail&group_id=9&atid=498&aid="


USERNAME = ''	# set to skip prompt
PASSWORD = ''	# set to skip prompt

## use this to avoid saving the username and password in the code file, 

#from config import USERNAME, PASSWORD

## 'config.py' is a file with only:
#USERNAME='foo'
#PASSWORD='bar'

#
###################


try:
	import html.parser
except:
	# python 2
	import htmllib as html
	oldparser = html.HTMLParser
	class HTMLParser(html.HTMLParser):
		def __init__(self):
			oldparser.__init__(self, None)

		def unescape(self, s):
			self.save_bgn()
			self.feed(s)
			return self.save_end()

	html.parser = html
	html.parser.HTMLParser = HTMLParser

try:
	import urllib.request
	import urllib.parse
except ImportError:
	import urllib
	import urllib2

	urllib.request = urllib2
	urllib.parse = urllib

def decode_htmlentities(string):
	p = html.parser.HTMLParser()
	return p.unescape(string)

## cache handling
def file_age_seconds(filename):
	stat = os.stat(filename)
	fileage = datetime.fromtimestamp(stat.st_mtime)
	now = datetime.now()
	delta = now - fileage
	return delta.seconds

def cache_is_recent():
	if os.path.isfile(LOCALCSV) :
		return file_age_seconds(LOCALCSV) < CACHETIME
	return False

def get_csv_file(url_login, url_csv, username, password):
	o = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
	urllib.request.install_opener(o)

	print("logging in...")
	p = urllib.parse.urlencode( { 'form_loginname': username, 'form_pw': password, 'login': 'Login with SSL', 'return_to': '' } )
	f = o.open(url_login,  p)
	f.close()

	print("downloading tracker report...")
	f = o.open( url_csv )
	if f.headers['Content-Type'] != 'text/comma-separated-values':
		return None
	content = f.read().decode('utf8')
	f.close()
	return content

if __name__ == '__main__':
	parser = optparse.OptionParser(
		usage='usage: %prog [options] search string',
		description='Search Blender Bug Tracker'
	)
	parser.add_option(
		'-u','--unassigned', action='store_true', 
		dest='unassigned', help='show only unassigned bugs'
	)
	parser.add_option(
		'-c','--categories', action='store_true', 
		dest='cats', help='show bug category'
	)
	parser.add_option(
		'-l','--link', action='store_true', 
		dest='links', help='show link to bug details'
	)
	options, filter_args = parser.parse_args()
	unassigned_only = options.unassigned
	show_cats = options.cats
	show_links = options.links

	# check if our local copy is recent, if not:
	# login and download the latest CSV from bugtracker
	if not cache_is_recent() :
		print("local copy too old -> fetching a recent one..")
		
		# are USERNAME / PASSWORD provided? if not, prompt for any missing
		if USERNAME == '' :
			USERNAME = raw_input('Username: ')
		if PASSWORD == '' :
			PASSWORD = getpass.getpass('Password: ')
			
		data = get_csv_file(URLLOGIN, URLCSV, USERNAME, PASSWORD)
		if data:
			with io.open(LOCALCSV, 'w', encoding='utf8') as f:
				f.write(data)
		else:
			sys.exit("Wrong login/password")
	
	# create a proper searchstring
	searchString = '|'.join(filter_args)
	search_re = re.compile('('+searchString+')', re.IGNORECASE)

	# parse csv and look for our searchstring
	reportReader = csv.reader(open(LOCALCSV, 'r'))
	for row in reportReader:
		if unassigned_only and row[7] != "Nobody" :
			continue
		
		summary = " "+ decode_htmlentities(row[11])
		assignee = " -> "+ decode_htmlentities(row[7])
		category = " " + decode_htmlentities(row[13]) if show_cats else ""
		link = " \t"+ URLDETAIL + row[0] if show_links else ""
		
		if search_re.search(summary) :
			# highlight the searchstring?
			if USECOLORS and platform.system() == 'Linux':
				summary = search_re.sub( "\033[1;33m\g<1>\033[1;m", summary )
				assignee = "\033[1;30m" +assignee +"\033[1;m"
				category = "\033[1;30m" + category + "\033[1;m"
				link = "\033[0;36m" + link + "\033[1;m"
			print("#"+ row[0] + category + summary + assignee + link)

