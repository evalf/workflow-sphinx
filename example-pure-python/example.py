__doc__ = 'example\n'

try:
    import typing_extensions
except ModuleNotFoundError:
    pass
else:
    __doc__ += '\nHAS_TYPING_EXTENSIONS\n'

try:
    import tomli
except ModuleNotFoundError:
    pass
else:
    __doc__ += '\nHAS_TOMLI\n'
