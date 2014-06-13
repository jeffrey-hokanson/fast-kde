fast-kde
========

An experiment in building fast [Kernel Density Estimators](https://en.wikipedia.org/wiki/Kernel_density_estimation) (KDEs) in Python.

The main goal of this project is to experiment in building fast numerical code that runs in Python,
spanning the gamut of pure Python, numpy, numexpr, theano, pyopencl, Cython, and pure C.

Objectives
----------
- Full test suite verifying accelerated code reproduces the correct results.
- Timing code comparing performance with established libraries, inspired by [Jake Vanderplas](http://jakevdp.github.io/blog/2013/12/01/kernel-density-estimation/):
	* [SciPy](http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html)
	* [statsmodels](http://statsmodels.sourceforge.net/devel/examples/notebooks/generated/kernel_density.html)
	* [Scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity)
