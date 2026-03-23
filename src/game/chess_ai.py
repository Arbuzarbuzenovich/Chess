"""Модуль искусственного интеллекта."""

class ChessAI:
    """Класс компьютерного соперника.

    Attributes:
        difficulty (str): Уровень сложности ИИ.
    """

    def __init__(self, difficulty="medium"):
        """Инициализирует шахматный искусственный интеллект.

        Args:
            difficulty (str): Уровень сложности.
        """
        self.difficulty = difficulty

    def choose_move(self):
        """Выбирает следующий ход для компьютерного соперника.

        Returns:
            str: Ход, выбранный ИИ.
        """
        return "e2-e4"

    def set_difficulty(self, difficulty):
        """Устанавливает новый уровень сложности.

        Args:
            difficulty (str): Новый уровень сложности.

        Returns:
            str: Текущий уровень сложности.
        """
        self.difficulty = difficulty
        return self.difficulty
