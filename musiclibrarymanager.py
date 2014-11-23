__author__ = 'gmoore'
import os
import shutil
import re

import util
import song
import unicodedata
import musiclibrary
import cPickle as pickle


class MusicLibraryManager(object):
    __libraryies = {}


    def createfrompath(self, path, name):
        # TODO add try catch
        print 'loading from path %s -- ' % path

        ml = musiclibrary.MusicLibrary
        ml.name = name
        ml.path = path

        u = util.Util()
        for p in u.allMusicFiles(path, "*.mp3"):
            # TODO change the filter to be all music files

            s = song.Song(p)
            ml.addsong(s)

        self.__libraryies.update({name: ml})
        return ml

    def finddups(self, musiclib):

        duplib = musiclibrary.MusicLibrary
        duplib.name = musiclib.name + '_' + 'dups'

        # find dups in library
        libdictionary = {}
        # create a dict of songs
        for s in musiclib.songs:
            #check to see if song is in temp dic if so add to dupdic
            if libdictionary.has_key(s.gethash):
                duplib.addsong(s)
            else:
                libdictionary.update({s.gethash: s})

        return duplib

    def deletesongs(self, musiclib, delsonglist):
        pass


    def createfromfile(self, file):
        pass

    def getmusiclibrary(self, name):
        return self.__libraryies.get(name)

    def loadlibary(self, librarypath):
        # TODO add try catch

        with open(librarypath, 'rb')as handle:
            return pickle.load(handle)

    def savelibrary(self, musiclib):
        # TODO Add try catch
        #TODO come up with file naming convension

        libdata = {'name': musiclib.name, 'path': musiclib.path, 'songs': musiclib.songs}

        with open('musiclib.name', 'wb')as handle:
            pickle.dump(libdata, handle)


    def orginizelibrary(self, path, copy=True):

        # loop through each file in the lib

        for song in self.songlib:

            # TODO Add try catch
            #create new directory if it does not exsit
            print 'starting %s ' % song.filepath
            print 'Album Artist: %s' % song.getAlbumArtist()
            print 'Album %s ' % song.getAlbum()

            #Prepare strings so they can be used as foldernames
            artist = re.sub('[^\w\-_\. ]', '_', song.getAlbumArtist())
            album = re.sub('[^\w\-_\. ]', '_', song.getAlbum())
            if isinstance(artist, unicode):
                artist = unicodedata.normalize('NFKD', artist).encode('ascii', 'ignore')
            if isinstance(album, unicode):
                album = unicodedata.normalize('NFKD', album).encode('ascii', 'ignore')

            #Create folders if they exsist
            print 'Album artist : %s and %s ' % (artist, album)
            dir = os.path.join(path, artist, album)
            self.mkdir_p(dir)

            #Copy the file to the new directory
            #Create a unique file name for file.
            spath = self.copyfile(dir, song.filename())

            if not os.path.exists(spath):
                print spath
                shutil.copy2(song.filepath, spath)
                print "created file: %s" % spath
            else:
                print "File exsits: %s" % spath
                self.dups += 1

    def copyfile(self, dir, filename):
        count = 1
        try:
            spath = os.path.join(dir, filename)
            if os.path.exists(spath):
                basename = os.path.basename(filename)
                ext = os.path.splitext(basename)[1]
                file = os.path.splitext(basename)[0]
                file = file + '[%s]' % count
                count += 1
                filename = file + ext

                self.copyfile(dir, filename)

            return spath

        except Exception, e:
            print e


    def mkdir_p(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)

        except Exception, e:
            print e

