"""Модуль сетевой синхронизации партии."""

class NetworkSync:
    """Класс синхронизации игрового состояния по сети.

    Attributes:
        last_state (str): Последнее синхронизированное состояние партии.
    """

    def __init__(self):
        """Инициализирует сервис сетевой синхронизации."""
        self.last_state = "initial"

    def sync_position(self):
        """Синхронизирует позицию шахматной партии.

        Returns:
            str: Сообщение о завершении синхронизации.
        """
        self.last_state = "synced"
        return "Позиция синхронизирована"

    def get_last_state(self):
        """Возвращает последнее состояние синхронизации.

        Returns:
            str: Последнее состояние партии.
        """
        return self.last_state
