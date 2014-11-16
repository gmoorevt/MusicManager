__author__ = 'gmoore'
import os, fnmatch
from mutagen.mp3 import MP3
from mutagen._id3util import ID3NoHeaderError
import unicodedata
import string
import hashlib

class Song(object):
    audio = None

    def __init__(self, path):
        # check for file
        #self.strpath self.fname = os.path.split(path)
        try:

            ext = os.path.splitext(path)
            self.tags = {}

            self.title = 'empty'
            self.artist = 'empty'
            self.album = 'empty'
            self.length ='empty'
            self.bitrate='empty'
            self.filepath = path
            self.genre = 'empty'
            self.tracknumber = 'empty'
            self.date = 'empty'
            self.composer = 'empty'
            self.albumartist = 'empty'

            if ext[1] == '.mp3':
                try:
                    self.audio = MP3(path)

                    self.audio.pprint()

                    if 'TPE1' in self.audio.tags:
                        self.artist = self.audio.tags['TPE1'].text[0]
                    else: print "No Artist"
                    if 'TALB' in self.audio.tags:
                        self.album = self.audio.tags['TALB'].text[0]
                    else: print 'No Album'
                    if 'TIT2' in self.audio.tags:
                        self.title = self.audio.tags['TIT2'].text[0]
                    else: print 'No Title'
                    if 'TCOM' in self.audio.tags:
                        self.composer = self.audio.tags['TCOM'].text[0]
                    else: print 'No Composer'
                    if 'TPE2' in self.audio.tags:
                        self.albumartist = self.audio.tags['TPE2'].text[0]
                    else: print 'No Album Artist'
                    if 'TDRC' in self.audio.tags:
                        self.date = self.audio.tags['TDRC'].text[0]
                    else: print 'No Date'
                    if 'TDRC' in self.audio.tags:
                        self.tracknumber = self.audio.tags['TDRC'].text[0]
                    else: print 'No tracknumber'

                    self.bitrate = self.audio.info.bitrate
                    self.length = self.audio.info.length

                except ID3NoHeaderError as e:
                    print e

                except Exception as e:
                    print "**************** ERROR ******************"
                    print e
                    print path
                    pass

            elif ext == '.mp4':
                pass

            elif ext == '.mwa':
                pass
        except Exception, e:
            print e

    def add_tag(self, name, value):
        self.tags.update({name: value})
        # self.tags['name']=value

    def filename(self):
        path, name = os.path.split(self.filepath)
        return name

    def getArtist(self):

        return self.artist

    def getAlbum(self):
        if self.album is not None:
            return self.album
        else:
            return 'No_Album_Name'

    def getAlbumArtist(self):
        if self.albumartist == 'empty':
            return self.artist
        else:
            return self.albumartist


    def getTitle(self):
        if self.title is not None:
            return self.title
        else:
            return self.filename()

    def getPath(self):
        return self.filepath

    def gethash(self):
        md5 = hashlib.md5("%s_%s_%s" % (self.getArtist(), self.getAlbum(), self.getTitle()))
        return md5.hexdigest()

    def print_tags(self):
        __doc__ = "prints all tags in song"
        print '************  Raw Output  ********************'
        # self.audio.pprint()

        print '***********   Properties  ********************'

        print 'Title: %s' % self.title
        print 'Artist: %s' % self.artist
        print 'Album: %s' % self.album
        print 'Length: %s' % self.length
        print 'Bitrate: %s' % self.bitrate
        print 'FilePath: %s' % self.filepath
        print 'Genre: %s' % self.genre
        print 'TrackNumber: %s' % self.tracknumber
        print 'Date: %s' % self.date
        print 'Composer: %s' % self.composer
        print 'Album-Artist: %s' % self.albumartist

