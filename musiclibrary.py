__author__ = 'gmoore'
import sqlite3
import util
import song
import os
import shutil
import re
import unicodedata



class MusicLibrary(object):

    songlib = []
    songcount = 0

    def __init__(self, name,path,):
        self.libname = name
        self.libpath = path

        #look to load library from DB


        #if no lib in DB then create it
        print 'name: %s'%self.libname
        print 'paht: %s'%self.libpath


        self.loadfrompath()

    def addsong(self,song):
        self.songlib.append(song)
        self.songcount += 1

    def delsong(self,song):
        self.songlib.remove(song)

    def loadfrompath(self):
        print 'loading from files'
        u = util.Util()
        for path in u.allMusicFiles(self.libpath,"*.mp3"):
            #print path
            s = song.Song(path)
            self.addsong(s)

    def orginizelibrary(self,path=None,copy = True,):

        #loop through each file in the lib
        if path is None:
            path = self.libpath

        for song in self.songlib:

            #TODO Add try catch
            #create new directory if it does not exsit
            print 'starting %s '% song.filepath
            print 'Album Artist: %s' % song.getAlbumArtist()
            print 'Album %s ' % song.getAlbum()

            #Prepare strings so they can be used as foldernames
            artist = re.sub('[^\w\-_\. ]', '_', song.getAlbumArtist())
            album = re.sub('[^\w\-_\. ]', '_',song.getAlbum())
            if isinstance(artist,unicode):

                artist = unicodedata.normalize('NFKD', artist).encode('ascii','ignore')
            if isinstance(album,unicode):
                album = unicodedata.normalize('NFKD', album).encode('ascii','ignore')

            print 'Album artist : %s and %s ' % (artist, album)
            dir = os.path.join(path,artist,album)
            print dir

            self.mkdir_p(dir)

            spath = os.path.join(dir,song.filename())
            print spath
            shutil.copy2(song.filepath,spath)

            print "created file: %s" %spath

    def mkdir_p(self,path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)

        except Exception, e:
            print e




        #except Exception, e:
        #            print "**************** Music ERROR ******************"
        #            print e

        #If copy make a copy of file and and create directory

