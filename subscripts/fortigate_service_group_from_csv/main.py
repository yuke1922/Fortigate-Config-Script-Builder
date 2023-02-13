import csv
import os

os.system('clear')
os.system('rm -rf ./addr_group_script.txt')

input_file = "Services_Group.csv"
outputfile = "svc_group_script.txt"
string = ""
string_of_members = ""
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        current_string = ""
        string_of_members = ""
        name = str(row['Name'])
        service = row['member']
        service_list = service.split(",")
        for iterance in service_list:
            #print(type(iterance))
            string_of_members += iterance + " "
        current_string = 'config firewall service group\nedit "'+ name + '"\nset member ' + string_of_members + '\nnext\nend\n'
        string += current_string


outfile = open(outputfile, 'w')
outfile.write(string)
outfile.close()