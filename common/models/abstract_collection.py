from abc import ABCMeta, abstractmethod


class AbstractCollection(Object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get(self, uuid):
        raise NotImplementedError

    @abstractmethod
    def find(self):
        raise NotImplementedError

    @abstractmethod
    def find_all(self, criteria):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self, uuid):
        raise NotImplementedError
