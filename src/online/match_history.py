"""Модуль истории сыгранных партий."""

class MatchHistory:
    """Класс хранения истории шахматных партий.

    Attributes:
        matches (list): Список сохраненных партий.
    """

    def __init__(self):
        """Инициализирует историю партий."""
        self.matches = []

    def save_match(self):
        """Сохраняет завершенную партию в историю.

        Returns:
            str: Сообщение о сохранении партии.
        """
        self.matches.append("match_1")
        return "Партия сохранена в историю"

    def get_matches(self):
        """Возвращает список сохраненных партий.

        Returns:
            list: История партий.
        """
        return self.matches
