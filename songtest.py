from mutagen.easyid3 import EasyID3
from mutagen import mp3
from mutagen.mp3 import MP3
import os, errno
import shutil

#from mutagen._id3util import ID3HHeaderError

musicfile = '/Users/gmoore/Music/Beatles - All You Need Is Love.mp3'

audio = MP3(musicfile)
print audio.info.length, audio.info.bitrate
print audio.tags

def mkdir_p(path):
	try:
		os.makedirs(path)

		print 'createfile %s' %path
		
	except OSError as exc: # Python >2.5
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			print'Tehre was a problem...'
			pass
		else: raise


print audio.tags['TPE1']
print audio.tags['TIT2']
print audio.tags['TALB']
print audio.tags['TALB']
d = os.path.join('/Users','gmoore/Music','ZZZ1GG55')
print d
f = os.path.join(d,'Beatles - All You Need Is Love.mp3')
#mkdir_p(d)
#os.mkdir('Users/gmoore/Music/AAAAAAAAA')
print f
#os.mkdir(d)
g = shutil.copy2(musicfile,f)
