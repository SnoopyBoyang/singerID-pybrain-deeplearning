
"""
Created on 2015-06-15

@author: zhangxulong
datasets are built in the form of [(MFCC_vector,Lable),(MFCC,Lable),(MFCC,Lable),(MFCC,Lable)]
then pickl in one pickle file
and the portion of train:valid:test = 12:1:3
"""
dataset_path = 'mp3'
import math
import os
from cPickle import dump
import cPickle as pkl
import numpy
from features import Features


# use mfcc feature
feature_params = {'sample_rate': 44100, 'feature': 'mfcc', 'nbpo': 12, 'ncoef': 10, 'lcoef': 0, 'lo': 63.5444,
				  'hi': 16000, 'nfft': 16384, 'wfft': 8192, 'nhop': 4410, 'log10': False, 'magnitude': True,
				  'power_ext': ".power", 'intensify': False, 'verbosity': 1, 'nsamples': None}

def grab_data(path):
	# grab the data and extract the MFCC feature of every music audio
	# parm path is the music data files here  under the same root is "musics"
	print "grab_data_from_path:%s" % path
	mfcc_vetor = []
	singer_lables = []

	for filename in os.listdir(path):

		#mfcc = Features(path + '/' + filename, feature_params)
		mfcc = Features(change_mp3_to_wav(path + '/' + filename), feature_params)
		datamfcc = mfcc.MFCC  # MFCC features
		print("==================================================================")
		print(path + '/' + filename)
		#singer_name = filename.split('_', 2)[0]
		singer_name = get_singer_name(path + '/' + filename)
		print("==================================================================")
		print(singer_name)
		singger_name_float = changestringtofloat(singer_name)
		print singer_name

		print "===============singername@mfcc============="
		print(singger_name_float)
		# change target label to float
		for row in range(len(datamfcc[1, :])-1):
			# split the matrix and match with the right singer
			datamfcc_row = datamfcc[:, row]
			nomlize_datamfcc_row = nomlize_data_row(datamfcc_row)
			mfcc_vetor.append(nomlize_datamfcc_row)
			singer_lables.append(singger_name_float)
	print singer_lables
	print"=================singerlabes==========listall========="

	train_set, valid_set, test_set = split_to_three_set(mfcc_vetor, singer_lables)
	dataset = (train_set, valid_set, test_set)
	return dataset
def split_to_three_set(mfcc_vetor_list, singer_lables_list):
	if len(mfcc_vetor_list)==len(singer_lables_list):
		totalL = len(mfcc_vetor_list)
	else:
		raise Exception("error, the lenth of vetor not equal the lables")
	trainL = totalL * 12 / 16
	validL = totalL * 13 / 16
	print "begin divide the dataset to three part: train, valid, and test."
	train_mfcc_vector = []
	train_singer_lable = []
	valid_mfcc_vector = []
	valid_singer_lable = []
	test_mfcc_vector = []
	test_singer_lable = []

	for index1 in range(0, trainL):
		train_mfcc_vector.append(mfcc_vetor_list[index1])
		train_singer_lable.append(singer_lables_list[index1])
	train = (train_mfcc_vector, train_singer_lable)
	for index2 in range(trainL, validL):
		valid_mfcc_vector.append(mfcc_vetor_list[index2])
		valid_singer_lable.append(singer_lables_list[index2])
	valid = (valid_mfcc_vector, valid_singer_lable)
	for index3 in range(validL, totalL):
		test_mfcc_vector.append(mfcc_vetor_list[index3])
		test_singer_lable.append(singer_lables_list[index3])
	test = (test_mfcc_vector, test_singer_lable)
	# train's structure is (array(), list)
	# train
	#train_pro structer is (ndarray of all the music mfcc,vector of all the siger name in float value)
	return train, valid, test

def change_to_ndarray(datalist):
	data_array = numpy.array(datalist)
	return data_array

def pkl_dataset(data_set):
	# begin pkl the (mfcc,singer) to a pkl file
	f = open('mfcc_sid.pkl', 'wb')
	dump(data_set, f, -1)
	print 'pkl_dataset done'
	f.close()
def load_dataset(dataset_path):
	#return the train, valid, test list in structure (mfcc, singer)
	f = open(dataset_path, 'rb')
	train, valid, test = pkl.load(f)
	return train, valid, test

def nomlize_data_row(data_row):
    # minimize the data row and eraser the nan data
	for data in range(len(data_row)):
		data_row[data] = data_row[data]

		if math.isnan(data_row[data]):
			data_row[data] = 0

	return data_row[0:10]#95dim mfcc vector only tale the first 10 as a new vector to reduce the data mass

def changestringtofloat(stringss):
	ta = 0
	for c in stringss:
		ta += (ord(c) * 100)
		tta = round(ta/1000, 4)

	return tta
def get_singer_name(mp3dirstring):
	# read the artist name from the Mp3 file
	from mutagen.mp3 import MP3
	import mutagen.id3
	from mutagen.easyid3 import EasyID3

	infovalue = MP3(mp3dirstring,ID3=EasyID3)
	artist = infovalue.get('artist')
	if artist == None:
		artist = "null"
	artist_name = "".join(artist)
	return artist_name
	# read the artist name from the Mp3 file

def change_mp3_to_wav(mp3dirstring):
	from pydub import AudioSegment
	song = AudioSegment.from_mp3(mp3dirstring)
	song_export_name='wav/'+mp3dirstring.split('.')[0].split('/')[1]+".wav"
	song.export(song_export_name, format="wav", bitrate="192k")
	return song_export_name

def main():

	ds = grab_data(dataset_path)
	# pylab.show()
	pkl_dataset(ds)
	# trainset, validset, testset = load_dataset('sid.pkl')

if __name__ == '__main__':
	main()



