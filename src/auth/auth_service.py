"""Модуль аутентификации пользователей."""

class AuthService:
    """Сервис регистрации и входа пользователей в систему.

    Attributes:
        users (dict): Словарь зарегистрированных пользователей.
    """

    def __init__(self):
        """Инициализирует сервис аутентификации."""
        self.users = {}

    def register(self, username, password):
        """Регистрирует нового пользователя.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль пользователя.

        Returns:
            str: Результат регистрации.
        """
        self.users[username] = password
        return "Пользователь зарегистрирован"

    def login(self, username, password):
        """Выполняет вход пользователя в систему.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль пользователя.

        Returns:
            str: Результат попытки входа.
        """
        if self.users.get(username) == password:
            return "Вход выполнен"
        return "Неверные учетные данные"
