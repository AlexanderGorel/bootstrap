################################################################### SYNOPSIS
#
# bootstrap a CrystFEL .stream file with the same number of indexed images as the original streamfile
#
################################################################### AUTHOR/REPOSITORY
#
# agorel@mr.mpg.de
#
# github repository: AlexanderGorel/bootstrap
#
################################################################### VERSION
#
# version 04.09.2025
#
################################################################### USAGE
#
# python3 bootstrap_stream.py -s something.stream -o something-bootstrapped.stream
#
################################################################### IMPORTS


import random
import re
#--------------------------------------- command line parameters
import sys #-> argv
import os #-> file checks
import getopt #-> command line parameters


####################################################### get opt

#--------------------------------------------------- USAGE
def usage():
    print(str(sys.argv[0])+" -s <stream_filename> -o <output_filename>")
    print("options:")
    print("-h --help")
    print("-s --stream_filename")
    print("-o --output_filename")

#--------------------------------------------------- GETOPTS

try:
    (opts, args) = getopt.getopt(sys.argv[1:], "hs:o:", ["help","stream_filename=","output_filename="])
except getopt.GetoptError:
    usage()
    sys.exit(1)

#--------------------------------------------------- NO OPTIONS -> NOTHING TO DO
if opts.__len__()==0:
    usage()
    sys.exit()

#################################################### PROCESS DATA
stream_filename=""
output_filename=""

#--------------------------------------------------- PROCESS ARGS
for (opt, arg) in opts:
#--------------------------------------------------- PRINT USAGE
    if opt in ("-h","--help"):
        usage()
        sys.exit()
#--------------------------------------------------- ASSIGN STREAMFILE
    elif opt in ("-s", "--stream_filename"):
        stream_filename = arg
        if (stream_filename == "") or not(os.path.isfile(stream_filename)):
            print("stream_filename"+stream_filename+" does not exist.")
            sys.exit(1)
#--------------------------------------------------- ASSIGN STREAMFILE
    elif opt in ("-o", "--output_filename"):
        output_filename = arg
        if (output_filename == "") or os.path.isfile(output_filename):
            print("output_filename:"+output_filename+" is not valid.")
            sys.exit(1)
#--------------------------------------------------- SOMETHING WENT REALLY WRONG
    else:
        print("unexpected option")
        sys.exit(1)
#--------------------------------------------------- CHECKS


######################################################## FUNCTIONS
def split(delimiters, string, maxsplit=0):
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)
######################################################## MAIN

fd=open(stream_filename,'r')
text=fd.read()
fd.close()

del1="----- End geometry file -----\n"
del2="----- End chunk -----"
#---------------------------------------------------- SPLIT AND SORT
parts=split([del1,del2],text)
print("split into parts.")
head=parts[0]

#chunk_list=filter(lambda x: "----- Begin chunk -----" in x,parts)

#---------------------------------------------------- GET THE CHUNKS WITH CRYSTALS
chunk_list=filter(lambda x: "--- Begin crystal" in x, parts)
print("got chunk list.")
#---------------------------------------------------- FORM CORRECT CHUNKS
chunk_list=[chunk.strip()+"\n"+del2+"\n" for chunk in chunk_list]
print("stripped chunks.")
#---------------------------------------------------- RANDOM PICK

randomchunk_list = [random.choice(chunk_list) for x in chunk_list]
print("random picked.")
#---------------------------------------------------- WRITE TEXT
fd=open(output_filename,'w')
fd.write(head)
fd.write(del1)
for chunk in randomchunk_list:
    fd.write(chunk)
fd.close()



