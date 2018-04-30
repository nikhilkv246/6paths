import commands                                                                                                     
import warnings                                                                                                     
import subprocess                                                                                                   
import os                                                                                                           
import time                                                                                                         
import sys                                                                                                          
                                                                                                                    
for i in range(0,10):                                                                                               
        print ("Iteration: " + str(i))                                                                              
        HOST="172.20.3.6"                                                                                           
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
        output = commands.getoutput("dig ex1.ans1.tld1")  
