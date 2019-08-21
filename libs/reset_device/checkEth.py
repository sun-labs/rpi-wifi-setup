#!/usr/bin/python3

import subprocess
import os
import time

def set_ap_client_mode():
  os.system('rm -f /etc/raspiwifi/host_mode')
  os.system('rm /etc/cron.raspiwifi/aphost_bootstrapper')
  os.system('cp /usr/lib/raspiwifi/reset_device/static_files/apclient_bootstrapper /etc/cron.raspiwifi/')
  os.system('chmod +x /etc/cron.raspiwifi/apclient_bootstrapper')
  os.system('mv /etc/dnsmasq.conf.original /etc/dnsmasq.conf')
  os.system('mv /etc/dhcpcd.conf.original /etc/dhcpcd.conf')
  os.system('reboot')


  if __name__ == "__main__":
    ifplugstatus_out_eth0 = subprocess.check_output(['ifplugstatus eth0']).decode('utf-8')

    if "eth0: unplugged" in ifplugstatus_out_eth0:
      set_ap_client_mode()
    else:
      exit()

