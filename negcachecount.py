import time
import sys
import os
import warnings

def NXDOMAIN_defense(count):
	if count > 10:
		return 1
	return 0

while True:
	time.sleep(0.25)
	os.system('rndc dumpdb -all')
	filename = "/var/cache/bind/named_dump.db"
	fr = open(filename, "r")
	count = 0

	for line in fr:
		for word in line.split():
			if "NXDOMAIN" in word:
				count += 1
	print "Number of records on the NXDOMAIN cache: ",count
	fr.close()
	c = NXDOMAIN_defense(count)
	print c
