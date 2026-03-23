"""Модуль профиля игрока."""

class PlayerProfile:
    """Класс профиля игрока.

    Attributes:
        nickname (str): Игровой псевдоним.
        rating (int): Текущий рейтинг игрока.
    """

    def __init__(self, nickname="player1", rating=1200):
        """Инициализирует профиль игрока.

        Args:
            nickname (str): Имя игрока.
            rating (int): Начальный рейтинг.
        """
        self.nickname = nickname
        self.rating = rating

    def get_profile_info(self):
        """Возвращает сведения о профиле игрока.

        Returns:
            dict: Данные профиля игрока.
        """
        return {"nickname": self.nickname, "rating": self.rating}

    def update_rating(self, points):
        """Изменяет рейтинг игрока.

        Args:
            points (int): Количество очков для изменения рейтинга.

        Returns:
            int: Обновленный рейтинг.
        """
        self.rating += points
        return self.rating
