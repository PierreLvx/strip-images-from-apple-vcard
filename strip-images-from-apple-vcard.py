#!/usr/bin/env python3

import sys
import os
import re

def checkArgs():
	numArgs = len(sys.argv)
	if (numArgs < 3):
		return False
	return True

def debugMsg(msg,type='Info'):
	print(type.upper() + ":")
	print("    " + msg)
	print("")
	
# ===================================================================
# CLI

if checkArgs():
	# Arguments provided on command line - must be a pro!
	filenameInput = sys.argv[1]
	filenameOutput = sys.argv[2]
else:
	filenameInput = input("Input file (.vcf): ")
	filenameOutput = input("Output file (.vcf): ")
	print("")

if not os.path.exists(filenameInput):
	debugMsg("File '" + filenameInput + "' not found",'Error')
	sys.exit(1)

if os.path.exists(filenameOutput):
	answer = input(filenameOutput + " already exists. Overwrite? (y/n)")
	if answer != 'y':
		debugMsg("Please rerun this tool and specify an output filename",'Error')
		sys.exit(1)
	else:
		print("")
	
debugMsg("Reading '" + filenameInput + "'",'Info')

infile = open(filenameInput)

clean = ""
for line in infile:
	if re.match('PHOTO',line):
		debugMsg("Found line starting with PHOTO. Skipping.")
		continue
	
	if re.match('\\s',line):
		debugMsg("Found line starting with space. Skipping.")
		continue
	
	clean += line

debugMsg("Writing " + filenameOutput)
	
outfile = open(filenameOutput,"w")
outfile.write(clean)

debugMsg("Done.")

sys.exit(0)
