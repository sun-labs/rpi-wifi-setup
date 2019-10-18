import RPi.GPIO as GPIO
import os
import time
import subprocess
import reset_lib
import os.path
from rpi_lib import getserial

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


counter = 0
serial = getserial().decode('utf-8')
serial_last_four = serial[-4:]
config_hash = reset_lib.config_file_hash()
ssid_prefix = config_hash['ssid_prefix'] + " "
reboot_required = False


reboot_required = reset_lib.wpa_check_activate(config_hash['wpa_enabled'], config_hash['wpa_key'])

reboot_required = reset_lib.update_ssid(ssid_prefix, serial_last_four)

if reboot_required == True:
    os.system('reboot')

# This is the main logic loop waiting for a button to be pressed on GPIO 18 for 10 seconds.
# If that happens the device will reset to its AP Host mode allowing for reconfiguration on a new network.
while True:
    while GPIO.input(15) == 1:
        time.sleep(1)
        counter = counter + 1

        print(counter)

        if counter <= 5:
            reset_lib.reset_to_host_mode()

        if GPIO.input(18) == 0:
            counter = 0
            break
    if (os.path.isfile('/media/pi/SL_RESET/reset.me')):
        reset_lib.reset_to_host_mode()

    time.sleep(1)
