""" Settings for kano_konnect """
try:
    from .local import *
except ImportError, exc:
    exc.args = tuple(
        ['%s (did you rename settings/local-example.py?)' % exc.args[0]])
    raise exc