""" Represents a User Object """

from common.models.abstract_model import AbstractModel


class User(AbstractModel):
    _uuid = None

    def __init__(self, values):
        super(User, self).__init__(values)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise AttributeError('User.email incoming value is empty.')
        self._email = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._first_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        if not self._uuid:
            self._uuid = value
