import os

def install_prereqs():
	os.system('clear')
	os.system('apt update')
	os.system('clear')
	print("Installing Python and dnsmasq...")
	print()
	os.system('apt install python3 python3-rpi.gpio python3-pip dnsmasq apache2 hostapd -y')
	os.system('apt install macchanger -n')
	os.system('clear')
	print("Installing Flask web server...")
	print()
	os.system('pip3 install flask pyopenssl')
	os.system('clear')

def copy_configs(wpa_enabled_choice):
	os.system('mkdir /usr/lib/raspiwifi')
	os.system('mkdir /etc/raspiwifi')
	os.system('cp -a libs/* /usr/lib/raspiwifi/')
	os.system('mv /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.original')
	os.system('rm -f ./tmp/*')
	os.system('mv /etc/dnsmasq.conf /etc/dnsmasq.conf.original')
	os.system('cp /usr/lib/raspiwifi/reset_device/static_files/dnsmasq.conf /etc/')

	if wpa_enabled_choice.lower() == "y":
		os.system('cp /usr/lib/raspiwifi/reset_device/static_files/hostapd.conf.wpa /etc/hostapd/hostapd.conf')
	else:
		os.system('cp /usr/lib/raspiwifi/reset_device/static_files/hostapd.conf.nowpa /etc/hostapd/hostapd.conf')

	os.system('mv /etc/dhcpcd.conf /etc/dhcpcd.conf.original')
	os.system('cp /usr/lib/raspiwifi/reset_device/static_files/dhcpcd.conf /etc/')
	os.system('mkdir /etc/cron.raspiwifi')
	os.system('cp /usr/lib/raspiwifi/reset_device/static_files/aphost_bootstrapper /etc/cron.raspiwifi')
	os.system('chmod +x /etc/cron.raspiwifi/aphost_bootstrapper')
	os.system('echo "# RaspiWiFi Startup" >> /etc/crontab')
	os.system('echo "@reboot root run-parts /etc/cron.raspiwifi/" >> /etc/crontab')
	os.system('sudo sed -i "/exit 0/i \sudo dhclient wlan0" /etc/rc.local') # Adding dhclient every boot, is needed for OS buster
	os.system('mv /usr/lib/raspiwifi/reset_device/static_files/raspiwifi.conf /etc/raspiwifi')
	os.system('touch /etc/raspiwifi/host_mode')
	os.system('chown -R www-data:www-data /var/www/html')
	os.system('cp /home/pi/rpi-wifi-setup/libs/configuration_app/.htaccess /var/www/html/')
	os.system('chown root:www-data /var/www/html/.htaccess')
	os.system('cp -f /home/pi/rpi-wifi-setup/libs/configuration_app/override.conf /etc/apache2/conf-available/')
	os.system('cd /etc/apache2/conf-enabled')
	# os.system('ln -s ../conf-available/override.conf /etc/apache2/conf-enabledoverride.conf')
	# os.system('cd /etc/apache2/mods-enabled')
	# os.system('ln -s ../mods-available/rewrite.load rewrite.load')
	# os.system('cp -f /home/pi/rpi-wifi-setup/libs/configuration_app/app.conf /etc/apache2/sites-available/')
	# os.system('cd /etc/apache2/sites-available/')
	os.system('ln -s /home/pi/rpi-wifi-setup/libs/configuration_app/override.conf /etc/apache2/conf-enabled/override.conf')
	os.system('ln -s /home/pi/rpi-wifi-setup/libs/configuration_app/rewrite.load /etc/apache2/mods-available/rewrite.load')
	os.system('cp -f /home/pi/rpi-wifi-setup/libs/configuration_app/app.conf /etc/apache2/sites-available/')
	os.system('sudo a2ensite app.conf')


def update_main_config_file(entered_ssid, auto_config_choice, auto_config_delay, ssl_enabled_choice, server_port_choice, wpa_enabled_choice, wpa_entered_key):
	if entered_ssid != "":
		os.system('sed -i \'s/RaspiWiFi Setup/' + entered_ssid + '/\' /etc/raspiwifi/raspiwifi.conf')
	if wpa_enabled_choice.lower() == "y":
		os.system('sed -i \'s/wpa_enabled=0/wpa_enabled=1/\' /etc/raspiwifi/raspiwifi.conf')
		os.system('sed -i \'s/wpa_key=0/wpa_key=' + wpa_entered_key + '/\' /etc/raspiwifi/raspiwifi.conf')
	if auto_config_choice.lower() == "y":
		os.system('sed -i \'s/auto_config=0/auto_config=1/\' /etc/raspiwifi/raspiwifi.conf')
	if auto_config_delay != "":
		os.system('sed -i \'s/auto_config_delay=300/auto_config_delay=' + auto_config_delay + '/\' /etc/raspiwifi/raspiwifi.conf')
	if ssl_enabled_choice.lower() == "y":
		os.system('sed -i \'s/ssl_enabled=0/ssl_enabled=1/\' /etc/raspiwifi/raspiwifi.conf')
	if server_port_choice != "":
		os.system('sed -i \'s/server_port=80/server_port=' + server_port_choice + '/\' /etc/raspiwifi/raspiwifi.conf')
