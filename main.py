class MaterialObject:
    def __init__(self, material: str, weight: float):
        """Конструктор для создания объекта "МатериальныйОбъект"

        Args:
            material (str): материал, из которого состоит объект
            weight (float): вес объекта

        """
        self.material = material
        self.weight = weight
class NonMaterialObject:
    def __init__(self, name: str, description: str):
        """Конструктор для создания объекта "НематериальныйОбъект"

        Args:
            name (str): название объекта
            description (str): описание объекта

        """
        self.name = name
        self.description = description
class SocialNetwork:
    def __init__(self, name: str, total_users: int):
        """Конструктор для создания объекта "СоциальнаяСеть"

        Args:
            name (str): название социальной сети
            total_users (int): количество зарегистрированных пользователей

        """
        self.name = name
        self.total_users = total_users
class MaterialObject:

    def move(self, x: float, y: float):
        """Метод для перемещения материального объекта в указанные координаты

        Args:
            x (float): координата по оси X
            y (float): координата по оси Y

        """

    def break_object(self):
        """Метод для разбивания материального объекта"""

    def repair_object(self):
        """Метод для ремонта материального объекта"""

Класс "НематериальныйОбъект":

class NonMaterialObject:
    ...

    def update_description(self, new_description: str):
        """Метод для обновления описания нематериального объекта

        Args:
            new_description (str): новое описание объекта"""

    def share(self, recipient: str):
        """Метод для передачи нематериального объекта определенному получателю

        Args:
            recipient (str): имя получателя"""

    def delete(self):
        """Метод для удаления нематериального объекта"""

Класс "СоциальнаяСеть":

class SocialNetwork:
    ...

    def create_profile(self, name: str, age: int):
        """Метод для создания профиля пользователя в социальной сети

        Args:
            name (str): имя пользователя
            age (int): возраст пользователя"""

    def add_friend(self, user_id: int, friend_id: int):
        """Метод для добавления друга пользователю по идентификаторам

        Args:
            user_id (int): идентификатор пользователя
            friend_id (int): идентификатор друга"""

    def post_message(self, user_id: int, message: str):
        """Метод для публикации сообщения от пользователя

        Args:
            user_id (int): идентификатор пользователя
            message (str): сообщение для публикации"""