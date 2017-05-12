__author__ = 'Jozef Tenus'	# v. 20.10.2016 11:29AM
import csv
import sys
import datetime
import codecs
import tkinter as tk
from tkinter import filedialog

timestart = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

myrange_start = 1
myrange_stop = 150
main_list = []
list1 = []


root = tk.Tk()
root.withdraw()
fname = filedialog.askopenfilename()
save_name = fname.replace('.csv', '')

with codecs.open(fname, 'r', encoding="latin-1") as csvfile:
	file_to_split = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in file_to_split:
		main_list.append(row)

for i in range(14):
	for i in range(myrange_start, myrange_stop):
		list1.append(main_list[i])

		save_name = fname.replace('.csv', '')

		with codecs.open(save_name + '_' + str(myrange_start) + '-' + str(myrange_stop) + '.csv', 'w', encoding="Latin-1") as outfile:
			writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			first_row = ['Email']
			writer.writerow(first_row)
			for i in list1:
				writer.writerow(i)

	list1 = []
	myrange_start += 150
	myrange_stop += 150


	# timestopdone = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
	
	# with codecs.open(fname + '_done_' + str(timestopdone) + '.csv', 'w', encoding="Latin-1") as EMfile:
	# 	writer = csv.writer(EMfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	# 	emailslistGG_fr = ['Primary Key', 'First Name', 'Surname', 'Company', 'Email']
	# 	writer.writerow(emailslistGG_fr)
		
	# 	for i in emailslistGG:
	# 		writer.writerow(i)
			
	# timestop = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	# # print('Emails created: ' + str(emailcntr) + ' (' + str(round((emailcntr/cntrpercent), 2)*100) + '%) in ' + str(timestop-timestart))
	# print('Emails created: ' + str(emailcntr) + ' (' + str(round((emailcntr/cntrpercent), 2)*100) + '%)')
