import time
import sys
import os
import warnings


def NXDOMAIN_defense(rate):
	if rate > 40:
		return 1
	return 0

def calculate_NXDOMAIN_count():
	os.system('rndc dumpdb -all')
	filename = "/var/cache/bind/named_dump.db"
	fr = open(filename, "r")
	count = 0

	for line in fr:
		for word in line.split():
			if "NXDOMAIN" in word:
				count += 1
	fr.close()
	return count

while True:
	time.sleep(2)

	count1 = calculate_NXDOMAIN_count()
	#print "Number of records on the NXDOMAIN cache Count1 : ",count1
	#res = NXDOMAIN_defense(count1)
	#print "Returned value: ",res

	time.sleep(0.5)
	
	count2 = calculate_NXDOMAIN_count()
	#print "Number of records on the NXDOMAIN cache Count2 : ",count2
	
	rate = (count2-count1)/0.5
	result = NXDOMAIN_defense(rate)
	print "Rate of NXDOMAIN records (per second): ",rate
	print "Return value: ", result
	#print "Difference ",(count2 - count1)
	#print "Rate of NXDOMAIN records per second: ",rate

	
	
