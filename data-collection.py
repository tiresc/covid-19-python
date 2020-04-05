import csv
import os 
import numpy
import platform
from pathlib import Path, PureWindowsPath
from git_clone import git_clone
file_list = [0]

multiple_datasets = False

def options():
	list = ['See specific day', 'compare two days']
	for x in range(0, len(list)):
		print('%d. %s'% (x,list[x]))

	choice = input("What would you like to do?")
	if choice == '0' :
		multiple_datasets = False
		return multiple_datasets
	elif choice == '1':
		multiple_datasets = True
		return multiple_datasets
	else:
		multiple_datasets = False
		return multiple_datasets

def get_file_list():
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

class DATA:
	def __init__(self):
		self.file_list = file_list
		self.covid_file = 0
		self.confirmed = 0
		self.deaths = 0
		self.recovered = 0
		self.active = 0
		self.file = ' '

	def get_csv(self):
		self.covid_file = input("Which day would you like to see stats for?(leave blank to see most recent day)")
		self.covid_file = int(self.covid_file)
		print(self.covid_file)
		#if self.covid_file <= 0 or self.covid_file >= len(self.file_list)-1:
		#	alt_file = str(self.file_list[0])
		#	return alt_file
		#else:
		self.file = str(self.file_list[self.covid_file])
		return self.file

	def print_stats(self):
		filename = ('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/' + self.get_csv())
		f = open(filename, 'r') 
		with f:
			reader = csv.DictReader(f)
			for row in reader:
				#All available rows
				#print(row['FIPS'], row['Admin2'], row['Province_State'], row['Country_Region'], row['Last_Update'], row['Lat'], row['Long_'], row['Confirmed'], row['Deaths'], row['Recovered'], row['Active'], row['Combined_Key'])
				#print(row['Province_State'],  row['Country_Region'], "Confirmed:", row['Confirmed'],"Deaths:", row['Deaths'], "Recovered:", row['Recovered'],"Active:", row['Active'])
				self.confirmed += int(row['Confirmed'])
				self.deaths += int(row['Deaths'])
				self.recovered += int(row['Recovered'])
		print("Confirmed: ", self.confirmed)
		print("Total Deaths: ", self.deaths)
		print("Total Recovered: ", self.recovered)

def download_data():
	if os.path.isdir('COVID-19'):
		print("Covid-19 data Exists!")
		answer  = input("update?")
		while answer.upper() == 'Y':
			os.system('rmdir /Q /s COVID-19')
			git_clone('https://github.com/CSSEGISandData/COVID-19.git')
			answer = 'N'
	else:
		print("data doesn't exist")
		print("cloning Repo")
		print("Downloading Covid-19 data...")
		git_clone('https://github.com/CSSEGISandData/COVID-19.git')



def list_covid_dir(file_list):
	# List covid directory w/ numbered associated with their order 
	for i, v in enumerate(file_list):
		print(i, v)

def compare( d_one, d_two):
	if int(d_one.covid_file) > int(d_two.covid_file) :
		confirmed_result = d_one.confirmed - d_two.confirmed
		deaths_result = d_one.deaths - d_two.deaths
		recovered_result = d_one.recovered - d_two.recovered
	else:
		confirmed_result = d_two.confirmed - d_one.confirmed
		deaths_result = d_two.deaths - d_one.deaths
		recovered_result = d_two.recovered - d_one.recovered
	print(' ')
	print('Difference in Deaths: %d' % deaths_result)
	print('Difference in Confirmed: %d' % confirmed_result)
	print('Difference in Recovered: %d' % recovered_result)


def based_on_datasets(data_sets):
	if data_sets == False:
		d_one = DATA()
		download_data()
		d_one.file_list = get_file_list()
		list_covid_dir(d_one.file_list)
		d_one.print_stats()
	elif data_sets == True:
		d_one = DATA()
		d_two = DATA()
		download_data()
		d_one.file_list = get_file_list()
		list_covid_dir(d_two.file_list)
		list_covid_dir(d_one.file_list)
		d_two.print_stats()
		d_one.print_stats()
		compare(d_one, d_two)
	else:
		d_one = DATA()
		download_data()
		d_one.file_list = get_file_list()
		list_covid_dir(d_one.file_list)
		d_one.print_stats()

def main():
	answer = options()
	based_on_datasets(answer)
	

if __name__ == "__main__":
    main()
