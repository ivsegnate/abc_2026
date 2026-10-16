class NotificationSender:
    def send(self, message: str, user) -> None:
        raise NotImplementedError("Метод send должен быть реализован в подклассах")


class EmailSender(NotificationSender):
    def send(self, message: str, user) -> None:
        print(f"Email для {user.name} | Образовательная платформа | {message}")


class SMSSender(NotificationSender):
    def send(self, message: str, user) -> None:
        truncated_message = message[:50]
        print(f"SMS для {user.name} | {truncated_message}")


class PushSender(NotificationSender):
    def send(self, message: str, user) -> None:
        print(f"Push для {user.name} | 🎓 {message}")


class User:
    def __init__(self, name: str, preferred_notifications: list[NotificationSender]):
        self.name = name
        self.preferred_notifications = preferred_notifications


def notify_user(user: User, message: str) -> None:
    for sender in user.preferred_notifications:
        sender.send(message, user)


if __name__ == "__main__":
    channels = [EmailSender(), PushSender()]
    maria = User(name="Мария", preferred_notifications=channels)
    text = "Блок аналитики начинается с 27 октября!"
    notify_user(maria, text)
