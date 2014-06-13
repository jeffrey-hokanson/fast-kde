#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import numpy as np
import timeit
import kde
from sklearn.neighbors import KernelDensity


bandwidth = 0.1
npoints = 101
xmin = 0
xmax = 1
data = np.random.rand(int(1e2))

def time_kde_python():
    """
    Calls kde's pure python implementation.

    We point to global variables so that we can pull in different test values 
    later.
    """
    global bandwidth, npoints, xmin, xmax, data
    kde.hat_linear(data, bandwidth = bandwidth, 
        xmin = xmin, xmax = xmax,
	npoints = npoints, code = 'python')

def time_kde_C():
    """
    Calls kde's pure C implementation.

    We point to global variables so that we can pull in different test values 
    later.
    """
    global bandwidth, npoints, xmin, xmax, data
    kde.hat_linear(data, bandwidth = bandwidth, 
        xmin = xmin, xmax = xmax,
	npoints = npoints, code = 'C')

def time_sklearn():
    """
    Same as above, for scikit learn
    """
    global bandwidth, npoints, xmin, xmax, data
    sk_kde = KernelDensity(kernel = 'linear', bandwidth = bandwidth)
    sk_kde.fit(data[:,np.newaxis])
    grid = np.linspace(xmin, xmax, npoints)
    return np.exp(sk_kde.score_samples(grid[:,np.newaxis]))


repeat = 10


ndata = np.logspace(0,4,10).astype(int)
# Setup data storage
times = {}
times['kde_python'] = np.zeros(ndata.shape[0])
times['kde_C'] = np.zeros(ndata.shape[0])
times['sklearn'] = np.zeros(ndata.shape[0])

idx = 0
for n in ndata:
    data = np.random.rand(n)
    times['kde_python'][idx] = min(timeit.Timer(time_kde_python).repeat(repeat = repeat, number = 1))
    times['kde_C'][idx] = min(timeit.Timer(time_kde_C).repeat(repeat = repeat, number = 1))
    times['sklearn'][idx] = min(timeit.Timer(time_sklearn).repeat(repeat = repeat, number = 1))
    idx += 1

print times['kde_python']
print times['kde_C']
print times['sklearn']
