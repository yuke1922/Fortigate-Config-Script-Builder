import csv
import os

os.system('clear')
os.system('rm -rf ./script.txt')

input_file = "IPV4_Addresses.csv"
outputfile = "script.txt"
string = ""
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Type'] == "subnet":
            name = str(row['Name'])
            address = str(row['Network'])
            current_string = "config firewall address\nedit " + name + "\nset subnet " + address + "\nnext\nend\n"
            string += current_string
        if row['Type'] == "geography":
            name = str(row['Name'])
            country = str(row['country'])
            current_string = "config firewall address\nedit " + name + "\nset type geography\nset country " + country + "\nnext\nend\n"
            string += current_string
        if row['Type'] == "fqdn":
            name = str(row['Name'])
            value = str(row['FQDN'])
            current_string = "config firewall address\nedit " + name + "\nset type fqdn\nset fqdn " + value + "\nnext\nend\n"
            string += current_string
        if row['Type'] == "iprange":
            name = str(row['Name'])
            value1 = str(row['Start-IP'])
            value2 = str(row['End-IP'])
            current_string = "config firewall address\n edit " + name + "\nset type iprange\nset start-ip " + value1 + "\nset end-ip " + value2 + "\nnext\nend\n"
            string += current_string


outfile = open(outputfile, 'w')
outfile.write(string)
outfile.close()