"""" Describes an abstract storage adapter """


class AbstractStorageAdapter:
    def __init__(self):
        pass

    def get(self, id):
        raise NotImplementedError

    def find(self):
        raise NotImplementedError

    def find_all(self, criteria):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
