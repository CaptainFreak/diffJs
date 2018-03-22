#!/usr/bin/python
import datetime
from sys import argv
import os


domain=argv[1]
all_domains=argv[2]
toolpath=os.getcwd()
first_time= False
if(not os.path.exists(toolpath+'/results/'+domain)):
	os.makedirs(toolpath+'/results/'+domain)
	first_time= True

if not first_time :
	os.system('rm '+toolpath+'/results/'+domain+'/urls.txt')

os.system('./javascript_files_extractor.py '+all_domains+' ./temp/js_files.txt')
os.system('./javascript_files_link_extractor.sh ./temp/js_files.txt ./results/'+domain+'/urls.txt ./dependency/relative-url-extractor/extract.rb')

if not first_time:
	os.system('./sendmail.sh')


os.system('git add . && git commit -m \"'+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")+domain+'\"')