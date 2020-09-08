
import json

class filemgr:
    def __init__(self):
        pass

    def read(self, _filename):
        lFile = open(_filename,"r")
        lBufferList = lFile.readlines()
        lFile.close()
        return lBufferList

    def write(self, _filename , _bufferlist):
        lNewFile = open(_filename,"w")
        lNewFile.writelines(_bufferlist)
        lNewFile.close()

    def readjson(self,_json):
        lData=None
        with open(_json) as json_data:
            lData = json.load(json_data)
        return lData
