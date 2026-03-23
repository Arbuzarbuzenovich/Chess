"""Модуль рейтинговой системы."""

class RatingSystem:
    """Класс расчета и обновления рейтинга игроков.

    Attributes:
        base_rating (int): Базовое значение рейтинга.
    """

    def __init__(self, base_rating=1200):
        """Инициализирует рейтинговую систему.

        Args:
            base_rating (int): Начальное значение рейтинга.
        """
        self.base_rating = base_rating

    def update_rating(self):
        """Обновляет рейтинг игрока после матча.

        Returns:
            str: Сообщение об обновлении рейтинга.
        """
        return "Рейтинг игрока обновлён"

    def get_base_rating(self):
        """Возвращает базовый рейтинг системы.

        Returns:
            int: Базовый рейтинг.
        """
        return self.base_rating
