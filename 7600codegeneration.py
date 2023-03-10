#!/usr/bin/env python3.4

from logging.config import valid_ident
from operator import length_hint
from os.path import expanduser
import sys
import subprocess
import re


#define Function
# while loop to provide user input
def get_user_input(prompt):
    value = input(prompt)
    if not value:
        raise ValueError("You must provide a valid response to continue!")
    return value


#define variables
home = expanduser("~")
logincfg = home+"/.cloginrc"
source_mc_config = home+"/"+"source_asr.cfg"
source_asr = input("Please enter source site asr TID: ")
target_asr = input("Please enter the target site asr TID: ")
target_mc_config = home+"/"+target_asr+".cfg" 


#dictonary to store user input based on the number of Bundle-Ethers that need to migrate and their respective numbers
# responses = {'be#1' : '', 'be#2' : '', 'be#3' : '', 'be#4' : '', 'be#5' : ''}
# x = []
# for i in range(n):
#     range(0, n)
#     x.append(input("Please enter only Bundle-Ether number (i.e. 50): "))
    # print(x)
bundlenumbers = []
n = int(input('How many Bundle-Ethers need to migrate?: ')) 
for i in range(n):
    bundlenum = int(input("What is the bundle number:"))
    bundlenumbers.append(bundlenum)
    

# for key, val in zip(responses, x):
#     responses[key] = val
# print("we need to migrate the following bundle-ethers: " + str(responses))


#grab input if arguments were not given
#this section of code is related to when network device is currently locked out for upcoming maintenances
if(len(sys.argv)==1):
    pass
elif (len(sys.argv)>1):
    if sys.argv[1]=="--lockout":
        logincfg=home+"/"+".clogingrm"
else:
    print("invalid arguments please run with no arguments or with --lockout")
    quit()
print(logincfg)


#let's pull down configuration from source site asr so script can extract and produce necessary configuration for target site asrs
cmd = "show run formal"


#run cmd against source asr with clogin
output=subprocess.check_output(['clogin', '-f', logincfg, '-c', cmd, source_asr])
file=open(home+"/"+"source_mc"+".cfg", "w")
file.write(output)
file.close()
# for i in output.splitlines():
    # i=i.decode("utf-8")
    # file.write(i+"\n")
# file.close


#this script segment identifies the mc l2vpn bridge groups that need to copied over to target asrs based on the identified bundle-ethers that need to be groomed
print()
print('-' * 232)
print()
bg = "identified l2vpn bridge groups that need to be copied to the target asrs"
x = bg.center(218)
print(x)
print()
print('-' * 232)
print()


#my thoughts here are to use a for loop to grab the dictonary keys that contain values
# for value in responses:
    

#this portion is my attempt to process through the list of Bundle-Ether numbers that the user inputted.
#it works but only for the first Bundle-Ether
# pattern_include = first_BE+"\." or second_BE+"\."
with open(source_mc_config) as file_out:
    with open(target_mc_config, 'w') as f:
        for each in file_out:
            # if "interface Bundle-Ether" in each and first_BE in each:
            # if each.startswith("interface Bundle-Ether"+ first_BE in each and second_BE in each):
            if "interface Bundle-Ether" in each:
            # if re.search(pattern_include, each) and each.startswith("interface Bundle-Ether"):
                print(each.strip())
                # f.writelines((each))
print()
print('-' * 232)
