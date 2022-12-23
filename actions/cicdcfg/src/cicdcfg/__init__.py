"""cicdcfg model
- tracks the version of the package
- provides a way to configure logging submodules

"""

import logging

__version__ = '0.3.0'

Logger = logging.getLogger(__name__)
# Logger.addHandler(logging.NullHandler())