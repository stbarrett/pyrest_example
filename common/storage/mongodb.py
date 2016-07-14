"""" Describes a MongoDB storage adapter """

from common.storage.abstract_storage_adapter import AbstractStorageAdapter
from common.exceptions.storage_error import StorageError
from common.exceptions.error_codes import STORAGE_RESOURCE_NOT_FOUND
from pymongo import MongoClient


class MongoDB(AbstractStorageAdapter):
    def __init__(self, connection, database):
        self.client = None
        self.connection = connection
        self.database = database
        self.db = None

    def _open(self):
        self.client = MongoClient(self.connection)
        self.db = getattr(self.client, self.database)

    """ Get record by uuid """
    def get(self, uuid):
        try:
            self._open()
            client = MongoClient()
            db = client.pyrest
            return db.users.find({"uuid": uuid})[0]
        except IndexError:
            raise StorageError('Resource not found.', STORAGE_RESOURCE_NOT_FOUND)  # handle resource not found error
        except TypeError:
            raise StorageError('Malformed request to storage found.', STORAGE_BAD_QUERY)

    """ find all records (no pagination) """
    def find_all(self, criteria={}):
        try:
            self._open()
            client = MongoClient()
            db = client.pyrest
            return db.users.find(criteria)
        except IndexError as error:
            pass  # handle resource not found error
        except TypeError as error:
            pass  # handle malformed request error
