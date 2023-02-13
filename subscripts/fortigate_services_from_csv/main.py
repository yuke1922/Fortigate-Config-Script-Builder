import csv
import os

os.system('clear')
os.system('rm -rf ./services_script.txt')

input_file = "Services.csv"
outputfile = "services_script.txt"
string = ""
output_block = ""
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tcp_ports = ""
        udp_ports = ""
        current_string_2 = ""
        current_string_3 = ""
        if row['category'] == "":
            if not row['visibility'] == "disable":
                name = str(row['Name'])
                if not row['tcp-portrange'] == "":
                    tcp_ports = str(row['tcp-portrange'])
                    current_string_2 = "set tcp-portrange " + tcp_ports + "\n"
                if not row['udp-portrange'] == "":
                    udp_ports = str(row['udp-portrange'])
                    current_string_3 = "set udp-portrange " + udp_ports + "\n"
                current_string_1 = 'config firewall service custom\nedit "' + name + '"\n'
                current_string_final = "next\nend\n"

                current_block = current_string_1 + current_string_2 + current_string_3 + current_string_final
                output_block += current_block

outfile = open(outputfile, 'w')
outfile.write(output_block)
outfile.close()