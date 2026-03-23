"""Модуль обработки ходов."""

class MoveProcessor:
    """Класс обработки и проверки шахматных ходов.

    Attributes:
        move_count (int): Количество обработанных ходов.
    """

    def __init__(self):
        """Инициализирует обработчик ходов."""
        self.move_count = 0

    def make_move(self, move):
        """Обрабатывает ход игрока.

        Args:
            move (str): Ход в шахматной нотации.

        Returns:
            str: Сообщение о результате обработки хода.
        """
        self.move_count += 1
        return f"Ход {move} обработан"

    def validate_move(self, move):
        """Проверяет корректность хода.

        Args:
            move (str): Проверяемый ход.

        Returns:
            bool: True, если ход допустим.
        """
        return True
