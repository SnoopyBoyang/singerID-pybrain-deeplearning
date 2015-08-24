import numpy
from features import Features
dataset = []
feature_params = {'sample_rate': 44100, 'feature': 'mfcc', 'nbpo': 12, 'ncoef': 10, 'lcoef': 0, 'lo': 63.5444,
                  'hi': 16000, 'nfft': 16384, 'wfft': 8192, 'nhop': 4410, 'log10': False, 'magnitude': True,
                  'power_ext': ".power", 'intensify': False, 'verbosity': 1, 'nsamples': None}

mfcc = Features('musics/linzx_02.wav', feature_params)
datamfcc = mfcc.MFCC  # MFCC features
singer_name = 'musics/linzx_02.wav'.split('_', 2)[0].split('/', 2)[1].__str__()

print "datamfcc.shape{==========%s}" % {datamfcc.shape}
print "type(datamfcc){==========%s}" % {type(datamfcc)}
for row in range(len(datamfcc[1, :])):
	print(row)
	print datamfcc[:, row]
print singer_name
dataset.append((datamfcc, singer_name))
ada = numpy.array(dataset)
print ada.shape
print ada[0][1]
print type(ada[0][0])
nda = ada[0][0]
vector = []
for row in range(len(nda[1, :])):
	print(row)
	vector.append((nda[:, row],singer_name))

print vector

