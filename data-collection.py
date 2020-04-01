import csv
import os 
import numpy
import platform
from pathlib import Path, PureWindowsPath
from git_clone import git_clone

def download_data():
	if os.path.isdir('COVID-19'):
		print("Covid-19 data Exists!")
		answer  = input("update?")
		while answer == 'Y':
			os.system('rmdir /Q /s COVID-19')
			git_clone('https://github.com/CSSEGISandData/COVID-19.git')
			answer = 'N'
	else:
		print("data doesn't exist")
		print("cloning Repo")
		print("Downloading Covid-19 data...")
		git_clone('https://github.com/CSSEGISandData/COVID-19.git')

def get_file_list():
	file_list = []
	unix_path = './COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'
	path_on_windows = '.\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports'
	rootDir = '.'
	print('csse_covid_19_daily_reports:')

	for dirName, subdirList, fileList in os.walk(rootDir):
		#print(dirName)
		if(platform.system() == 'Linux' or platform.system() == 'Darwin'):
			if(dirName == unix_path):
				for fname in fileList:
					#print("\t%s" % fname)
					file_list.append(fname)		
		elif platform.system() == 'Windows':
			#print(dirName)
			if(dirName == path_on_windows):
				for fname in fileList:
					#print("\t%s" % fname)
					file_list.append(fname)
		else:
			print("os not recognized")

	file_list.pop()
	file_list.pop(0)
	return file_list


def get_csv(file_list):
	choice = input("Which day would you like to see stats for?(leave blank to see most recent day)")
	choice = int(choice)
	print(file_list[choice])
	file = str(file_list[choice])
	return file

def print_stats(confirmed,deaths, recovered):
	confirmed_string = str(confirmed)
	print("Confirmed: ", confirmed_string)
	print("Total Deaths: ", deaths)
	print("Total Recovered: ", recovered)
	#print("Total Active: ", active)
	
def list_covid_dir(file_list):
	for i, v in enumerate(file_list):
		print(i, v)

def main():
	download_data()
	file_list = get_file_list()
	list_covid_dir(file_list)
	filename = ('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/' + get_csv(file_list))

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
	print_stats(confirmed,deaths,recovered)

if __name__ == "__main__":
    main()
