#! /usr/bin/python 

import os
import sys

COMPILECMD="g++ -g -std=c++1z %s -o exe"

def command(aCommand):
	ret=os.system(aCommand)
	if(ret):
		print "could not execute command %s"%(aCommand)

if __name__ == "__main__":
	os.system('clear')
        hasCompiled=False
        for element in os.listdir(os.getcwd()):
            if("cxx" in element):
                command(COMPILECMD%(element))
                hasCompiled=True
                break

        if(hasCompiled):
            command("./exe")
	    print '' 
	    print '-----------------------------------------------------'
            command("valgrind ./exe")
	else:
		print "not any source to compile"
