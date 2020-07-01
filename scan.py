#-----------------------------------------------------------------------------#
# library imports
#-----------------------------------------------------------------------------#

import os
from time import gmtime, strftime





#-----------------------------------------------------------------------------#
# constants
#-----------------------------------------------------------------------------#

SCAN_PATH = "scanReports/"

TIME_STAMP = strftime("%Y-%m-%d_%H:%M:%S", gmtime())

CURRENT_SCAN_PATH = SCAN_PATH+"SCAN_"+TIME_STAMP





#-----------------------------------------------------------------------------#
# getting device's list
#-----------------------------------------------------------------------------#

# device scan (saved in a file)
os.system("sudo nmap -sn 192.168.0.0/24 > hosts.txt")


# reading the file
file = None
file_content = ""

try:
    file = open('hosts.txt', 'r')
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
for i,ip in enumerate(hostsIP):
    if hostsName[i] != "Unknown":
        os.system("echo '\n\n---"+hostsName[i]+"' >> tmp_scan_results.txt")
    else:
        os.system("echo '\n\n---UNKNOWN' >> tmp_scan_results.txt")
    os.system("sudo nmap -F "+ip+" >> tmp_scan_results.txt")

os.system("echo '\n\n\t\t-----END SCAN RESULTS-----' >> tmp_scan_results.txt")





#-----------------------------------------------------------------------------#
# writing results
#-----------------------------------------------------------------------------#

# create folders

if not os.path.isdir(SCAN_PATH):
    os.system("mkdir "+SCAN_PATH)

os.system("mkdir "+CURRENT_SCAN_PATH)