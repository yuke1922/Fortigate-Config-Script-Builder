import os


#Enable Debug
debug = "False"

#Cleanup from previous
os.system("rm -rf ./output/")
os.system("mkdir output")

#Set up environment
source_folder = "./sources/"
output_folder = "./output/"
subscript_folder = "./subscripts/"
starting_dir = os.getcwd()
working_folder = "./work_area/"


#Source file Prep
source_file_list = os.listdir(source_folder)
if debug == "True":
    print(source_file_list)
for filename in source_file_list:
    current_file_to_clean = source_folder + filename
    #Remove first three lines in each source file to create legitimate CSV file
    for n in range(1,4):
        with open(current_file_to_clean, 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[1:])

#Scriptlet Prep Area - move appropriate files into working folders
##Starting with IPv4 Address Objects
os.system("cp " + source_folder + "IPV4_Addresses.csv " + subscript_folder + "fortigate_address_objects_from_csv/")
## Service Objects
os.system("cp " + source_folder + "Services.csv " + subscript_folder + "fortigate_services_from_csv/")
## Address Group Objects
os.system("cp " + source_folder + "IPV4_AddressGRP.csv " + subscript_folder + "fortigate_address_group_from_csv/")
## Service Group Objects
os.system("cp " + source_folder + "Services_Group.csv " + subscript_folder + "fortigate_service_group_from_csv/")
## IP Pool Objects
os.system("cp " + source_folder + "IPpool.csv " + subscript_folder + "fortigate_ippool_from_csv/")
## VIP Objects
os.system("cp " + source_folder + "VIP.csv " + subscript_folder + "fortigate_vip_from_csv/")

#Scriptlet Execution area
## IPv4 Address Objects
os.system("cd " + subscript_folder + "\ncd fortigate_address_objects_from_csv\npython3 main.py\n")
## Service Objects
os.system("cd " + subscript_folder + "\ncd fortigate_services_from_csv\npython3 main.py")
## Address Group Objects
os.system("cd " + subscript_folder + "\ncd fortigate_address_group_from_csv\npython3 main.py")
## Service Group Objects
os.system("cd " + subscript_folder + "\ncd fortigate_service_group_from_csv\npython3 main.py")
## IP Pool Objects
os.system("cd " + subscript_folder + "\ncd fortigate_ippool_from_csv\npython3 main.py")
## VIP Objects
os.system("cd " + subscript_folder + "\ncd fortigate_vip_from_csv\npython3 main.py")

## Take Output scripts and arrange them in work area
os.system("cp " + subscript_folder + "fortigate_address_objects_from_csv/script.txt " + working_folder + "001_ipv4addr.txt")
os.system("cp " + subscript_folder + "fortigate_services_from_csv/services_script.txt " + working_folder + "002_services.txt")
os.system("cp " + subscript_folder + "fortigate_vip_from_csv/vip_script.txt " + working_folder + "003_vip.txt")
os.system("cp " + subscript_folder + "fortigate_ippool_from_csv/IPPool_script.txt " + working_folder + "004_ippool.txt")
os.system("cp " + subscript_folder + "fortigate_address_group_from_csv/addr_group_script.txt " + working_folder + "005_addrgrp.txt")
os.system("cp " + subscript_folder + "fortigate_service_group_from_csv/svc_group_script.txt " + working_folder + "006_svcgrp.txt")

#Concatenate output files into script
os.system("cat " + working_folder + "* > " + output_folder + "final_script.txt")