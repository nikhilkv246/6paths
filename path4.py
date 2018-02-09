import xlwt
import commands
import warnings
import subprocess
import os
import time
import sys

book = xlwt.Workbook()
sh = book.add_sheet("ANS Path")

col1_name = 'Query Time in ms'
col2_name = 'Difference Time(End - Start) in ms'

sh.write(0, 0, col1_name)
sh.write(0, 1, col2_name)

for i in range(0,10):
	time.sleep(0.25)
	print ("Iteration: " + str(i))
	HOST="172.20.2.6"
	COMMAND="/etc/init.d/bind9 restart"

	ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	                       shell=False,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)
	result = ssh.stdout.readlines()
	if result == []:
	    error = ssh.stderr.readlines()	
	    print >>sys.stderr, "ERROR: %s" % error
	else:
	     print result
	
	os.system("/etc/init.d/dnsmasq restart")
	os.system("dig ex1.ans1.tld1")


	start = time.time()
	output = commands.getoutput("dig ex2.ans1.tld1")
	difftim = (((time.time() - start) * 1000))

	list_of_words = output.split(' ')
	Query_time = int(list_of_words[list_of_words.index("time:") + 1])

	sh.write(i+1, 0, Query_time)
	sh.write(i+1, 1, difftim)

	print("Query time " + str(Query_time) + " ms")
	print("Difference time " + str(difftim) + " ms\n")

book.save("path4.xls")
