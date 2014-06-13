fast-kde
========

An experiment in building fast [Kernel Density Estimators](https://en.wikipedia.org/wiki/Kernel_density_estimation) (KDEs) in Python.

The main goal of this project is to experiment in building fast numerical code that runs in Python,
spanning the gamut of pure Python, numpy, numexpr, theano, pyopencl, Cython, and pure C.
We are particularly interested in special cases where we are sampling the kernel density estimate on a regular grid in one and two dimensions
-- an application that frequently appears when visualizing results.
With regular samples, we can reduce memory access for compactly supported kernels (e.g., tophat; not Gaussian) which decreases runtime.


Objectives
----------
- Full test suite verifying accelerated code reproduces the correct results.
- Timing code comparing performance with established libraries, inspired by [Jake Vanderplas](http://jakevdp.github.io/blog/2013/12/01/kernel-density-estimation/):
	* [SciPy](http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html)
	* [statsmodels](http://statsmodels.sourceforge.net/devel/examples/notebooks/generated/kernel_density.html)
	* [Scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity)
