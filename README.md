# Raspberry-Pi-based-portable-port-scanner
This allows to scan ports of devices on a network, by connecting to it via ethernet.



Presentation
-
I don't think to have a real use of this, since I am not performing *on-site pentesting*, but it still felt like a good idea. I wanted to work on a project hardware related (like using a Raspberry), InfoSec related and with some programming (not only uploading a script on the micro-computer). This seems to check every condition so far. Let's see where it get's me ;-)



Features
-
* Different levels of agressivity (faster : simple results, slower : complexe results)
  * *Fast* : Performs a basic scan on the 100 most common ports for each device (nmap -F)
  * *Medium* : *to explain*
  * *Slow* : Performs an advanced scan, by scanning every port for each device, and by using os and service detection (nmap -A -T4 -p-)
* Working on battery
* Storing the result in a clean way, to be analysed later on a computer
* *And more to come*



Installation
-
Not there yet ;-)



Usage
-
Not there yet ;-)



Doing it yourself
-
The detailed instructions and evey needed files to make this project yourself are available in the ```Ressources``` folder