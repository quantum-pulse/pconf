
from lib.filemgr import *

SPACE=" "

class compilermgr:
    def __init__(self,_jsonconf):
        self.__config=_jsonconf 

    def __unmarshalize(self,_strlist,_echar=''):
        token=' '
        lBuffer=""
        for index,element in enumerate(_strlist):
            if('-' not in element):
                if(index < len(_strlist)-1):
                    lBuffer+='-'+_echar+element+token
                else:
                    lBuffer+='-'+_echar+element
            else:
                if(index < len(_strlist)-1):
                    lBuffer+=element+token
                else:
                    lBuffer+=element
                
        return lBuffer

    def __concat(self,*args):
        lBuffer="" 
        for item in args:
            lBuffer+=item+SPACE
        return lBuffer
    
    def generate(self):
        lConfig=filemgr().readjson(self.__config)
        return self.__concat(lConfig['compiler'],self.__unmarshalize(lConfig['flags']),"%s","-o",self.__unmarshalize(lConfig["sharedlib"],'l'))
