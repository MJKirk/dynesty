import numpy as np
import dynesty

"""
Run a series of basic tests of the 2d eggbox
"""

# seed the random number generator
np.random.seed(56432)

nlive = 100
printing = False

# EGGBOX


# see 1306.2144
def loglike_egg(x):
    logl = ((2 + np.cos(x[0] / 2) * np.cos(x[1] / 2))**5)
    return logl


def prior_transform_egg(x):
    return x * 10 * np.pi


def test_dyn():
    # hard test of dynamic sampler with high dlogz_init and small number
    # of live points
    ndim = 2
    bound = 'multi'
    sampler = dynesty.DynamicNestedSampler(loglike_egg,
                                        prior_transform_egg,
                                        ndim,
                                        nlive=nlive,
                                        bound=bound,
                                        sample='unif')
    sampler.run_nested(dlogz_init=1, print_progress=printing)
    logz_truth = 235.856
    assert (abs(logz_truth - sampler.results.logz[-1]) <
                5. * sampler.results.logzerr[-1])
