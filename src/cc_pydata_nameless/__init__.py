import logging
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass

# Initialize ``logging.NullHandler`` for cc_pydata_nameless package
logging.getLogger('cc_pydata_nameless').addHandler(logging.NullHandler())
