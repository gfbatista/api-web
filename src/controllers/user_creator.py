from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface # noqa

class UserCreator:
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository
