#!/usr/bin/env python
import os,sys,shutil,time

FileDictionary = {}
        
def GetAssetName (aFile):
    aFile, fileExtension = os.path.splitext(os.path.basename(aFile))
    assetName = aFile
    print fileExtension
    
    chunkSplit = aFile.rsplit("_",1)
    if len(chunkSplit) == 2:
        assetName = chunkSplit[0]
        
    return assetName, fileExtension

location = os.path.dirname(os.path.realpath(__file__))

everything = os.listdir(location)

for item in everything:
    if os.path.isfile(item) and os.path.basename(item) != "sortfiles.py":
        assetName, ext = GetAssetName(item)
        if ext == ".png":
            folder = os.path.join(location,assetName)
            if not os.path.isdir(folder):
                os.mkdir(folder + "\\")
            destination = os.path.join(folder,os.path.basename(item))
            
            #print destination
            shutil.copy(item, destination)