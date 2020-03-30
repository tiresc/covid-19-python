#pip pycurl
import csv
import os 
import time
import subprocess
from pathlib import Path, PureWindowsPath
from git_clone import git_clone
from datetime import date

today = date.today()

# dd/mm/YY
month = 0
day = 0
year = 0
month = int(today.strftime("%m"))
day = int(today.strftime("%d"))
year = '2020'
print("d1 =", month, day)


#stats = dict( Deaths=0, Recovered=0, Active=0 )
rootDir = '.'
'''for dirName, subdirList, fileList,  in os.walk(rootDir):
	print('%s' %dirName)
	for fname in fileList:
		print('\t%s' % fname)
		if(fname == 'COVID-19'):
			cloned = True'''


#if os.path.isdir('COVID-19'):
#	print("yes")
#	os.system('rmdir /Q /s COVID-19')
#	os.system('echo git clone https://github.com/CSSEGISandData/COVID-19.git')	
#else:

#os.system('echo git clone https://github.com/CSSEGISandData/COVID-19.git')

if os.path.isdir('COVID-19'):
	print("yes")
	os.system('rmdir /Q /s COVID-19')
	git_clone('https://github.com/CSSEGISandData/COVID-19.git')
else:
	print("no")
	git_clone('https://github.com/CSSEGISandData/COVID-19.git')




file = '0' + str(month) + '-' + str(day-1) + '-' + str(year) + '.csv'
filename = ('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/' + file)

# Convert path to Windows format
confirmed = 0
deaths = 0
recovered = 0
active = 0

f = open(filename, 'r') 

with f:
	reader = csv.DictReader(f)
	for row in reader:
		#print(row['FIPS'], row['Admin2'], row['Province_State'], row['Country_Region'], row['Last_Update'], row['Lat'], row['Long_'], row['Confirmed'], row['Deaths'], row['Recovered'], row['Active'], row['Combined_Key'])
		print(row['Province_State'],  row['Country_Region'], "Confirmed:", row['Confirmed'],"Deaths:", row['Deaths'], "Recovered:", row['Recovered'],"Active:", row['Active'])
		confirmed += int(row['Confirmed'])
		deaths += int(row['Deaths'])
		recovered += int(row['Recovered'])
		active += int(row['Active'])
confirmed_string = str(confirmed)
print("Confirmed: ", confirmed_string[0:3]+ ',' + confirmed_string[3:6] )
print("Total Deaths: ", deaths)
print("Total Recovered: ", recovered)
print("Total Active: ", active)
