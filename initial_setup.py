import os
import sys
import setup_lib


if os.getuid():
    sys.exit('You need root access to install!')


os.system('clear')
print()
print()
print("###################################")
print("##### RaspiWiFi Intial Setup  #####")
print("###################################")
print()
print()
entered_ssid = "SL screen"
wpa_enabled_choice = "N"
wpa_entered_key = "coolscreen"
auto_config_choice = "Y"
auto_config_delay = "60"
server_port_choice = "80"
ssl_enabled_choice = "N"
print()
print()

setup_lib.install_prereqs()
setup_lib.copy_configs(wpa_enabled_choice)
setup_lib.update_main_config_file(entered_ssid, auto_config_choice, auto_config_delay, ssl_enabled_choice, server_port_choice, wpa_enabled_choice, wpa_entered_key)
os.system('reboot')
