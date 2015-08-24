__author__ = 'Administrator'
"""
Created on 2015-05-27

@author: zhangxulong
datasets are built in the form of [(MFCC,Lable),(MFCC,Lable),(MFCC,Lable),(MFCC,Lable)]
then pickl in one pickle file
and the portion of train:valid:test = 12:1:3
"""
dataset_path = 'musics'

import os
from cPickle import dump
import cPickle as pkl
import numpy
from use_dbn_on_bigset.features import Features


# use mfcc feature
feature_params = {'sample_rate': 44100, 'feature': 'mfcc', 'nbpo': 12, 'ncoef': 10, 'lcoef': 0, 'lo': 63.5444,
				  'hi': 16000, 'nfft': 16384, 'wfft': 8192, 'nhop': 4410, 'log10': False, 'magnitude': True,
				  'power_ext': ".power", 'intensify': False, 'verbosity': 1, 'nsamples': None}
dataset = []
def grab_data(path):
	# grab the data and extract the MFCC feature of every music audio
	# parm path is the music data files here  under the same root is "musics"
	print "grab_data_from_path:%s" % path
	for filename in os.listdir(path):

		mfcc = Features(path + '/' + filename, feature_params)
		datamfcc = mfcc.MFCC  # MFCC features
		singer_name = filename.split('_', 2)[0]

		dataset.append((datamfcc, singer_name))

	return dataset
def pkl_dataset(data_set):
	# begin pkl the (mfcc,singer) to a pkl file
	f = open('mfcc_sid.pkl', 'wb')
	dump(data_set, f, -1)
	print 'pkl_dataset done'
	f.close()
def load_dataset(dataset_path):
	#return the train, valid, test list in structure (mfcc, singer)
	f = open(dataset_path, 'rb')
	dataset_load = pkl.load(f)
	# trainL:validL:testL=12:1:3
	totalL = len(dataset_load)
	trainL = totalL * 12 / 16
	validL = totalL * 13 / 16
	print "begin divide the dataset to three part: train, valid, and test."
	inputdata = []
	tagetlable = []
	for datalable in dataset_load:
		inputdata.append(datalable[0])
		tagetlable.append(datalable[1])
	train = []
	valid = []
	test = []
	for index1 in range(0, trainL):
		train.append((inputdata[index1], tagetlable[index1]))

	for index2 in range(trainL, validL):
		valid.append((inputdata[index2], tagetlable[index2]))
	for index3 in range(validL, totalL):
		test.append((inputdata[index3], tagetlable[index3]))
	# train's structure is (array(), list)
	# train
	train_pro = dataset_pro(train)
	valid_pro = dataset_pro(valid)
	test_pro = dataset_pro(test)

	#train_pro structer is (ndarray of all the music mfcc,vector of all the siger name in float value)
	return train_pro, valid_pro, test_pro
def dataset_pro(dataset_origin):

	singer_lables = []
	# change the data to vector list
	mfcc_vetor = []
	for data_target in dataset_origin:
		data_ndarray = numpy.array(data_target[0])
		for row in range(len(data_ndarray[1,:])):
			data_ndarray_row = data_ndarray[:,row]

			nomlize_data_ndarray_row = nomlize_data_row(data_ndarray_row)
			mfcc_vetor.append(nomlize_data_ndarray_row)
			# change target label to float
			targetfloat = changestringtofloat(data_target[1])
			singer_lables.append(targetfloat)
	singer_lables = numpy.array(singer_lables)
	mfcc_vetor = numpy.array(mfcc_vetor).transpose()

	return mfcc_vetor,singer_lables
def nomlize_data_row(data_row):
	row_max = numpy.argmax(data_row)
	nomlize_row = data_row / row_max
	return nomlize_row

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
