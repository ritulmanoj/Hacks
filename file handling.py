# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:44:49 2020

@author: Manoj kumar
"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
avg = 0
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        count = count + 1
        f = line.find(":")
        line = line.rstrip()
        fline = float(line[f+1:])
        total += fline
        avg = total/count
        
print("Average spam confidence: " + str(avg))

