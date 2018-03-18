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

os.system('cd '+toolpath+'/results/'+domain)
if not first_time :
	os.system('rm '+toolpath+'/results/'+domain+'/urls.txt')

os.system('./javascript_files_extractor.py '+all_domains+' ./temp/js_files.txt')
os.system('./javascript_files_link_extractor.sh ./temp/js_files.txt ./temp/urls.txt ./dependency/relative-url-extractor/extract.rb')
os.system('cp ./temp/urls.txt '+toolpath+'/results/'+domain)

if not first_time:
	os.system('git diff HEAD^ HEAD')


os.system('git add . && git commit -m \"'+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")+domain+'\"')