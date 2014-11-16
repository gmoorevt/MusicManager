__author__ = 'gmoore'
import musiclibrary
import sqlite3

class musicdb(object):
    db = sqlite3
    __InserntSong__ = ''' INSERT INTO songs(title, artist,album,filename,path)
                                VALUES (?,?,?,?,?);  '''

    __InsertLib__ = ''' INSERT INTO musiclibrary(name,path,songcount)
                                VALUES (?,?,?); '''

    def __init__(self,fname='musicdb'):
        try:

            self.db = sqlite3.connect(fname)
            self.createtables()
            self.dbname = fname

        except Exception as e:
            print e

    def createtables(self):
       try:
           cursor = self.db.cursor()
           cursor.execute('''CREATE TABLE If NOT EXISTS songs
                            (
                            title           TEXT    NOT NULL,
                            artist          TEXT    NOT NULL,
                            album           TEXT,
                            filename        TEXT    NOT NULL,
                            path            TEXT    NOT NULL);''')
           self.db.commit()
           print 'Created Song table'
           cursor.execute('''CREATE TABLE IF NOT EXISTS musiclibrary
                            (
                            name  TEXT  NOT NULL ,
                            path  TEXT  NOT NULL ,
                            songcount   INTEGER
                            );''')
           self.db.commit()
           print 'created Music Library Table'

       except Exception as e:
           print e


    def testdb(self):
        try:
            cursor = self.db.cursor()
            title = 'best cool song'
            artist = 'Harry Chapin'
            album = 'Greatest hits'
            filename = 'song.mp3'
            path = '/Users/gmoore/Music/song.mp3'
            cursor.execute(self.__InserntSong__,
                           (title,artist,album,filename,path))

            self.db.commit()
            id = cursor.lastrowid
            print ('Last row id: %d' %id)

            print 'creating library '
            libname = 'test library'
            libpath = '/Users/gmoore/Music'
            sc = 200

            cursor.execute(self.__InsertLib__,(libname,libpath,sc))
            self.db.commit()
            id = cursor.lastrowid
            print('Created new Library ID: %d' %id)

        except Exception as e:
            print e

    def savesong(self,song):
        try:
            db = sqlite3.connect(self.dbname)
            cursor = db.cursor()
            title = song.getTitle()
            artist = song.getArtist()
            album = song.getAlbum()
            filename = song.filename()
            path = song.getPath()
            cursor.execute(self.__InserntSong__,(title,artist,album,filename,path))
            db.commit()
            id = cursor.lastrowid
            print ('Last row id: %d' %id)

        except Exception as e:
            print e
        finally:
            self.db.close()

    def savemusiclib(self,name,path,songcount,songs):
        try:
            db = sqlite3.connect(self.dbname)
            cursor = db.cursor()
            cursor.execute(self.__InsertLib__,(name,path,songcount))
            id = cursor.lastrowid
            print ('Last row id: %d' %id)

        except Exception as e:
            print e
    def getmusiclib(self,path):
        try:
            path = path
            db = sqlite3.connect(self.dbname)
            cursor = db.execute("SELECT name,path,songcount from musiclibrary")
            rl= cursor.fetchone()

            ml = musiclibrary.MusicLibrary(rl[0],rl[1])
            return ml

        except Exception as e:
            print e
