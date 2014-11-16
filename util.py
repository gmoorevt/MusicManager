__author__ = 'gmoore'

from mutagen.easyid3 import EasyID3
import os, fnmatch
import sqlite3

class Util:
    count = 1


    def allMusicFiles(self,root,patterns='*',single_level=False,yield_folders=False):
        print 'start'
        #global count
        patterns = patterns.split(';')
        for path, subdirs, files in os.walk(root):
            if yield_folders:
                files.extend(subdirs)
            files.sort()
            for name in files:
                for pattern in patterns:
                    if fnmatch.fnmatch(name,pattern):
                        yield os.path.join(path,name)
                        #global count += 1
                        break
                if single_level:
                    break
    def getid3Tags(self,fname,path):

        audio = EasyID3(path)
       # print audio[title]

        return audio.items()


    def getDB(self,filename ='musicdb.sql'):
        db = sqlite3.connect(filename)


