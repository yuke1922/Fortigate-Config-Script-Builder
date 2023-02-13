import csv
import os

os.system('clear')
os.system('rm -rf ./IPPool_script.txt')

input_file = "IPpool.csv"
outputfile = "IPPool_script.txt"
string = ""
output_block = ""
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        start_ip = row['startip']
        end_ip = row['endip']
        name = row['Name']
        string_start = 'config firewall ippool\nedit "' + name + '"\nset startip ' + start_ip + '\nset endip ' + end_ip + '\nnext\nend\n'

string +=string_start

outfile = open(outputfile, 'w')
outfile.write(string)
outfile.close()