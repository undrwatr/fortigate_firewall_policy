#!/usr/bin/env python3

#2-24-2022 initial program creation to login to the firewalls and pull back the firewall policy and put it into a CSV.
#2-25-2022 Updated program and then fixed some comments.

from netmiko import ConnectHandler
import cred

#log into each of the firewalls in the devices.txt and pull down the config and then pull out the specific information and put into a csv file.

fw_config = open("fw.txt", "w")
with open ("devices.txt", "r") as file:
    for device_name in file:
        device = {
            "device_type": "fortinet",
            "host": device_name,
            "username": cred.rancid_username,
            "password": cred.rancid_password,
            "secret" : cred.rancid_password
        }

        net_connect = ConnectHandler(**device)
        net_connect.enable()

        cmd = "show firewall policy"
        output = net_connect.send_command(cmd)
        output1 = output.strip()
        fw_config.write(output1)
fw_config.close()

#Open the config we just downloaded and then iterate through to pull out the necessary information.
config = open("fw.txt", "r")
fw_csv = open(device_name + ".csv", "w")

#build out the column headings
fw_csv.write('name,src interface, dest interface, src add, dest add, service,' + '\n')

for line in config:
    if "set name" in line:
        line = line.lstrip(' ')
        line = line.lstrip('set name')
        line = line.strip('\n')
        fw_csv.write(line + ',')
    elif "set srcintf" in line:
        line = line.lstrip(' ')
        line = line.lstrip('set srcintf')
        line = line.strip('\n')
        fw_csv.write(line + ',')
    elif "set dstintf" in line:
        line = line.lstrip(' ')
        line = line.lstrip('set dstintf')
        line = line.strip('\n')
        fw_csv.write(line + ',')
    elif "set srcaddr" in line:
        line = line.lstrip(' ')
        line = line.lstrip('set srcaddr')
        line = line.strip('\n')
        fw_csv.write(line + ',')
    elif "set dstaddr" in line:
        line = line.lstrip(' ')
        line = line.lstrip('set dstaddr')
        line = line.strip('\n')
        fw_csv.write(line + ',')
    elif "set service" in line:
        line = line.lstrip(' ')
        line = line.lstrip('set service')
        line = line.strip('\n')
        fw_csv.write(line + ',' + '\n')
    else:
        continue

config.close()
fw_csv.close()