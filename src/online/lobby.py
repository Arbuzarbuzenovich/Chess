"""Модуль игрового лобби."""

class Lobby:
    """Класс игрового лобби для создания сетевых комнат.

    Attributes:
        rooms (list): Список доступных игровых комнат.
    """

    def __init__(self):
        """Инициализирует игровое лобби."""
        self.rooms = []

    def create_room(self):
        """Создает новую игровую комнату.

        Returns:
            str: Сообщение о создании комнаты.
        """
        self.rooms.append("room_1")
        return "Игровая комната создана"

    def list_rooms(self):
        """Возвращает список доступных комнат.

        Returns:
            list: Список игровых комнат.
        """
        return self.rooms
