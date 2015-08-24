# # First we need to import the necessary components from PyBrain.
# from pybrain.datasets            import ClassificationDataSet
# from pybrain.utilities           import percentError
# from pybrain.tools.shortcuts     import buildNetwork
# from pybrain.supervised.trainers import BackpropTrainer
# from pybrain.structure.modules   import SoftmaxLayer
# # Furthermore, pylab is needed for the graphical output.
# from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
# from scipy import diag, arange, meshgrid, where
# from numpy.random import multivariate_normal


# # read the artist name from the Mp3 file
# from mutagen.mp3 import MP3
# import mutagen.id3
# from mutagen.easyid3 import EasyID3
#
#
# from pydub import AudioSegment
#
# song = AudioSegment.from_mp3("fz.mp3")
# song.export("fzw.wav", format="wav", bitrate="192k")
#
#
#
# # infovalue = MP3(mp3dirstring,ID3=EasyID3)
# # artist = infovalue.get('artist')
# # artist_name = "".join(artist)
#
# # read the artist name from the Mp3 file
# mp3dirstring = "mp3/mp3.wsv"
# song_export_name='wav/'+mp3dirstring.split('.')[0].split('/')[1]+".wav"
# print(song_export_name)

mp3dirstring ="mp3/01-Sunday_Bloody_Sunday.mp3"
# read the artist name from the Mp3 file
from mutagen.mp3 import MP3
import mutagen.id3
from mutagen.easyid3 import EasyID3

infovalue = MP3(mp3dirstring,ID3=EasyID3)
artist = infovalue.get('artist')
print artist
if artist == None:
	artist = "null"
artist_name = "".join(artist)
print artist_name
# read the artist name from the Mp3 file