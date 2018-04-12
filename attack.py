import random
import time
import commands
import sys
import os
import warnings
import string

count = 1000
while count>0:
	domain =  ''.join(random.choice('abcdefghijklmono') for _ in range(6))
	ans =  ''.join(random.choice('pqrstuvwxyzabcdef') for _ in range(6))
	tld =  ''.join(random.choice('abcdefuvwxyzpqrst') for _ in range(6))
	full = domain +'.'+ ans+'.' + tld
	os.system('dig ' +full)
	count = count -1
