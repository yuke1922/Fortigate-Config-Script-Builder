import csv
import os

os.system('clear')
os.system('rm -rf ./vip_script.txt')

input_file = "VIP.csv"
outputfile = "vip_script.txt"
string = ""
output_block = ""
string_start = "config firewall vip\n"
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        string_extintf = ""
        ext_port = ""
        int_port = ""
        vip_name = row['Name']
        string_name = "edit " + '"' + vip_name + '"\n'
        if not row['extintf'] == "any":
            ext_intf = row['extintf']
            string_extintf = "set extintf " + ext_intf + "\n"
        if row['extintf'] == "any":
            ext_intf = "any"
            string_extintf = "set extintf any\n"
        ext_ip = row['extip']
        int_ip = row['mappedip']
        string_ipaddr = "set extip " + ext_ip + "\nset mappedip " + int_ip + "\n"
        if row['portforward'] == "enable":
            ext_port = row['extport']
            int_port = row['mappedport']
        if row['portforward'] == "enable":
            string_ports = "set portforward enable\nset extport " + str(ext_port) + "\nset mappedport " + str(int_port) + "\nnext\nend\n"
        

        output_block += string_start + string_name + string_ipaddr + string_extintf + string_ports

outfile = open(outputfile, 'w')
outfile.write(output_block)
outfile.close()