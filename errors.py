# Custom Error Classes file

class Error(Exception):
    """ Base class for other classes"""
    pass

class Invalid_Move(Error):
    """ Player tried to put a piece on a taken square """
    pass