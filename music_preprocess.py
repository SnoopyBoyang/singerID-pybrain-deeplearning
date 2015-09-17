"""
Created on 2015-05-27

@author: zhangxulong
datasets are built in the form of [(MFCC,Lable),(MFCC,Lable),(MFCC,Lable),(MFCC,Lable)]
then pickl in one pickle file
and the portion of train:valid:test = 12:1:3
"""
dataset_path = 'musics'

import os
import pylab
from cPickle import dump
import cPickle as pkl
import numpy
import theano

from features import Features

# use mfcc feature
feature_params = {'sample_rate': 44100, 'feature': 'mfcc', 'nbpo': 12, 'ncoef': 10, 'lcoef': 0, 'lo': 63.5444,
                  'hi': 16000, 'nfft': 16384, 'wfft': 8192, 'nhop': 4410, 'log10': False, 'magnitude': True,
                  'power_ext': ".power", 'intensify': False, 'verbosity': 1, 'nsamples': None}
dataset = []


def grab_data(path):
    # grab the data and extract the MFCC feature of every music audio
    print "grab_data"
    for filename in os.listdir(path):
        print filename
        mfcc = Features(path + '/' + filename, feature_params)
        datamfcc = mfcc.MFCC  # MFCC features
        dataset.append((datamfcc, filename))


def pkl_dataset(data_set):
    f = open('sid.pkl', 'wb')
    dump(data_set, f, -1)
    print 'pkl_dataset'
    f.close()


def load_dataset(dataset_path):
    dataset_path = 'sid.pkl'
    f = open(dataset_path, 'rb')
    dataset_load = pkl.load(f)
    # trainL:validL:testL=12:1:3
    totalL = len(dataset_load)
    trainL = totalL * 12 / 16
    validL = totalL * 13 / 16
    # print "load_dataset and the portion of train:valid:test is given as below"
    # print totalL, trainL, validL
    inputdata = []
    tagetlable = []
    for datalable in dataset_load:
        inputdata.append(datalable[0])
        tagetlable.append(datalable[1])

    train = []
    valid = []
    test = []
    for inputindex in range(0, trainL):
        train.append((inputdata[inputindex], tagetlable[inputindex]))
    for index in range(trainL, validL):
        valid.append((inputdata[index], tagetlable[index]))
    for index in range(validL, totalL):
        test.append((inputdata[index], tagetlable[index]))
    return train, valid, test


def changestringtofloat(stringss):
    ta = 0
    for c in stringss:
        ta += (ord(c) * 100)
    return ta


def main():
    grab_data(dataset_path)
    pylab.show()
    pkl_dataset(dataset)
    trainset, validset, testset = load_dataset('sid.pkl')


if __name__ == '__main__':
    main()
