#-----------------------------------------------------------------------------#
# library imports
#-----------------------------------------------------------------------------#

import os
from time import localtime, strftime
import ipcalc




print("[+] Starting script\n") # remove on raspberry implementation

#-----------------------------------------------------------------------------#
# constants
#-----------------------------------------------------------------------------#

SCAN_PATH = "../scanReports/"

TIME_STAMP = strftime("%Y-%m-%d_%H:%M:%S", localtime())

CURRENT_SCAN_PATH = SCAN_PATH+"FAST_SCAN_"+TIME_STAMP+"/"

localIP = os.popen("sudo ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*  netmask ([0-9]*\.){3}[0-9]*' | grep -v '127.0.0\.*' | grep -Eo '([0-9]*\.){3}[0-9]*'").read().split("\n")
NETWORK = str(ipcalc.IP(localIP[0], mask=localIP[1]).guess_network())





#-----------------------------------------------------------------------------#
# getting device's list
#-----------------------------------------------------------------------------#

# device scan
print("[+] Starting network scan\n") # remove on raspberry implementation

hosts_scan = os.popen("sudo nmap -sn "+NETWORK).read()

hosts_scan = hosts_scan.split("\n")
for line in hosts_scan:
    if line == "":
        hosts_scan.remove(line)
hosts_scan = "\n".join(hosts_scan)


#making an ip list
hostsIP = []
hostsName = []

for i,line in enumerate(hosts_scan.split("\n")):
    
    if i%3 == 1 and i != len(hosts_scan.split("\n"))-1 and line.split()[-1][0] != "(":

        hostsIP.append(line.split()[-1])

        try :
            if hosts_scan.split("\n")[i+2].split()[0] == "MAC":
                hostsName.append(hosts_scan.split("\n")[i+2].split("(")[-1].split(")")[0])
            else:
                hostsName.append("Unknown")
        except:
            hostsName.append("Unknown")





#-----------------------------------------------------------------------------#
# port scan
#-----------------------------------------------------------------------------#

#fast scan
print("[+] Starting hosts scan") # remove on raspberry implementation

results = []
for ip in hostsIP:
    print("\t"+str(len(hostsIP)-len(results))+" hosts left") # to replace with a screen display information on the raspberry
    results.append(os.popen("sudo nmap -F "+ip).read())







#-----------------------------------------------------------------------------#
# writing results
#-----------------------------------------------------------------------------#
print("\n[+] Writing results\n") # remove on raspberry implementation

# create folders

if not os.path.isdir(SCAN_PATH):
    os.system("mkdir "+SCAN_PATH)

os.system("mkdir "+CURRENT_SCAN_PATH)


# writing scan summary

file = None
try:
    file = open(CURRENT_SCAN_PATH+"summary.txt","w")
    file.write("\t\t----- SCAN RESULT SUMMARY -----\n\n\n")
    file.write("Fast scan : Scans for the 100 most common ports for each detected device (nmap -F)\n\n")
    file.write("Scan performed at :"+TIME_STAMP.replace("_"," ")+"\n\n")
    file.write(str(len(hostsIP))+" hosts detected :\n")
    for i in range(len(hostsIP)):
        file.write("\t+ "+hostsIP[i]+"\t: "+hostsName[i]+"\n")
    file.write("\n\n\t\t----- END SCAN REPORT -----")

finally:
    if file is not None:
       file.close()


# writting scan report for each host
unknown = 1
for i in range (len(hostsIP)):
    
    if hostsName[i] == "Unknown":
            name = "Unknown_"+str(unknown)
            unknown += 1
    else:
        name = hostsName[i]
    file = None
    try:
        file = open(CURRENT_SCAN_PATH+name,"w")
        file.write(results[i])
    finally:
        if file is not None:
            file.close()


print("[+] Script successfully terminated") # remove on raspberry implementation