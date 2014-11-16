__author__ = 'gmoore'
import os
import song,musicdb
import musiclibrary
import readline
import dupinator
import song



print "Music Organizer "
print "Enter your description of what to do..."

def start():
    while True:

        input = raw_input('What do you want to do? ').strip()
        if input == "test":
            s = song.Song('/Users/gmoore/Music/Beatles - All You Need Is Love.mp3')
            s.print_tags()

            print'*******************'



            print 'running testing suite'

        if input =="GetLib":
            input = raw_input('enter library name ').strip()
            #ml = musicdb.musicdb('geody2')
            ml = musiclibrary.MusicLibrary(input,'/Users/gmoore/Music/')
            ml.orginizelibrary('/Users/gmoore/MusicLib')


            #ml.getmusiclib('/Users/gmoore/Music')
            print 'getting ml....'

        elif input == "Songtest":
            s = song.Song("/Users/gmoore/Music/Band - Acadian Driftwood.mp3")
            print s.gethash()

            print"************"
            s.print_tags()

        elif input == "dup":
            newtest()

        elif input =='open dir':
            path = raw_input('enter your directory').strip()
            print path
        elif input =='exit':
            break
        else:
            print 'invalide command'



def getlib():
    db = musicdb.musicdb('geody2')
    db.getmusiclib('/Users/gmoore/Music')
    db.getmusiclib()


def test():
    db = musicdb.musicdb('geody2')
    db.testdb()

def newtest():
    ml = musiclibrary.MusicLibrary('test2','/Users/gmoore/Music')

    print ml.songcount
    #print ml.songlib

    dp = dupinator.Dupinator()


    dp.finddups(ml.songlib)
    print 'number of dups: %s'% dp.dupscount

    dp.listdups()


def newtest2():
    u = util.Util()
    for path in u.allMusicFiles("/Users/gmoore/Music/musictest","*.mp3;*.m4a;*.wav"):
        print path
        s = song.Song(path)
        print 'song: %s'% s.filename()




'''
def loadlib(self,path):

    lib = musiclibrary.MusicLibrary('1stLib',path)





print 'starting main'

u = util.Util()

s = song.Song('/Users/gmoore/Music/Kinks - Australia.mp3')
s.print_tags()

db = musicdb.musicdb(fname='geody')
db.testdb()

db.savesong(s)
'''

'''
for path in u.allMusicFiles("/Users/gmoore/Music","*.mp3;*.m4a;*.wav"):
    print path
    s = song.Song(path)
    db.savesong(s)
    print 'saved song'
'''

#db.testdb()

#print "Song: ",  s

#print audiofile
#a = audiofile['title']
#print a
#a =  a[0].encode('ascii')

#print a

#if not os.path.exists(a):
 #   os.makedirs(a)

#print EasyID3.valid_keys.keys()

#audiofile.pprint()


#
# paths = u.allMusicFiles("/Users/gmoore/Music","*.mp3")

#for file in paths:
 #   print file

   # print u.getidTags("test",file)

#for each file in list of potential files:

# Check ID3 Tags for Album and Artist

#filetags = u.getid3Tags("test","/Users/gmoore/Music/Wallflowers - 6th Avenue Heartache.mp3")


if __name__ == '__main__':
    start()
