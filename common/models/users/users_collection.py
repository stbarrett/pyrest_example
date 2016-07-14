from common.models.abstract_collection import AbstractCollection
from common.storage.mongodb import MongoDB
from common.models.users.user import User


class UsersCollection(AbstractCollection):
    def __init__(self):
        self.database = "pyrest"  # TODO: make config generated
        pass

    def delete(self, uuid):
        pass

    def get(self, uuid):
        db = MongoDB("mongodb://127.0.0.1:27019", self.database)  # TODO: make config generated
        return User(db.get(uuid))

    def find(self):
        pass

    def find_all(self, criteria={}):
        db = MongoDB("mongodb://127.0.0.1:27019", self.database)  # TODO: make config generated
        results = []
        query_results = db.find_all(criteria)
        for result in query_results:
            results.append(User(result))
        return results

    def update(self):
        pass