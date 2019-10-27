__str__ = 'error which are more certain to the system is written here'
__all__ = ['SlotError', 'SizeError', 'CarError', 'FileError']


class Error(Exception):
    pass


class FileError(Error):
    """
    no file present in system or  permission error
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class SizeError(Error):
    """SIZE ERROR : invalid size for parking lot"""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


class SlotError(Error):
    """slot error , check if it is already empty or invalid"""

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


class CarError(Error):
    """ no car with this color found"""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)
