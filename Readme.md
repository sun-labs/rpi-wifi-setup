[![Analytics](https://ga-beacon.appspot.com/UA-19159071-9/rpi-wifi-setup)](https://github.com/igrigorik/ga-beacon)
[![Sun Labs](https://img.shields.io/badge/%20-Developed%20at%20Sun%20Labs-black?labelColor=ffe601&style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAGKSURBVHgB7Zi/SgNBEMZnxFpTC4J9BNPaWVpa2VrZi3kAkzc4a4maMjZJaWkndjaCnQHF1j8vsO6czQ63d3uXZGAS5oOB5Hbmu/vtLnPsoftEByugNVgRGYg2GYg2GYg2GYg2GYg2GYg2GYg2GYg2rTdJ/v718fN/oGxtIrQ2YKGaxz8JQuaXVw5u7wCm7+GIg04boLMLcHGOsLMNM2lh/nRmL4teF5yfFZe7JoJyq7yk/aMgX6/oDvbr3SAMP4N5bQpAwj8KcnRYbuaXOI+ycXrAFIiEP8SWO2ae9ZHNBv2+yTB606wPldtJwp+BvD0VC1PbhWooJ6yhfR+rkfRn75GHR8c6B3WK8XV1G4zlUCcajorf/ST9GchwxE163XptlXLOTvm1yX0xT9KfgTy/8MG9NtTWyTGy/9OPYo6kP4bffnGLL5cfgyZK1Uv6sxUJl3mWN3WqXtKfgYwHCL5P5zEZNJutOvWS/mxrLbPsPKJNBqJNBqJNBqJNBqJNBqJNBqJNBqJNBqJNf0F+WMETxwNrAAAAAElFTkSuQmCC)](https://sunlabs.se)

THIS REPO IS BASED ON https://github.com/jasbur/RaspiWiFi
All cred to @jasbur with RaspiWiFi

Just leave it in Configuration Mode, connect to the "SL screen [xxxx] Setup" access
point. The Pi will be addressable at 10.0.0.1 using all the normal methods you
might use while connected through a network.

SL screen has been tested with the Raspberry Pi 4 with Buster.

### SCRIPT-BASED INSTALLATION INSTRUCTIONS:

Navigate to the directory where you downloaded or cloned SL screen
Run:

`sudo python3 initial_setup.py`

This script will install all necessary prerequisites and copy all necessary
config and library files, then reboot. When it finishes booting it should
present itself in "Configuration Mode" as a WiFi access point with the
name "SL screen [xxxx]".

The original GIT directory that you ran the Initial Setup is no longer
needed after installation and can be safely deleted. All necessary files are
copied to ´/usr/lib/raspiwifi/´ on setup.


### CONFIGURATION:
<ul>
<li>"SSID Prefix" [default: "RaspiWiFi Setup"]: This is the prefix of the SSID
      that your Pi will broadcast for you to connect to during
      Configuration Mode (Host Mode). The last four of you Pi's serial number
      will be appended to whatever you enter here.</li>
<br/>
<li>"WPA Encryption" [default: No]: If oyu enable this setting the Access Point
      created during Configuration Mode will be encrypted using WPA2 encryption.
      The prompt following this one will let you specify the Wireless Key to be
      used. You can leave the password blank if you chose 'N' to this option.</li>
<br/>
<li>"Auto-Config mode" [default: n]: If you choose to enable this mode your Pi
      will check for an active connection while in normal operation mode (Client Mode).
      If an active connection has been determined to be lost, the Pi will reboot
      back into Configuration Mode (Host Mode) automatically.</li>
<br/>
<li>"Auto-Config delay" [default: 300 seconds]: This is the time in consecutive
      seconds to wait with an inactive connection before triggering a reset into
      Configuration Mode (Host Mode). This is only applicable if the
      "Auto-Config mode" mentioned above is set to active.</li>
<br/>
<li>"Server port" [default: 80]: This is the server port that the web server
      hosting the Configuration App page will be listening on. If you change
      this port make sure to add it to the end of the address when you're
      connecting to it. For example, if you speficiy 12345 as the port number
      you would navigate to the page like this: http://10.0.0.1:12345 If you
      leave the port at the default setting [80] there is no need to specify the
      port when navigating to the page.</li>
<br/>
<li>"SSL Mode" [default: n]: With this option enabled your RaspiWifi
      configuration page will be sent over an SSL encrypted connection (don't
      forget the "s" when navigating to https://10.0.0.1:9191 when using
      this mode). You will get a certificate error from your web browser when
      connecting. The error is just a warning that the certificate has not been
      verified by a third party but everything will be properly encrypted anyway.</li>
<br/>
<li>All of these variables can be set at any time after the Initial Setup has
been running by editing the /etc/raspiwifi/raspiwifi.conf</li>
<br/>
</ul>
      
### USAGE:

<ol>
<li>Connect to the "SL screen [xxxx]" access point using any other WiFi enabled
device.</li>

<li>A captive portal will open (tested on android, iOS and mac) 
Else  Navigate to [10.0.0.1], using any web browser on the device you
connected with. 
(don't forget to manually start with [https://] when using SSL mode)</li>

<li>Select the WiFi connection you'd like your Raspberry Pi to connect to from
the drop down list and enter its wireless password on the page provided. If no
encryption is enabled, leave the password box blank. You may also manually
specify your network information by clicking on the "manual SSID entry ->" link.</li>

<li>Click the "Connect" button.</li>

<li>At this point your Raspberry Pi will reboot and connect to the access point
specified.</li>

<li>You can also use the Pi in a point-to-point connection mode by leaving it in
Configuration Mode. All services will be addresible in their normal way at
10.0.0.1 while connected to the "SL screen [xxxx]" AP.</li>
</ol>

### ALT USAGE:
<ol>
<li>Connect an ethernet cable to the device when in AP mode, the device will reboot
      into client mode.</li> 
</ol>


### RESETTING THE DEVICE:
<ul>
 <li>If GPIO 15 is pulled HIGH for 5 seconds or more the Raspberry Pi will reset
all settings, reboot, and enter "Configuration Mode" again. It's useful to have
a simple button wired on GPIO 15 to reset easily if moving to a new location,
or if incorrect connection information is ever entered. Just press and hold for
10 seconds or longer. </li>

<li>Put a USB-drive to some of the USB-ports on the device, the USB must me named `SL_RESET`
and contain a file named `reset.me`. After the USB been plugged in for 5 secounds it can saftely
be disconnected and the reset will be followed by a reboot. </li>

<li>You can also reset the device by running the manual_reset.py in the
´/usr/lib/raspiwifi/reset_device´ directory as root or with sudo.</li>
</ul>

### UNINSTALLATION:

You can uninstall SL screen at any time by running:

   `sudo python3 /usr/lib/raspiwifi/uninstall.python3`

You can also run it from the `libs/` directory from a fresh clone if you've
installed from a previous version and don't have `/usr/lib/raspiwifi/uninstall.py`
available.
