"""
 Entry point to run service / web API in async mode with gevent
"""

from gevent import monkey

monkey.patch_all()

# re-export
import algorithms_api