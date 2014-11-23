__author__ = 'gmoore'
import song
import util


class MusicLibrary(object):
    songs = []
    songcount = 0
    name = ''
    createdate = ''
    path = ''

    def addsong(self, song):
        self.songs.append(song)
        self.songcount += 1

    def delsong(self, song):
        self.songs.remove(song)

    def printsongs(self):
        for s in self.songs:
            s.print_tags()


