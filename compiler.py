#! /usr/bin/python 

import os
import sys

COMPILECMDCXX="g++-7 -g -std=c++1z %s -o exe"
COMPILECMDC="gcc-7 -g %s -o exe"
COMPILECMDRUST="rustc -g %s -o exe"

COMPILEPROJECT=["Makefile","CMakeLists.txt"]
EXTENSIONTYPE=["hpp,cpp,hxx,cxx,h,c"]

def strInContainer(aStr,aContainer):
    if any(aStr == element for element in aContainer):
        return True
    return False

def generateCond(aContainer):
    lCondition=""
    for element in aContainer:
        lCondition+=element+" and "
        if(aContainer[len(aContainer) -1] == element):
            lCondition+=element
        else:
            lCondition+=element+" and "
    return lCondition

def isExecutable(aFile):
    ret=os.system("test -x %s"%(aFile))
    if(ret):
        return False
    return True

def command(aCommand):
	ret=os.system(aCommand)
	if(ret):
		print "could not execute command %s"%(aCommand)

def loadPlugins():
    hasCompiled=False
    for element in os.listdir(os.getcwd()):

        if("CMakeLists.txt" in element and ".sw" not in element):
            command("cmake .")
            command("make")
            break

        if("Makefile" in element and ".sw" not in element):
            #print os.getcwd()
            #print sys.argv[1]
            #lPath2Dir=sys.argv[1]
            #command("make -C %s"%(lPath2Dir))
            #wait= input("PRESS ENTER TO CONTINUE.")
            command("make")
            break

        if(".cxx" in element and ".sw" not in element):
            command(COMPILECMDCXX%(element))
            hasCompiled=True
            break

        if(".c" in element and ".sw" not in element):
            command(COMPILECMDC%(element))
            hasCompiled=True
            break

        if(".py" in element and ".sw" not in element and element != "compiler.py"):
            if(not isExecutable(element)):
                command("chmod a+x %s"%(element))
            command("./%s"%(element))
            break

        if(".rs" in element and ".sw" not in element):
            command(COMPILECMDRUST%(element))
            hasCompiled=True
            break

    return hasCompiled

if __name__ == "__main__":

	os.system('clear')
        print sys.argv
        ret = loadPlugins()
        if(strInContainer("--val",sys.argv)):
            if(ret and strInContainer("exe",os.listdir(os.getcwd()))):
                command("./exe")
                print '' 
	        print '-----------------------------------------------------'
                command("valgrind ./exe")
        elif(strInContainer("--gdb",sys.arg)):
            if(ret and strInContainer("exe",os.listdir(os.getcwd()))):
                print 'launching gdb'
                print '-----------------------------------------------------'
                commnad("gdb exe")
        else:
            if(ret and strInContainer("exe",os.listdir(os.getcwd()))):
                command("./exe")
#	else:
#		print "not any source to compile"
