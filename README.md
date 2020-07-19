# Raspberry-Pi-based-portable-port-scanner
This device allows you to perform a port scan of every device available on a network you are connected to (Ethernet or WIFI)



Presentation
-
I don't think to have a real use of this, since I am not performing *on-site pentesting*, but it still felt like a good idea. I wanted to work on a project hardware related (like using a Raspberry), InfoSec related and with some programming (not only uploading a script on the micro-computer). This seems to check every condition so far. Let's see where it get's me ;-)

**DISCLAIMER :** The number of targets might change from a scan to another on the same network. It's a nmap related issue. Some hosts are not always detected by the preliminary scan, that lists the available hosts.



Features
-
* Different levels of agressivity (faster : simple results, slower : complexe results)
  * *Fast* : Performs a basic scan on the 100 most common ports for each device (```nmap -F```)
  * *Slow* : Performs an advanced scan, by scanning every port for each device, and by using os and service detection (```nmap -A -T4 -p-```)
* Working on battery
* Storing the result in a clean way, to be analysed later on a computer
* Data visualisation in 2 ways :
  * *raw* : the data is visualized in it's standard format, and accessed via SSH
  * *on a web interface* : when powerd on, the device runs a local server, which hosts the web interface, diplaying the results


LEDs
-
There a are two LEDs to indicate status. Here are the different states :
* **Stady green light** : Device is powered on, ready to scan
* **Blinking green light** : Device is scanning
* **Stady red light** (for 2s) : Device shuting down or rebooting
* **Stady green light and blinking red light** : scan reports are deleted



Installation
-
Not there yet ;-)



Usage
-
There are three buttons, with each a primary functionality, and a secondary functionality.
* **Button 1** : 
  * *Simple press* : system shutdown (once the red LED is off, you can turn of the powersource)
  * *3s press* : system reboot (don't remove the powersource, and wait for the green LED to turn back on)
* **Button 2** :
  * *Simple press* : fast scan
  * *3s press* : identifying the approximate number of targets on the network (displays it)
* **Button 3** :
  * *Simple press* : complete scan
  * *3s press* : Deleting all scan reports stored on the devices memory



Doing it yourself
-
Evey necessary file to make this project yourself are available in the ```Ressources``` folder. A detailed tutorial is will be available on my website here : *LINK UNAVAILABLE YET*



Note to myself
-
**Next steps :**
* Adding a 7 segment display to display the number of hosts left to scan
* Adding a functionality to juste get the approximative number of targets on the network
* make it work on battery
* Working on a web interface to visualize the results