import xlwt
import commands
import warnings
import subprocess
import os
import time
import sys

book = xlwt.Workbook()
sh = book.add_sheet("RR's Cache")

col1_name = 'Query Time in ms'
col2_name = 'Difference Time(End - Start) in ms'

sh.write(0, 0, col1_name)
sh.write(0, 1, col2_name)

for i in range(0,10):
	time.sleep(0.25)
	print ("Iteration: " + str(i))
	
	os.system("dig ex1.ans1.tld1")
	os.system("/etc/init.d/dnsmasq restart")


	start = time.time()
	output = commands.getoutput("dig ex1.ans1.tld1")
	difftim = (((time.time() - start) * 1000))

	list_of_words = output.split(' ')
	Query_time = int(list_of_words[list_of_words.index("time:") + 1])

	sh.write(i+1, 0, Query_time)
	sh.write(i+1, 1, difftim)

	print("Query time " + str(Query_time) + " ms")
	print("Difference time " + str(difftim) + " ms\n")

book.save("path6.xls")
