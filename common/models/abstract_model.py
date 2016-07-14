""" Abstract Model """

from abc import ABCMeta, abstractmethod
from bson import ObjectId
import uuid


class AbstractModel(Object):
    __metaclass__ = ABCMeta

    """ Pre-populate values """

    def __init__(self, values):
        for k, v in values.items():
            if isinstance(v, ObjectId):
                v = str(v)
            setattr(self, k, v)

        if 'uuid' not in values:
            self._uuid = uuid.uuid4()  # generate unique identifier. Important ID that can be used as shard key, etc.

    """
        Our models use _attr style to represent instance variables. We need to remove the '_' from our dict
        so we return true field names. Probably better solution, but hey, this is a quick demo...
    """

    def as_dict(self):
        return_dict = {}
        for k, v in self.__dict__.iteritems():
            return_dict[k[1:len(k)]] = v

        return return_dict
