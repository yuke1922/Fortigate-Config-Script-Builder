import csv
import os

os.system('clear')
os.system('rm -rf ./addr_group_script.txt')

input_file = "IPV4_AddressGRP.csv"
outputfile = "addr_group_script.txt"
string = ""
string_of_members = ""
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        current_string = ""
        string_of_members = ""
        name = str(row['Name'])
        address = row['member']
        address_list = address.split(",")
        for iterance in address_list:
            #print(type(iterance))
            string_of_members += '"' + iterance + '" '
        #Add quote to beginning of member string
        current_string = 'config firewall addrgrp\nedit "'+ name + '"\nset member ' + string_of_members + '\nnext\nend\n'
        string += current_string

outfile = open(outputfile, 'w')
outfile.write(string)
outfile.close()