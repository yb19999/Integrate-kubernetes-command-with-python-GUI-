#!/usr/bin/python3


import subprocess

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

#print("my content from python cgi bin")
c = subprocess.getoutput("date")
print(c)
