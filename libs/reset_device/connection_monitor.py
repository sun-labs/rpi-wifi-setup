import time
import sys
import os
import reset_lib

WAITFORCONNECTION = 30 #Time after boot that the system will check for wifi connection before turning in to AP.
no_conn_counter = 0
consecutive_active_reports = 0
config_hash = reset_lib.config_file_hash()


# If auto_config is set to 0 in /etc/raspiwifi/raspiwifi.conf exit this script
if config_hash['auto_config'] == "0":
    while True:
        time.sleep(5)

        if reset_lib.is_wifi_active() == False:
            no_conn_counter += 5
            consecutive_active_reports = 0
        # If iwconfig report association with an AP add 1 to the
        # consecutive_active_reports counter and 10 to the no_conn_counter
        else:
            consecutive_active_reports += 1
            no_conn_counter += 5
            # Since wpa_supplicant seems to breifly associate with an AP for
            # 6-8 seconds to check the network key the below will reset the
            # will exit the program only if thre 5 second checks have come up active.
            if consecutive_active_reports >= 3:
                sys.exit()

        # If the number of seconds not associated with an AP is greater or
        # equal to the auto_config_delay specified in the /etc/raspiwifi/raspiwifi.conf
        # trigger a reset into AP Host (Configuration) mode.
        if no_conn_counter <= WAITFORCONNECTION:
            reset_lib.reset_to_host_mode()
            sys.exit()


else:
    # Main connection monitoring loop at 10 second interval
    while True:
        time.sleep(10)

        # If iwconfig report no association with an AP add 10 to the "No
        # Connection Couter"
        if reset_lib.is_wifi_active() == False:
            no_conn_counter += 10
            consecutive_active_reports = 0
        # If iwconfig report association with an AP add 1 to the
        # consecutive_active_reports counter and 10 to the no_conn_counter
        else:
            consecutive_active_reports += 1
            no_conn_counter += 10
            # Since wpa_supplicant seems to breifly associate with an AP for
            # 6-8 seconds to check the network key the below will reset the
            # no_conn_counter to 0 only if two 10 second checks have come up active.
            if consecutive_active_reports >= 2:
                no_conn_counter = 0
                consecutive_active_reports = 0

        # If the number of seconds not associated with an AP is greater or
        # equal to the auto_config_delay specified in the /etc/raspiwifi/raspiwifi.conf
        # trigger a reset into AP Host (Configuration) mode.
        if no_conn_counter >= int(config_hash['auto_config_delay']):
            reset_lib.reset_to_host_mode()
