#-----------------------------------------------------------------------------#
# library imports
#-----------------------------------------------------------------------------#

import os
from time import localtime, strftime





#-----------------------------------------------------------------------------#
# constants
#-----------------------------------------------------------------------------#

SCAN_PATH = "scanReports/"

TIME_STAMP = strftime("%Y-%m-%d_%H:%M:%S", localtime())

CURRENT_SCAN_PATH = SCAN_PATH+"MAX_SCAN_"+TIME_STAMP+"/"





#-----------------------------------------------------------------------------#
# getting device's list
#-----------------------------------------------------------------------------#

# device scan (saved in a file)
os.system("sudo nmap -sn 192.168.0.0/24 > hosts.txt")


# reading the file
file = None
file_content = ""

try:
    file = open("hosts.txt", "r")
    file_content = file.read()
    file_content = file_content.split("\n")
    for line in file_content:
        if line == "":
            file_content.remove(line)
    file_content = "\n".join(file_content)

finally:
    if file is not None:
       file.close()


#making an ip list
hostsIP = []
hostsName = []

for i,line in enumerate(file_content.split("\n")):
    
    if i%3 == 1 and i != len(file_content.split("\n"))-1 and line.split()[-1][0] != "(":

        hostsIP.append(line.split()[-1])

        try :
            if file_content.split("\n")[i+2].split()[0] == "MAC":
                hostsName.append(file_content.split("\n")[i+2].split("(")[-1].split(")")[0])
            else:
                hostsName.append("Unknown")
        except:
            hostsName.append("Unknown")


# removing hosts.txt file
os.system("rm hosts.txt")





#-----------------------------------------------------------------------------#
# port scan
#-----------------------------------------------------------------------------#

#fast scan
    # creating file
os.system("echo '\t\t-----SCAN RESULTS-----' > tmp_scan_results.txt")

    # scanning
results = []
for ip in hostsIP:

    os.system("sudo nmap -A -T4 -p- "+ip+" > tmp_scan_results.txt")
    file = None
    try:
        file = open("tmp_scan_results.txt","r")
        results.append(file.read())
    finally:
        if file is not None:
            file.close()

os.system("rm tmp_scan_results.txt")







#-----------------------------------------------------------------------------#
# writing results
#-----------------------------------------------------------------------------#

# create folders

if not os.path.isdir(SCAN_PATH):
    os.system("mkdir "+SCAN_PATH)

os.system("mkdir "+CURRENT_SCAN_PATH)


# writing scan summary

file = None
try:
    file = open(CURRENT_SCAN_PATH+"summary.txt","w")
    file.write("\t\t----- SCAN RESULT SUMMARY -----\n\n\n")
    file.write("Complete scan : Scans every port with os and service detection (nmap -A -T4 -p-)\n\n")
    file.write("Scan performed at :"+TIME_STAMP.replace("_"," ")+"\n\n")
    file.write(str(len(hostsIP))+" hosts detected :\n")
    for i in range(len(hostsIP)):
        file.write("\t+ "+hostsIP[i]+" : "+hostsName[i]+"\n")
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