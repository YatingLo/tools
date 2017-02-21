# -*- encoding:utf-8 -*-
import os
import json
import sys

CONFIG_FILE = 'DirectionList.json'

def ReadConfig(path_root):
    path = os.path.normpath(os.path.join(path_root, CONFIG_FILE))
    try:
        f = open(path)
        cfg = json.load(f, encoding='utf8')
        f.close()
    except:
        print("Configuration file \"%s\" is not existed or broken!" % path)
    finally:
        f.close()
    return cfg

def GetFiles(folderPath):
    fileStr = "";
    for dirpath, dirnames, filenames in os.walk(folderPath):
        for filename in filenames:
            extension = os.path.splitext(filename)[1]
            if 0 == cmp(extension,".png") or 0 == cmp(extension,".jpg"):
                fileStr += " " + os.path.join(dirpath, filename);
            else:
                print("file \"%s\" not suport." % filename);
    return fileStr;
    
def CreateAtlas(path_root, max_size, resPath, desPath, fileName):
    dataName = os.path.join(desPath, fileName + ".plist");
    sheetName = os.path.join(desPath, fileName + ".png");
    files = GetFiles(resPath);
    commandStr = "TexturePacker --format cocos2d";
    commandStr += " --max-size " + str(max_size);
    commandStr += " --data " + dataName;
    commandStr += " --sheet " + sheetName;
    commandStr += " --extrude 1";
#    commandStr += " --allow-free-size";
    commandStr += files;
    
    print("CommandStr: %s" % commandStr)
    os.system(commandStr)
    
def CreateFiles(path_root, ConfigInfo):
    file_list = [];
    
    max_size = ConfigInfo['max_size']
    file_list = ConfigInfo['file_list']
    
    for value in file_list:
         resourcePath  = os.path.normpath(os.path.join(path_root, value['from']))
         destinationPath = os.path.normpath(os.path.join(path_root, value['to']))
         fileName = value['name']
         
         if not os.path.exists(resourcePath):
             print("%s Not exists." % resourcePath)
             continue
         if not os.path.exists(destinationPath):
             os.makedirs(destinationPath)
         CreateAtlas(path_root, max_size, resourcePath, destinationPath, fileName)

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    ConfigInfo = ReadConfig(current_dir)
    CreateFiles(current_dir, ConfigInfo)
    
    print("the end")
    raw_input("")