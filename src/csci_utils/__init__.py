from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution

# code from setup tools_scm https://github.com/pypa/setuptools_scm
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
