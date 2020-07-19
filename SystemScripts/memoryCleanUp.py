import os

try:
    print('trying...')
    os.system("rm -rf /home/pi/scanReports")
except:
    pass