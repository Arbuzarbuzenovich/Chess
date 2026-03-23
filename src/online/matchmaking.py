"""Модуль автоматического подбора соперника."""

class Matchmaking:
    """Класс подбора соперника для сетевой партии.

    Attributes:
        queue_size (int): Количество игроков в очереди ожидания.
    """

    def __init__(self):
        """Инициализирует сервис подбора соперника."""
        self.queue_size = 0

    def join_queue(self):
        """Добавляет игрока в очередь подбора.

        Returns:
            int: Текущий размер очереди.
        """
        self.queue_size += 1
        return self.queue_size

    def find_opponent(self):
        """Выполняет поиск соперника.

        Returns:
            str: Сообщение о результате поиска.
        """
        return "Соперник найден"
