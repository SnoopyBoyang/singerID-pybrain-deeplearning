# # # First we need to import the necessary components from PyBrain.
# # from pybrain.datasets            import ClassificationDataSet
# # from pybrain.utilities           import percentError
# # from pybrain.tools.shortcuts     import buildNetwork
# # from pybrain.supervised.trainers import BackpropTrainer
# # from pybrain.structure.modules   import SoftmaxLayer
# # # Furthermore, pylab is needed for the graphical output.
# # from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
# # from scipy import diag, arange, meshgrid, where
# # from numpy.random import multivariate_normal
#
#
# # # read the artist name from the Mp3 file
# # from mutagen.mp3 import MP3
# # import mutagen.id3
# # from mutagen.easyid3 import EasyID3
# #
# #
# # from pydub import AudioSegment
# #
# # song = AudioSegment.from_mp3("fz.mp3")
# # song.export("fzw.wav", format="wav", bitrate="192k")
# #
# #
# #
# # # infovalue = MP3(mp3dirstring,ID3=EasyID3)
# # # artist = infovalue.get('artist')
# # # artist_name = "".join(artist)
# #
# # # read the artist name from the Mp3 file
# # mp3dirstring = "mp3/mp3.wsv"
# # song_export_name='wav/'+mp3dirstring.split('.')[0].split('/')[1]+".wav"
# # print(song_export_name)
#
# mp3dirstring ="mp3/01-Sunday_Bloody_Sunday.mp3"
# # read the artist name from the Mp3 file
# from mutagen.mp3 import MP3
# import mutagen.id3
# from mutagen.easyid3 import EasyID3
#
# infovalue = MP3(mp3dirstring,ID3=EasyID3)
# artist = infovalue.get('artist')
# print artist
# if artist == None:
# 	artist = "null"
# artist_name = "".join(artist)
# print artist_name
# # read the artist name from the Mp3 file
# from features import Features
# # use mfcc feature
# feature_params = {'sample_rate': 44100, 'feature': 'mfcc', 'nbpo': 12, 'ncoef': 10, 'lcoef': 0, 'lo': 63.5444,
# 				  'hi': 16000, 'nfft': 16384, 'wfft': 8192, 'nhop': 4410, 'log10': False, 'magnitude': True,
# 				  'power_ext': ".power", 'intensify': False, 'verbosity': 1, 'nsamples': None}
# mfcc_test = Features("wav/01-1999.wav",feature_params)
# datamfcc_test = mfcc_test.MFCC
# print "datamfcc_test_size================================="
# print(datamfcc_test.size)
# print(datamfcc_test.shape)
# import numpy as np
# count = 0
# for datacontend in  datamfcc_test:
#     for dataitem in datacontend:
#         if (np.isnan(dataitem)):
#             count += 1
#             print dataitem
#             print("data is nan===============")
# print datamfcc_test[0,1]
# print count
# print datamfcc_test[2,:].size
# import numpy as np
# data=[]
# print "data=[]"
# print data
# print("data_min_row=[]")
# data_min_row=[]
# print data_min_row
# data=np.array([[1 ,2 ,3],[22,33,44],[555,666,777],[1234,3456,5543]],dtype=int)
#
# print "data"
# print data
# for row in range(len(data[1])):
#     print"data_row"
#     data_row=data[:,row]
#     print(data_row)
#     data_min_row=data_row[0:2]
#     print "data_min_row"
#     print data_min_row
# print "okay"
cmd = "hello world & git push it to the github, okay?"
print "A: pls tell me what should I do for you ? B:%s"%cmd