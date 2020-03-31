import csv
import os 
import numpy
from pathlib import Path, PureWindowsPath
from git_clone import git_clone
from datetime import date

def download_data():
	if os.path.isdir('COVID-19'):
		print("yes")
		answer  = input("update?")
		while answer == 'Y':
			os.system('rmdir /Q /s COVID-19')
			git_clone('https://github.com/CSSEGISandData/COVID-19.git')
			answer = 'N'
	else:
		print("Downloading Covid-19 data...")
		git_clone('https://github.com/CSSEGISandData/COVID-19.git')


download_data()

file_list = []

rootDir = '.'
print('csse_covid_19_daily_reports:')

for dirName, subdirList, fileList in os.walk(rootDir):
	if(dirName == '.\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports'):
		for fname in fileList:
			file_list.append(fname)
			

file_list.pop()
file_list.pop(0)
default_choice = len(file_list) - 1

for i, v in enumerate(file_list):
	print(i, v)

choice = int(input("Which day would you like to see stats for?(leave blank to see most recent day)"))
print(file_list[choice])
file = str(file_list[choice])


filename = ('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/' + file)

confirmed = 0
deaths = 0
recovered = 0
active = 0

f = open(filename, 'r') 
with f:
	reader = csv.DictReader(f)
	for row in reader:
		#All available rows
		#print(row['FIPS'], row['Admin2'], row['Province_State'], row['Country_Region'], row['Last_Update'], row['Lat'], row['Long_'], row['Confirmed'], row['Deaths'], row['Recovered'], row['Active'], row['Combined_Key'])
		#print(row['Province_State'],  row['Country_Region'], "Confirmed:", row['Confirmed'],"Deaths:", row['Deaths'], "Recovered:", row['Recovered'],"Active:", row['Active'])
		confirmed += int(row['Confirmed'])
		deaths += int(row['Deaths'])
		recovered += int(row['Recovered'])
		#active += int(row['Active'])

def print_stats():
	confirmed_string = str(confirmed)
	print("Confirmed: ", confirmed_string[0:3]+ ',' + confirmed_string[3:6] )
	print("Total Deaths: ", deaths)
	print("Total Recovered: ", recovered)
	#print("Total Active: ", active)

print_stats()