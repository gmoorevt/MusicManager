__author__ = 'gmoore'
import hashlib
import song



class Dupinator(object):

    potentialdups = []
    dupscount = 0
    songs = {} # list of songs


    def listdups(self):

        sl = self.songs.values()

        for l in sl:
            if len(l) > 1:
                print 'found files with dups'
                for s in l:
                    print s.getPath()
            else:
                print 'Not Dup'
                l[0].getPath()

    def listdup(self,songlist):

        for s in songlist:
            k = s.gethash()
            if self.songs.has_key(k):
                self.potentialdups.append(s)
                print 'found dup: %s'% s.getTitle()
                print 'path; %s'% s.getPath()
            else:
                self.songs[k] = s

    def finddups(self,songlist):
        try:
            print 'looking for dups'
            for s in songlist:

                h = s.gethash()
                print h
                if self.songs.has_key(h):
                    print "found key"
                    self.potentialdups.append(s)
                    x = self.songs[h]
                    x.append(s)
                    self.dupscount += 1


                else:
                    print "adding key"
                    self.songs[h] = [s]

                print 'dups: %s'%self.dupscount

        except Exception as e:
            print e



'''
Find a list of files that are dups
>Go through a list of files and create a hash of the name,artist,album
>Get a list of files that are thought to be dups
>Look for check if this



'''
