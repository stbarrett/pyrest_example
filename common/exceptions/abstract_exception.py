""" Common exception that can be changed to output errors in our own format """


class AbstractException(Exception):
    def __init__(self):
        self.message = None
        self.error_code = None
