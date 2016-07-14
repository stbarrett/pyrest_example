from common.exceptions.abstract_exception import AbstractException
from common.exceptions.error_codes import STORAGE_ERROR


class StorageError(AbstractException):
    def __init__(self, message, detailed_error_code):
        self.detailed_error_code = detailed_error_code
        self.error_code = STORAGE_ERROR
        self.message = message
