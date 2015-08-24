# Author: Nicolas Boulanger-Lewandowski
# University of Montreal, 2012


import sys
import cPickle
import os

import numpy
import theano
import theano.tensor as T


def gauss_newton_product(cost, p, v, s):  # this computes the product Gv = J'HJv (G is the Gauss-Newton matrix)
  Jv = T.Rop(s, p, v)
  HJv = T.grad(T.sum(T.grad(cost, s)*Jv), s, consider_constant=[Jv], disconnected_inputs='ignore')
  Gv = T.grad(T.sum(HJv*s), p, consider_constant=[HJv, Jv], disconnected_inputs='ignore')
  Gv = map(T.as_tensor_variable, Gv)  # for CudaNdarray
  return Gv


class hf_optimizer(object):
  '''Black-box Theano-based Hessian-free optimizer.
See (Martens, ICML 2010) and (Martens & Sutskever, ICML 2011) for details.

Useful functions:
__init__ :
  Compiles necessary Theano functions from symbolic expressions.
train :
  Performs HF optimization following the above references.'''




