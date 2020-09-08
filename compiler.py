#! /usr/bin/python3

import os
import sys

COMPILECMDCXX="clang++-10 -g3 -rdynamic -std=c++20 -stdlib=libstdc++ %s -o exe -lpthread -lsqlite3 -lstdc++fs -lwebrequest -lsystools -lrequestparser -ltools -lpugixml"# -luuid "

COMPILECMDC="gcc-7 -g3 %s -o exe -lpthread -lm"
COMPILECMDRUST="rustc -g %s -o exe"

COMPILEPROJECT=["Makefile","CMakeLists.txt"]
EXTENSIONTYPE=["hpp,cpp,hxx,cxx,h,c"]

ETYPE=[".c",".cxx",".py",".go"]
FTYPECOMMAND={"rs":"rust-gdb exe","c":"gdb exe","cxx":"gdb exe","py":"python -m pdb %s"}

EXETYPE={"python":"./%s"}

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
        print("could not execute command %s"%(aCommand))
        sys.exit()

def checkCommandLineArgs(aCmdline):
    if(len(aCmdline.split(" "))>1):
        return True
    else:
        return False

def prepareCommandArgs(_args,_ftype):

    lArgs= _args.split(" ")
    lCommand=None
    if( _ftype == "py"):
        lCommand="./%s"
    else:
        lCommand="./exe"

    for nelement in lArgs :
        lCommand=lCommand+" %s"%(nelement)

    return lCommand

def mktCompiling():
    if("Gen3" in os.listdir(os.getcwd())):
            return True
    return False

def compileMktSoft():
    os.chdir("build")
    ret=os.system("ninja -j12")
    os.chdir("..")
    if(ret==0):
        return "mktsoft",True
    return None,False

def loadPlugins():
    ftype=None
    hasCompiled=False

    for element in os.listdir(os.getcwd()):
        #configuration for MKT
        if("Gen3" in element and ".sw" not in element):
            print("Gen3 has been detected")
            print("exiting compiling manager")
            sys.exit()

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
            ftype="cxx"
            break

        if(".c" in element and ".sw" not in element):
            command(COMPILECMDC%(element))
            hasCompiled=True
            ftype="c"
            break

        if(".toml" in element and ".sw" not in element):
            command("cargo build")
            break

        if(".py" in element and ".sw" not in element and element != "compiler.py"):
            if(not isExecutable(element)):
                command("chmod a+x %s"%(element))
            command("./%s"%(element))
            hasCompiled=True
            ftype="py"
            break

        if(".rs" in element and ".sw" not in element):
            command(COMPILECMDRUST%(element))
            hasCompiled=True
            ftype="rs"
            break

        if("CMakeLists.txt" in os.listdir(os.getcwd())):
            # foldername = os.path.basename(os.getcwd()) todo you should be able to launch compiling from anywhere based on the existence of the CMakeList
            if not os.path.exists("build"):
                os.makedirs("build")
            os.chdir("build")
            command("cmake .. -DCMAKE_C_COMPILER=clang-9 -DCMAKE_CXX_COMPILER=clang++-9")
            command("make")
            os.chdir("..")
            break

    return ftype,hasCompiled,element

def setTasks():
    ret=True
    ftype=None
    for element in os.listdir(os.getcwd()):
        for fitem in ETYPE:
            if(fitem in element and ".sw" not in element):
                ftype=element[1:]
                print(ftype)
    return ret,ftype

if __name__ == "__main__":

    os.system('clear')
    print(sys.argv)

    filetype = None
    ret = False

    if(mktCompiling()):
        filetype,ret = compileMktSoft()
    else:
        #quick patch todo improve
        if( len(sys.argv) > 2 ):
            if( ".qml" in sys.argv[2] and len(sys.argv) == 3):
                    command("qmlscene %s"%(sys.argv[2]))
            else:
                filetype,ret,element = loadPlugins()
        else:
            filetype,ret,element = loadPlugins()

    if(strInContainer("--compile",sys.argv)):
        sys.exit()

    if(strInContainer("--val",sys.argv)):
        if(ret and strInContainer("exe",os.listdir(os.getcwd()))):
            command("./exe")
            print ('')
            print ('-----------------------------------------------------')
            command("valgrind ./exe")

    elif(strInContainer("--debug",sys.argv)):
        if(ret and strInContainer("exe",os.listdir(os.getcwd()))):
            print ('launching debugger')
            print ('-----------------------------------------------------')
        if(filetype != None):
            if(filetype == "c" or filetype == "cxx"):
                command("gdb exe")
            if(filetype == "rs"):
                command("rust-gdb exe")

        if(ret and filetype=="py"):
            print('launching py debugger')
            print('-----------------------------------------------------')
            command("python -m pdb %s"%(sys.argv[2]))

    elif(strInContainer("--args",sys.argv)):
        #should be able to pass multiple args ex: exe arg1 arg2 arg3 ... argn
        print('launching with args')
        print('-----------------------------------------------------')
        cli_args=raw_input("args ?\n")
        lCommand = prepareCommandArgs( cli_args , filetype )

        if(ret and filetype=="py"):
            command( lCommand%( element ) )

        if(ret and strInContainer("exe",os.listdir(os.getcwd()))):
            command( lCommand )

    else:
        if(ret and strInContainer("exe",os.listdir(os.getcwd()))):
            command("./exe")
