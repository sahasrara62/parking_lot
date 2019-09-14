
__all__ = ['SlotError','SizeError', 'CarError','FileError']


class Error(Exception):
    pass


class FileError(Error):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)


class SizeError(Error):
    """SIZE ERROR : invalid size for parking lot"""
    def __init__(self, msg):
        self.msg =msg
    def __str__(self):
        return str(self.msg)




class SlotError(Error):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)

    """slot error , check if it is already empty or invalid"""
    pass


class CarError(Error):
    """ no car with this color found"""
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return str(self.msg)

