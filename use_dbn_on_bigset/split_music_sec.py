__author__ = 'Administrator'

import os
import os.path
import pylab
try:
    import pyadb
except ImportError:
    pass
rootdir = "origin_musics"  # store the origin music file

def read(fname, dtype='<f8'):
        """
        ::

            read a binary little-endien row-major adb array from a file.
            Uses open, seek, fread
        """
        fd = None
        data = None
        try:
            fd = open(fname, 'rb')
            dim = pylab.np.fromfile(fd, dtype='<i4', count=1)
            data = pylab.np.fromfile(fd, dtype=dtype)
            data = data.reshape(-1,dim)
            return data
        except IOError:
            print "IOError: Cannot open %s for reading." %(fname)
            raise IOError
        finally:
            if fd:
                fd.close()
def write(fname,data, dtype='<f8'):
        """
        ::

            write a binary little-endien row-major adb array to a file.
        """
        fd = None
        rows,cols=data.shape
        try:
            fd = open(fname, 'wb')
            pylab.array([cols],dtype='<i4').tofile(fd)
            data = pylab.np.array(data,dtype=dtype)
            data.tofile(fd)
        except IOError:
            print "IOError: Cannot open %s for writing." %(fname)
            raise IOError
        finally:
            if fd:
                fd.close()
def split_music_into_pieces(filepath):
 for file in os.walk(filepath):
  file_name = file[2]
  data = read(file_name)
  for data_item in range(len(data)/10):
   write(file_name+"("+data_item+")",data[data_item])
   # TODO split