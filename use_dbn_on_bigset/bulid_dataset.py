
"""
Created on 2015-06-15

@author: zhangxulong
datasets are built in the form of [(MFCC_vector,Lable),(MFCC,Lable),(MFCC,Lable),(MFCC,Lable)]
then pickl in one pickle file
and the portion of train:valid:test = 12:1:3
"""
dataset_path = 'musics'
import math
import os
from cPickle import dump
import cPickle as pkl
import numpy
from use_dbn_on_bigset.features import Features


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

		mfcc = Features(path + '/' + filename, feature_params)
		datamfcc = mfcc.MFCC  # MFCC features
		singer_name = filename.split('_', 2)[0]
		singger_name_float = changestringtofloat(singer_name)
		# change target label to float
		for row in range(len(datamfcc[1, :])):
			# split the matrix and match with the right singer
			datamfcc_row = datamfcc[:, row]
			nomlize_datamfcc_row = nomlize_data_row(datamfcc_row)
			mfcc_vetor.append(nomlize_datamfcc_row)
			singer_lables.append(singger_name_float)
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
	train = (change_to_ndarray(train_mfcc_vector), change_to_ndarray(train_singer_lable))
	for index2 in range(trainL, validL):
		valid_mfcc_vector.append(mfcc_vetor_list[index2])
		valid_singer_lable.append(singer_lables_list[index2])
	valid = (change_to_ndarray(valid_mfcc_vector), change_to_ndarray(valid_singer_lable))
	for index3 in range(validL, totalL):
		test_mfcc_vector.append(mfcc_vetor_list[index3])
		test_singer_lable.append(singer_lables_list[index3])
	test = (change_to_ndarray(test_mfcc_vector), change_to_ndarray(test_singer_lable))
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
	for data in range(len(data_row)):
		if math.isnan(data_row[data]):
			data_row[data] = 0
	return data_row

def changestringtofloat(stringss):
	ta = 0
	for c in stringss:
		ta += (ord(c) * 100)
	return ta
def main():

	ds = grab_data(dataset_path)
	# pylab.show()
	pkl_dataset(ds)
	# trainset, validset, testset = load_dataset('sid.pkl')

if __name__ == '__main__':
	main()
