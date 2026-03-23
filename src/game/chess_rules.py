"""Модуль правил шахматной партии."""

class ChessRules:
    """Класс проверки правил шахматной игры."""

    def is_checkmate(self):
        """Определяет наличие мата.

        Returns:
            bool: True, если поставлен мат.
        """
        return False

    def is_stalemate(self):
        """Определяет наличие патовой ситуации.

        Returns:
            bool: True, если зафиксирован пат.
        """
        return False

    def is_check(self):
        """Определяет наличие шаха королю.

        Returns:
            bool: True, если король находится под шахом.
        """
        return False
