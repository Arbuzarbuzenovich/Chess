"""Модуль настроек приложения."""

class Settings:
    """Класс управления настройками приложения.

    Attributes:
        theme (str): Активная тема оформления.
        sound_enabled (bool): Флаг включения звука.
    """

    def __init__(self, theme="light", sound_enabled=True):
        """Инициализирует настройки приложения.

        Args:
            theme (str): Начальная тема оформления.
            sound_enabled (bool): Состояние звука.
        """
        self.theme = theme
        self.sound_enabled = sound_enabled

    def apply_theme(self, theme_name):
        """Применяет выбранную тему оформления.

        Args:
            theme_name (str): Название темы.

        Returns:
            str: Сообщение о применении темы.
        """
        self.theme = theme_name
        return f"Тема {theme_name} применена"

    def toggle_sound(self):
        """Переключает состояние звука.

        Returns:
            bool: Новое состояние звука.
        """
        self.sound_enabled = not self.sound_enabled
        return self.sound_enabled
