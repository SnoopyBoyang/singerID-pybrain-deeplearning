__author__ = 'zhangxulong'
from numpy import *
import dnn
import time
from bulid_dataset import load_dataset
from pybrain.utilities import percentError
# time_start
timestart = time.time()
# trainset, validset, testset = music_preprocess.load_dataset("sid.pkl")
trainset, validset, testset = load_dataset("mfcc_sid.pkl")
# train
train_data = trainset[0]
train_target = trainset[1]

# set the layers parm,and the max is 8 now
layers = [10, 20, 10,20]
# run the dnn ,first autoencoder and then DNNRegressor
autoencoder = dnn.AutoEncoder(train_data, train_data, train_target, layers, hidden_layer="TanhLayer", final_layer="SoftmaxLayer", compression_epochs=5, bias=True, autoencoding_only=True, dropout_on=True)
print("1here is okay")#============================================================
autoencoder.fit()
# time end
timeend = time.time()
# train time
traintime = timeend - timestart
print"====================train the dnn take %d second =========================="%traintime
#test
test_time_start=time.time()
test_target= testset[1]
predict_target=[]
for test_data in testset[0]:
    predict_target.append( argmax(autoencoder.predict(test_data)))
test_result= 100-percentError(predict_target,test_target)
print "the test result is %s"%str(test_result)
test_time_end=time.time()
test_time= test_time_end-test_time_start
print"====================make the test take %d second =========================="%test_time
