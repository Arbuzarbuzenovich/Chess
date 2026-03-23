"""Модуль контроля игрового времени."""

class TimerController:
    """Класс управления таймером шахматной партии.

    Attributes:
        time_limit (int): Лимит времени в секундах.
        is_running (bool): Состояние таймера.
    """

    def __init__(self, time_limit=600):
        """Инициализирует таймер партии.

        Args:
            time_limit (int): Время на игрока в секундах.
        """
        self.time_limit = time_limit
        self.is_running = False

    def start_timer(self):
        """Запускает таймер партии.

        Returns:
            str: Сообщение о запуске таймера.
        """
        self.is_running = True
        return "Таймер партии запущен"

    def stop_timer(self):
        """Останавливает таймер партии.

        Returns:
            str: Сообщение об остановке таймера.
        """
        self.is_running = False
        return "Таймер партии остановлен"
