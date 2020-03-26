# Custom Error Classes file

class Error(Exception):
    """ Base class for other classes"""
    pass

class InvalidMoveError(Error):
    """ Player tried to put a piece on a taken square """
    pass

class InputError(Error):
    """ Player put in an unexpected input """